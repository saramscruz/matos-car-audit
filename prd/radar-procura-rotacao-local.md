# Radar de Procura e Rotação Local — Desenho de Projeto

**Autora:** Sara Cruz · **Data:** 07/07/2026 · **Cliente-alvo:** Grupo A MatosCar (Pedro Matos)
**Natureza:** projeto próprio, para demonstração de competência e proposta de continuidade.

---

## 1. A ideia numa frase

Cruzar três camadas de dados — **todas públicas ou do próprio cliente** — para transformar o retrato estático que já existe (Módulos 1-3) num **ciclo que prova impacto**: escolher uma correção concreta, medir antes, corrigir, medir depois. Não é mais um relatório; é uma decisão com resultado verificável.

## 2. O que o dono disse que precisa (e que este projeto respeita)

1. **Uma decisão, não uma descrição** — o projeto gira à volta de *uma* correção-piloto com antes-e-depois.
2. **As marcas onde ele fatura** — a camada de rotação cobre **todas** as marcas do stock, não só as 5 do estudo.
3. **Abrantes como história** — acompanhamento trimestral datado da nova abertura.
4. **Honestidade nas costuras** — "proxy de rotação", nunca "vendas confirmadas".
5. **Uma folha, não um calhamaço** — o entregável é uma página de decisão.
6. **Zero risco e quase zero esforço para ele** — só dados públicos/próprios; do cliente só preciso de 20 min e da autorização para usar o site dele.

---

## 3. As três camadas de dados — e porque nenhuma tem risco

| Camada | O que mede | Fonte | Estatuto legal | Limitação declarada |
|---|---|---|---|---|
| **A · Procura & visibilidade** | Onde há procura e se a MatosCar aparece | Google Trends (API pública) + SERP/Google Business (pesquisa manual) | Público, sem ToS de terceiros | Índice relativo; snapshot dinâmico |
| **B · Rotação do próprio stock** | Preço, km, ano e dias-listado por marca/distrito | amatoscar.pt (site do próprio cliente) | Site do cliente, com autorização dele | "Desaparecer do stock" ≠ "vendido" — **proxy**, não facto |
| **C · Contexto de mercado** | Matrículas nacionais por marca | ACAP (comunicados mensais gratuitos) | Público e gratuito | Só nível **nacional**; a desagregação distrital é paga (Autoinforma) — fica de fora |

**Deliberadamente fora de âmbito:** Standvirtual e OLX Auto. Os termos profissionais da Standvirtual proíbem agregar os dados deles para divulgação a terceiros. Preço relativo face à concorrência fica arquivado como Fase futura, condicionado a API/parceria — nunca a scraping. *(Nota: esta leitura contratual não é parecer jurídico; a confirmar antes de qualquer uso.)*

**A camada B resolve a crítica das marcas de volume:** como é o próprio site, cobre Kia, Peugeot, Toyota, Opel e as restantes 29 marcas ao mesmo custo — a rotação não fica limitada às 5 marcas do estudo.

---

## 4. A decisão-âncora (o piloto que fecha o ciclo)

**Correção escolhida:** o perfil de Google Business da **BYD em Castelo Branco**, hoje ocupado por um concorrente (a Rodda) por falta de perfil dedicado. É o candidato ideal: isolado, barato de corrigir, e com efeito diretamente atribuível.

**O ciclo:**

1. **Antes (T0):** registar o estado atual — a MatosCar não tem Knowledge Panel próprio para "BYD Castelo Branco"; aparece a Rodda. Registar também a rotação-proxy da BYD nesse catchment (dias-listado medianos).
2. **Ação:** criar/corrigir o perfil (execução do cliente ou recomendação para a equipa dele).
3. **Depois (T0 + 6-8 semanas):** repetir a mesma pesquisa e comparar.

**Métrica primária = visibilidade** (aparece ou não no painel/Local Pack). É limpa e diretamente causada pela correção. **Métrica secundária = rotação-proxy**, apresentada como sinal exploratório e direcional — 6-8 semanas é curto e ruidoso para rotação, e há confundidores; só ganha força ao longo de trimestres. *Prometer a visibilidade como prova; a rotação como hipótese a acompanhar.* Esta distinção é, ela própria, o que impressiona: mostra que sei o que uma correção prova e o que não prova.

---

## 5. Abrantes — a história recorrente

