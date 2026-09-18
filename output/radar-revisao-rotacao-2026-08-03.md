# Radar de Procura e Rotação Local — Revisão de rotação (03-08-2026)

*Lembrete único agendado há ~3 semanas. Primeira versão gerada automaticamente às 09:30 (antes de o scrape de hoje fechar); **atualizado às 10:09 com a recolha de 03/08 já concluída** — o alerta de "ficheiro vazio" ficou resolvido.*

**Regra de ouro:** "saída de stock" é **PROXY**, nunca venda confirmada.

---

## 1. Passaram ~3 semanas — o que já temos

- **Baseline T0:** 12–13/07/2026 (~197 viaturas).
- **13 recolhas** acumuladas: 12, 13, 20, 21, 22, 23, 24, 27, 28, 29, 30, 31 de julho e **03 de agosto**.
- **Stock atual (03/08):** 197 viaturas usadas. Concentração em Évora **125/197 = 63%** (estável face aos ~65% de T0). Preço mediano 27.250 €.
- Última recolha completa: **03/08** (197 viaturas, 100% nos campos-chave, km 91%). Confirmado: a recolha de hoje **correu bem** — fechou às 10:09, depois de o lembrete ter gerado a primeira versão às 09:30. O alerta de ficheiro vazio já não se aplica.

## 2. Sinal de rotação — ainda insuficiente para uma mediana

O próprio pipeline recusa-se a reportar durações, e com razão:

- `_sobrevivencia.csv`: **estado = insuficiente, 3 eventos de 30 exigidos** → "NÃO reportar durações de listagem".
- Log de rotação (03/08): 244 veículos acompanhados em 13 recolhas; **entrada observada: 51 | saída observada: 47 | DURAÇÕES COMPLETAS: 3**. As saídas-proxy subiram (de 38 para 47), mas as durações completas continuam **paradas em 3** — confirma que o bloqueio é tempo de observação, não frequência.
- `_rotacao-por-distrito-marca.csv`: **todas as medianas suprimidas** ("sem durações completas" ou n<5). A única marca com algumas durações completas é Opel/Évora (n=3), ainda abaixo do mínimo (n≥5).

Porquê: só há "duração completa" quando vimos a viatura **entrar E sair** dentro da janela. Com apenas ~3 semanas de observação, quase todo o stock de T0 está censurado à esquerda (não sabemos a data real de entrada). É uma limitação de **tempo de observação**, não de dados em falta.

### O que dá para ler (proxy, com cautela)
Saídas-proxy acumuladas por marca em Évora (foco volume): BMW 7, Opel 6, Hyundai 4, Peugeot 4, Kia 3, Nissan 3, VW 3, BYD 1, Skoda 1, Volvo 1. Fora de Évora, contagens de 1–2. **Nenhuma mediana de dias-listado é reportável ainda.**

Preços: 28 alterações na recolha de 03/08 (27 descidas, 1 subida), descida mediana ~500 €.

### Estimativa de ordem de grandeza (NÃO é a mediana — só sanity check)
- 47 saídas-proxy sobre um stock médio de ~200, em 22 dias (12/07→03/08) → ~23% em 22 dias → hazard ≈ **1,1%/dia**.
- Mediana sob hazard constante = ln(2)/0,011 ≈ **~65 dias**.
- Consistente com a hipótese de "~60 dias" do PRD, mas assenta em pressupostos fortes (hazard constante) e em apenas 3 durações completas. **Tratar como palpite, não como resultado.**

## 3. Calibração da cadência de recolha — a decisão central desta revisão

Facto: a recolha **não** tem corrido semanal — corre **quase todos os dias** (`_cadencia.csv`: 12 intervalos, mediana **1 dia**, máx 7). Para um stock que roda na escala de **~2 meses**, isto é sobre-amostragem.

**Recomendação:** aliviar de quase-diária para **semanal** (ou a cada 10–14 dias).
- A regra "amostrar 3–4× dentro do tempo de rotação" com mediana provável ~60–70 dias → uma recolha a cada **10–15 dias** chega para estimar a rotação.
- Sugiro **semanal** como meio-termo: mantém a censura de intervalo apertada (data de saída ±7 dias em vez de ±14) por muito pouco esforço extra, e alinha com a janela de segunda-feira já agendada.
- Mudar em `scripts/stock-radar/AGENDAR-WINDOWS.md` (Windows Task Scheduler).

