# -*- coding: utf-8 -*-
"""
Resumo de um snapshot de stock (T0). Não precisa de rede.
USO:  python resumo_snapshot.py
Lê o snapshot mais recente em data/stock-snapshots/ e imprime a fotografia:
total, preço mediano, distribuição por distrito, por marca e por combustível.
"""
import csv, glob, io, os, statistics
from collections import Counter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SNAPDIR = os.path.join(ROOT, "data", "stock-snapshots")

def num(x):
    try:
        return int(x)
    except Exception:
        return None

def main():
    files = [f for f in sorted(glob.glob(os.path.join(SNAPDIR, "snapshot-*.csv")))
             if "SAMPLE" not in f.upper()]
    if not files:
        print("Sem snapshots em", SNAPDIR); return
    path = files[-1]
    raw = open(path, "rb").read().replace(b"\x00", b"").decode("utf-8", "ignore")
    rows = list(csv.DictReader(io.StringIO(raw)))
    print("Ficheiro:", os.path.basename(path))
    print("TOTAL viaturas:", len(rows))

    prec = [num(r.get("preco_eur")) for r in rows]
    prec = [p for p in prec if p]
    if prec:
        print("Preço — mediano: %d€ | min: %d€ | max: %d€ (%d com preço)"
              % (statistics.median(prec), min(prec), max(prec), len(prec)))
    semloc = sum(1 for r in rows if not r.get("distrito")
                 or "sem localiz" in r["distrito"] or "mapear" in r["distrito"])
    print("Distrito por mapear/sem localização:", semloc)

    print("\n=== POR DISTRITO ===")
    for d, n in Counter((r.get("distrito") or "(vazio)") for r in rows).most_common():
        ps = [num(r.get("preco_eur")) for r in rows if (r.get("distrito") or "(vazio)") == d]
        ps = [p for p in ps if p]
        med = ("%d€" % statistics.median(ps)) if ps else "-"
        print("  %-28s %3d   preço mediano %s" % (d, n, med))

    print("\n=== POR MARCA (top 15) ===")
    for m, n in Counter((r.get("marca") or "?") for r in rows).most_common(15):
        print("  %-16s %3d" % (m, n))

    print("\n=== COMBUSTÍVEL ===")
    for c, n in Counter((r.get("combustivel") or "(vazio)") for r in rows).most_common():
        print("  %-12s %3d" % (c, n))

if __name__ == "__main__":
    main()
