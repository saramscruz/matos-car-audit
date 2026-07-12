# Síntese Consolidada — Módulo 1 (Google Trends)
## MatosCar — Auditoria de Procura Digital

**Data da recolha:** 07/07/2026 (recolha completa que substitui a de 29-30/06/2026) · **Síntese reconciliada:** 07/07/2026
**Âmbito:** 5 marcas (BMW, Audi, Volkswagen, BYD, Citroën), 20 queries, 12 meses de dados (Google Trends, Portugal)
**Distritos de referência MatosCar (Módulo 1):** Castelo Branco, Évora, Beja, Portalegre, Guarda. *(Rede MatosCar completa: 7 distritos — Abrantes, Beja, Castelo Branco, Évora, Guarda, Portalegre, Santarém. Abrantes e Santarém ficam fora do Módulo 1 por desenho do PRD, só entram no Módulo 3. Setúbal NÃO é distrito MatosCar — ver nota na secção 5.)*

Este documento cruza os achados registados marca a marca durante o fieldwork e organiza-os por tema, não por marca, para servir de base à construção do relatório final e às decisões de prioridade do Módulo 2 e 3.

---

> **[ESTADO: RECONCILIADA COM OS DADOS DE 07/07/2026]** Todas as secções desta síntese foram reescritas a partir dos 5 ficheiros de marca (`data/[marca]/[marca].md`), cujos valores foram verificados um a um contra os CSVs originais do Google Trends (304 verificações numéricas, zero discrepâncias). A versão anterior reflectia a recolha de 29-30/06/2026 e continha vários findings que já não se confirmavam. Principais correcções face a essa versão:
>
> - **Portalegre / Citroën (secções 2, 3, 9):** o antigo finding "Portalegre lidera o ranking nacional absoluto para Citroën (1º lugar) na marca e no C3" **não se confirma**. Portalegre está em 7º (marca) e 4º (C3) entre os distritos MatosCar. O distrito MatosCar mais forte no C3 é agora **Santarém** (2º nacional). O resultado de modelo mais espectacular do módulo passou a ser **BMW Série 1 em Portalegre** (2º nacional, índice 94).
> - **"Marca > modelo" (secção 3):** deixou de ser "quase universal" — só se verifica em 3 marcas (VW, BMW, BYD); Audi e Citroën mantêm cobertura completa dos 6 distritos.
> - **"Preço domina" (secção 4):** deixou de ser universal — "preço" só lidera claramente na VW T-Roc.
> - **Concorrência EV (secção 6):** a tabela antiga (concorrente "único" para BMW e Audi; "Stellantis" para Citroën) não corresponde aos dados; substituída pela lista real.
> - **Erro Setúbal/Beja/Guarda:** eliminado — todas as secções usam agora a lista fixa e correcta de 6 distritos MatosCar.
> - **Secção 10.1 (pico dos eléctricos):** corrigida — os picos são dispersos entre março e junho, não um pico único de fevereiro/março.
>
> Secções 1, 2 e 10.2 já tinham sido reconciliadas em 07/07/2026 e mantêm-se.

---

## 1. Demand Tier por marca — CORRIGIDO EM 07/07/2026

> **Nota metodológica (substitui a versão anterior desta secção):** a versão anterior classificava as 5 marcas como "Demand Tier: High" comparando directamente os ranges de índice de cada query de marca (ex: "BMW 75-85 vs. BYD 55-100"). Isto não é uma comparação válida — o protocolo (`google-trends-protocol.md`, regra 7) já avisa que não se deve comparar duas marcas no mesmo gráfico, precisamente porque **cada query do Google Trends normaliza o seu próprio pico a 100, independentemente das outras**. O índice 100 da BYD e o índice 100 da BMW não representam o mesmo volume real de pesquisas. A única recolha onde as 5 marcas estão de facto na mesma escala é o Módulo 0 (`data/modulo0.md`), e essa mostra uma hierarquia muito diferente da sugerida pela tabela anterior. Esta secção separa agora os dois conceitos, que não devem voltar a ser fundidos num "tier" único.

