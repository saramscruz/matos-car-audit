# -*- coding: utf-8 -*-
"""
Junta os snapshots datados e produz os derivados do Radar de Stock.

USO:  python merge_snapshots.py
LÊ :  data/stock-snapshots/snapshot-AAAA-MM-DD_HHMMSS.csv
      (>= 2 datas para rotação; várias capturas no mesmo dia -> usa a mais recente)

GERA: _rotacao.csv                    presença e duração por veículo
      _rotacao-por-distrito-marca.csv resumo agregado (com supressão de n baixo)
      _precos-historico.csv           preço por veículo x data  [FACTO]
      _precos-alteracoes.csv          só os veículos que mudaram de preço  [FACTO]
      _sobrevivencia.csv              Kaplan-Meier (só quando houver eventos que cheguem)
      _cadencia.csv                   intervalo entre recolhas consecutivas

--------------------------------------------------------------------------
DEFINIÇÕES — declarar sempre no relatório
--------------------------------------------------------------------------
first_seen  = 1ª data em que o veículo aparece NOS SNAPSHOTS (não é a data de
              entrada no stand: se o carro já lá estava na 1ª recolha, a data
              real de entrada é desconhecida — CENSURA À ESQUERDA)
last_seen   = última data em que aparece

entrada_observada = first_seen > primeira recolha global. Só nesse caso a data
              de entrada é um facto observado.
saida_observada   = o veículo não está na recolha mais recente.

dias_listado_min  = last_seen - first_seen
                    LIMITE INFERIOR. O carro pode ter entrado antes da 1ª
                    recolha e/ou saído em qualquer momento depois do last_seen.
dias_listado_max  = (recolha seguinte ao last_seen) - first_seen, para quem saiu.
                    Para quem continua em stock não há máximo (ainda a decorrer).
                    A duração verdadeira está algures dentro de [min, max].

duracao_completa  = entrada_observada E saida_observada. SÓ estes veículos têm
                    uma duração de listagem verdadeiramente medida. Qualquer
                    estatística de duração calculada fora deste conjunto é
                    enviesada e não deve ser reportada como tal.

estado = "em stock" se está na recolha mais recente; senão "saiu do stock".
         "saiu do stock" != "vendido" — pode ser venda, devolução, reanúncio,
         retirada do site ou falha de recolha. É PROXY, sempre.

IDENTIDADE EM DOIS NÍVEIS (ver build_presence)
  id (do sitemap) -> SEMPRE disponível, mesmo quando a ficha não descarrega.
                     É a fonte fiável de PRESENÇA.
  matricula       -> só existe se a ficha descarregou, mas sobrevive a um
                     reanúncio (id novo, mesmo carro). É a identidade do VEÍCULO.

  Usar só a matrícula geraria uma SAÍDA FALSA sempre que uma ficha falhasse: o
  carro continua no sitemap, mas sem matrícula parecia ter desaparecido. Usar só
  o id perderia os reanúncios. Logo: presença pelo id, identidade pela matrícula,
  e ids que partilham matrícula são colapsados num único veículo.

  Um id cuja ficha nunca descarregou fica como veículo próprio, marcado com
  identidade_incerta=1: conta para a presença, mas não se funde com nenhum outro.
--------------------------------------------------------------------------
"""
import csv
import datetime
import glob
import os
import statistics
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SNAPDIR = os.path.join(ROOT, "data", "stock-snapshots")

# --------------------------------------------------------------------------
# Parâmetros de honestidade estatística
# --------------------------------------------------------------------------
# Uma recolha com menos do que esta fracção da recolha ANTERIOR é tratada como
# partida e ignorada. Comparar com a anterior (e não com o máximo histórico)
# evita que um inventário que encolheu legitimamente ao longo de meses vá
# arrastando o limiar consigo. 0.85 é apertado de propósito: a 0.5, uma recolha
# com 60% do stock passava e injectava ~80 saídas falsas.
MIN_SNAPSHOT_FRACTION = 0.85

# Abaixo deste nº de durações completas, uma célula do resumo não recebe
# mediana — só a contagem. A mediana de 1 ou 2 observações é a observação.
MIN_N_PARA_MEDIANA = 5

