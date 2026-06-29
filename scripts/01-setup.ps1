# 01-setup.ps1
# MatosCar Regional Demand Audit - Project Setup
# Uso: .\01-setup.ps1 [-RootPath "C:\caminho\para\projecto"]

param(
    [string]$RootPath = ".\matos-car-audit"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$divider = "-" * 50

function Write-Step {
    param([string]$Message)
    Write-Host ""
    Write-Host "> $Message" -ForegroundColor Cyan
}

function Write-Done {
    param([string]$Message)
    Write-Host "  OK $Message" -ForegroundColor Green
}

function Write-Warn {
    param([string]$Message)
    Write-Host "  AV $Message" -ForegroundColor Yellow
}

# --- VERIFICACOES ---

Write-Step "A verificar dependencias"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git nao encontrado. Instala em https://git-scm.com antes de continuar."
    exit 1
}
Write-Done "Git disponivel ($(git --version))"

$root = $RootPath

if (Test-Path $root) {
    Write-Warn "A pasta '$RootPath' ja existe."
    $confirm = Read-Host "  Continuar mesmo assim? Os ficheiros existentes nao sao apagados. (s/n)"
    if ($confirm -ne "s") {
        Write-Host "  Setup cancelado." -ForegroundColor Red
        exit 0
    }
}

# --- ESTRUTURA DE PASTAS ---

Write-Step "A criar estrutura de pastas em '$root'"

$brands = @("bmw", "audi", "volkswagen", "byd", "citroen")
$modules = @("trends", "funnel", "competitive")

$folders = @(
    "$root\prd",
    "$root\methodology",
    "$root\data",
    "$root\scripts",
    "$root\output\drafts",
    "$root\output\final"
)

foreach ($brand in $brands) {
    foreach ($module in $modules) {
        $folders += "$root\assets\$brand\$module"
    }
    $folders += "$root\data\$brand"
}

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
}

Write-Done "$($folders.Count) pastas criadas"

# --- FICHEIROS DE REGISTO POR MARCA ---

Write-Step "A criar ficheiros de registo por marca"

$brandTemplate = @'
# MARCA - Registo de Fieldwork
**MatosCar Regional Demand Audit - 2026**

---

## Modulo 1 - Google Trends

> Preencher com base no protocolo: methodology/google-trends-protocol.md

**Sessao**
- Data:
- Hora de inicio:

**Sintese**
- Demand tier: [ High / Medium / Low / Emerging ]
- Finding (uma frase):

---

## Modulo 2 - Funil Digital

> Preencher com base no protocolo: methodology/funnel-observation-checklist.md

**Sessao**
- Data:
- Hora de inicio:

**Scorecard**
| Checkpoint | Resultado |
|-----------|-----------|
| CP1 Findability | |
| CP2 Listing/stock | |
| CP3 Preco visivel | |
| CP4 CTA | |
| CP5 Pos-clique | |
| CP6 Formulario | |
| CP7 Mobile | |
| CP8 Chat/callback | |
| CP9 Campanhas | |
| CP10 Conteudo EV | |

**O que funciona:**
-

**O que esta em falta:**
-

**Finding (uma frase):**

---

## Modulo 3 - Visibilidade Competitiva

> Preencher com base no protocolo: methodology/competitive-visibility-protocol.md

**Sessao**
- Data:
- Hora de inicio:

| Distrito | MatosCar organico | MatosCar maps | Anuncio pago | Concorrente principal |
|----------|:-----------------:|:-------------:|:------------:|----------------------|
| Castelo Branco | | | | |
| Evora | | | | |
| Beja | | | | |
| Portalegre | | | | |
| Guarda | | | | |
| Abrantes | | | | |
| Santarem | | | | |

**Finding (uma frase):**

---

## Finding final desta marca (para o relatorio)

> Uma frase. Vai directamente para a pagina da marca no PDF.

'@

