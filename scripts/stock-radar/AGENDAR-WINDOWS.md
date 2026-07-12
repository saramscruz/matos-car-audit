# Agendar a recolha automática (Windows)

Há duas camadas de agendamento — usa uma ou as duas.

## 1. Lembrete via Claude (já criado)
Já ficou criada uma tarefa no Claude que te avisa **a cada trimestre** (8 de março, junho, setembro e dezembro, 9h) para correres a recolha e me colares os resultados. Corre enquanto a app Claude estiver aberta; se estiver fechada na data, dispara no arranque seguinte. Geres em **Scheduled**, na barra lateral.

## 2. Automação 100% local (Windows Task Scheduler)
Isto faz a recolha correr **sozinha na tua máquina**, sem depender de nada — é onde ela deve viver, porque é a tua máquina que alcança o site.

**Passo único — cola este comando no PowerShell** (abre como Administrador):

```
schtasks /Create /TN "MatosCar Radar Stock" /TR "C:\Users\saram\matos-car-audit\scripts\stock-radar\run-radar.bat" /SC MONTHLY /MO 3 /D 8 /ST 09:00
```

- `/SC MONTHLY /MO 3 /D 8` → a cada 3 meses, no dia 8
- `/ST 09:00` → às 9h
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