### 1.1 — Magnitude relativa entre marcas (única fonte comparável: Módulo 0)

Do gráfico comparativo directo (`data/modulo0.md`, 29/06/2026, mesma janela e mesma escala para as 5 marcas):

1. **BMW** — índice 75-100, domina claramente.
2. **Audi** — índice 35-50, muito abaixo da BMW.
3. **Citroën** — índice 15-25.
4. **Volkswagen** e **BYD** — abaixo de 15, "indistinguíveis a esta escala" (nota do próprio registo de campo).

Esta é a hierarquia a citar sempre que o relatório final precisar de dizer "qual marca tem mais procura que qual" em termos de volume absoluto. Não é suficientemente granular para separar VW de BYD com confiança — se essa distinção for importante para o cliente, é preciso recolha adicional (ver proposta em aberto, secção 1.3).

### 1.2 — Forma da procura por marca (válido dentro da própria query, não comparável entre marcas)

Cada linha descreve o comportamento de cada marca em relação a si própria (tendência, volatilidade, sazonalidade). Os valores de índice **não podem ser comparados entre linhas** — só a forma (estável/crescente/decrescente, picos, vales) é informativa entre marcas.

| Marca | Índice médio (própria escala) | Pico / Vale | Tendência (própria escala) |
|---|---|---|---|
| BMW | 81,3 | 100 / 69 | Estável (delta -2,4) |
| Audi | 85,3 | 100 / 60 | Estável (delta -3,4) |
| Volkswagen | 72,2 | 100 / 58 | Crescente (delta +11,2) |
| BYD | 69,5 | 100 / 54 | Crescente (delta +11,3) — única marca com sinal de crescimento sustentado nas duas recolhas (30/06 e 07/07) |
| Citroën | 85,8 | 100 / 65 | Estável (delta -4,3) |

Dados de 07/07/2026, já corrigidos (ver ficheiros de marca individuais).

### 1.3 — Proposta em aberto, não implementada

Se for necessário para o relatório final separar VW e BYD com confiança (hoje indistinguíveis no Módulo 0), a opção mais direta é repetir o Módulo 0 em subgrupos menores (ex: só Citroën + VW + BYD, sem BMW/Audi a esmagar a escala) ou usar um proxy externo de volume absoluto (registo automóvel ACAP, Google Keyword Planner). Nenhuma destas foi feita — fica registada como decisão pendente, não como acção tomada.

---

## 2. O finding geográfico central: hierarquia de adequação aos distritos MatosCar — CORRIGIDO EM 07/07/2026

> **Nota metodológica:** versão anterior desta secção, com a hierarquia "Citroën excecional > BYD muito forte > VW favorável > Audi intermédio > BMW desfavorável", baseava-se nos dados de 30/06/2026 (com o erro Setúbal/Beja/Guarda). Com os dados corrigidos de 07/07/2026 e a lista certa de 6 distritos, a hierarquia muda de forma substancial — em particular, a Audi sobe e a BYD desce.

Posição nacional (de 20) de cada distrito MatosCar, na query da marca de cada uma das 5 marcas:

| Marca | Castelo Branco | Évora | Beja | Portalegre | Guarda | Santarém | Posição média |
|---|---|---|---|---|---|---|---|
| Citroën | 8 | 12 | 4 | 7 | 6 | 5 | **7,0** |
| Volkswagen | 15 | 14 | 4 | 3 | 5 | 10 | **8,5** |
| Audi | 15 | 17 | 14 | 9 | 2 | 8 | **10,8** |
| BMW | 14 | 19 | 16 | 12 | 9 | 7 | **12,8** |
| BYD | 15 | 9 | 18 | 16 | 12 | 10 | **13,3** |