# Abaixo deste nº de eventos não se estima curva de sobrevivência.
MIN_EVENTOS_PARA_KM = 30


def _d(s):
    return datetime.date.fromisoformat(s)


def load_snapshots():
    """Devolve [(data, linhas)] ordenado, já filtrado de capturas partidas."""
    files = sorted(glob.glob(os.path.join(SNAPDIR, "snapshot-*.csv")))
    files = [f for f in files if "SAMPLE" not in f.upper()]
    loaded = []
    for f in files:
        stamp = os.path.basename(f).replace("snapshot-", "").replace(".csv", "")
        date = stamp[:10]
        # utf-8-sig tolera BOM; \x00 e defensivo contra escritas interrompidas.
        raw = open(f, "rb").read().replace(b"\x00", b"").decode("utf-8-sig", "ignore")
        rows = list(csv.DictReader(raw.splitlines()))
        loaded.append((date, stamp, rows))

    # Varias capturas no mesmo dia: fica a mais recente desse dia.
    by_date = {}
    for date, stamp, rows in loaded:
        if date not in by_date or stamp > by_date[date][0]:
            by_date[date] = (stamp, rows)
    seq = [(date, rows) for date, (stamp, rows) in sorted(by_date.items())]

    # Guarda de sanidade em cadeia: cada recolha e comparada com a ultima
    # recolha ACEITE, para uma captura partida nao contaminar a rotacao.
    kept, ref = [], None
    for date, rows in seq:
        if ref is not None and len(rows) < MIN_SNAPSHOT_FRACTION * ref:
            print("  [aviso] recolha %s ignorada: %d linhas (< %d%% da anterior "
                  "aceite, %d) - provavelmente incompleta."
                  % (date, len(rows), int(MIN_SNAPSHOT_FRACTION * 100), ref))
            continue
        kept.append((date, rows))
        ref = len(rows)
    return kept


def build_presence(snaps):
    """Presenca por veiculo, com identidade em dois niveis.

    id (do sitemap)  -> SEMPRE disponivel, mesmo quando a ficha nao descarrega.
                        E por isso a fonte fiavel de PRESENCA.
    matricula        -> so existe quando a ficha descarregou, mas sobrevive a um
                        reanuncio (id novo, mesmo carro). E a identidade do
                        VEICULO.

    Usar so a matricula criaria uma saida falsa sempre que uma ficha falhasse
    (o carro esta no sitemap, mas sem matricula parecia ter desaparecido).
    Usar so o id perderia os reanuncios. Logo: presenca pelo id, identidade pela
    matricula, e os ids que partilham matricula sao colapsados num unico veiculo.

    Um id cuja ficha nunca descarregou fica como veiculo proprio, com
    identidade_incerta=1 - conta para a presenca, mas nao se funde com nada.
    """
    id_dates = defaultdict(set)
    id_rows = defaultdict(dict)
    id_mat = {}
    incompletos = defaultdict(int)

    for date, rows in snaps:
        for r in rows:
            vid = (r.get("id") or "").strip()
            if not vid:
                continue
            id_dates[vid].add(date)
            id_rows[vid][date] = r
            mat = (r.get("matricula") or "").strip()
            completo = (r.get("registo_completo") or "1").strip() != "0"
            if mat and completo:
                id_mat.setdefault(vid, mat)
            else:
                incompletos[date] += 1

    pres = defaultdict(set)
    hist = defaultdict(dict)
    rowsbykey = {}
    ids_por_chave = defaultdict(set)
    incerta = set()

    for vid, datas in id_dates.items():
        mat = id_mat.get(vid)
        chave = mat or ("id:" + vid)
        if not mat:
            incerta.add(chave)
        pres[chave] |= datas
        ids_por_chave[chave].add(vid)
        for d, r in id_rows[vid].items():
            # Se duas listagens do mesmo carro coexistirem na mesma data
            # (reanuncio sobreposto), fica a que tem ficha completa.
            ant = hist[chave].get(d)
            if ant is None or not (ant.get("matricula") or "").strip():
                hist[chave][d] = r

    for chave in pres:
        rowsbykey[chave] = hist[chave][max(hist[chave])]

    return pres, rowsbykey, hist, incompletos, ids_por_chave, incerta


