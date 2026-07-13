# -*- coding: utf-8 -*-
"""
Junta os snapshots datados e calcula o PROXY de rotação por veículo.

USO:  python merge_snapshots.py
LÊ :  data/stock-snapshots/snapshot-AAAA-MM-DD_HHMMSS.csv  (>= 2 datas p/ rotação;
      várias capturas no mesmo dia -> usa a mais recente desse dia)
GERA: data/stock-snapshots/_rotacao.csv           (por veículo)
      data/stock-snapshots/_rotacao-por-distrito-marca.csv (resumo)

DEFINIÇÕES (declarar sempre):
  first_seen  = 1ª data em que o veículo aparece nos snapshots
  last_seen   = última data em que aparece
  dias_listado_min = last_seen - first_seen   (LIMITE INFERIOR: o carro pode ter
                    entrado antes do 1º snapshot e/ou saído entre snapshots)
  estado      = "em stock" se está no snapshot mais recente; senão "saiu do stock"
  "saiu do stock" != "vendido" — pode ser venda, devolução, re-anúncio ou erro.
  Chave do veículo = matrícula (estável); se faltar, cai no id do anúncio.
"""
import csv
import glob
import os
import statistics
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SNAPDIR = os.path.join(ROOT, "data", "stock-snapshots")

# Fracao do maior snapshot abaixo da qual uma captura e tratada como partida e
# ignorada (mesma logica do gate do README: "se der zero ou metade, parar").
# Evita que uma recolha incompleta injete uma data falsa e contamine a rotacao.
MIN_SNAPSHOT_FRACTION = 0.5

def load_snapshots():
    files = sorted(glob.glob(os.path.join(SNAPDIR, "snapshot-*.csv")))
    files = [f for f in files if "SAMPLE" not in f.upper()]
    loaded = []
    for f in files:
        stamp = os.path.basename(f).replace("snapshot-", "").replace(".csv", "")
        date = stamp[:10]  # AAAA-MM-DD (o resto do nome, se existir, e a hora)
        with open(f, encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        loaded.append((date, stamp, rows))
    # Guarda de sanidade: descartar capturas com contagem implausivelmente baixa
    # (< metade da maior recolha), para uma captura partida nao poluir a rotacao.
    if loaded:
        max_rows = max(len(rows) for _, _, rows in loaded)
        kept = []
        for date, stamp, rows in loaded:
            if max_rows and len(rows) < MIN_SNAPSHOT_FRACTION * max_rows:
                print("  [aviso] captura %s ignorada: %d linhas (< %d%% da maior "
                      "recolha, %d) - provavelmente incompleta." %
                      (stamp, len(rows), int(MIN_SNAPSHOT_FRACTION * 100), max_rows))
            else:
                kept.append((date, stamp, rows))
        loaded = kept
    # Cada recolha e um ficheiro proprio; se houver varias no mesmo dia, a rotacao
    # usa a mais recente desse dia (o maior timestamp no nome do ficheiro).
    by_date = {}
    for date, stamp, rows in loaded:
        if date not in by_date or stamp > by_date[date][0]:
            by_date[date] = (stamp, rows)
    return [(date, rows) for date, (stamp, rows) in sorted(by_date.items())]

def key(row):
    return (row.get("matricula") or "").strip() or ("id:" + (row.get("id") or "").strip())

def main():
    snaps = load_snapshots()
    if len(snaps) < 2:
        print("Só há %d snapshot(s). A rotação precisa de pelo menos 2 datas." % len(snaps))
        print("Este é o comportamento esperado no arranque: capturar hoje, repetir daqui a semanas.")
        return
    dates = [d for d, _ in snaps]
    latest = dates[-1]

    veh = {}
    for date, rows in snaps:
        for r in rows:
            k = key(r)
            v = veh.setdefault(k, {"first_seen": date, "last_seen": date, "row": r})
            v["last_seen"] = date
            v["first_seen"] = min(v["first_seen"], date)
            if date == latest:
                v["row"] = r  # dados mais recentes

    out = []
    for k, v in veh.items():
        r = v["row"]
        d0 = _d(v["first_seen"]); d1 = _d(v["last_seen"])
        dias = (d1 - d0).days
        estado = "em stock" if v["last_seen"] == latest else "saiu do stock"
        out.append({
            "chave": k, "marca": r.get("marca"), "modelo_versao": r.get("modelo_versao"),
            "distrito": r.get("distrito"), "preco_eur": r.get("preco_eur"),
            "first_seen": v["first_seen"], "last_seen": v["last_seen"],
            "dias_listado_min": dias, "estado": estado,
        })

    per_vehicle = os.path.join(SNAPDIR, "_rotacao.csv")
    with open(per_vehicle, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader(); w.writerows(out)

    # Resumo por distrito x marca (mediana de dias dos que SAÍRAM = proxy de rotação)
    grp = defaultdict(list)
    for o in out:
        if o["estado"] == "saiu do stock":
            grp[(o["distrito"], o["marca"])].append(o["dias_listado_min"])
    summary = []
    for (dist, marca), vals in sorted(grp.items()):
        summary.append({"distrito": dist, "marca": marca, "saidos": len(vals),
                        "dias_mediana_proxy": round(statistics.median(vals), 1)})
    per_group = os.path.join(SNAPDIR, "_rotacao-por-distrito-marca.csv")
    with open(per_group, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["distrito", "marca", "saidos", "dias_mediana_proxy"])
        w.writeheader(); w.writerows(summary)

    print("Veículos acompanhados: %d (%d datas: %s)" % (len(out), len(dates), ", ".join(dates)))
    print("Escrito: %s" % per_vehicle)
    print("Escrito: %s" % per_group)
    print("LEMBRETE: 'saiu do stock' é PROXY, não venda confirmada.")

def _d(s):
    import datetime
    return datetime.date.fromisoformat(s)

if __name__ == "__main__":
    main()
