# -*- coding: utf-8 -*-
"""
Teste offline dos extractores (sem rede). Gate de validação da lógica de parsing.
Corre a partir da pasta scripts/stock-radar/:  python tests/test_parse.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scrape_stock as S  # noqa: E402

def test_extract_fields():
    text = open(os.path.join(os.path.dirname(__file__), "fixture_l200.txt"), encoding="utf-8").read()
    f = S.extract_fields(text)
    assert f["matricula"] == "AV66RF", f["matricula"]
    assert f["data_matricula"] == "03/01/2023", f["data_matricula"]
    assert f["km"] == 100312, f["km"]
    assert f["combustivel"] == "Diesel", f["combustivel"]
    assert f["potencia_cv"] == 150, f["potencia_cv"]
    assert f["transmissao"] == "Manual", f["transmissao"]
    assert f["stand_cidade"] == "Beja", f["stand_cidade"]
    assert f["stand_marca"] == "Hyundai", f["stand_marca"]   # só o token antes de "A MatosCar"
    assert f["distrito"] == "Beja", f["distrito"]
    assert f["ano"] == 2023, f["ano"]

def test_location_sem_prefixo():
    # ficha sem marca antes de "A MatosCar" (o caso das 23 que falhavam)
    f = S.extract_fields("Hyundai i10 1.0 MPi Comfort MY25 (TT) A MatosCar | Évora Veículos relacionados")
    assert f["distrito"] == "Évora", f["distrito"]
    assert f["stand_cidade"] == "Évora", f["stand_cidade"]

def test_fuel_fallback():
    # quase-novo sem campo rápido "Combustível", mas com "sem chumbo" na ficha
    f = S.extract_fields("Potência 62 CV Transmissão Manual Consumo 5.1 L/100 "
                         "Combustível sem chumbo, 95 e Gasolina")
    assert f["combustivel"] == "Gasolina", f["combustivel"]

def test_clean_title():
    # o og:title real inclui id + "| A MatosCar" — tem de ser limpo
    t = S.clean_title("Mitsubishi L200 2.4 DID-D CD Invite Space Cab 2772879158 | A MatosCar")
    assert t == "Mitsubishi L200 2.4 DID-D CD Invite Space Cab", t
    b, m = S.split_brand_model(t)
    assert b == "Mitsubishi" and m == "L200 2.4 DID-D CD Invite Space Cab", (b, m)

def test_split_brand_model():
    b, m = S.split_brand_model("Mitsubishi L200 2.4 DID-D CD Invite Space Cab")
    assert b == "Mitsubishi", b
    assert m.startswith("L200"), m
    b2, _ = S.split_brand_model("Mercedes Benz Classe A 180d")
    assert b2 == "Mercedes Benz", b2

def test_ids_from_listing():
    sample = ('[](https://www.amatoscar.pt/carro-usado/kia-stonic-1-0-t-gdi-6mt-drive-2772817124/ "x") '
              '[Ver carro](https://www.amatoscar.pt/carro-usado/kia-stonic-1-0-t-gdi-6mt-drive-2772817124/)')
    ids = S.extract_listing_ids(sample)
    assert ids == [("2772817124", "/carro-usado/kia-stonic-1-0-t-gdi-6mt-drive-2772817124/")], ids

if __name__ == "__main__":
    n = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print("OK  %s" % name); n += 1
    print("\n%d testes passaram." % n)
