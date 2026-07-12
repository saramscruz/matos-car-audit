# Radar de Stock — scraper do amatoscar.pt (Fase 1)

Captura o inventário de **usados** do site do próprio cliente e, ao longo do tempo,
mede a **rotação** (proxy) por marca e por distrito. Faz parte do projeto
"Radar de Procura e Rotação Local" (`prd/radar-procura-rotacao-local.md`).

> **Regra de ouro:** "desaparecer do stock" **não** é "vendido". Este scraper mede
> **presença** no site. A rotação é um **proxy**, nunca uma venda confirmada — e tem
> de ser sempre apresentada assim.

---

## Porque é sem risco

- Alvo: **amatoscar.pt**, o site do próprio cliente (com a autorização dele). Não há
  agregação de terceiros — a Standvirtual/OLX ficam deliberadamente de fora.
- `robots.txt` (verificado 08/07/2026): só bloqueia `/wp-admin/`. `/carros-usados/` e
  `/carro-usado/` são permitidos, com **Crawl-delay: 10s** — que o scraper respeita.

## Estrutura verificada (08/07/2026)

Inspecionei a estrutura real antes de escrever os seletores (não são um palpite):

- **Inventário:** lido do **sitemap** `coches-ocasion-sitemap.xml` (191 URLs em
  08/07/2026, a bater com o contador "191 viaturas" do site). **Atenção:** a paginação
  visível (`/carros-usados/2`) é enganosa — devolve sempre a página 1 (verificado
  08/07/2026); por isso o inventário vem do sitemap, que é a fonte canónica.
- **Ficha:** `/carro-usado/<slug>-<id>/`. Expõe:
  - preço via meta-tag padrão `og:price:amount` (estável);
  - bloco "Informações": Potência, Transmissão, Quilómetros, **Data matrícula**,
    Combustível, **Matrícula** (ID único e estável do carro);
  - **localização**: `"<Marca> A MatosCar | <Cidade>"` → dá o **distrito** (catchment).
- Os seletores assentam em **meta-tags padrão + rótulos de texto**, não em classes CSS
  frágeis. Por isso resistem a mudanças de tema do site.

---

## Instalar

```bash
pip install requests beautifulsoup4
```

## Correr

```bash
# 1) Capturar o snapshot de hoje (listagem + fichas; respeita o crawl-delay de 10s)
python scrape_stock.py
#    -> data/stock-snapshots/snapshot-AAAA-MM-DD.csv

# variantes:
python scrape_stock.py --lite        # só inventário do sitemap, sem localização (rápido)
python scrape_stock.py --limit 3     # teste rápido: só 3 viaturas (visita 3 fichas)

# 2) Só quando houver >= 2 snapshots (ex.: um agora, outro daqui a 4-6 semanas):
python merge_snapshots.py
#    -> _rotacao.csv  +  _rotacao-por-distrito-marca.csv
```

**Tempo de execução:** com crawl-delay de 10s e ~191 fichas, um snapshot completo
demora **~35 min**. É deliberado (politesse). Para um ciclo trimestral, é irrelevante.

---

## Gate de validação (correr antes de confiar em qualquer número)

1. **Lógica de parsing (offline, sem rede):**
   ```bash
   python tests/test_parse.py     # deve imprimir "6 testes passaram."
   ```
   Já validado em 08/07/2026 contra o texto real da ficha (fixture do L200).
2. **Contagem:** o nº de linhas do snapshot tem de bater (±poucas unidades, o stock muda)
   com o contador **"N viaturas"** do site. Se der zero ou metade, **parar** e rever.
3. **Spot-check:** abrir 5 fichas no browser (DevTools) e confirmar à mão que preço, km,
   matrícula e cidade no CSV coincidem com a página.

Só depois destes três passos os números entram num relatório.

---

## Esquema do snapshot (`snapshot-AAAA-MM-DD.csv`)

`snapshot_date, id, matricula, marca, modelo_versao, ano, combustivel, km,
preco_eur, potencia_cv, transmissao, stand_marca, stand_cidade, distrito,
data_matricula, url`

Chave estável do veículo = **matrícula** (a ficha expõe-na); se faltar, usa-se o `id` do anúncio.

## Estado desta entrega (honesto)

- **Feito e validado:** estrutura inspecionada; scraper + config + merge escritos;
  extractores testados contra a página real (`tests/`); esquema definido; catchment por
  distrito resolvido via ficha.
- **Amostra de demonstração:** `data/stock-snapshots/snapshot-2026-07-08-SAMPLE.csv` —
  **12 viaturas** (a 1ª página da listagem, capturada em 08/07/2026; a ficha do L200 já
  enriquecida com localização = Beja). Serve para veres o formato com dados reais.
- **Por correr na tua máquina:** o snapshot **completo (~191)** — este ambiente não tem
  rede aberta para o site. Corre `python scrape_stock.py` no teu computador; deve produzir
  ~191 linhas. Repete daqui a 4-6 semanas para o `merge` dar a primeira rotação.

## Limitações a declarar sempre

- **Proxy ≠ venda.** Saída do stock pode ser venda, devolução, re-anúncio ou erro.
- **`dias_listado_min` é limite inferior** — o carro pode ter entrado antes do 1º snapshot.
- **Catchment** vem do campo "A MatosCar | Cidade" da ficha (com ou sem marca antes).
  Confirmado em 08/07/2026 para Beja, Guarda, Portalegre, Évora e Castelo Branco;
  distrito preenchido em ~100% do stock. Abrantes/Santarém = 0 viaturas.
- **Viaturas quase-novas:** a ficha de um carro (quase) novo mostra "Consumo" em vez de
  "Quilómetros" e omite o campo rápido "Combustível". Nesses casos **km fica vazio de
  propósito** (não há km real a reportar) e o combustível é recuperado da ficha técnica
  apenas quando é inequívoco ("sem chumbo"→Gasolina, "gasóleo"→Diesel); caso contrário
  fica vazio (nunca se adivinha elétrico/híbrido). Completude T0 (snapshot 12/07/2026, 193 viaturas): km ~91%, combustível ~99% (1 em falta).
- **Uso interno/analítico**, com autorização do cliente. Sem republicação de comparações
  com preços de terceiros (ver nota legal no PRD).