def main():
    snaps = load_snapshots()
    if len(snaps) < 2:
        print("So ha %d recolha(s) valida(s). A rotacao precisa de pelo menos 2 datas."
              % len(snaps))
        print("E o comportamento esperado no arranque: capturar hoje, repetir depois.")
        return

    dates = [d for d, _ in snaps]
    primeira, ultima = dates[0], dates[-1]
    idx = {d: i for i, d in enumerate(dates)}

    pres, rowsbykey, hist, incompletos, ids_por_chave, incerta = build_presence(snaps)

    out = []
    for mat, ds in sorted(pres.items()):
        r = rowsbykey[mat]
        fs, ls = min(ds), max(ds)
        entrada_obs = fs > primeira
        saida_obs = ls != ultima

        dias_min = (_d(ls) - _d(fs)).days
        # Limite superior: para quem saiu, a saida deu-se algures ate a recolha
        # SEGUINTE ao last_seen. Para quem esta em stock, o spell ainda decorre.
        if saida_obs:
            prox = dates[idx[ls] + 1]
            dias_max = (_d(prox) - _d(fs)).days
        else:
            dias_max = ""   # em curso, sem maximo conhecido

        # Reentrada: presente em N datas mas o intervalo cobre mais do que N.
        span = idx[ls] - idx[fs] + 1
        reentradas = span - len(ds)

        out.append({
            "chave": mat,
            "marca": r.get("marca"),
            "modelo_versao": r.get("modelo_versao"),
            "distrito": r.get("distrito"),
            "preco_eur": r.get("preco_eur"),
            "first_seen": fs,
            "last_seen": ls,
            "recolhas_presente": len(ds),
            "entrada_observada": int(entrada_obs),
            "saida_observada": int(saida_obs),
            "duracao_completa": int(entrada_obs and saida_obs),
            "dias_listado_min": dias_min,
            "dias_listado_max": dias_max,
            "reentradas": reentradas,
            "ids_anuncio": " ".join(sorted(ids_por_chave[mat])),
            "identidade_incerta": int(mat in incerta),
            "estado": "saiu do stock" if saida_obs else "em stock",
        })

    _escrever(os.path.join(SNAPDIR, "_rotacao.csv"), out)

    completos = [o for o in out if o["duracao_completa"]]
    saidos = [o for o in out if o["saida_observada"]]

    _resumo_grupo(out)
    _precos(hist, dates)
    _kaplan_meier(out)
    _cadencia(dates, out)

    print("Veiculos acompanhados: %d (%d recolhas: %s)"
          % (len(out), len(dates), ", ".join(dates)))
    if incompletos:
        print("  [aviso] fichas incompletas excluidas da rotacao: %s"
              % ", ".join("%s=%d" % (d, n) for d, n in sorted(incompletos.items())))
    if incerta:
        print("  [aviso] %d anuncio(s) cuja ficha nunca descarregou: contam para\n         a presenca mas nao se fundem com nenhuma matricula." % len(incerta))
    reanunciados = sum(1 for c in ids_por_chave.values() if len(c) > 1)
    if reanunciados:
        print("  [nota] %d veiculo(s) com mais de um anuncio (reanuncio) -\n         colapsados numa unica identidade pela matricula." % reanunciados)
    reent = sum(1 for o in out if o["reentradas"] > 0)
    if reent:
        print("  [aviso] %d veiculo(s) com reentrada (saiu e voltou) - verificar "
              "se e reanuncio ou falha de recolha." % reent)
    print("  entrada observada: %d | saida observada: %d | DURACOES COMPLETAS: %d"
          % (sum(o["entrada_observada"] for o in out), len(saidos), len(completos)))
    if not completos:
        print("  >> Nenhum veiculo tem entrada E saida observadas. Nenhuma duracao")
        print("     de listagem e hoje mensuravel. NAO reportar dias em stock.")
    print("LEMBRETE: 'saiu do stock' e PROXY, nao venda confirmada.")


def _escrever(path, rows):
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("Escrito: %s" % path)


