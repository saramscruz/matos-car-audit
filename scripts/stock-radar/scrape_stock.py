# -*- coding: utf-8 -*-
"""
Radar de Stock — captura um snapshot do inventário de usados de amatoscar.pt.

USO:
    python scrape_stock.py                # snapshot completo (listagem + fichas)
    python scrape_stock.py --lite         # só listagem (rápido, sem localização)
    python scrape_stock.py --max-pages 3  # limitar páginas (teste)

SAÍDA:
    data/stock-snapshots/snapshot-AAAA-MM-DD.csv

DEPENDÊNCIAS:  pip install requests beautifulsoup4

IMPORTANTE (declarar sempre no relatório):
  "desaparecer do stock" != "vendido". Este snapshot mede PRESENÇA no site.
  A rotação (dias-listado) sai de comparar snapshots ao longo do tempo
  (ver merge_snapshots.py), e é um PROXY, nunca uma venda confirmada.

As funções extract_* trabalham sobre TEXTO e são testáveis sem rede
(ver test_parse.py). Só fetch_* precisa de internet.
"""
import argparse
import csv
import datetime as _dt
import os
import re
import sys
import time

import config as C

# ----------------------------------------------------------------------------
# Extractores puros (regex sobre texto) — testáveis offline
# ----------------------------------------------------------------------------
ID_IN_URL = re.compile(r"/carro-usado/([a-z0-9\-]+?)-(\d{6,})/?", re.I)

def extract_listing_ids(html_or_text: str):
    """Devolve lista de (id, url_relativa_slug) únicos encontrados no texto/HTML."""
    seen, out = set(), []
    for m in re.finditer(r"/carro-usado/([a-z0-9\-]+?-(\d{6,}))/?", html_or_text, re.I):
        slug, vid = m.group(1), m.group(2)
        if vid not in seen:
            seen.add(vid)
            out.append((vid, "/carro-usado/%s/" % slug))
    return out

def _num(s):
    """'100.312' -> 100312 ; '31.450' -> 31450 ; devolve None se vazio."""
    if s is None:
        return None
    s = re.sub(r"[^\d]", "", s)
    return int(s) if s else None

def extract_fields(text: str) -> dict:
    """Extrai os campos da ficha a partir do TEXTO da página (soup.get_text)."""
    f = {}
    def grab(pat, flags=re.I):
        m = re.search(pat, text, flags)
        return m.group(1).strip() if m else None

    f["matricula"]   = grab(r"Matr[íi]cula\s*[:\-]?\s*([A-Z0-9]{6})")
    f["data_matricula"] = grab(r"Data\s*matr[íi]cula\s*[:\-]?\s*(\d{2}/\d{2}/\d{4})")
    f["km"]          = _num(grab(r"Quil[óo]metros\s*[:\-]?\s*([\d\.]+)\s*kms"))
    f["combustivel"] = grab(r"Combust[íi]vel\s*[:\-]?\s*(Diesel|Gasolina|El[ée]trico|H[íi]brido)")
    # Fallback SÓ para fichas de quase-novos sem o campo rápido "Combustível":
    # âncoras fiáveis na ficha técnica. Nunca inferir elétrico (evita falsos
    # positivos, ex.: "direcção assistida eléctrica"); fica em branco se incerto.
    if not f["combustivel"]:
        low = text.lower()
        if "sem chumbo" in low:
            f["combustivel"] = "Gasolina"
        elif "gasóleo" in low or "gasoleo" in low:
            f["combustivel"] = "Diesel"
    f["potencia_cv"] = _num(grab(r"Pot[êe]ncia\s*[:\-]?\s*([\d\.]+)\s*CV"))
    f["transmissao"] = grab(r"Transmiss[ãa]o\s*[:\-]?\s*(Autom[áa]tica|Manual)")
    # Localização: "<Marca> A MatosCar | <Cidade>"
    # Localização no formato "[Marca] A MatosCar | Cidade". A marca do stand é
    # OPCIONAL (há fichas só com "A MatosCar | Évora"). Percorremos todas as
    # ocorrências e ficamos com a 1ª cuja cidade casa com um distrito MatosCar —
    # isto ignora o nome do site ("A MatosCar | Carros Novos...") sem risco.
    f["stand_marca"] = f["stand_cidade"] = None
    f["distrito"] = "(sem localização)"
    for mm in re.finditer(r"(?:([A-Za-zÀ-ÿ]+)\s+)?A\s*MatosCar\s*\|\s*([A-Za-zÀ-ÿ][\wÀ-ÿ\- ]{1,30})", text):
        raw = mm.group(2).strip().lower()
        for key in sorted(C.CATCHMENT, key=len, reverse=True):
            if raw.startswith(key):
                f["stand_marca"] = mm.group(1)
                f["stand_cidade"] = key.title()          # cidade canónica limpa
                f["distrito"] = C.CATCHMENT[key]
                break
        if f["stand_cidade"]:
            break
    # Ano derivado da data de matrícula
    if f["data_matricula"]:
        f["ano"] = int(f["data_matricula"][-4:])
    return f

