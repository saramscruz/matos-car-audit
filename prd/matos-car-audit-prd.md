# PRD — MatosCar Regional Demand Audit
**Versão 2 — Junho 2026**

---

## Project overview

A short-form digital demand audit for A MatosCar, covering five brands across the full group geography plus the new Abrantes location. Deliverable is a PDF report pitched to Pedro Matos, owner of the group, as a freelance analytical engagement.

---

## Objective

Identify where digital search demand for MatosCar's key brands exists across their operating regions, cross-reference it with their current digital funnel, and produce 3-5 actionable recommendations.

---

## Audience

Pedro Matos — group owner, non-technical. Report must be readable without analytical background. Data supports the argument; it does not lead it. The goal is for Pedro Matos to find at least one thing he did not know before.

---

## Brands in scope — and why these five

| Marca | Posicionamento | Razão de inclusão |
|-------|---------------|-------------------|
| BMW | Premium europeu | Volume premium mais pesquisado em PT; presença histórica MatosCar |
| Audi | Premium europeu | Concorre directamente com BMW; base de procura sólida em PT |
| Volkswagen | Volume europeu mainstream | Marca de maior volume histórico; âncora do portfólio |
| BYD | EV emergente, preço de entrada | Early mover regional; dinâmica de procura ainda em formação |
| Citroën | Volume mainstream, EV acessível | ë-C3 como entrada EV; renovação recente do C3 em 2024 |

**Nota de justificação para o relatório:** estas cinco marcas cobrem o espectro completo do portfólio MatosCar — premium europeu com volume (BMW, Audi, VW), EV emergente com preço de entrada (BYD) e volume mainstream com presença histórica forte e transição eléctrica activa (Citroën). As restantes marcas do grupo ficam fora de âmbito neste primeiro engagement.

---

## Geography in scope

| Distrito / Região | Capital | Módulo 1 (Trends) | Módulo 3 (Visibilidade) |
|-------------------|---------|-------------------|------------------------|
| Centro / Beira Interior | Castelo Branco | ✓ | ✓ |
| Alentejo Central | Évora | ✓ | ✓ |
| Baixo Alentejo | Beja | ✓ | ✓ |
| Alto Alentejo | Portalegre | ✓ | ✓ |
| Beira Interior Norte | Guarda | ✓ | ✓ |
| Santarém (Abrantes — nova abertura junho 2026) | Abrantes / Santarém | — | ✓ |

**Nota sobre Abrantes:** a MatosCar abriu em Abrantes em junho de 2026 (confirmado no banner da homepage em 29/06/2026). Esta presença não estava na geografia original. O Módulo 3 cobre Abrantes e Santarém para avaliar se a nova abertura tem já visibilidade digital — ou se é um dealer fisicamente aberto mas digitalmente invisível.

Google Trends regional data used where available. Portugal-level data used as baseline where regional granularity is insufficient.

---

## Out of scope

- Todas as outras marcas do portfólio MatosCar (Kia, Hyundai, Toyota, Opel, Peugeot, Nissan, Fiat, Volvo, Mercedes, Skoda, Dacia, DS, Isuzu, Ford, etc.)
- Paid advertising performance (sem acesso à conta Google Ads)
- CRM ou dados internos de vendas (sem acesso)
- Granularidade ao nível da cidade (Google Trends não suporta filtragem por cidade de forma fiável)
- Execução das recomendações (este engagement é de análise e proposta; execução a negociar em follow-up)

---

## Limitações metodológicas — a declarar explicitamente no relatório

O Google Trends tem restrições que o relatório deve reconhecer:

- **Índice relativo, não volume absoluto.** O índice 0-100 representa interesse relativo ao pico no período; não é número de pesquisas.
- **Distritos com população pequena** (Portalegre, Beja, Guarda) frequentemente retornam "dados insuficientes" a nível sub-regional.
- **Comparações entre marcas de volume muito diferente distorcem a escala.** BMW e BYD no mesmo gráfico fazem o BYD aparecer quase a zero — não por ausência de procura, mas por diferença de escala. As queries correm separadas por marca; a comparação multi-marca é usada apenas como visão geral contextual.
- **Os dados são retrospectivos e actualizados dinamicamente.** A data de cada pesquisa é registada em todas as capturas.

Declarar estas limitações não é fraqueza — é credibilidade.

---

## Methodology

### Módulo 0 — Visão geral comparativa (fazer primeiro)

Antes de qualquer query individual, correr esta pesquisa única:

**Query:** `BMW, Audi, Volkswagen, BYD, Citroën`
**Janela:** Últimos 12 meses
**Geografia:** Portugal

Tirar screenshot. Este gráfico estabelece a hierarquia de interesse relativo entre as cinco marcas a nível nacional. É o dado de contexto que enquadra todos os findings individuais. Se mostrar algo inesperado (ex: BYD a ganhar terreno sobre Citroën), essa é a primeira descoberta do relatório.

---

