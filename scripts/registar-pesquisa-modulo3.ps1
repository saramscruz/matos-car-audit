# registar-pesquisa-modulo3.ps1
# Modulo 3 - Visibilidade Competitiva - amatoscar.pt
#
# Script interactivo para registar UMA pesquisa de cada vez.
# Faz as perguntas na ordem exacta do protocolo (competitive-visibility-protocol.md),
# mostra um resumo, e so escreve nos ficheiros depois de confirmares.
#
# Como usar:
#   1. Faz a pesquisa no Chrome incognito a 390px primeiro.
#   2. Tira o screenshot e guarda-o nesta sessao (o script ajuda-te a nomear no fim).
#   3. Corre este script e responde as perguntas com base no que viste no ecra.
#
# O script escreve em:
#   - brands\[marca].md           (registo detalhado, igual ao Modulo 2)
#   - assets\_geral\modulo3-tracking.md   (tabela resumo)
#   - methodology\modulo3-tracking.md     (copia identica, mantida em sincronia)

$ErrorActionPreference = "Stop"

function Ask($pergunta) {
    return Read-Host $pergunta
}

function AskSimNao($pergunta) {
    do {
        $r = Read-Host "$pergunta (s/n)"
        $r = $r.Trim().ToLower()
    } while ($r -ne "s" -and $r -ne "n")
    return $r
}

Write-Host ""
Write-Host "=== Modulo 3 - Registo de Pesquisa ===" -ForegroundColor Cyan
Write-Host "Responde com base apenas no que esta visivel no ecra, sem scroll." -ForegroundColor DarkGray
Write-Host ""

# --- Identificacao da pesquisa ---
$marcas = @("BMW", "Audi", "Volkswagen", "BYD", "Citroen")
Write-Host "Marcas disponiveis: $($marcas -join ', ')"
$marca = Ask "Marca"
$marcaPasta = $marca.ToLower() -replace "ë", "e" -replace "é", "e"

$distrito = Ask "Distrito (ex: Beira Interior, Alentejo Central, Santarem/Abrantes)"
$cidade = Ask "Capital pesquisada (ex: Castelo Branco, Evora, Abrantes, Santarem)"
$query = Ask "Query exacta tal como escrita no Google (ex: BMW Castelo Branco)"
$dataObs = Ask "Data da observacao (dd/mm/aaaa)"
$horaObs = Ask "Hora (hh:mm)"

# --- Anuncios pagos ---
Write-Host ""
Write-Host "--- ANUNCIOS PAGOS ---" -ForegroundColor Yellow
$temAnuncio = AskSimNao "Existe algum anuncio pago nos resultados"
$anunciante1 = ""
$anunciante2 = ""
$matosAnuncio = "n"
if ($temAnuncio -eq "s") {
    $anunciante1 = Ask "Anunciante 1 (nome/dominio)"
    $anunciante2 = Ask "Anunciante 2 (deixa vazio se nao existir)"
    $matosAnuncio = AskSimNao "A MatosCar tem anuncio pago"
}

# --- Resultados organicos ---
Write-Host ""
Write-Host "--- RESULTADOS ORGANICOS ---" -ForegroundColor Yellow
$res1 = Ask "Resultado 1 (titulo + dominio)"
$res2 = Ask "Resultado 2 (titulo + dominio)"
$res3 = Ask "Resultado 3 (titulo + dominio)"
$matosOrganico = AskSimNao "A MatosCar aparece nos primeiros 3 resultados organicos"
$posOrganico = ""
$matosOutroPonto = ""
if ($matosOrganico -eq "s") {
    $posOrganico = Ask "Em que posicao (1, 2 ou 3)"
} else {
    $matosOutroPonto = AskSimNao "Aparece noutro ponto visivel da SERP sem scroll"
    if ($matosOutroPonto -eq "s") {
        $matosOutroPonto = Ask "Descreve onde"
    } else {
        $matosOutroPonto = "n"
    }
}

# --- Local Pack ---
Write-Host ""
Write-Host "--- GOOGLE MAPS / LOCAL PACK ---" -ForegroundColor Yellow
$temLocalPack = AskSimNao "Existe Local Pack (bloco de mapas) nos resultados"
$matosMaps = "n"
$posMaps = ""
$outrosDealersMaps = ""
if ($temLocalPack -eq "s") {
    $matosMaps = AskSimNao "A MatosCar aparece no Local Pack"
    if ($matosMaps -eq "s") {
        $posMaps = Ask "Posicao no Local Pack (1, 2 ou 3)"
    }
    $outrosDealersMaps = Ask "Outros dealers no Local Pack (nome + cidade, separados por vírgula)"
}

# --- Concorrentes ---
Write-Host ""
Write-Host "--- CONCORRENTES IDENTIFICADOS ---" -ForegroundColor Yellow
$conc1 = Ask "Concorrente 1 (nome + dominio, deixa vazio se nao houver)"
$conc2 = Ask "Concorrente 2 (deixa vazio se nao houver)"
$conc3 = Ask "Concorrente 3 (deixa vazio se nao houver)"
$concorrentePrincipal = Ask "Concorrente PRINCIPAL desta pesquisa (para a tabela de tracking)"

