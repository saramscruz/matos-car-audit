# Agendar a recolha automática (Windows)

## 1. Recolha automática vs. folha de decisão
A **recolha** corre sozinha, **todos os dias úteis** (ver secção 2) — não precisas de a lançar. A **folha de decisão** para o cliente monta-se **quando precisares** (tipicamente antes de falares com o Pedro Matos), a partir dos snapshots já acumulados: pede ao Claude "constrói a folha a partir dos logs mais recentes de `data\stock-snapshots\_logs\`" e cola os `_rotacao-*.txt` e `_resumo-*.txt`.

*(Existiu um lembrete trimestral no Claude para isto — entretanto desativado, porque a recolha semanal automática o tornou redundante. A folha passa a ser um entregável **a pedido**, não uma tarefa de calendário. Para o remover também da barra lateral, apaga-o em **Scheduled**.)*

## 2. Automação 100% local (Windows Task Scheduler)
Isto faz a recolha correr **sozinha na tua máquina**, sem depender de nada — é onde ela deve viver, porque é a tua máquina que alcança o site.

**Passo único — cola este comando no PowerShell** (abre como Administrador):

```
schtasks /Create /F /TN "MatosCar Radar Stock" /TR "C:\Users\saram\matos-car-audit\scripts\stock-radar\run-radar.bat" /SC WEEKLY /D MON,TUE,WED,THU,FRI /ST 09:30
```

> **Usa `/Create /F`, não `/Change`.** O `schtasks /Change` **não aceita** `/SC` nem `/D` — só altera hora, comando e credenciais, não o padrão de recorrência. Para mudar a frequência ou os dias é preciso recriar a tarefa; o `/F` sobrepõe a existente sem pedir confirmação.

Confirma que pegou:

```
schtasks /Query /TN "MatosCar Radar Stock"
```

O **Next Run Time** tem de passar a ser o próximo dia útil às **09:30**. Se continuar a mostrar a hora antiga, o comando não foi aplicado (janela sem privilégios de administrador, tipicamente).

- `/D MON,TUE,WED,THU,FRI` → **dias úteis**, sem fins-de-semana
- `/ST 09:30` → às 9h30
- Voltar a semanal? Troca por `/SC WEEKLY /D MON`.

> **Porquê diária e não trimestral:** a folha de decisão ao cliente é trimestral, mas a *recolha* tem de ser mais frequente do que o fenómeno que mede. A largura do intervalo entre recolhas **é** a resolução com que qualquer duração pode ser medida. Com snapshots trimestrais, os carros que entram e saem dentro do mesmo trimestre ficam invisíveis, e o dias-listado dos restantes fica com incerteza de ±90 dias. Recolher em dias úteis e **agregar** na folha trimestral dá a melhor resolução sem carga relevante para o cliente. Ver "recolha ≠ entrega" no PRD (`prd/radar-procura-rotacao-local.md`, secção 8).
>
> **A cadência não é uniforme, e isso está registado.** De 2ª a 6ª o intervalo é de 1 dia; de 6ª para 2ª é de 3 dias. Além disso, a série começou semanal (12→13/07 = 1 dia, 13→20/07 = 7 dias). O `_cadencia.csv` regista o intervalo de cada par de recolhas consecutivas, para a nota metodológica sair dos dados. **Períodos com cadências diferentes não são directamente comparáveis:** amostragem esparsa não vê os carros que entram e saem dentro do intervalo, logo sobre-representa os lentos. Ao comparar períodos, ou restringe a janelas com a mesma cadência, ou degrada a série densa à resolução da mais esparsa.
>
> **Objectivo declarado do período diário:** medir a fracção de viaturas que roda abaixo dos 3-4 dias — número que hoje é desconhecido e que o `merge_snapshots.py` passa a imprimir assim que existirem durações completas. Com esse número decide-se, com dados, se é seguro voltar a bissemanal ou semanal.
- O `run-radar.bat` corre o snapshot + diagnóstico + resumo + rotação e guarda tudo em `data\stock-snapshots\_logs\`.

**Testar já** (sem esperar pela data):
```
schtasks /Run /TN "MatosCar Radar Stock"
```
ou simplesmente faz duplo-clique no `run-radar.bat`. Demorou **~90 min** na recolha de 20/07/2026 (208 viaturas, crawl-delay de 10s). O tempo cresce com o inventário: conta ~26s por viatura.

> **A máquina tem de estar ligada às 9h30.** Uma recolha diária que falha metade dos dias é pior do que uma semanal fiável: as falhas criam buracos irregulares, que é exactamente o que a cadência densa procura eliminar. Se souberes de antemão que vais estar fora, é preferível assumir a falha e registá-la do que fingir que a série é diária.

**Ver / apagar a tarefa:**
```
schtasks /Query /TN "MatosCar Radar Stock"
schtasks /Delete /TN "MatosCar Radar Stock" /F
```

## Depois de cada recolha
Abre os logs `_resumo-*.txt` e `_rotacao-*.txt` em `data\stock-snapshots\_logs\` e cola-os ao Claude — a partir daí atualiza-se a folha de decisão com a rotação nova (proxy). Nota: a rotação só aparece a partir da 2ª recolha. **Estado em 20/07/2026: 0 durações completas** em 214 veículos — nenhuma duração de listagem é ainda reportável. O sinal utilizável hoje é o preço (`_precos-alteracoes.csv`), que é facto observado e não sofre censura.
