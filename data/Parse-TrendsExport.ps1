<#
.SYNOPSIS
    Le os 4 ficheiros CSV exportados do Google Trends (multiTimeline, geoMap,
    relatedQueries, relatedEntities) para uma query, e gera o bloco de texto
    ja preenchido no formato do template do google-trends-protocol.md.

.DESCRIPTION
    Objectivo: eliminar o erro de transcricao manual que gerou o problema
    Setubal/Beja/Guarda encontrado na auditoria original. Os 6 distritos
    MatosCar sao uma lista fixa no codigo, nao uma copia manual - por isso
    o erro deixa de ser possivel.

.PARAMETER FolderPath
    Pasta onde estao os 4 CSVs desta query (multiTimeline.csv, geoMap.csv,
    relatedQueries.csv, relatedEntities.csv).

.PARAMETER QueryLabel
    Texto exacto da query, ex: "BMW" ou "BMW Serie 1".

.PARAMETER DataPesquisa
    Data da sessao de recolha, formato dd/MM/yyyy.

.EXAMPLE
    .\Parse-TrendsExport.ps1 -FolderPath "C:\...\bmw\trends\bmw-marca" -QueryLabel "BMW" -DataPesquisa "06/07/2026"
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$FolderPath,

    [Parameter(Mandatory = $true)]
    [string]$QueryLabel,

    [Parameter(Mandatory = $true)]
    [string]$DataPesquisa,

    [string]$OutputFile = $null,

    [string]$Observacao = $null,

    [string]$Screenshot = $null
)

# --- Lista fixa dos 6 distritos MatosCar (nao editar por sessao) ---
# Fonte: matos-car-audit-prd.md - geografia do audit.
# Setubal NAO esta nesta lista deliberadamente - nao e distrito MatosCar.
$DistritosMatosCar = @('Castelo Branco', 'Évora', 'Beja', 'Portalegre', 'Guarda', 'Santarém')

function Get-CleanLines {
    param([string]$Path, [bool]$Required = $true)
    if (-not (Test-Path $Path)) {
        if ($Required) {
            throw "Ficheiro nao encontrado: $Path"
        } else {
            return $null
        }
    }
    Get-Content -Path $Path -Encoding UTF8
}

function Parse-MultiTimeline {
    param([string]$Path)
    $lines = Get-CleanLines -Path $Path -Required $true
    $data = foreach ($line in $lines) {
        $t = $line.Trim()
        if ($t -eq '' -or $t.StartsWith('Categoria') -or $t.StartsWith('Semana')) { continue }
        $parts = $t -split ','
        if ($parts.Count -ge 2 -and $parts[1] -match '^\d+$') {
            [PSCustomObject]@{ Semana = $parts[0]; Indice = [int]$parts[1] }
        }
    }
    if ($data.Count -eq 0) { throw "multiTimeline.csv nao devolveu pontos validos - confirmar o ficheiro." }
    return $data
}

function Parse-GeoMap {
    param([string]$Path)
    $lines = Get-CleanLines -Path $Path -Required $false
    if ($null -eq $lines) { return @() }
    $data = foreach ($line in $lines) {
        $t = $line.Trim()
        if ($t -eq '' -or $t.StartsWith('Categoria') -or $t.StartsWith('Regi')) { continue }
        $parts = $t -split ','
        if ($parts.Count -ge 2) {
            $valorTexto = $parts[1].Trim()
            if ($valorTexto -match '^\d+$') {
                [PSCustomObject]@{ Regiao = $parts[0].Trim(); Indice = [int]$valorTexto }
            } elseif ($valorTexto -eq '<1') {
                # Google Trends escreve "<1" para valores positivos mas abaixo de 1 - nao e ausencia de dados
                [PSCustomObject]@{ Regiao = $parts[0].Trim(); Indice = 0 }
            }
        }
    }
    return $data
}

function Parse-TopRising {
    param([string]$Path)
    $lines = Get-CleanLines -Path $Path -Required $false
    $top = @()
    $rising = @()
    if ($null -eq $lines) {
        return @{ Top = $top; Rising = $rising; SemDados = $true }
    }
    $mode = $null
    foreach ($line in $lines) {
        $t = $line.Trim()
        if ($t -eq 'TOP') { $mode = 'TOP'; continue }
        if ($t -eq 'RISING') { $mode = 'RISING'; continue }
        if ($t -eq '' -or $t.StartsWith('Categoria') -or $t.StartsWith('"')) { continue }
        $parts = $t -split ','
        if ($parts.Count -ge 2) {
            $obj = [PSCustomObject]@{ Termo = $parts[0]; Valor = $parts[1] }
            if ($mode -eq 'TOP') { $top += $obj }
            elseif ($mode -eq 'RISING') { $rising += $obj }
        }
    }
    return @{ Top = $top; Rising = $rising; SemDados = $false }
}

# --- Ler os 4 ficheiros ---
$timeline = Parse-MultiTimeline (Join-Path $FolderPath 'multiTimeline.csv')
$geo      = Parse-GeoMap        (Join-Path $FolderPath 'geoMap.csv')
$queries  = Parse-TopRising     (Join-Path $FolderPath 'relatedQueries.csv')
$entities = Parse-TopRising     (Join-Path $FolderPath 'relatedEntities.csv')

# --- Estatisticas da serie temporal ---
$indiceMedio = [math]::Round((($timeline.Indice | Measure-Object -Average).Average), 1)
$pico = $timeline | Sort-Object Indice -Descending | Select-Object -First 1
$vale = $timeline | Sort-Object Indice | Select-Object -First 1

