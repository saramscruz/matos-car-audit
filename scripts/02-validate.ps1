# 02-validate.ps1
# MatosCar Regional Demand Audit — Validação de Fieldwork
# Verifica que os campos obrigatórios estão preenchidos antes de escrever o relatório
# Uso: .\02-validate.ps1 [-RootPath "C:\caminho\para\projecto"]

param(
    [string]$RootPath = ".\matos-car-audit"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

function Write-Step {
    param([string]$Message)
    Write-Host "`n▸ $Message" -ForegroundColor Cyan
}

function Write-Pass {
    param([string]$Message)
    Write-Host "  ✓ $Message" -ForegroundColor Green
}

function Write-Fail {
    param([string]$Message)
    Write-Host "  ✗ $Message" -ForegroundColor Red
}

function Write-Warn {
    param([string]$Message)
    Write-Host "  ⚠ $Message" -ForegroundColor Yellow
}

# Verifica se uma linha no ficheiro está preenchida (não vazia após o delimitador)
function Test-FieldFilled {
    param(
        [string[]]$Lines,
        [string]$FieldPattern
    )
    $line = $Lines | Where-Object { $_ -match $FieldPattern } | Select-Object -First 1
    if (-not $line) { return $false }
    # Remove o padrão e verifica se sobra conteúdo
    $value = $line -replace $FieldPattern, "" -replace "^\s*:\s*", "" -replace "^\s*\|\s*", "" 
    $value = $value.Trim(" ", "|", "[", "]")
    return ($value.Length -gt 0 -and $value -notmatch "^\[" -and $value -ne "")
}

# ─────────────────────────────────────────────
# VERIFICAR PASTA
# ─────────────────────────────────────────────

if (-not (Test-Path $RootPath)) {
    Write-Error "Pasta '$RootPath' não encontrada. Corre primeiro o 01-setup.ps1."
    exit 1
}

$root = Resolve-Path $RootPath
$brands = @("bmw", "audi", "volkswagen", "byd", "citroen")
$errors = 0
$warnings = 0
$passed = 0

Write-Host "`nMatosCar Audit — Validação de Fieldwork" -ForegroundColor White
Write-Host ("─" * 50) -ForegroundColor DarkGray
Write-Host "  Projecto: $root" -ForegroundColor Gray
Write-Host "  Data: $(Get-Date -Format 'dd/MM/yyyy HH:mm')" -ForegroundColor Gray

# ─────────────────────────────────────────────
# VERIFICAR FICHEIROS DE MARCA
# ─────────────────────────────────────────────

foreach ($brand in $brands) {

    Write-Step $brand.ToUpper()

    $filePath = "$root\data\$brand\$brand.md"

    # Ficheiro existe?
    if (-not (Test-Path $filePath)) {
        Write-Fail "Ficheiro $brand.md não encontrado em data\$brand\"
        $errors++
        continue
    }

    $lines = Get-Content $filePath -Encoding UTF8

    # ── MÓDULO 1 ──
    $m1Date    = Test-FieldFilled $lines "^- Data:"
    $m1Tier    = $lines | Where-Object { $_ -match "Demand tier:" -and $_ -match "(High|Medium|Low|Emerging)" }
    $m1Finding = $lines | Select-String "Finding \(uma frase\):" | Select-Object -Skip 0 -First 1

    # Finding preenchido = linha seguinte ao label tem conteúdo
    $m1FindingIdx = ($lines | Select-String "## Módulo 1" | Select-Object -First 1).LineNumber
    $m1FindingFilled = $false
    if ($m1FindingIdx) {
        $findingLine = $lines | Where-Object { $_ -match "^- Finding \(uma frase\):" } | Select-Object -First 1
        if ($findingLine) {
            $val = ($findingLine -replace "^- Finding \(uma frase\):\s*", "").Trim()
            $m1FindingFilled = $val.Length -gt 3
        }
    }

    if ($m1Date)              { Write-Pass "M1 — Data preenchida";          $passed++ }
    else                      { Write-Warn "M1 — Data em falta";            $warnings++ }

    if ($m1Tier)              { Write-Pass "M1 — Demand tier preenchido";   $passed++ }
    else                      { Write-Fail "M1 — Demand tier em falta";     $errors++ }

    if ($m1FindingFilled)     { Write-Pass "M1 — Finding preenchido";       $passed++ }
    else                      { Write-Fail "M1 — Finding em falta";         $errors++ }

    # ── MÓDULO 2 ──
    $m2Date = Test-FieldFilled $lines "^- Data:" # segunda ocorrência
    
    # Scorecard: verifica se pelo menos 8 dos 10 checkpoints têm valor
    $scorecardLines = $lines | Where-Object { $_ -match "^\| CP\d" }
    $filledCPs = ($scorecardLines | Where-Object { 
        $_ -match "\|\s*(Bom|Aceitável|Problema|Falha)\s*\|" 
    }).Count

    $m2Finding = $lines | Where-Object { $_ -match "^\*\*Finding \(uma frase\):\*\*" }
    $m2FindingIdx = [array]::IndexOf($lines, ($m2Finding | Select-Object -First 1))
    $m2FindingFilled = $false
    if ($m2FindingIdx -ge 0 -and $m2FindingIdx -lt ($lines.Count - 1)) {
        $nextLine = $lines[$m2FindingIdx + 1].Trim()
        $m2FindingFilled = $nextLine.Length -gt 3 -and $nextLine -ne ""
    }

    if ($filledCPs -ge 8)     { Write-Pass "M2 — Scorecard preenchido ($filledCPs/10 checkpoints)"; $passed++ }
    elseif ($filledCPs -ge 5) { Write-Warn "M2 — Scorecard incompleto ($filledCPs/10 checkpoints)"; $warnings++ }
    else                      { Write-Fail "M2 — Scorecard em falta ($filledCPs/10 checkpoints)";    $errors++ }

    if ($m2FindingFilled)     { Write-Pass "M2 — Finding preenchido";       $passed++ }
    else                      { Write-Fail "M2 — Finding em falta";         $errors++ }

    # ── MÓDULO 3 ──
    $districtLines = $lines | Where-Object { 
        $_ -match "^\|\s*(Castelo Branco|Évora|Beja|Portalegre|Guarda|Abrantes|Santarém)\s*\|" 
    }
    $filledDistricts = ($districtLines | Where-Object { 
        ($_ -split "\|" | Where-Object { $_.Trim() -match "^[✓✗?]$" }).Count -gt 0
    }).Count

    $m3Finding = $lines | Where-Object { $_ -match "^\*\*Finding \(uma frase\):\*\*" } | Select-Object -Last 1
    $m3FindingIdx = [array]::LastIndexOf($lines, $m3Finding)
    $m3FindingFilled = $false
    if ($m3FindingIdx -ge 0 -and $m3FindingIdx -lt ($lines.Count - 1)) {
        $nextLine = $lines[$m3FindingIdx + 1].Trim()
        $m3FindingFilled = $nextLine.Length -gt 3 -and $nextLine -ne ""
    }

    if ($filledDistricts -ge 6) { Write-Pass "M3 — Tabela de distritos preenchida ($filledDistricts/7)"; $passed++ }
    elseif ($filledDistricts -ge 3) { Write-Warn "M3 — Tabela incompleta ($filledDistricts/7 distritos)"; $warnings++ }
    else                        { Write-Fail "M3 — Tabela de distritos em falta";                          $errors++ }

    if ($m3FindingFilled)       { Write-Pass "M3 — Finding preenchido";       $passed++ }
    else                        { Write-Fail "M3 — Finding em falta";         $errors++ }

    # ── FINDING FINAL ──
    $finalFindingSection = $lines | Where-Object { $_ -match "^## Finding final desta marca" }
    $finalIdx = [array]::IndexOf($lines, ($finalFindingSection | Select-Object -First 1))
    $finalFilled = $false
    if ($finalIdx -ge 0) {
        # Procura a primeira linha com conteúdo após o header da secção
        for ($i = $finalIdx + 1; $i -lt [Math]::Min($finalIdx + 5, $lines.Count); $i++) {
            $l = $lines[$i].Trim()
            if ($l.Length -gt 5 -and $l -notmatch "^>" -and $l -notmatch "^#") {
                $finalFilled = $true
                break
            }
        }
    }

    if ($finalFilled) { Write-Pass "Finding final preenchido";  $passed++ }
    else              { Write-Fail "Finding final em falta";     $errors++ }

    # ── SCREENSHOTS ──
    foreach ($module in @("trends", "funnel", "competitive")) {
        $assetPath = "$root\assets\$brand\$module"
        $count = (Get-ChildItem $assetPath -File -ErrorAction SilentlyContinue).Count
        if ($count -gt 0) { Write-Pass "Assets $module — $count ficheiro(s)"; $passed++ }
        else              { Write-Warn "Assets $module — pasta vazia (screenshots em falta)"; $warnings++ }
    }
}

# ─────────────────────────────────────────────
# RESULTADO FINAL
# ─────────────────────────────────────────────

Write-Host "`n" + ("─" * 50) -ForegroundColor DarkGray
Write-Host "  RESULTADO DA VALIDAÇÃO" -ForegroundColor White
Write-Host "  ✓ Passou:    $passed" -ForegroundColor Green
Write-Host "  ⚠ Avisos:   $warnings" -ForegroundColor Yellow
Write-Host "  ✗ Erros:    $errors" -ForegroundColor Red
Write-Host ("─" * 50) -ForegroundColor DarkGray

if ($errors -eq 0 -and $warnings -eq 0) {
    Write-Host "`n  Fieldwork completo. Podes começar a escrever o relatório.`n" -ForegroundColor Green
    exit 0
} elseif ($errors -eq 0) {
    Write-Host "`n  Fieldwork essencial completo. Resolve os avisos antes de entregar.`n" -ForegroundColor Yellow
    exit 0
} else {
    Write-Host "`n  Fieldwork incompleto. Resolve os erros antes de escrever o relatório.`n" -ForegroundColor Red
    exit 1
}