**Ponto importante:** o que falta para uma mediana real é **tempo decorrido**, não frequência. Aumentar a cadência não acelera a acumulação das 30 durações completas — só o tempo o faz (à medida que as 51 entradas pós-T0 forem saindo). Realisticamente, mais algumas semanas a meses até termos curva de sobrevivência.

## 4. Recolhas falhadas / degradadas

- Completude **sólida** nas 13 recolhas (197–222 viaturas por recolha, 100% nos campos-chave, km estável a ~91%). Nenhuma caiu abaixo do limiar de sanidade (50% da maior), logo nenhuma foi ignorada no merge.
- Notas menores: 1 ficha incompleta excluída em 23/07; 17 viaturas sem km em 03/08 (não crítico).
- **Sem alertas abertos:** a recolha de 03/08 concluiu (197 viaturas). Nada a reexecutar.

## 5. Folha de decisão para o Pedro Matos

**Não construída nesta revisão**, por decisão consciente: sem medianas de dias-listado reportáveis, a folha não teria o número central (rotação-proxy por distrito/marca). Fica como entregável **a pedido**, assim que houver ≥30 durações completas (ou pelo menos ≥5 por célula distrito/marca nas marcas de volume). Para a BYD (stock mínimo — 1 em Évora), o sinal útil continua a ser **visibilidade (Google Business)**, não rotação.

---

### Próximos passos sugeridos
1. Reduzir a cadência do Task Scheduler de quase-diária para **semanal** (`scripts/stock-radar/AGENDAR-WINDOWS.md`).
2. Rever de novo dentro de ~4–6 semanas: verificar se as durações completas se aproximam de 30 para libertar a curva de sobrevivência e, aí sim, a folha de decisão para o Pedro Matos.

---

## Registo de leituras diárias (pós-revisão)

Leituras confirmadas depois da revisão de 03/08. Cadência mantém-se diária. Métrica central a acompanhar: **durações completas** (precisa ≥30 para libertar a curva de sobrevivência). "Saída de stock" continua a ser PROXY.

| Data | Stock | Évora | Preço mediano | Entrada-proxy | Saída-proxy | **Durações completas** | Preços alterados | Notas |
|---|---|---|---|---|---|---|---|---|
| 03/08 | 197 | 125 (63%) | 27.250 € | 51 | 47 | 3 / 30 | 28 (27↓) | recolha confirmada; sem alertas |
| 05/08 | 205 | 127 (62%) | 26.950 € | 63 | 51 | 3 / 30 | 28 (27↓) | BYD 1→3 em stock |
| 06/08 | 204 | 127 (62%) | 27.120 € | 66 | 55 | 4 / 30 | 29 (28↓) | +1 duração completa vs 03/08 |
| 07/08 | 202 | 125 (62%) | 26.970 € | 68 | 59 | 4 / 30 | 30 (29↓) | — |
| 10/08 | 198 | 122 (62%) | 27.120 € | 68 | 63 | 6 / 30 | 30 (29↓) | +2 durações completas; fim de semana sem recolha (08–09) |
| 11/08 | 202 | 124 (61%) | 26.970 € | 72 | 63 | 6 / 30 | 32 (31↓) | — |
| 12/08 | 205 | 124 (61%) | 26.950 € | 75 | 63 | 6 / 30 | 32 (31↓) | — |
| 13/08 | 202 | 121 (60%) | 26.950 € | 75 | 66 | 7 / 30 | 32 (31↓) | +1 duração completa |

Leitura (03→13/08): 10 recolhas, durações completas de 3 para **7 / 30** — ainda insuficiente, sem mediana de dias-listado reportável em nenhuma data. Ritmo de acumulação ~0,4/dia úteis; ao mesmo passo, o limiar de 30 fica realisticamente a **~7–9 semanas** de distância (meados a fim de outubro). A concentração em Évora afrouxou de leve (63%→60%), dentro do ruído normal. Preços mantêm pressão descendente constante (~31 descidas por recolha, mediana ~500 €). Confirma-se que o bloqueio é tempo de calendário, não frequência.