def clean_title(t):
    """Remove o sufixo '| A MatosCar' e o id final que o og:title da página inclui."""
    if not t:
        return t
    t = t.split("|")[0]                    # tira "| A MatosCar"
    t = re.sub(r"\s+\d{6,}\s*$", "", t)    # tira o id final
    return t.strip()

def split_brand_model(title: str):
    """'Mitsubishi L200 2.4 DID-D...' -> ('Mitsubishi', 'L200 2.4 DID-D...')."""
    if not title:
        return None, None
    for b in C.BRANDS:  # BRANDS ordenado com as de 2 palavras primeiro
        if title.lower().startswith(b.lower()):
            return b, title[len(b):].strip()
    parts = title.split(" ", 1)
    return parts[0], (parts[1] if len(parts) > 1 else "")

# ----------------------------------------------------------------------------
# Fetch + parsing de HTML (precisa de rede)
# ----------------------------------------------------------------------------
def _get(url):
    import requests
    last = None
    for attempt in range(C.MAX_RETRIES):
        try:
            r = requests.get(url, headers={"User-Agent": C.USER_AGENT}, timeout=C.REQUEST_TIMEOUT)
            if r.status_code == 200:
                return r.text
            last = "HTTP %s" % r.status_code
        except Exception as e:  # noqa
            last = str(e)
        time.sleep(C.CRAWL_DELAY_SECONDS)
    print("  [aviso] falha ao obter %s (%s)" % (url, last), file=sys.stderr)
    return None

def _meta(soup, prop):
    tag = soup.find("meta", attrs={"property": prop}) or soup.find("meta", attrs={"name": prop})
    return tag.get("content").strip() if tag and tag.get("content") else None

def parse_detail_html(html: str) -> dict:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    rec = {}
    raw_title = _meta(soup, "og:title") or (soup.title.get_text() if soup.title else "")
    rec["titulo"] = clean_title(raw_title)
    rec["marca"], rec["modelo_versao"] = split_brand_model(rec["titulo"])
    price = _meta(soup, "og:price:amount") or _meta(soup, "product:price:amount")
    rec["preco_eur"] = int(float(price)) if price else None
    canonical = soup.find("link", rel="canonical")
    rec["url"] = (canonical.get("href") if canonical else _meta(soup, "og:url")) or ""
    m = re.search(r"-(\d{6,})/?$", rec["url"])
    rec["id"] = m.group(1) if m else None
    rec.update(extract_fields(soup.get_text(" ", strip=True)))
    return rec

def crawl_inventory(limit=None):
    """Lê o sitemap dos usados e devolve lista de (id, detail_url).

    Fonte canónica (ver config.SITEMAP_USED). Evita a paginação da listagem,
    que é enganosa (/carros-usados/2 devolve a mesma página 1).
    """
    xml = _get(C.SITEMAP_USED)
    time.sleep(C.CRAWL_DELAY_SECONDS)
    if not xml:
        print("  [erro] não consegui obter o sitemap %s" % C.SITEMAP_USED, file=sys.stderr)
        return []
    found = extract_listing_ids(xml)
    print("  sitemap: %d anúncios de usados" % len(found))   # total real (antes do limite)
    inv = [(vid, C.BASE + u) for vid, u in found]
    if limit:
        inv = inv[:limit]
        print("  (limitado a %d para teste)" % limit)
    return inv

FIELDS = ["snapshot_date", "id", "matricula", "marca", "modelo_versao", "ano",
          "combustivel", "km", "preco_eur", "potencia_cv", "transmissao",
          "stand_marca", "stand_cidade", "distrito", "data_matricula", "url"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lite", action="store_true", help="só inventário do sitemap, sem visitar fichas")
    ap.add_argument("--limit", type=int, default=None, help="limitar nº de viaturas (teste)")
    args = ap.parse_args()

    today = _dt.date.today().isoformat()
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    outdir = os.path.join(root, C.SNAPSHOT_DIR)
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "snapshot-%s.csv" % today)

    print("A recolher inventário do sitemap %s ..." % C.SITEMAP_USED)
    inv = crawl_inventory(limit=args.limit)
    print("Inventário: %d anúncios." % len(inv))

    rows = []
    enrich = C.ENRICH_DETAIL and not args.lite
    for i, (vid, url) in enumerate(inv, 1):
        rec = {"snapshot_date": today, "id": vid, "url": url}
        if enrich:
            html = _get(url)
            time.sleep(C.CRAWL_DELAY_SECONDS)
            if html:
                rec.update(parse_detail_html(html))
                rec["snapshot_date"], rec["id"] = today, vid
            if i % 10 == 0:
                print("  fichas: %d/%d" % (i, len(inv)))
        rows.append({k: rec.get(k) for k in FIELDS})

    with open(outpath, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    print("Snapshot guardado: %s (%d linhas)" % (outpath, len(rows)))
    print("Lembrete: 'preço' e 'presença' são factos; 'rotação' sai de merge_snapshots.py e é PROXY.")

if __name__ == "__main__":
    main()