### Módulo 1 — Search demand (Google Trends PT)

#### Regras de consistência — obrigatórias

1. **Nunca comparar marcas no mesmo gráfico** (excepto Módulo 0). As escalas são incompatíveis. Cada query corre isolada.
2. **Janela temporal fixa: últimos 12 meses** (julho 2025 — junho 2026). Registar a data exacta de cada pesquisa.
3. **Geographies em sequência fixa:** primeiro Portugal (baseline nacional), depois sub-região disponível mais próxima da área de operação. Registar exactamente o que o Google Trends devolve — "Região Centro", "Beira Interior", "dados insuficientes", etc.

#### Queries por marca

**BMW**

| Query | Propósito |
|-------|-----------|
| `BMW` | Interesse geral na marca |
| `BMW Série 1` | Modelo de entrada — maior volume esperado |
| `BMW eléctrico` | Intenção EV na marca premium |
| `BMW concessionário` | Intenção de compra local |

**Audi**

| Query | Propósito |
|-------|-----------|
| `Audi` | Interesse geral |
| `Audi A3` | Modelo de maior volume histórico em PT |
| `Audi eléctrico` | Intenção EV |
| `Audi concessionário` | Intenção local |

**Volkswagen**

| Query | Propósito |
|-------|-----------|
| `Volkswagen` | Interesse geral |
| `VW Golf` | Modelo âncora — referência histórica |
| `VW eléctrico` | Intenção EV — ID.3/ID.4 |
| `Volkswagen concessionário` | Intenção local |

**BYD**

| Query | Propósito |
|-------|-----------|
| `BYD` | Interesse geral — baseline de reconhecimento de marca |
| `BYD Dolphin` | Modelo de entrada mais pesquisado em PT |
| `BYD preço` | Intenção de compra — sinal mais valioso para marca nova sem rede de retalho estabelecida |
| `BYD Portugal` | Especificidade geográfica — marca ainda em afirmação nacional |

*Nota: para BYD, `BYD preço` é provavelmente mais reveladora do que `BYD concessionário` — pessoas que ainda não sabem que existe um dealer local vão pesquisar preço primeiro.*

**Citroën**

| Query | Propósito |
|-------|-----------|
| `Citroën` | Interesse geral |
| `Citroën C3` | Modelo de maior volume — renovado em 2024 |
| `Citroën eléctrico` | Intenção EV — ë-C3 |
| `Citroën concessionário` | Intenção local |

#### Template de registo — por query

Para cada uma das 20 queries (4 por marca × 5 marcas), preencher:

```
Query: [texto exacto pesquisado]
Data da pesquisa: [dd/mm/aaaa]
Janela: Últimos 12 meses
Geografia testada: Portugal / [sub-região se disponível]

Índice médio: [0-100 — valor visual da linha]
Pico: [mês e índice aproximado]
Vale: [mês e índice aproximado]
Tendência: Crescente / Estável / Decrescente / Sazonal

Top 5 queries relacionadas — secção "Em alta":
1.
2.
3.
4.
5.

Top 5 queries relacionadas — secção "Top":
1.
2.
3.
4.
5.

Dados regionais devolvidos: Sim / Não / Insuficientes
Se sim, regiões com índice mais alto:
1.
2.
3.

Observação livre (uma frase — esta frase vai para o relatório):
```

**A observação livre não é opcional.** É onde se escreve o finding que aparece na página da marca.

**Output do módulo:** demand tier por marca (High / Medium / Low / Emerging) e um finding distintivo por marca.

---

### Módulo 2 — Digital funnel observation

Walk do site amatoscar.pt para cada uma das 5 marcas.

**Checkpoints:**

| # | Checkpoint |
|---|-----------|
| 1 | A marca é encontrável a partir da homepage? |
| 2 | Existe uma página dedicada ao modelo ou listing de stock? |
| 3 | O preço está visível no listing? |
| 4 | Existe um CTA "Reservar" ou equivalente? |
| 5 | O que acontece ao clicar "Reservar"? |
| 6 | Existe formulário de contacto? Que campos tem? |
| 7 | A página é mobile-friendly a 390px? |
| 8 | Existe live chat ou opção de callback? |
| 9 | Existem campanhas activas para esta marca? |
| 10 | Existe conteúdo específico sobre EV para esta marca? |

Registar observações com screenshots. Data de observação indicada em todas as evidências.

---

### Módulo 3 — Competitive visibility

Para cada marca, uma pesquisa Google em Chrome incógnito a 390px para cada distrito.

**Distritos (6):** Castelo Branco, Évora, Beja, Portalegre, Guarda, Abrantes/Santarém

**Queries:**

- `[marca] [capital de distrito]` (ex: "BMW Castelo Branco", "Citroën Évora", "BYD Portalegre")

**Para Abrantes/Santarém, correr dois formatos por marca:**
- `[marca] Abrantes`
- `[marca] Santarém`