def _resumo_grupo(out):
    """Resumo por distrito x marca.

    A mediana so e calculada sobre DURACOES COMPLETAS (entrada e saida
    observadas). Calcula-la sobre todas as saidas seria enviesado duas vezes:
    para baixo pela censura a esquerda (first_seen nao e a entrada real) e para
    baixo outra vez pela sobrevivencia (os carros lentos ainda nao sairam, logo
    nao entram na conta).
    """
    grp = defaultdict(lambda: {"saidos": 0, "completos": []})
    for o in out:
        if o["saida_observada"]:
            g = grp[(o["distrito"], o["marca"])]
            g["saidos"] += 1
            if o["duracao_completa"]:
                g["completos"].append(o["dias_listado_min"])

    summary = []
    for (dist, marca), g in sorted(grp.items()):
        n = len(g["completos"])
        if n >= MIN_N_PARA_MEDIANA:
            med = round(statistics.median(g["completos"]), 1)
            nota = ""
        else:
            med = ""
            nota = ("sem duracoes completas" if n == 0
                    else "n=%d < %d, mediana suprimida" % (n, MIN_N_PARA_MEDIANA))
        summary.append({"distrito": dist, "marca": marca,
                        "saidos": g["saidos"], "duracoes_completas": n,
                        "dias_mediana": med, "nota": nota})
    _escrever(os.path.join(SNAPDIR, "_rotacao-por-distrito-marca.csv"), summary)


def _precos(hist, dates):
    """Historico de precos - FACTO observado, sem censura.

    O preco e o sinal temporal mais forte que estes snapshots dao: e observado
    directamente, nao depende de inferir nada, e um corte de preco antecede
    tipicamente a saida. Ao contrario da rotacao, esta utilizavel desde a
    segunda recolha.
    """
    longo, alter = [], []
    for mat in sorted(hist):
        serie = []
        for d in dates:
            r = hist[mat].get(d)
            if not r:
                continue
            p = (r.get("preco_eur") or "").strip()
            longo.append({"chave": mat, "data": d, "preco_eur": p,
                          "marca": r.get("marca"),
                          "modelo_versao": r.get("modelo_versao"),
                          "distrito": r.get("distrito")})
            if p:
                serie.append((d, int(p)))
        if len(serie) >= 2 and len({p for _, p in serie}) > 1:
            p0, p1 = serie[0][1], serie[-1][1]
            ult = hist[mat][serie[-1][0]]
            alter.append({
                "chave": mat,
                "marca": ult.get("marca"),
                "modelo_versao": ult.get("modelo_versao"),
                "distrito": ult.get("distrito"),
                "preco_inicial": p0, "preco_actual": p1,
                "variacao_eur": p1 - p0,
                "variacao_pct": round(100.0 * (p1 - p0) / p0, 1) if p0 else "",
                "data_inicial": serie[0][0], "data_actual": serie[-1][0],
                "n_precos_distintos": len({p for _, p in serie}),
                "trajectoria": " -> ".join("%s:%d" % (d, p) for d, p in serie),
            })
    _escrever(os.path.join(SNAPDIR, "_precos-historico.csv"), longo)
    _escrever(os.path.join(SNAPDIR, "_precos-alteracoes.csv"), alter)
    if alter:
        desc = [a for a in alter if a["variacao_eur"] < 0]
        sub = [a for a in alter if a["variacao_eur"] > 0]
        print("Precos alterados: %d (%d descidas, %d subidas)"
              % (len(alter), len(desc), len(sub)))
        if desc:
            med = statistics.median([abs(a["variacao_eur"]) for a in desc])
            print("  descida mediana: %d EUR" % med)


