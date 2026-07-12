# -*- coding: utf-8 -*-
"""
Configuração do Radar de Stock — amatoscar.pt (site do próprio cliente).

Fundamentado na estrutura REAL do site, inspecionada em 08/07/2026:
- Listagem: /carros-usados/ , paginada /carros-usados/2 ... /carros-usados/N
- Ficha:    /carro-usado/<slug>-<id>/  (o <id> final é o ID do anúncio)
- A ficha expõe: og:price:amount (preço), e um bloco "Informações" com
  Potência, Transmissão, Quilómetros, Data matrícula, Combustível, Matrícula,
  e a localização no formato "<Marca> A MatosCar | <Cidade>".

robots.txt (08/07/2026): só bloqueia /wp-admin/. Crawl-delay: 10s → RESPEITAR.
"""

BASE = "https://www.amatoscar.pt"
# Fonte de inventário: o sitemap dedicado aos usados (All in One SEO), atualizado
# diariamente. Fonte CANÓNICA e fiável — 191 URLs em 08/07/2026, a bater com o
# contador "191 viaturas" do site. Preferível à paginação da listagem, que é
# enganosa: /carros-usados/2 devolve a MESMA página 1 (verificado em 08/07/2026).
SITEMAP_USED = BASE + "/coches-ocasion-sitemap.xml"

# Politesse — o robots.txt pede Crawl-delay de 10 segundos. Não baixar disto.
CRAWL_DELAY_SECONDS = 10
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
# User-agent identificável, com contacto (boa prática; é o site do cliente).
USER_AGENT = "MatosCar-StockRadar/1.0 (analista: Sara Cruz; contacto: saramscruz@gmail.com)"

# Enriquecer cada anúncio visitando a ficha (necessário para localização/distrito,
# matrícula e data de matrícula). Se False, faz só o inventário rápido da listagem.
ENRICH_DETAIL = True

# Pastas de saída (relativas à raiz do projeto)
SNAPSHOT_DIR = "data/stock-snapshots"

# Marcas canónicas (do filtro do próprio site) — usadas para separar marca de modelo.
# Nota: as de duas palavras têm de vir antes para o "startswith" mais longo ganhar.
BRANDS = [
    "Alfa Romeo", "Mercedes Benz",
    "Audi", "BMW", "BYD", "Citroen", "Cupra", "DS", "Fiat", "Ford",
    "Hyundai", "Isuzu", "Kia", "Mitsubishi", "Nissan", "Opel", "Peugeot",
    "Renault", "SEAT", "Skoda", "Toyota", "Volkswagen", "Volvo",
]

# Mapa cidade->distrito MatosCar. A localização da ficha vem como "| <Cidade>".
# CONFIRMADO em 08/07/2026: "Beja". As restantes são o mapeamento esperado dos
# stands do grupo (Guarda, Castelo Branco, Portalegre, Évora, Beja + nova zona
# Abrantes/Santarém). ESTENDER à medida que aparecerem novas cidades no campo.
CATCHMENT = {
    "beja": "Beja",
    "évora": "Évora", "evora": "Évora",
    "portalegre": "Portalegre",
    "castelo branco": "Castelo Branco", "covilhã": "Castelo Branco",
    "covilha": "Castelo Branco", "fundão": "Castelo Branco", "fundao": "Castelo Branco",
    "guarda": "Guarda",
    "abrantes": "Santarém (Abrantes)", "santarém": "Santarém", "santarem": "Santarém",
}

def city_to_district(city: str) -> str:
    """Mapeia a cidade do stand para o distrito MatosCar (exata ou por prefixo mais longo)."""
    if not city:
        return "(desconhecido)"
    low = city.strip().lower()
    if low in CATCHMENT:
        return CATCHMENT[low]
    for key in sorted(CATCHMENT, key=len, reverse=True):
        if low.startswith(key):
            return CATCHMENT[key]
    return city.strip() + " (a mapear)"
