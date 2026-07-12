@echo off
REM ============================================================
REM  Radar de Stock MatosCar - recolha trimestral automatica
REM  Corre o snapshot, o diagnostico, o resumo e a rotacao,
REM  e guarda os logs em data\stock-snapshots\_logs\
REM ============================================================

cd /d "C:\Users\saram\matos-car-audit\scripts\stock-radar"

set LOGDIR=..\..\data\stock-snapshots\_logs
if not exist "%LOGDIR%" mkdir "%LOGDIR%"
set STAMP=%DATE:~-4%-%DATE:~3,2%-%DATE:~0,2%

echo [%STAMP%] A recolher snapshot...
python scrape_stock.py            > "%LOGDIR%\%STAMP%-scrape.txt"    2>&1
echo [%STAMP%] A diagnosticar...
python diagnose.py                > "%LOGDIR%\%STAMP%-diagnose.txt"  2>&1
echo [%STAMP%] A resumir...
python resumo_snapshot.py         > "%LOGDIR%\%STAMP%-resumo.txt"    2>&1
echo [%STAMP%] A calcular rotacao (precisa de >=2 snapshots)...
python merge_snapshots.py         > "%LOGDIR%\%STAMP%-rotacao.txt"   2>&1

echo.
echo Concluido. Logs em: %LOGDIR%
echo Abre os ficheiros _resumo e _rotacao e cola-os ao Claude para atualizar a folha de decisao.
