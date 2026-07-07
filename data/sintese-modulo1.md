# Síntese Consolidada — Módulo 1 (Google Trends)
## MatosCar — Auditoria de Procura Digital

**Data:** 30/06/2026
**Âmbito:** 5 marcas (BMW, Audi, Volkswagen, BYD, Citroën), 20 queries, 12 meses de dados (Google Trends, Portugal)
**Distritos de referência MatosCar (Módulo 1):** Castelo Branco, Évora, Beja, Portalegre, Guarda. *(Rede MatosCar completa: 7 distritos — Abrantes, Beja, Castelo Branco, Évora, Guarda, Portalegre, Santarém. Abrantes e Santarém ficam fora do Módulo 1 por desenho do PRD, só entram no Módulo 3. Setúbal NÃO é distrito MatosCar — ver nota na secção 5.)*

Este documento cruza os achados registados marca a marca durante o fieldwork e organiza-os por tema, não por marca, para servir de base à construção do relatório final e às decisões de prioridade do Módulo 2 e 3.

---

> **[AVISO — DOCUMENTO DESACTUALIZADO, 07/07/2026]** As 20 queries do Módulo 1 foram todas re-recolhidas em 07/07/2026 (ver `data/bmw/bmw.md`, `data/audi/audi.md`, `data/volkswagen/volkswagen.md`, `data/byd/byd.md`, `data/citroen/citroen.md`, já corrigidos e verificados contra os CSVs originais). Esta síntese ainda reflecte os dados de 29-30/06/2026 e **contém pelo menos um finding central que já não se confirma**:
>
> - **Secção 2 e 3 (Citroën / Portalegre):** o finding "Portalegre lidera o ranking nacional absoluto para Citroën (1º lugar, índice 100) tanto na marca como no C3" **não se confirma nos dados de 07/07/2026**. Nos números novos, Portalegre está em 7º lugar (marca) e 4º lugar (C3) entre os distritos MatosCar — ainda um bom resultado, mas já não excepcional nem "sem precedentes". A Citroën marca tem agora o conjunto de distritos MatosCar mais homogéneo de todas as marcas (todos entre índice 84-95), o que pode ser a base de um finding novo, mas diferente do anterior.
> - **Secções 2, 5 e 9 (Setúbal):** esta versão já identifica correctamente que Setúbal não é distrito MatosCar, mas ainda usa dados de origem (BMW, Audi, VW, BYD, Citroën antigos) que, nos ficheiros de marca, misturavam Setúbal com a lista real de 6 distritos (Castelo Branco, Évora, Beja, Portalegre, Guarda, Santarém) — nomeadamente omitindo Beja e/ou Guarda em vários casos. Os ficheiros de marca já estão corrigidos; esta síntese ainda não.
> - **Secção 1 (Demand Tier) e restantes secções:** os ranges de índice e vários números pontuais mudaram ligeiramente entre 30/06 e 07/07/2026 (o próprio protocolo documenta que os dados do Trends são um snapshot dinâmico). Não foi feita uma reconciliação completa número a número desta síntese — recomenda-se reescrevê-la a partir dos 5 ficheiros de marca já corrigidos, em vez de corrigir isoladamente os pontos acima.
>
> Secções 10.1 e 10.2 (pesquisa externa sobre incentivos fiscais e produção do C3) não dependem dos números do Trends e continuam válidas.

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

## 3. O padrão "marca > modelo": efeito de agregação quase universal

Em **4 das 5 marcas** (BMW, Audi, Volkswagen, BYD), a query do modelo mais vendido/popular mostrou alcance geográfico **menor** do que a query da marca nos distritos MatosCar:

- **Audi A3** vs. Audi marca: distritos MatosCar descem de posições 9-17 para 12-17.
- **VW T-Roc** vs. VW marca: Portalegre desaparece completamente dos dados; só Santarém mantém força.
- **BYD Atto 3** vs. BYD marca: Portalegre desaparece; os restantes 4 distritos mantêm-se fortes mas mais baixos.
- (BMW Série 1 não foi comparado diretamente com a mesma granularidade nesta síntese, mas o padrão de queda de visibilidade ao nível do distrito foi consistente nas restantes.)

**A Citroën é a única exceção a este padrão.** O Citroën C3 manteve Portalegre em 1º lugar nacional absoluto, com índice idêntico ao da marca (100). Isto é singular no módulo inteiro e sugere uma relação muito específica e não apenas residual entre o distrito de Portalegre e este modelo — vale a pena investigar a causa concreta no Módulo 2/3 (presença de concessionário forte, campanha local, ou perfil demográfico particularmente afinado com o segmento do C3).

---

## 4. Padrão universal: "preço" domina a intenção de pesquisa

Em todas as marcas onde houve consulta relacionada de modelo específico, o termo "preço" (ou variantes "[modelo] + preço") liderou ou esteve muito próximo do topo das consultas principais:

- Audi A3: "audi a3 tdi" no topo, mas o padrão geral da query é dominado por termos de geração/motorização.
- VW T-Roc: "volkswagen t-roc preço" lidera com índice 100, mais do dobro do segundo lugar.
- BYD Atto 3: "byd atto 3 preço" lidera com índice 100.
- Citroën C3: "citroën c3 preço" surge na 5ª posição das consultas principais.

**Implicação:** o consumidor português em fase de pesquisa de modelo específico está predominantemente em funil de compra ativo e sensível a preço, não em fase de descoberta genérica. Isto reforça a importância de conteúdo com preços claros e atualizados nas páginas de produto da MatosCar.

---

## 5. Veículos elétricos: padrão estrutural residual, sem exceção

Em todas as 5 marcas, a query "[marca] eléctrico" mostrou:

- Volume de pesquisa muito mais baixo e mais irregular (picos pontuais, não procura contínua) do que a query da marca.
- Geografia muito mais restrita: entre 5 e 12 sub-regiões com dados (de 20 possíveis), nunca as 20 completas.
- Setúbal — que não é distrito de operação MatosCar, mas serve de comparativo ligado à hipótese "efeito Autoeuropa" testada em volkswagen.md — foi a sub-região mais consistentemente presente nestas queries (aparece em BMW, Audi, VW, Citroën eléctrico). Entre os distritos MatosCar reais, Santarém foi o mais presente.

| Marca | Sub-regiões com dados (eléctrico) | Distrito(s) com dados — MatosCar e comparativos |
|---|---|---|
| BMW | 6 | Apenas Santarém |
| Audi | 6 | Setúbal e Lisboa |
| Volkswagen | 5 (a mais residual) | Apenas Setúbal |
| BYD | 12 (a mais ampla) | Évora, Santarém, Setúbal |
| Citroën | 6 | Santarém (forte, índice 92), Setúbal |

*Nota: Setúbal e Lisboa não são distritos MatosCar — surgem aqui como pontos de comparação (Setúbal ligado à hipótese "efeito Autoeuropa", testada em volkswagen.md e não confirmada como padrão geral; Lisboa como referência de área metropolitana).*

**Achado metodológico importante (BYD eléctrico vs. BYD marca):** confirmou-se que a query "[marca] eléctrico" capta um público distinto da query da marca, mesmo numa marca 100% eléctrica como a BYD. A query "BYD eléctrico" foi dominada por termos genéricos ("carro elétrico") e por uma lista de concorrência muito mais ampla (8+ fabricantes) do que a query "BYD", que captou um público mais fiel e decidido pela marca. **Implicação para SEO/conteúdo:** páginas otimizadas para o nome da marca captam intenção de compra mais decidida; páginas otimizadas para "carro elétrico" competem por um público mais amplo mas menos qualificado, exigindo estratégias de conteúdo diferentes.

---

## 6. Concorrência percebida nos eléctricos: amplitude crescente por marca

A lista de fabricantes concorrentes associados nas queries de eléctrico cresceu de forma consistente ao longo do módulo:

| Marca | Concorrência associada (eléctrico) |
|---|---|
| BMW | BYD (único) |
| Audi | Tesla (único) |
| Volkswagen | 9 fabricantes (Tesla, BYD, Nissan, Hyundai, Kia, Jeep, Volvo, Mercedes-Benz, Renault, Peugeot) |
| BYD | 8+ fabricantes nos primeiros 10 tópicos (VW, Nissan, Fiat, Tesla, Honda, Leapmotor, Ford) |
| Citroën | Peugeot e Fiat — único caso de concorrência "de grupo industrial" (Stellantis), distinta da lógica inter-marcas das restantes |

**Padrão geral:** marcas premium alemãs (BMW, Audi) têm concorrência percebida estreita e específica; marcas generalistas (VW, BYD) competem num espaço muito mais disputado; a Citroën tem uma dinâmica própria, ligada à partilha de plataforma com outras marcas do mesmo grupo.

A **BYD** é a marca chinesa mais recorrente como concorrente associado em todo o módulo — apareceu nas queries de BMW, Audi (via Tesla, indiretamente), Volkswagen e Citroën, sendo a referência chinesa mais consistente do mercado português atual.

---

## 7. "[Marca] concessionário": ausência de procura nas 5 marcas testadas

Em todas as 5 marcas, a query "[marca] concessionário" não teve volume relevante de pesquisa em nenhum distrito do país, incluindo os 6 distritos MatosCar. O padrão repetiu-se de forma idêntica mesmo na Citroën, apesar do seu desempenho forte nas restantes 3 queries.

**Leitura metodológica (5 réplicas independentes, mesma recolha):** nas 5 marcas testadas, o Google Trends não devolveu volume mensurável para "concessionário", independentemente da marca, da maturidade da rede de distribuição ou do volume geral de procura pela marca. Cinco resultados nulos consistentes é um indício razoavelmente forte de que este termo não é como os portugueses procuram pontos de venda — mas continua a ser uma inferência a partir de 5 marcas e uma recolha, não uma prova sobre o Google Trends em geral. Esta dimensão **deve ser medida no Módulo 3** (SEO local, Google Business Profile, auditoria de presença digital directa), que é onde os dados directos e replicáveis existem.

---

## 8. Sinais de mercado de usados e manutenção

Dois padrões distintos emergiram nas consultas relacionadas:

- **Audi A3:** 6 das 10 consultas principais referiam-se a gerações antigas (8L, 8P) e motorizações descontinuadas (1.9 TDI) — sinal de que a procura por "Audi A3" em Portugal é maioritariamente sobre usado/manutenção, não compra de novo.
- **Citroën C3:** motor PureTech aparece como consulta técnica própria, possivelmente ligado a queixas mediáticas conhecidas sobre este motor; mas "usado" e "novo" aparecem em posições próximas e equilibradas, sem o domínio de uma geração específica.
- **BYD:** Standvirtual (plataforma de usados) surge como tópico em ascensão tanto na query da marca como no Atto 3 — sinal de mercado secundário já ativo para uma marca jovem, distinto do padrão de "gerações antigas" das marcas estabelecidas.

**Implicação:** a MatosCar deve considerar conteúdo e oferta diferenciados consoante a marca — para a Audi, há sinal forte de procura por peças/manutenção de gerações antigas; para a BYD, há oportunidade emergente em retoma e usados de uma marca ainda recente.

---

## 9. Distritos MatosCar: desempenho cruzado entre marcas

Sintetizando o comportamento de cada distrito ao longo de todas as marcas analisadas:

- **Portalegre:** o distrito mais instável entre marcas —