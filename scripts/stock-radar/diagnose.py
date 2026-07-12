# -*- coding: utf-8 -*-
"""
Diagnóstico de qualidade do snapshot T0 (sem rede).
USO:  python diagnose.py
Imprime: completude por campo, chave de rotação (matrícula única?),
extremos de preço, e os URLs das viaturas com problemas (para investigar).
"""
import csv, glob, io, os, statistics
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SNAPDIR = os.path.join(ROOT, "data", "stock-snapshots")

def num(x):
    try: return int(x)
    except: return None

def main():
    files = [f for f in sorted(glob.glob(os.path.join(SNAPDIR, "snapshot-*.csv"))) if "SAMPLE" not in f.upper()]
    if not files:
        print("Sem snapshots."); return
    raw = open(files[-1], "rb").read().replace(b"\x00", b"").decode("utf-8", "ignore")
    rows = list(csv.DictReader(io.StringIO(raw)))
    n = len(rows)
    print("Ficheiro: %s  |  %d viaturas\n" % (os.path.basename(files[-1]), n))

    print("=== COMPLETUDE POR CAMPO ===")
    for c in ["matricula","marca","modelo_versao","ano","combustivel","km","preco_eur","stand_cidade","distrito","data_matricula"]:
        cheio = sum(1 for r in rows if (r.get(c) or "").strip() and "sem localiz" not in (r.get(c) or "") and "mapear" not in (r.get(c) or ""))
        print("  %-16s %3d/%d  (%d%%)" % (c, cheio, n, round(100*cheio/n)))

    print("\n=== CHAVE DE ROTAÇÃO (matrícula) ===")
    mats = [(r.get("matricula") or "").strip() for r in rows]
    vazias = sum(1 for m in mats if not m)
    dups = [m for m,c in Counter(m for m in mats if m).items() if c > 1]
    print("  sem matrícula: %d  |  matrículas duplicadas: %d %s" % (vazias, len(dups), dups[:10]))

    print("\n=== EXTREMOS DE PREÇO (verificar se reais) ===")
    ok = [r for r in rows if num(r.get("preco_eur"))]
    ok.sort(key=lambda r: num(r["preco_eur"]))
    for r in ok[:2] + ok[-3:]:
        print("  %8s€  %s %s  [%s]" % (r["preco_eur"], r.get("marca"), (r.get("modelo_versao") or "")[:35], r.get("url")))

    def listar(titulo, pred, k=6):
        hits = [r for r in rows if pred(r)]
        print("\n=== %s (%d) — até %d URLs para investigar ===" % (titulo, len(hits), k))
        for r in hits[:k]:
            print("  %-9s %-10s %s" % (r.get("marca"), (r.get("preco_eur") or "")+"€", r.get("url")))

    listar("SEM DISTRITO", lambda r: not r.get("distrito") or "sem localiz" in r["distrito"] or "mapear" in r["distrito"])
    listar("SEM COMBUSTÍVEL", lambda r: not (r.get("combustivel") or "").strip())
    listar("SEM KM", lambda r: not (r.get("km") or "").strip())

if __name__ == "__main__":
    main()