def _cadencia(dates, out):
    """Regista o intervalo entre recolhas consecutivas.

    A cadencia nao e uniforme por desenho (dias uteis: 1 dia de 2a a 6a, 3 dias
    no salto de 6a para 2a) nem ao longo do tempo (a serie comecou semanal).
    A largura do intervalo E a resolucao com que qualquer duracao pode ser
    medida nesse periodo, por isso tem de sair dos dados e nao da memoria: e o
    que permite escrever a nota metodologica e decidir se periodos com cadencias
    diferentes sao comparaveis.

    Imprime tambem a fraccao de spells curtos, que e o numero necessario para
    decidir mais tarde se e seguro reduzir a frequencia: se uma fatia relevante
    das viaturas roda abaixo de N dias, amostrar de N em N dias torna-as
    invisiveis e enviesa tudo para o lado lento.
    """
    linhas = []
    for ant, act in zip(dates, dates[1:]):
        linhas.append({"data_anterior": ant, "data": act,
                       "intervalo_dias": (_d(act) - _d(ant)).days})
    _escrever(os.path.join(SNAPDIR, "_cadencia.csv"), linhas)
    if not linhas:
        return
    ints = [l["intervalo_dias"] for l in linhas]
    print("Cadencia: %d intervalo(s), min %d / mediana %.1f / max %d dias"
          % (len(ints), min(ints), statistics.median(ints), max(ints)))

    completos = [o for o in out if o["duracao_completa"]]
    if not completos:
        print("  (fraccao de rotacao rapida: por medir - ainda nao ha spells completos)")
        return
    for limiar in (2, 4, 7):
        r = sum(1 for o in completos if int(o["dias_listado_max"]) <= limiar)
        print("  spells completos com duracao <= %d dias: %d/%d (%.0f%%)"
              % (limiar, r, len(completos), 100.0 * r / len(completos)))


def _kaplan_meier(out):
    """Estimador produto-limite, com variancia de Greenwood. So stdlib.

    Restringido a coorte com ENTRADA OBSERVADA - aqueles cujo relogio arranca
    num facto e nao numa data arbitraria de inicio de observacao.

    As duracoes de quem saiu sao interval-censuradas em [min, max]; usa-se o
    ponto medio, convencao corrente mas aproximacao. O tratamento exacto e o
    estimador de Turnbull, fora do ambito da stdlib. Enquanto o intervalo for
    de 7 dias a aproximacao domina o resultado - mais uma razao para apertar a
    cadencia de recolha antes de reportar isto.
    """
    coorte = [o for o in out if o["entrada_observada"]]
    eventos = [o for o in coorte if o["saida_observada"]]
    path = os.path.join(SNAPDIR, "_sobrevivencia.csv")

    if len(eventos) < MIN_EVENTOS_PARA_KM:
        with open(path, "w", newline="", encoding="utf-8") as fh:
            fh.write("estado,eventos,minimo_exigido,nota\r\n")
            fh.write("insuficiente,%d,%d,\"Curva nao estimada: sao precisos %d "
                     "eventos (saidas com entrada observada) e ha %d. "
                     "NAO reportar duracoes de listagem.\"\r\n"
                     % (len(eventos), MIN_EVENTOS_PARA_KM,
                        MIN_EVENTOS_PARA_KM, len(eventos)))
        print("Escrito: %s  (insuficiente: %d evento(s) de %d)"
              % (path, len(eventos), MIN_EVENTOS_PARA_KM))
        return

    obs = []
    for o in coorte:
        if o["saida_observada"]:
            t = (o["dias_listado_min"] + int(o["dias_listado_max"])) / 2.0
            obs.append((t, 1))
        else:
            obs.append((float(o["dias_listado_min"]), 0))
    obs.sort()

    linhas, S, varsum = [], 1.0, 0.0
    for t in sorted({t for t, e in obs if e == 1}):
        n_risco = sum(1 for tt, _ in obs if tt >= t)
        d = sum(1 for tt, e in obs if tt == t and e == 1)
        if n_risco == 0:
            continue
        S *= (1 - d / n_risco)
        if n_risco > d:
            varsum += d / (n_risco * (n_risco - d))
        se = S * (varsum ** 0.5)
        linhas.append({"dias": t, "em_risco": n_risco, "saidas": d,
                       "sobrevivencia": round(S, 4),
                       "erro_padrao": round(se, 4),
                       "ic95_inf": round(max(0.0, S - 1.96 * se), 4),
                       "ic95_sup": round(min(1.0, S + 1.96 * se), 4)})
    _escrever(path, linhas)
    mediana = next((l["dias"] for l in linhas if l["sobrevivencia"] <= 0.5), None)
    print("Kaplan-Meier: %d eventos, mediana = %s"
          % (len(eventos), ("%.1f dias" % mediana) if mediana else "nao atingida"))


if __name__ == "__main__":
    main()