*(Posição média = média das 6 posições nacionais; quanto mais baixo, melhor. Critério de resumo escolhido por simplicidade e transparência — não é a única forma válida de agregar os 6 valores, e não foi cruzado aqui com índice médio ou contagem no top 10 nacional.)*

Ordenando as 5 marcas por este critério:

1. **Citroën** — a mais forte e a mais consistente. Todos os 6 distritos entre a 4ª e a 12ª posição nacional, sem nenhum a cair para a segunda metade da tabela.
2. **Volkswagen** — segunda melhor. Beja e Portalegre entre os mais fortes de todo o módulo (4º e 3º lugar nacional); Évora e Castelo Branco mais fracos (14º/15º).
3. **Audi** — sobe da classificação "intermédia" anterior por causa de Guarda, em 2º lugar nacional (índice 96) — o resultado mais forte de qualquer distrito em qualquer marca de todo o módulo. Os restantes distritos da Audi são mais fracos (9º a 17º), o que confirma que este é um resultado pontual de Guarda, não um padrão geral da marca.
4. **BMW** — quarta posição. Guarda (9º) e Santarém (7º) são razoáveis, mas Évora (19º) e Beja (16º) puxam a média para baixo.
5. **BYD** — a mais fraca por este critério, ao contrário da classificação "muito forte" da versão anterior. Beja caiu para 18º lugar nacional; só Évora (9º) mantém um resultado forte.

**Implicação directa (revista):** ao contrário da leitura anterior, não há uma dicotomia clara "Citroën/BYD fortes vs. BMW/Audi fracas" — a Audi tem, na verdade, o resultado mais forte de qualquer distrito em todo o módulo (Guarda), e a BYD tem o resultado mais fraco (Beja). A força geográfica de cada marca varia por distrito mais do que por marca — decisões de investimento em visibilidade local provavelmente precisam de ser por marca **e** por distrito, não só por marca.

---

## 3. "Marca > modelo": o efeito de agregação é real mas NÃO universal — CORRIGIDO EM 07/07/2026

> **Nota metodológica:** a versão anterior afirmava que a query do modelo tinha alcance geográfico menor em "4 das 5 marcas" e que "a Citroën C3 manteve Portalegre em 1º lugar nacional absoluto". Nenhuma das duas se confirma nos dados de 07/07/2026 (verificados contra os CSVs).

Número de distritos MatosCar (de 6) com dados (índice ≠ 0) na query da marca vs. na query do modelo:

| Marca | Modelo | Distritos c/ dados: marca → modelo | Efeito |
|---|---|---|---|
| Audi | A3 | 6 → 6 | sem perda de cobertura |
| Citroën | C3 | 6 → 6 | sem perda de cobertura |
| BMW | Série 1 | 6 → 4 | perde Beja e Guarda |
| BYD | Atto 3 | 6 → 4 | perde Portalegre e Guarda |
| Volkswagen | T-Roc | 6 → 1 | só sobra Santarém |

O estreitamento geográfico ao passar de marca para modelo existe, mas só em três marcas — severo na VW, moderado em BMW e BYD. Na Audi e na Citroën o modelo mantém a cobertura completa dos 6 distritos. **Não é universal.**

Dois resultados de modelo destacam-se, ambos em Portalegre e em sentido contrário à ideia de "perda":

- **BMW Série 1 em Portalegre: 2º lugar nacional (índice 94)** — o resultado de modelo mais forte de qualquer distrito MatosCar no módulo. É um outlier a investigar no Módulo 2/3 (concessionário forte, campanha local, ou artefacto de amostra pequena).
- **Citroën C3:** o distrito MatosCar mais forte é agora **Santarém** (2º nacional, índice 89), com Portalegre em 4º (índice 80) — forte, mas já não o "1º lugar absoluto" que a versão anterior reportava.

---