$n = $timeline.Count
$q = [math]::Max([int]([math]::Floor($n * 0.25)), 1)
$inicio = ($timeline[0..($q - 1)].Indice | Measure-Object -Average).Average
$fim    = ($timeline[($n - $q)..($n - 1)].Indice | Measure-Object -Average).Average
$delta  = $fim - $inicio

if ($delta -gt 8) {
    $tendencia = "Crescente (sugestao automatica - delta +$([math]::Round($delta,1)) entre inicio e fim do periodo)"
} elseif ($delta -lt -8) {
    $tendencia = "Decrescente (sugestao automatica - delta $([math]::Round($delta,1)) entre inicio e fim do periodo)"
} else {
    $tendencia = "Estavel (sugestao automatica - delta $([math]::Round($delta,1)), dentro da margem de ruido). CONFIRMAR VISUALMENTE se ha padrao sazonal - o script nao detecta sazonalidade."
}

# --- Sub-regiao ---
if ($geo.Count -eq 0) {
    $top5Nacional = @()
    $distritosResult = $DistritosMatosCar | ForEach-Object {
        [PSCustomObject]@{ Distrito = $_; Posicao = 'SEM DADOS SUFICIENTES'; Indice = '-' }
    }
} else {
    $geoOrdenado = $geo | Sort-Object Indice -Descending
    $top5Nacional = $geoOrdenado | Select-Object -First 5

    $distritosResult = foreach ($d in $DistritosMatosCar) {
        $posicao = 1
        $encontrado = $null
        foreach ($row in $geoOrdenado) {
            if ($row.Regiao -eq $d) { $encontrado = $row; break }
            $posicao++
        }
        if ($encontrado) {
            [PSCustomObject]@{ Distrito = $d; Posicao = $posicao; Indice = $encontrado.Indice }
        } else {
            [PSCustomObject]@{ Distrito = $d; Posicao = 'SEM DADOS SUFICIENTES'; Indice = '-' }
        }
    }
}

# --- Montar o bloco de texto final ---
$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("## Query: $QueryLabel")
[void]$sb.AppendLine("Data da pesquisa: $DataPesquisa")
[void]$sb.AppendLine("Janela: Ultimos 12 meses | Geografia: Portugal")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Volume")
[void]$sb.AppendLine("Indice medio: $indiceMedio")
[void]$sb.AppendLine("Pico: semana de $($pico.Semana), indice $($pico.Indice)")
[void]$sb.AppendLine("Vale: semana de $($vale.Semana), indice $($vale.Indice)")
[void]$sb.AppendLine("Tendencia: $tendencia")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Consultas relacionadas - Top (ate 5)")
if ($queries.SemDados) {
    [void]$sb.AppendLine("SEM DADOS SUFICIENTES (ficheiro relatedQueries.csv nao disponivel na exportacao)")
} else {
    $queries.Top | Select-Object -First 5 | ForEach-Object { [void]$sb.AppendLine("- $($_.Termo) - $($_.Valor)") }
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Consultas relacionadas - Em ascensao (ate 5)")
if ($queries.SemDados) {
    [void]$sb.AppendLine("SEM DADOS SUFICIENTES (ficheiro relatedQueries.csv nao disponivel na exportacao)")
} else {
    $queries.Rising | Select-Object -First 5 | ForEach-Object { [void]$sb.AppendLine("- $($_.Termo) - $($_.Valor)") }
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Topicos relacionados - Top (ate 5)")
if ($entities.SemDados) {
    [void]$sb.AppendLine("SEM DADOS SUFICIENTES (ficheiro relatedEntities.csv nao disponivel na exportacao)")
} else {
    $entities.Top | Select-Object -First 5 | ForEach-Object { [void]$sb.AppendLine("- $($_.Termo) - $($_.Valor)") }
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Topicos relacionados - Em ascensao (ate 5)")
if ($entities.SemDados) {
    [void]$sb.AppendLine("SEM DADOS SUFICIENTES (ficheiro relatedEntities.csv nao disponivel na exportacao)")
} else {
    $entities.Rising | Select-Object -First 5 | ForEach-Object { [void]$sb.AppendLine("- $($_.Termo) - $($_.Valor)") }
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Top 5 nacional (sub-regiao)")
$i = 1
$top5Nacional | ForEach-Object { [void]$sb.AppendLine("$i. $($_.Regiao) - $($_.Indice)"); $i++ }
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Distritos MatosCar (lista fixa de 6 - gerado programaticamente, Setubal excluido por definicao)")
$distritosResult | ForEach-Object { [void]$sb.AppendLine("- $($_.Distrito): posicao $($_.Posicao), indice $($_.Indice)") }
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Observacao livre")
if ($Observacao) {
    [void]$sb.AppendLine($Observacao)
} else {
    [void]$sb.AppendLine("[ preencher manualmente - uma frase para o relatorio ]")
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("### Screenshot")
if ($Screenshot) {
    [void]$sb.AppendLine($Screenshot)
} else {
    [void]$sb.AppendLine("[ nome do ficheiro ]")
}
[void]$sb.AppendLine("")
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("")

$resultado = $sb.ToString()

Write-Host $resultado

if ($OutputFile) {
    Add-Content -Path $OutputFile -Value $resultado -Encoding UTF8
    Write-Host "`n--- Bloco acrescentado a: $OutputFile ---"
}
