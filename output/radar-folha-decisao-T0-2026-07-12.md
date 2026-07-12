# Radar de Stock — Folha de Decisão · **T0**
**A MatosCar · Usados · 12/07/2026 · Sara Cruz**
*Dados públicos do próprio site (amatoscar.pt). "Saída de stock" é proxy, não venda confirmada.*

---

## A fotografia de hoje

**193 viaturas** usadas em stock online · preço mediano **27.500 €** (de 8.950 € a 171.265 €) · **39% eletrificadas** (45 elétricos + 30 híbridos).

Este é o **ponto de partida (T0)**. A rotação — quanto tempo cada carro fica listado — nasce quando repetirmos a recolha em setembro (T1) e dezembro (T2). Hoje fixamos a base.

---

## Onde está o stock — concentração extrema em Évora

| Distrito | Viaturas | % | Preço mediano |
|---|---:|---:|---:|
| **Évora** | 126 | **65%** | 30.200 € |
| Guarda | 33 | 17% | 26.000 € |
| Castelo Branco | 16 | 8% | 19.700 € |
| Portalegre | 9 | 5% | 20.250 € |
| Beja | 9 | 5% | 23.450 € |
| **Abrantes / Santarém** | **0** | 0% | — |

**Três leituras diretas:**

- **Dois terços do stock estão em Évora — e é lá que estão os carros mais caros** (mediana 30.200 €, acima da média global). Évora não é só o maior armazém do usado; é o de maior valor. É também o distrito onde o Módulo 3 mostrava a MatosCar mais visível: força de stock e força digital coincidem no mesmo sítio.
- **Abrantes/Santarém tem zero viaturas usadas online.** A loja nova (junho 2026) não tem expressão nem na procura (Módulo 3) nem no stock — o digital ainda não acompanhou a abertura física, por dois ângulos independentes.
- **A cauda é fina:** Portalegre (9) e Beja (9) têm stock reduzido. Antes de investir em visibilidade nesses distritos, vale confirmar se há sequer inventário para sustentar procura local.

---

## Que marcas — o volume não são as marcas do audit

| Marca | Stock | | Marca | Stock |
|---|---:|---|---|---:|
| BMW | 27 | | Volkswagen | 12 |
| Nissan | 24 | | Volvo | 11 |
| Hyundai | 23 | | Opel | 11 |
| Kia | 17 | | Audi | 8 |
| Peugeot | 15 | | Fiat | 8 |
| Toyota | 14 | | Citroën 5 · BYD 3 | |
| | | | *Outras (15)* | 15 |

*(Total 193. "Outras" reúne Isuzu, Ford, SEAT, Mercedes-Benz, DS, Cupra, Mitsubishi, Renault, Mini, Skoda e Alfa Romeo.)*

**Leitura para decidir onde medir rotação:** o stock real vive nas marcas de volume (Nissan, Hyundai, Kia, Toyota, Peugeot) e na BMW. As três marcas que o audit apontou como digitalmente fracas — Audi (8), Citroën (5) e **BYD (3)** — têm inventário demasiado pequeno para medir rotação com confiança. **Implicação:** a análise de rotação foca-se nas marcas de volume e em Évora; para a BYD, o sinal útil é a **visibilidade** (perfil de Google), não a rotação.

---

## A decisão deste trimestre

1. **Baseline fixado (T0).** 193 viaturas, com distrito, preço, matrícula e data — a régua contra a qual mediremos setembro e dezembro.
2. **Piloto de visibilidade (independente da rotação):** corrigir o perfil de Google Business da BYD e da Audi (que hoje cedem o espaço a concorrentes) e **re-medir a SERP em 6-8 semanas**. Prova limpa e atribuível, não depende de volume de stock.
3. **A confirmar com a equipa:** porque é que Abrantes não tem stock online — e se a concentração de 65% em Évora reflete a estrutura real do grupo ou uma escolha de exposição digital.

## O que medimos no próximo trimestre (T1, setembro)

- **Rotação-proxy** por distrito e marca (dias-listado), focada em Évora e nas marcas de volume.
- **Efeito do piloto:** a BYD/Audi passaram a ter perfil próprio na pesquisa local?
- **Abrantes:** já aparece algum stock ou visibilidade?

---

## Qualidade dos dados (T0)

| Campo | Completo | Nota |
|---|---:|---|
| matrícula (chave de rotação) | **100%** | única, sem duplicados — rotação fiável em T1 |
| distrito / cidade | **100%** | 193/193 atribuídos a distrito MatosCar |
| preço | 100% | extremos verificados (Twingo 8.950 € · BMW M5 171.265 €) — reais |
| marca · modelo · ano · data matrícula | 100% | — |
| combustível | 99% no CSV · **100% conhecido** | o único em branco é o Nissan Juke 1.0 DIG-T (ficha sem campo de combustível nem ficha técnica); confirmado à mão como **Gasolina** pelo nome do motor (DIG-T = turbo gasolina). Não inferido no automático, para não introduzir adivinhação no pipeline. |
| quilómetros | 91% | 18 em falta = viaturas **quase-novas** (a ficha mostra "Consumo", não km) — ausência genuína, não erro |

*Método: recolha de 12/07/2026 via sitemap do próprio site (193/193 viaturas), fichas lidas individualmente para localização, matrícula e preço. Contagem de linhas (193) bate com o contador "viaturas" do sitemap. Rotação ainda não disponível (precisa de ≥2 recolhas). Nenhum dado de terceiros; nenhuma comparação de preços externa. Parsing validado por testes automáticos (`tests/test_parse.py`).*

---

### Nota de reconciliação (para o dossiê, não para o cliente)

Esta folha substitui o rascunho de 08/07/2026, cujos valores foram escritos a partir de uma recolha que não ficou guardada no projeto. A recolha de 12/07/2026 (`data/stock-snapshots/snapshot-2026-07-12.csv`, 193 linhas) é a primeira fixada e reproduzível — é este o T0 oficial. As diferenças face ao rascunho são pequenas e coerentes com 4 dias de rotação de stock (mediana e extremos idênticos; distritos ±1-2 viaturas).