A MatosCar abriu fisicamente em Abrantes em junho de 2026. O Módulo 3 já mediu **ausência digital total (0 de 5 marcas)** em junho/julho. O projeto repete essa medição em **setembro** e **dezembro**, com as mesmas queries e formatos, para dar um antes-e-depois ligado a uma decisão real e recente do cliente. É a cara do relatório — concreto, datado, e sobre algo que ele decidiu este ano.

---

## 6. Inventário honesto — o que já existe vs. o que falta

*(Escrito assim de propósito, para não voltar a apresentar como pronto aquilo que ainda não está.)*

**Já feito e verificado:**
- Módulo 1 (Trends) — completo, 5 marcas, 20 queries, síntese reconciliada e verificada contra os CSVs.
- Módulo 2 (funil) — completo, 10 checkpoints, 5 marcas.
- Módulo 3 (visibilidade) — **completo, 35/35 pesquisas**, 7 distritos, síntese fechada.
- Findings de marca e mapa de confiança — preenchidos.

**Por construir (o novo trabalho deste projeto):**
- **Scraper do amatoscar.pt** — ainda não existe. Requer construir do zero e **validar os seletores no DevTools antes de prometer qualquer número de rotação**. Gate obrigatório: se não devolver viaturas reais, não avança.
- **Primeiros snapshots de stock** — zero capturados até agora.
- **Extração ACAP nacional** — ainda por fazer.
- **Piloto de correção + re-medição** — por executar.
- **Re-medições trimestrais de Abrantes** (set/dez) — por fazer.

---

## 7. Plano por fases (sequência realista)

| Fase | Trabalho | Depende de |
|---|---|---|
| **0 — Base** | Já concluída (Módulos 1-3). Serve de T0 para visibilidade. | — |
| **1 — Stock** | Construir e **validar** o scraper do site próprio; primeiro snapshot; definir "dias-listado" e o catchment de cada distrito. | Autorização do cliente p/ usar o site |
| **2 — Contexto** | Puxar matrículas ACAP nacionais por marca; alinhar com as marcas de volume. | — |
| **3 — Piloto** | Executar o ciclo antes/depois da correção do GBP da BYD em Castelo Branco. | Fase 1 (para a rotação-proxy) |
| **4 — Cadência** | Re-medir Abrantes (set, dez) e consolidar o formato trimestral. | Fases 1-3 |

Ordem inegociável: **validar o scraper antes** de prometer rotação a quem quer que seja.

---

## 8. O entregável — uma folha, trimestral

Uma página de decisão por trimestre, com quatro blocos:

1. **Tier de procura por marca/distrito** (Camada A) — já existe o desenho.
2. **Rotação-proxy do stock próprio** por marca/distrito (Camada B) — sempre rotulada como proxy.
3. **Contexto nacional ACAP** por marca (Camada C) — para separar "problema local" de "mercado a abrandar".
4. **A decisão do trimestre** — uma correção, o antes-e-depois da anterior, e o próximo passo.

Formato: uma página acionável; o detalhe fica em anexo para quem quiser.

---

## 9. O que preciso do cliente (e o que NÃO preciso)

**Preciso apenas de:**
- 20 minutos para saber que marcas e que lojas lhe interessam mais (priorizar as de volume).
- O "sim" para usar os dados do site dele (amatoscar.pt).

**Não preciso de:** dados internos, DMS, CRM, orçamento, nem de scraping de terceiros. Nada que o exponha a um processo. *(O acesso a GA/Ads/vendas é a Fase seguinte — quando ele quiser sair do proxy para o dado real.)*

---

## 10. Como o dono vai avaliar (as três perguntas dele)

1. Trouxe uma **decisão**, não uma descrição?
2. **Provei** que funcionou, com antes-e-depois?
3. Falei em **euros e rotação**, ou em índices e cliques?

O projeto está desenhado para responder "sim" às três — com a honestidade de dizer, em cada número, até onde ele prova.

---

## 11. Riscos e limites (declarados à partida)

- **Proxy ≠ venda.** Desaparecer do stock pode ser venda, devolução, re-anúncio ou erro. Nunca apresentar como venda confirmada.
- **Atribuição do piloto.** A visibilidade é atribuível à correção; a rotação, não isoladamente em 6-8 semanas.
- **ACAP distrital é paga** — o contexto fica ao nível nacional por marca.
- **Scraper por validar** — o número de rotação só se promete depois do gate de DevTools.
- **Leitura contratual, não jurídica** — a exclusão da Standvirtual assenta na leitura dos ToS, a confirmar com apoio jurídico antes de qualquer publicação comparativa.