## 4. Intenção transacional ao nível do modelo — mas a alavanca varia por marca — CORRIGIDO EM 07/07/2026

> **Nota metodológica:** a versão anterior afirmava que "preço domina" de forma universal. Nos dados de 07/07/2026, "preço" só lidera claramente numa marca (VW). Nas outras, a consulta dominante ao nível do modelo é outra.

Consulta relacionada no topo de cada query de modelo:

- **VW T-Roc:** "volkswagen t-roc preço" — índice 100, a consulta dominante. Único caso onde "preço" lidera claramente.
- **BMW Série 1:** dominado por "bmw serie 1" / "serie 1"; "bmw série 1 preço" em 3º (67) e "bmw série 1 usado" (32) — intenção mista preço/usado.
- **Audi A3:** dominado por geração/motorização ("audi a3 tdi" 100, "8l", "8p"); "audi a3 2025 preço" apenas como termo em ascensão (+250%).
- **BYD Atto 3:** dominado por geografia / afirmação de marca ("byd atto 3 portugal" 100, "byd portugal" 96); "byd atto 3 price" em 8º (40).
- **Citroën C3:** dominado pela variante e pelo ano-modelo ("citroen c3 aircross" 100, "citroen c3 2025", "citroen c3 2026" +4 650%) — "preço" não aparece no topo.

**Implicação:** ao nível do modelo a pesquisa é transacional (variantes concretas, anos-modelo, preço, "usado"), mas a alavanca dominante muda por marca — preço na VW, variante/novidade na Citroën, geração/usado na Audi e BMW, afirmação de marca na BYD. O conteúdo de produto da MatosCar deve responder à alavanca dominante de cada marca, não assumir "preço" para todas.

---

## 5. Veículos elétricos: procura residual, geografia restrita, ancorada em Santarém — CORRIGIDO EM 07/07/2026

Em todas as 5 marcas, a query "[marca] eléctrico" mostrou volume muito mais baixo e irregular do que a query da marca, e geografia restrita. Contagens verificadas contra os CSVs:

| Marca | Sub-regiões com dados (de 20) | Distrito(s) MatosCar com dados |
|---|---|---|
| Audi | 13 | Castelo Branco (90), Santarém (38) |
| BMW | 11 | Santarém (51) |
| BYD | 11 | Santarém (63) |
| Citroën | 11 | Santarém (71) |
| Volkswagen | 5 (a mais residual) | nenhum distrito MatosCar |

**Santarém é o único distrito MatosCar presente de forma consistente** nas queries de eléctrico (4 das 5 marcas; ausente só na VW). Castelo Branco surge com força pontual na Audi (índice 90, 2º nacional). **Setúbal — que NÃO é distrito MatosCar — está presente nas 5 queries de eléctrico** (índices 34-69), o comparativo mais consistente; é contexto de mercado (zona industrial, hipótese "efeito Autoeuropa" testada e não confirmada como padrão geral em volkswagen.md), não prioridade de investimento MatosCar.

**Achado metodológico (mantém-se):** a query "[marca] eléctrico" capta um público distinto e menos qualificado do que a query da marca — dominada por termos genéricos ("carro elétrico" lidera as consultas em Audi, BMW e BYD eléctrico). **Implicação SEO:** páginas otimizadas para o nome da marca captam intenção mais decidida; páginas otimizadas para "carro elétrico" competem por público mais amplo mas menos qualificado, exigindo estratégias de conteúdo diferentes.

---

## 6. Concorrência percebida nos eléctricos — o padrão anterior não se confirma — CORRIGIDO EM 07/07/2026

> **Nota metodológica:** a tabela anterior (BMW "BYD único"; Audi "Tesla único"; Citroën "Peugeot/Fiat — Stellantis") não corresponde aos dados de 07/07/2026. As queries de eléctrico da Audi e da BMW mostram uma lista ampla, não um concorrente único; as da VW e da Citroën não devolveram entidades relacionadas suficientes para qualquer lista de concorrência.