foreach ($brand in $brands) {
    $content = $brandTemplate -replace "MARCA", $brand.ToUpper()
    $path = "$root\data\$brand\$brand.md"
    if (-not (Test-Path $path)) {
        Set-Content -Path $path -Value $content -Encoding UTF8
        Write-Done "$brand.md criado"
    } else {
        Write-Warn "$brand.md ja existe - nao substituido"
    }
}

# --- README ---

Write-Step "A criar README.md"

$readmeContent = @'
# MatosCar Regional Demand Audit - 2026

Demand signal audit para A MatosCar, cobrindo 5 marcas na area de operacao do grupo.
Prepared by Sara Cruz.

---

## Estrutura

```
matos-car-audit/
  prd/                          PRD e documentacao de projecto
  methodology/                  Protocolos de fieldwork
  data/[marca]/[marca].md       Registo de fieldwork por marca
  assets/[marca]/trends/        Screenshots Google Trends
  assets/[marca]/funnel/        Screenshots observacao do site
  assets/[marca]/competitive/   Screenshots pesquisas competitivas
  scripts/                      Scripts PowerShell
  output/drafts/                Rascunhos do relatorio
  output/final/                 PDF final
```

---

## Sequencia de execucao

| Dia | Tarefa |
|-----|--------|
| Dia 0 | Setup do projecto |
| Dia 1 | Google Trends - 5 marcas |
| Dia 2 | Observacao do funil - 5 marcas |
| Dia 3 | Visibilidade competitiva - 35 pesquisas |
| Dia 4-5 | Redaccao do relatorio |
| Dia 6 | Producao do PDF |
| Dia 7 | Revisao e entrega |

---

## Marcas em scope

BMW - Audi - Volkswagen - BYD - Citroen

## Geografia em scope

Castelo Branco - Evora - Beja - Portalegre - Guarda - Abrantes/Santarem
'@

$readmePath = "$root\README.md"
if (-not (Test-Path $readmePath)) {
    Set-Content -Path $readmePath -Value $readmeContent -Encoding UTF8
    Write-Done "README.md criado"
} else {
    Write-Warn "README.md ja existe - nao substituido"
}

# --- GITIGNORE ---

Write-Step "A criar .gitignore"

$gitignoreContent = @'
# Sistema
.DS_Store
Thumbs.db
desktop.ini

# Output intermedio
output/drafts/*.tmp

# Credenciais
*.env
secrets.ps1
api-key.txt
'@

$gitignorePath = "$root\.gitignore"
if (-not (Test-Path $gitignorePath)) {
    Set-Content -Path $gitignorePath -Value $gitignoreContent -Encoding UTF8
    Write-Done ".gitignore criado"
} else {
    Write-Warn ".gitignore ja existe - nao substituido"
}

# --- GIT INIT ---

Write-Step "A inicializar repositorio Git"

Push-Location $root

if (Test-Path ".git") {
    Write-Warn "Repositorio Git ja inicializado - a saltar"
} else {
    git init | Out-Null
    git add . | Out-Null
    git commit -m "chore: setup inicial do projecto MatosCar audit" | Out-Null
    Write-Done "Repositorio inicializado com commit inicial"
}

Pop-Location

# --- SUMARIO ---

Write-Host ""
Write-Host $divider -ForegroundColor DarkGray
Write-Host "  Setup concluido." -ForegroundColor White
Write-Host "  Projecto em: $root" -ForegroundColor White
Write-Host ""
Write-Host "  Proximos passos:" -ForegroundColor White
Write-Host "  1. Copia os ficheiros de metodologia para $root\methodology\" -ForegroundColor Gray
Write-Host "  2. Copia o PRD para $root\prd\" -ForegroundColor Gray
Write-Host "  3. Liga o repositorio ao GitHub:" -ForegroundColor Gray
Write-Host "     git remote add origin https://github.com/[username]/matos-car-audit.git" -ForegroundColor DarkGray
Write-Host "     git push -u origin main" -ForegroundColor DarkGray
Write-Host "  4. Comeca o fieldwork: Dia 1 - Google Trends" -ForegroundColor Gray
Write-Host $divider -ForegroundColor DarkGray
Write-Host ""
