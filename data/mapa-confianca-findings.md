# Mapa de Confiança dos Findings — MatosCar Regional Demand Audit

**Data:** 07/07/2026
**Âmbito:** classifica os findings dos Módulos 1 (Google Trends), 2 (funil digital) e 3 (visibilidade competitiva) por nível de confiança, para orientar a redação do relatório final.
**Objectivo:** decidir o que **lidera** o relatório, o que serve de **suporte enquadrado**, e o que fica como **pergunta de follow-up** em vez de afirmação ao cliente.

---

## Como ler este mapa

Três níveis de confiança:

- **Alta** — observação directa e verificável, ou facto estrutural (configuração, presença/ausência) que não muda numa nova recolha. É onde o relatório deve assentar as afirmações fortes.
- **Média** — observação única mas plausível e internamente consistente; ou dado do Trends que é comparável mas grosseiro. Usar como suporte, sempre com o enquadramento da limitação.
- **Especulativa** — snapshot único que pode mudar, inferência, ou anomalia por explicar. Não afirmar ao cliente; apresentar como pergunta ou hipótese.

**Caveat transversal (aplica-se a tudo abaixo):** cada módulo resulta de **uma única sessão de recolha, por um investigador, sem repetição** — e o Módulo 3 num único browser/IP (com uma contaminação de geolocalização já confirmada). Os dados do Google Trends são, além disso, um snapshot dinâmico: entre 30/06 e 07/07/2026 um finding central mudou o suficiente para colapsar. Por isso, mesmo os findings "Alta" baseados no Trends referem-se à **forma** do dado (hierarquia, presença/ausência), não a posições numéricas exactas.

---

## Findings de Confiança ALTA — devem liderar o relatório

Quase todos vêm dos Módulos 2 e 3 (observação directa de configuração e presença), não do Trends.

