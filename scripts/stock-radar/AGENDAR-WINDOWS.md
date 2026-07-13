# Agendar a recolha automática (Windows)

## 1. Recolha automática vs. folha de decisão
A **recolha** corre sozinha, **semanalmente** (ver secção 2) — não precisas de a lançar. A **folha de decisão** para o cliente monta-se **quando precisares** (tipicamente antes de falares com o Pedro Matos), a partir dos snapshots já acumulados: pede ao Claude "constrói a folha a partir dos logs mais recentes de `data\stock-snapshots\_logs\`" e cola os `_rotacao-*.txt` e `_resumo-*.txt`.

*(Existiu um lembrete trimestral no Claude para isto — entretanto desativado, porque a recolha semanal automática o tornou redundante. A folha passa a ser um entregável **a pedido**, não uma tarefa de calendário. Para o remover também da barra lateral, apaga-o em **Scheduled**.)*

## 2. Automação 100% local (Windows Task Scheduler)
Isto faz a recolha correr **sozinha na tua máquina**, sem depender de nada — é onde ela deve viver, porque é a tua máquina que alcança o site.

**Passo único — cola este comando no PowerShell** (abre como Administrador):

```
schtasks /Create /TN "MatosCar Radar Stock" /TR "C:\Users\saram\matos-car-audit\scripts\stock-radar\run-radar.bat" /SC WEEKLY /D MON /ST 09:00
```

- `/SC WEEKLY /D MON` → **todas as segundas-feiras** (recolha densa, para medir a rotação com precisão)
- `/ST 09:00` → às 9h
- Preferes quinzenal? Troca por `/SC WEEKLY /MO 2 /D MON` (de 2 em 2 semanas).

> **Porquê semanal e não trimestral:** a folha de decisão ao cliente é trimestral, mas a *recolha* tem de ser mais frequente do que o fenómeno que mede. Com snapshots só de 90 em 90 dias, os carros que entram e saem dentro do mesmo trimestre ficam invisíveis à rotação, e o dias-listado dos restantes fica com incerteza de até ±90 dias. Recolher semanal e **agregar** na folha trimestral dá rotação precisa sem carga extra para o cliente. Ver a nota "recolha ≠ entrega" no PRD (`prd/radar-procura-rotacao-local.md`, secção 8).
- O `run-radar.bat` corre o snapshot + diagnóstico + resumo + rotação e guarda tudo em `data\stock-snapshots\_logs\`.

**Testar já** (sem esperar pela data):
```
schtasks /Run /TN "MatosCar Radar Stock"
```
ou simplesmente faz duplo-clique no `run-radar.bat`. Demora ~32 min (respeita o crawl-delay de 10s do site).

**Ver / apagar a tarefa:**
```
schtasks /Query /TN "MatosCar Radar Stock"
schtasks /Delete /TN "MatosCar Radar Stock" /F
```

## Depois de cada recolha
Abre os logs `_resumo-*.txt` e `_rotacao-*.txt` em `data\stock-snapshots\_logs\` e cola-os ao Claude — a partir daí atualiza-se a folha de decisão com a rotação nova (proxy). Nota: a rotação só aparece a partir da **2ª** recolha (T1, setembro), quando já há dois snapshots para comparar.