# --- Screenshot e observacao ---
Write-Host ""
$screenshotNome = "$($cidade.ToLower() -replace ' ','-' -replace 'é','e' -replace 'ã','a')-$($marcaPasta).png"
Write-Host "Nome de screenshot esperado: $screenshotNome" -ForegroundColor DarkGray
$confirmaScreenshot = AskSimNao "Confirmas que ja guardaste o screenshot com este nome em assets\$marcaPasta\competitive\"
$observacao = Ask "Observacao livre (uma frase, so se houver algo inesperado - deixa vazio se nao)"

# --- Resumo antes de gravar ---
Write-Host ""
Write-Host "=== RESUMO ===" -ForegroundColor Cyan
Write-Host "Marca: $marca | Distrito: $distrito | Cidade: $cidade"
Write-Host "Query: $query"
Write-Host "MatosCar organico top3: $matosOrganico $(if($posOrganico){"(pos $posOrganico)"})"
Write-Host "MatosCar Local Pack: $matosMaps $(if($posMaps){"(pos $posMaps)"})"
Write-Host "Anuncio pago presente: $temAnuncio | MatosCar tem anuncio: $matosAnuncio"
Write-Host "Concorrente principal: $concorrentePrincipal"
Write-Host "Screenshot confirmado: $confirmaScreenshot"
Write-Host ""

$confirmaGravar = AskSimNao "Confirmas que queres GRAVAR este registo nos ficheiros"
if ($confirmaGravar -ne "s") {
    Write-Host "Cancelado. Nada foi escrito." -ForegroundColor Red
    exit
}

# --- Escrever no ficheiro da marca ---
$ficheiroMarca = ".\brands\$marcaPasta.md"
if (-not (Test-Path $ficheiroMarca)) {
    Write-Host "AVISO: $ficheiroMarca nao encontrado. Nada foi escrito na marca." -ForegroundColor Red
} else {
    $bloco = @"

## Modulo 3 - Pesquisa: $query
Query: $query
Distrito / cidade: $distrito / $cidade
Data: $dataObs  Hora: $horaObs

— ANUNCIOS PAGOS —
Existe anuncio pago: $temAnuncio
Anunciante 1: $anunciante1
Anunciante 2: $anunciante2
MatosCar tem anuncio pago: $matosAnuncio

— RESULTADOS ORGANICOS —
Resultado 1: $res1
Resultado 2: $res2
Resultado 3: $res3
MatosCar aparece nos top 3 organicos: $matosOrganico
Posicao: $posOrganico
Aparece noutro ponto visivel sem scroll: $matosOutroPonto

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack: $temLocalPack
MatosCar aparece no Local Pack: $matosMaps
Posicao no Local Pack: $posMaps
Outros dealers no Local Pack: $outrosDealersMaps

— CONCORRENTES IDENTIFICADOS —
1. $conc1
2. $conc2
3. $conc3

Screenshot: $screenshotNome
Observacao livre: $observacao
"@
    Add-Content -Path $ficheiroMarca -Encoding UTF8 -Value $bloco
    Write-Host "Gravado em $ficheiroMarca" -ForegroundColor Green
}

# --- Escrever linha de log na tabela de tracking (ambas as copias) ---
# Nota: como a tabela markdown e dificil de editar linha-a-linha por script de forma fiavel,
# em vez de tentar localizar e substituir a celula exacta (fragil, propenso a erro),
# acrescentamos um registo estruturado no fim do ficheiro, numa secção "Log de pesquisas".
# Tu depois transferes para a tabela principal quando reveres - ou usamos isto tal como esta,
# a tua escolha.

$linhaLog = "| $marca | $distrito | $cidade | ``$query`` | $matosOrganico$(if($posOrganico){" (pos $posOrganico)"}) | $matosMaps$(if($posMaps){" (pos $posMaps)"}) | $temAnuncio | $matosAnuncio | $concorrentePrincipal | $screenshotNome |"

$ficheirosTracking = @(".\assets\_geral\modulo3-tracking.md", ".\methodology\modulo3-tracking.md")
foreach ($ft in $ficheirosTracking) {
    if (-not (Test-Path $ft)) {
        Write-Host "AVISO: $ft nao encontrado. Linha de log nao escrita aqui." -ForegroundColor Red
        continue
    }
    $conteudo = Get-Content $ft -Raw -Encoding UTF8
    if ($conteudo -notmatch "## Log de pesquisas registadas \(automatico\)") {
        Add-Content -Path $ft -Encoding UTF8 -Value "`n---`n`n## Log de pesquisas registadas (automatico)`n`n| Marca | Distrito | Cidade | Query | MatosCar organico | MatosCar maps | Anuncio pago | MatosCar anuncio | Concorrente principal | Screenshot |`n|---|---|---|---|---|---|---|---|---|---|"
    }
    Add-Content -Path $ft -Encoding UTF8 -Value $linhaLog
    Write-Host "Linha de log acrescentada em $ft" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== Registo concluido. ===" -ForegroundColor Cyan
Write-Host "Lembra-te: aguarda pelo menos 30 segundos antes da proxima pesquisa (regra 5 do protocolo)." -ForegroundColor DarkGray