| # | Finding | Evidência | Porque é Alta |
|---|---------|-----------|---------------|
| A1 | **A MatosCar cede o Knowledge Panel a concorrentes ou à marca errada em Audi e BYD** (Google Business Profile mal segmentado por marca). | M3, observado em vários distritos (Castelo Branco, Portalegre, etc.). | Facto estrutural de configuração; consistente entre distritos; não muda numa nova recolha. É o achado mais accionável do audit. |
| A2 | **Audi e Volkswagen têm visibilidade fraca ou nula da MatosCar em todo o território.** | M3, 6-7 distritos. Audi: 1/7 com presença; VW: fraco no orgânico (1/7). | Padrão consistente em todos os distritos — estrutural, não geográfico. |
| A3 | **BMW e Citroën têm presença digital forte e consistente nos 5 distritos históricos.** | M3, presença em Local Pack/KP e orgânico. | Padrão repetido e estável. |
| A4 | **Abrantes/Santarém: ausência digital total da MatosCar nas 5 marcas, nos dois formatos de pesquisa.** | M3, 0/5 em Abrantes e 0/5 em Santarém. | Ausência simétrica e total; corroborada pela abertura física ser de junho/2026 (nova). Forte e accionável. |
| A5 | **Zero investimento pago da MatosCar em 35 pesquisas; concorrência anunciou em 7.** | M3, 0/35. | Observação directa e exaustiva. |
| A6 | **Existe um mecanismo de reserva real e funcional — mas só nos USADOS** (sinal de 300€, stock com matrícula, preço fixo, CTA "Reservar"). | M2 CP10, confirmado em 3 marcas (Peugeot, Mercedes, VW). | Observado directamente; template partilhado. Reenquadra o "sem venda online" dos CP2/4/5. |
| A7 | **As páginas de carros NOVOS das 5 marcas não têm CTA de avanço comercial** — só "Quero experimentar" (test-drive). | M2 CP4, 5/5. | Observado directamente nas 5. |
| A8 | **As 5 marcas do audit estão ausentes do hub /veiculos-eletricos/** (os destaques são de outras marcas do grupo). | M2 CP10. | Observado directamente. |
| A9 | **Não há contacto telefónico por instalação — só uma linha central.** | M2 CP8. | Observado directamente. |
| A10 | **"[marca] concessionário" não tem volume de pesquisa mensurável** (5 marcas, resultado nulo; BYD sem sequer série temporal). | M1, 5 réplicas nulas. | Cinco nulos independentes na mesma recolha — robusto como afirmação sobre este termo neste mercado. |
| A11 | **Os picos de "[marca] eléctrico" estão dispersos entre março e junho de 2026, não num pico único de fev/março.** | M1, verificado contra os CSVs (BMW mar, Audi/BYD abr, Citroën mai, VW jun). | Facto de série temporal verificado ao dado. |

---

## Findings de Confiança MÉDIA — suporte, sempre com enquadramento

| # | Finding | Evidência | Porque é Média (o enquadramento a incluir) |
|---|---------|-----------|--------------------------------------------|
| M1 | **Hierarquia de procura absoluta: BMW ≫ Audi ≫ Citroën > {VW ≈ BYD}.** | Módulo 0 (única fonte comparável). | O topo (BMW, depois Audi) é sólido; a base (Citroën vs VW vs BYD) é frágil e **VW/BYD são indistinguíveis** a esta escala. Recolha única, lida de um gráfico. |
| M2 | **A EV é procura residual, geograficamente restrita, ancorada em Santarém.** | M1, 5 marcas; Santarém presente em 4/5 queries eléctrico. | A forma estrutural (menos volume, menos distritos) é robusta; a âncora Santarém é consistente mas de recolha única. |
| M3 | **Ao nível do modelo, a alavanca de pesquisa varia por marca** (preço na VW; variante/novidade na Citroën; geração/usado na Audi/BMW; marca na BYD). | M1, consultas relacionadas. | Consultas relacionadas são mais estáveis que a geografia, mas continua recolha única. |
| M4 | **Audi A3 e BMW Série 1 sinalizam mercado de usados/manutenção** (gerações antigas, peças). | M1, consultas relacionadas (8L, 8P, 1.9 TDI, E46, embraiagem). | Sinal qualitativo estável (procura por gerações antigas não é sensível ao snapshot), mas não quantificado. |
| M5 | **Citroën C3 é procura de gama nova** (Aircross, anos-modelo 2025-26), não de usado. | M1 + corroboração externa (recuperação da produção do C3, §10.2 da síntese M1). | Consultas relacionadas claras + facto externo confirmado. |
| M6 | **A Citroën é a marca com procura mais uniforme nos distritos MatosCar e melhor alinhamento EV.** | M1, índices 84-95 em todos os 6 distritos. | Padrão claro, mas assente em posições do Trends (snapshot). |
| M7 | **Desalinhamento procura↔promoção: a Citroën é forte na procura mas tem 0 campanhas activas.** | M2 CP9 (0 campanhas) + M1 (procura forte). | A contagem de campanhas é um snapshot de um dia (rotativas); a força de procura é do Trends. Combinação de duas fontes Média. |
| M8 | **A BYD já intrude na consideração de EV premium** (aparece em BMW e Audi eléctrico). | M1, termos em ascensão. | Direccionalmente claro, recolha única. |
| M9 | **Mobile-friendly e preço visível assumidos nas 5 marcas.** | M2 CP3/CP7, observado só na BYD e estendido por template partilhado. | Extensão razoável do template, mas não observado marca a marca. |
| M10 | **Identidade dos concorrentes** (Carby o mais forte; Cremilcar recorrente em Abrantes; Gavis na Guarda, etc.). | M3, aparições em SERP + nº de avaliações. | Proxies de visibilidade, não de quota de mercado; sessão única com uma contaminação de IP confirmada. |

---

## Findings ESPECULATIVOS — perguntas de follow-up, não afirmações

Apresentar como hipóteses ou perguntas ao cliente; **não** como conclusões.

| # | Finding | Porque é especulativo |
|---|---------|-----------------------|
| E1 | **BMW Série 1 em Portalegre em 2º lugar nacional (índice 94).** | Snapshot único, query de baixo volume e volátil (pico 100 / vale 0), sem explicação. Pode ser artefacto de amostra pequena. Interessante — mas não deve ser manchete. |
| E2 | **Ligação causal entre os picos de EV e uma fase concreta do incentivo fiscal.** | O incentivo é real e datado, mas os picos estão dispersos e desfasados; atribuir causalidade a uma fase específica exige alinhamento semana-a-semana ainda não feito. |
| E3 | **Explicação para a força/uniformidade da Citroën nos distritos MatosCar.** | Sem informação pública que a explique; só verificável com dados internos (concessionário local, campanhas, perfil INE). |
| E4 | **A distinção de volume entre VW e BYD.** | Indistinguíveis no Módulo 0; qualquer afirmação de que uma tem mais procura que a outra precisa de fonte externa de volume absoluto (ACAP, Keyword Planner). |

---

## Caveats a declarar explicitamente no relatório (página de nota metodológica)

1. **Recolha única por módulo, sem repetição** — Módulo 3 num único browser/IP.
2. **Google Trends é índice relativo e snapshot dinâmico** — as posições numéricas exactas não são estáveis (um finding central mudou em 7 dias); reportar em tiers e formas, não em posições.
3. **Contaminação de geolocalização por IP** confirmada no Módulo 3 (AI Overview referiu Fundão, a localização real da analista, em modo incógnito).
4. **Falta uma âncora de volume absoluto** — a distinção VW/BYD e a magnitude real de cada marca ficam por resolver sem ACAP/Keyword Planner.
5. **Visibilidade competitiva ≠ procura** — a ausência da MatosCar numa SERP é um problema de configuração/presença, não prova de ausência de procura.

---

## Recomendação de ordenação do relatório (mapeada às páginas do PRD)

- **Executive summary (pág. 2):** liderar com **um** achado Alta e accionável. Candidato mais forte: **A4 (Abrantes/Santarém invisível)** ou **A1 (Knowledge Panel cedido em Audi/BYD)** — ambos são "coisas que o Pedro Matos não sabia" e desbloqueáveis. Recomendação headline associada: corrigir a configuração de GBP por marca / dar expressão digital a Abrantes.
- **Nota metodológica (pág. 3):** os 5 caveats acima. Declará-los é credibilidade, não fraqueza.
- **Páginas por marca (4-8):** usar o "Finding final" já preenchido em cada `data/[marca]/[marca].md`, com o demand tier (base Módulo 0) como enquadramento — nunca posições numéricas do Trends como se fossem exactas.
- **Findings transversais (pág. 9):** construir sobre os Alta (A1, A2, A3, A6, A8) e o desalinhamento M7 (Citroën forte na procura, zero campanhas). Enquadrar M1 (hierarquia) como contexto.
- **Recomendações (pág. 10):** priorizar quick wins ancorados nos Alta — (a) segmentar GBP por marca (A1/A2); (b) replicar o fluxo de reserva dos Usados nos Novos (A6/A7); (c) integrar as 5 marcas no hub EV (A8); (d) dar presença digital a Abrantes (A4).
- **Próximos passos (pág. 11):** o que uma 2ª recolha e o acesso a GA/Ads/CRM/ACAP desbloqueariam — em particular resolver E4 (volume absoluto) e E1-E3 (anómalos).

**Princípio:** o relatório lidera pelos achados operacionais robustos (Módulos 2 e 3) e usa o Trends (Módulo 1) como contexto enquadrado. O material mais frágil (posições do Trends, anómalos) nunca deve aparecer como afirmação de topo.