O que os dados de 07/07/2026 mostram (entidades/consultas relacionadas das queries de eléctrico):

- **BMW eléctrico:** Mercedes (recorrente), Porsche, e BYD em ascensão (+50%) — vários, não um.
- **Audi eléctrico:** Mercedes, BMW, Tesla, Cupra, Porsche, Fiat — cross-shopping premium amplo.
- **BYD eléctrico / Atto 3:** a lista mais ampla de todas — Tesla, Renault, Volvo, Hyundai, Cupra, MG4, Kia EV6, Leapmotor, XPeng, Changan, Jaecoo. Cross-shopping de EV de valor / chineses.
- **VW eléctrico:** demasiado residual — só "volkswagen elétrico id 4 preço". Sem lista de concorrência.
- **Citroën eléctrico:** sem entidades relacionadas na exportação. Sem lista de concorrência.

**Padrão que se sustenta:** as marcas premium (Audi, BMW) fazem cross-shopping com outras premium/EV (Mercedes, Tesla, Porsche), **mas a BYD já intrude nessa consideração premium** (aparece em BMW eléctrico e em Audi A3 em ascensão, +160%). A BYD é a referência chinesa mais recorrente do módulo. **O que NÃO se confirma** é a leitura "amplitude crescente marca a marca" nem a concorrência Stellantis específica da Citroën — não há dados que a sustentem nesta recolha.

---

## 7. "[Marca] concessionário": ausência de procura nas 5 marcas testadas — CONFIRMADO EM 07/07/2026

Em todas as 5 marcas, a query "[marca] concessionário" não teve volume relevante de pesquisa em nenhum dos 6 distritos MatosCar. A nível nacional, a procura é quase inexistente: a série temporal de Audi, BMW, Citroën e VW tem apenas 1 a 2 semanas com valor não-nulo (um pico isolado normalizado a 100, tudo o resto a zero), e o `geoMap` devolve valor apenas em uma ou duas sub-regiões (nenhuma delas distrito MatosCar). O padrão repetiu-se de forma idêntica mesmo na Citroën, apesar do seu desempenho forte nas restantes 3 queries. O caso mais extremo é a **BYD concessionário**, cujo `multiTimeline.csv` não devolveu sequer uma série temporal — nem o pico isolado das outras quatro — volume insuficiente para qualquer dado.

**Leitura metodológica (5 réplicas independentes, mesma recolha):** nas 5 marcas testadas, o Google Trends não devolveu volume mensurável para "concessionário", independentemente da marca, da maturidade da rede de distribuição ou do volume geral de procura pela marca. Cinco resultados nulos consistentes é um indício razoavelmente forte de que este termo não é como os portugueses procuram pontos de venda — mas continua a ser uma inferência a partir de 5 marcas e uma recolha, não uma prova sobre o Google Trends em geral. Esta dimensão **deve ser medida no Módulo 3** (SEO local, Google Business Profile, auditoria de presença digital directa), que é onde os dados directos e replicáveis existem.

---

## 8. Sinais de usados/manutenção vs. novidade de gama — AMPLIADO EM 07/07/2026

Dois modelos de entrada de marcas estabelecidas mostram forte sinal de **usado/manutenção**:

- **Audi A3:** consultas dominadas por gerações antigas (8L, 8P) e motorizações descontinuadas (1.9 TDI, 2.0, 1.6); entidade "Bomba injetora". Procura maioritariamente sobre usado/manutenção, não compra de novo.
- **BMW Série 1 (novo nesta correcção):** "bmw série 1 usado" no topo (32) e entidades de peças / gerações antigas — E46, Capô, Embraiagem, Volante, "used". É o mesmo sinal de usado/manutenção da Audi, que a versão anterior não tinha identificado na BMW.

O pólo oposto é a **novidade de gama**:

- **Citroën C3:** dominado pelo novo C3 / C3 Aircross e anos-modelo 2025-2026 ("citroen c3 2026" +4 650% em ascensão) — sinal de lançamento recente, não de mercado de usados. (A consulta técnica "citroën c3 puretech" e a entidade "Motores PureTech" +120% também surgem, mais abaixo — interesse técnico/fiabilidade do motor, coerente com queixas mediáticas conhecidas, mas não domina.)
- **BYD Atto 3:** interesse em variante / ano novo (Evo, 2026). "Standvirtual" aparece de forma modesta (25º nas consultas do Atto 3; entidade em ascensão na query da marca) — sinal incipiente de mercado secundário para uma marca jovem, mas não um padrão como o das gerações antigas alemãs.

**Implicação:** conteúdo diferenciado por marca — peças/manutenção e oferta de usado para os modelos de entrada Audi e BMW; informação de gama nova para Citroën e BYD.

---

## 9. Distritos MatosCar: leitura cruzada entre marcas — CORRIGIDO EM 07/07/2026

Sintetizando o comportamento de cada distrito ao longo de todas as marcas (posições nacionais verificadas contra os CSVs):

- **Santarém:** o distrito mais consistentemente forte. Bem posicionado em Citroën (5º na marca, 2º no C3, 3º no eléctrico), presente em BYD (10º na marca e no Atto 3) e em VW (10º na marca, e o **único** distrito com dados no T-Roc e no eléctrico VW). É o âncora de eléctricos do grupo. Candidato a prioridade transversal de investimento.
- **Guarda:** o resultado individual mais forte de todo o módulo — **Audi marca em 2º lugar nacional (índice 96)**, e Audi A3 em 4º. É a excepção que puxa a Audi para cima; fora da Audi, é mediano. Stronghold específico da Audi.
- **Portalegre:** o mais volátil. Vai do topo (VW marca 3º; **BMW Série 1 2º, índice 94**) à ausência total de dados (VW T-Roc, BYD Atto 3). Não há um padrão de distrito — há resultados pontuais fortes por combinação marca/modelo.
- **Évora:** fraco no premium (Audi marca 17º, BMW 19º), mas é o **melhor distrito MatosCar da BYD** (9º na marca, 6º no Atto 3).
- **Castelo Branco:** geralmente baixo, com uma excepção clara — **Audi eléctrico (2º nacional, índice 90)**.
- **Setúbal (comparativo, não distrito MatosCar):** presente nas 5 queries de eléctrico — procura real e sustentada por elétricos nesta zona industrial (hipótese "efeito Autoeuropa" testada e não confirmada como padrão geral em volkswagen.md). Contexto de mercado, não prioridade de investimento MatosCar.

**Leitura global:** a força de cada distrito depende mais da combinação marca×distrito do que do distrito em si. Santarém (Citroën / eléctricos) e Guarda (Audi) são os dois pontos fortes mais claros; Portalegre é forte mas imprevisível. Isto reforça a implicação da secção 2: as decisões de visibilidade local precisam de ser por marca **e** por distrito.

---

## 10. Perguntas em aberto — respostas factuais encontradas

Das 4 perguntas levantadas, 2 têm resposta factual confirmável por pesquisa externa; as outras 2 exigem dados internos da MatosCar ou trabalho de campo do Módulo 3, não pesquisa documental.

### 10.1 — PARCIALMENTE RESPONDIDA, COM CORREÇÃO (07/07/2026): os picos nos elétricos e a relação com os incentivos fiscais