Total de pesquisas: 35 (5 marcas × 5 distritos originais + 5 marcas × 2 queries Abrantes/Santarém = 35)

**Registar para cada pesquisa:**

- A MatosCar aparece nos resultados?
- Quem mais aparece (dealers concorrentes)?
- Existe listagem Google Maps / Business da MatosCar para esta marca nesta cidade?
- Existem anúncios pagos? De quem?

**Nota sobre Abrantes:** o objectivo específico aqui é detectar a tensão entre presença física (abertura junho 2026) e presença digital. Se a MatosCar abriu mas não aparece nas pesquisas locais, isso é um finding accionável imediato para Pedro Matos.

Observação de superfície apenas — sem análise aprofundada de concorrentes.

---

## Deliverable — PDF report structure

| Página | Conteúdo |
|--------|---------|
| 1 | Capa — A MatosCar · Análise de Procura Digital · Portugal Interior · 2026 · Prepared by Sara Cruz |
| 2 | Executive summary — 3 frases máximo. Um finding principal. Uma recomendação headline. |
| 3 | Nota metodológica — o que foi medido, como, e o que não foi. Limitações declaradas explicitamente. Justificação da selecção das 5 marcas. |
| 4–8 | Findings por marca — uma página por marca (ver estrutura abaixo) |
| 9 | Findings transversais — 2-3 observações across all five brands. Tensão EV: procura em crescimento vs. prontidão digital do funil. Nota sobre Abrantes. |
| 10 | Recomendações — 3-5 recomendações específicas e accionáveis. Foco em quick wins. Para cada recomendação: o que deve ser feito, por quem, e o que desbloquearia. |
| 11 | Próximos passos — o que um follow-up engagement incluiria. Que acesso a dados desbloquearia análise mais profunda (GA, Google Ads, CRM). |

**Estrutura da página por marca (páginas 4-8):**

- Procura: índice, tendência, query distintiva
- Funil digital: o que funciona, o que está em falta
- Visibilidade competitiva: a MatosCar aparece nos 6 distritos?
- Um finding, numa frase

---

## File structure

```
matos-car-audit/
  README.md
  prd/
    matos-car-audit-prd-v2.md
  methodology/
    google-trends-protocol.md
    funnel-observation-checklist.md
  brands/
    bmw.md
    audi.md
    volkswagen.md
    byd.md
    citroen.md
  assets/
    bmw/
      trends/
      funnel/
      competitive/
    audi/
      trends/
      funnel/
      competitive/
    volkswagen/
      trends/
      funnel/
      competitive/
    byd/
      trends/
      funnel/
      competitive/
    citroen/
      trends/
      funnel/
      competitive/
  report/
    matos-car-demand-audit-2026.pdf
```

---

## Sequencing

### Semana 1 — Fieldwork

| Dia | Tarefa |
|-----|--------|
| Dia 1 | Módulo 0: pesquisa comparativa das 5 marcas. Módulo 1: Google Trends para todas as 5 marcas — 20 queries + template de registo completo. Screenshots e notas em brands/[marca].md. |
| Dia 2 | Módulo 2: Observação do site para todas as 5 marcas. Screenshots em assets/[marca]/funnel/. Notas em brands/[marca].md. |
| Dia 3 | Módulo 3: 35 pesquisas competitivas — 5 marcas × 7 queries distritais (incluindo Abrantes/Santarém duplo formato). Notas em brands/[marca].md. |

### Semana 2 — Report

| Dia | Tarefa |
|-----|--------|
| Dia 4 | Escrever páginas de findings por marca (5 páginas). |
| Dia 5 | Escrever executive summary, findings transversais, recomendações, próximos passos. |
| Dia 6 | Design e produção do PDF. |
| Dia 7 | Revisão, correcção, finalização. |

---

## Success criteria

- Pedro Matos lê o relatório e encontra pelo menos uma coisa que não sabia.
- Pelo menos uma recomendação é accionada.
- O engagement abre conversa sobre acesso mais profundo (GA, Ads, CRM).

---

## What this is not

- Um audit completo de marketing digital
- Um audit de SEO
- Um audit de paid media
- Uma análise de CRM
- Um relatório de inteligência competitiva

É um demand signal audit — mostra onde existe interesse e se o funil digital está posicionado para o capturar.

---

## Changelog

| Versão | Data | Alterações |
|--------|------|-----------|
| v1 | — | PRD inicial |
| v2 | 29/06/2026 | Geografia actualizada: Santarém/Abrantes adicionado (nova abertura junho 2026). Justificação formal da selecção das 5 marcas. Módulo 1 redesenhado: protocolo Google Trends com regras de consistência, queries exactas por marca, template de registo estruturado, Módulo 0 adicionado. Módulo 3 expandido: 35 pesquisas (era 25). Limitações metodológicas formalizadas em secção própria. Observação de surface do site (amatoscar.pt) incorporada como contexto. Âmbito das recomendações clarificado: proposta, não execução. |