> **Correcção metodológica:** a versão anterior desta secção afirmava um "pico de fevereiro/março 2026, transversal às 5 marcas", e ligava-o directamente à 1ª fase do incentivo (candidaturas 29/12/2025–12/02/2026). Ao cruzar essa afirmação com as séries temporais dos próprios CSVs (`multiTimeline.csv` de cada query `[marca] eléctrico`), verifica-se que **não há um pico único em fev/mar comum às cinco marcas**. Os picos reais estão dispersos e, na maioria, ocorrem *depois* de a 1ª fase fechar:
>
> | Query | Semana de pico | Índice de pico | Melhor valor em fev–mar |
> |---|---|---|---|
> | BMW eléctrico | 22/03/2026 | 100 | 100 (o único que pica perto da janela) |
> | BYD eléctrico | 05/04/2026 | 100 | 55 |
> | Audi eléctrico | 12/04/2026 | 100 | 77 |
> | Citroën eléctrico | 24/05/2026 | 100 | 55 |
> | Volkswagen eléctrico | 28/06/2026 | 100 | **0** (sem procura mensurável em fev–mar) |
>
> Só a **BMW** pica dentro/perto da janela da 1ª fase. As restantes quatro picam entre abril e junho, e a **VW eléctrico está a zero em todo o fevereiro–março**. Portanto, a leitura "pico transversal de fev/mar causado pela 1ª fase do incentivo" **não é sustentada pelos dados**.

**O que se confirma (e o que não).** O incentivo é real e as suas datas estão verificadas: a 1ª fase do Incentivo à Aquisição de Veículos de Emissões Nulas (Fundo Ambiental) esteve aberta a candidaturas entre **29 de dezembro de 2025 e 12 de fevereiro de 2026**, com **4.000€ por veículo para pessoas singulares** (mediante abate, para veículos novos até 38.500€). Uma **2ª fase** abriu a **12 de junho de 2026** (candidaturas até 27/07/2026), também com 4.000€ por veículo. *Os montantes globais de dotação citados na versão anterior (17,6 M€ na 1ª fase; ~20 M€ na 2ª) não foram confirmados nas fontes consultadas em 07/07/2026 — as fontes apontam ~10 M€ para a fase de junho de 2026 e não confirmam os 17,6 M€. Tratar os valores de dotação como não confirmados até verificação directa.*

**Leitura corrigida da relação picos ↔ incentivos.** Cruzando as duas fases com os picos observados, o padrão mais plausível é o **inverso** do que a versão anterior sugeria: os picos tardios (Citroën em maio, VW em junho) alinham-se melhor com a **antecipação/abertura da 2ª fase (junho)** do que com a 1ª fase (que fechou em fevereiro); e o pico da BMW (março) surge já *depois* do fecho da 1ª fase, sugerindo um efeito de cauda, não de janela. Em nenhuma marca o pico coincide com o *interior* da janela de candidaturas da 1ª fase (dez–fev). Ou seja: há provavelmente uma relação entre procura por elétricos e o calendário de incentivos, mas ela é dispersa, desfasada e específica por marca — não um pico único e sincronizado.

*Fontes: Fundo Ambiental (Mobilidade Verde Passageiros 2025/2026, 1ª e 2ª fase); ECO/SAPO (11/06/2026), consultadas em 07/07/2026. Séries temporais: CSVs `multiTimeline.csv` das 5 queries `[marca] eléctrico` do próprio Módulo 1.*

**Implicação para o relatório final (mantida, reforçada):** a cautela original continua correcta e agora está melhor fundamentada — picos de procura por elétricos **não** devem ser lidos como tendência orgânica de mercado sem cruzar com o calendário de incentivos. Mas o relatório deve descrever os picos como **dispersos entre março e junho de 2026, específicos por marca**, e não como um pico único de fevereiro/março. Se for necessário afirmar causalidade com um incentivo concreto, isso exige alinhar a semana de pico de cada marca com a fase de incentivo activa nessa data — não uma atribuição global.

### 10.2 — PARCIALMENTE RESPONDIDA, COM CORREÇÃO: a queda de produção do C3

**A informação original precisa de ajuste.** A fonte usada na pesquisa de mercado preliminar (Razão Automóvel) indicava que a Citroën foi uma das duas únicas marcas do Top 10 português a registar quebra de vendas em 2025 (-1,1%), "devido a problemas que afetaram a produção do C3". A pesquisa adicional mostra que este foi um problema **pontual, já em recuperação durante o próprio 2025**, não uma tendência persistente: em outubro de 2025, as vendas do C3 subiram 40% (12.771 unidades) e o C3 Aircross cresceu 519% (8.030 unidades), ao ponto da Stellantis reforçar a produção com 400 novas contratações na unidade de Rennes para responder à procura.

Isto é coerente com o que observámos no Trends: a query da marca e do C3 mostraram tendência de subida ao longo do período analisado, não quebra — porque os dados de 12 meses do Trends (jun/2025 a jun/2026) captam precisamente a fase de recuperação, não a fase de quebra que a precedeu.

*Fonte: Razão Automóvel (artigo sobre aumento de produção do C3, nov. 2025), cruzada com a fonte original sobre marcas mais vendidas 2025.*

**Implicação para o relatório final:** ao mencionar este episódio ao cliente, é importante apresentá-lo como uma fase já ultrapassada e seguida de recuperação forte, não como uma fragilidade atual da marca — caso contrário a leitura fica desatualizada e desalinhada com os próprios dados de procura que o módulo recolheu.

### 10.3 — NÃO RESPONDÍVEL POR PESQUISA EXTERNA: os anómalos de Portalegre (reformulado em 07/07/2026)

> **Nota:** a versão anterior desta pergunta assentava na premissa "Portalegre lidera o ranking nacional para Citroën e para o C3", que **não se confirma** nos dados de 07/07/2026 (Portalegre está em 7º na marca e 4º no C3). A pergunta foi reformulada em torno dos anómalos que os dados corrigidos realmente mostram.

Portalegre continua a ser o distrito mais imprevisível do módulo, mas os resultados que pedem explicação mudaram:

- **BMW Série 1 em Portalegre — 2º lugar nacional (índice 94):** o resultado de modelo mais forte de qualquer distrito MatosCar, e num modelo/marca onde Portalegre é fraco ao nível da marca (12º). É o anómalo mais nítido a explicar.
- **Homogeneidade da Citroën:** a Citroën marca tem o conjunto de distritos MatosCar mais uniforme de todas as marcas (todos entre índice 84-95, posições 4-12) — força consistente, não um pico isolado.

As hipóteses plausíveis — concessionário local forte, campanha regional recente, perfil demográfico do distrito — não são verificáveis por pesquisa documental. **Só podem ser respondidas com dados internos da MatosCar ou trabalho de campo do Módulo 2/3** (posição do concessionário local, histórico de campanhas na região, dados INE de perfil socioeconómico).

### 10.4 — NÃO RESPONDÍVEL POR PESQUISA EXTERNA: desalinhamento Golf/T-Roc

Já está confirmado, com fonte direta da SIVA, que o T-Roc é o modelo mais vendido da Volkswagen em Portugal, apesar do Golf dominar a pesquisa orgânica. O que falta — se isto representa uma oportunidade de SEO subexplorada para o T-Roc, ou simplesmente reflete inércia de marca histórica do Golf sem implicação prática — não é uma questão factual respondível por pesquisa, é uma decisão de estratégia de conteúdo a tomar com o cliente, possivelmente testável através de dados próprios de SEO/analytics da MatosCar caso já tenha páginas indexadas para ambos os modelos.

---

*Fontes: Google Trends (Portugal, últimos 12 meses, recolha de 07/07/2026 — substitui a de 29-30/06/2026), com valores verificados contra os CSVs originais de cada query. Complementado com pesquisa de mercado pontual para confirmação de modelos mais vendidos (ACAP, Razão Automóvel, SIVA, Auto.pt) e de incentivos fiscais (Fundo Ambiental, ECO/SAPO), fontes citadas nos ficheiros de marca individuais e na secção 10.*
