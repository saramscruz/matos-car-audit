# BMW - Registo de Fieldwork
**MatosCar Regional Demand Audit - 2026**

---

## Modulo 1 - Google Trends

> Preencher com base no protocolo: methodology/google-trends-protocol.md

**Sessao**
- Data: 07/07/2026 (recolha refeita - substitui a sessao de 06/07/2026)
- Hora de inicio: nao registada com precisao (primeira exportacao de CSV: 12:36)

**Sintese**
- Demand tier: **Alta** (base: Módulo 0, única fonte comparável entre marcas — BMW é a líder absoluta, índice 75-100. NÃO comparar médias por query entre marcas: cada query normaliza o seu próprio pico a 100.) Tendência da marca: estável, ligeiro declínio (delta −2,4). Dados verificados 07/07/2026.
- Finding (uma frase): A BMW tem a maior procura absoluta das cinco marcas, mas essa força concentra-se no nome da marca e dilui-se ao nível do modelo, eléctrico e concessionário — com Santarém como único distrito MatosCar consistente e um outlier por explicar: a BMW Série 1 em Portalegre (2º nacional, índice 94).

---

## Modulo 2 - Funil Digital

> Preencher com base no protocolo: methodology/funnel-observation-checklist.md
> [RECONSTRUIDO EM 07/07/2026 a partir dos screenshots originais em assets/bmw/funnel/ - esta seccao estava vazia, apesar dos screenshots e da recolha existirem. Ver tambem sintese-modulo2.md, que ja citava a BMW antes desta reconstrucao.]

**Sessao**
- Data: 30/06/2026 (reconstituida a partir do relogio visivel nos screenshots - nao ha registo textual da hora de inicio da sessao)
- Hora de inicio: aprox. 15:42

**Sintese**
- CP1: Bom (1 clique, mas ver nota sobre rota alternativa)
- CP2: Aceitável (sem stock real, sem secção Motorizações)

---

## Módulo 2 — CP1 — Findability a partir da homepage

Marca: BMW
Data da observação: 30/06/2026
Hora de início: aprox. 15:42

Resultado: Bom
Caminho percorrido: Homepage > clique no logo BMW no carousel de marcas (visível directamente, sem interacção com a seta, por coincidência de timing no carregamento da página) > /gama/bmw/
Número de cliques: 1
Nota metodológica: o carousel de marcas é automático/rotativo — a posição da BMW não é fixa (mesma ressalva já registada para a Audi). Existe também um segundo screenshot (`cp1-rota-alternativa-dropdown.png`) que documenta uma rota alternativa: o selector "Encontre o seu carro" na homepage, com uma dropdown de marcas (Alfa Romeo, Audi, BMW, BYD, Citroën, ...) como caminho de descoberta que não depende do timing do carousel. BMW foi a primeira marca observada na sequência do Módulo 2, o que pode explicar por que esta rota alternativa foi documentada aqui e não nas restantes 4 marcas — não há confirmação de que tenha sido testada com o mesmo rigor nas outras marcas.
Screenshot: assets/bmw/funnel/cp1-pagina-gama-bmw.png, assets/bmw/funnel/cp1-rota-alternativa-dropdown.png
Observação: Página dedicada com URL própria (/gama/bmw/), título "Carros BMW Novos e Usados à Venda em Portugal". Três modelos em destaque no listing: Novo i3 (preço "A Consultar" — não segue o padrão "Desde X€" das outras marcas), Novo i5 M60 xDrive Touring (110.000€) e Novo i5 Touring (75.000€). Os três destaques são variantes do i3/i5 (eléctricos ou híbridos de gama alta) — nenhum modelo de combustão pura em destaque nesta amostra.

---

## Módulo 2 — CP2 — Página de modelo ou listing de stock

Marca: BMW
Data da observação: 30/06/2026
Hora de início: aprox. 16:08

Resultado: Aceitável
URL da página de marca/modelo encontrada: /carros-bmw/bmw-novo-i3/
Stock real visível: não
Número aproximado de unidades listadas: 0 (ficha de modelo genérica, sem VIN, matrícula ou quilometragem)
Screenshot: assets/bmw/funnel/cp2-modal-test-drive.png
Observação: Página "BMW Novo i3" sem stock concreto. Texto promocional describe autonomia até 500 km (WLTP) e o design da nova geração, mas **não há secção "Motorizações"** — diferença notável face às outras marcas (Audi tinha 1 variante listada, Volkswagen tinha 5, Citroën tinha 5 variantes todas rotuladas correctamente como eléctricas). Isto é consistente com o que a síntese do Módulo 2 já registava ("BMW i3: secção ausente — só galeria e vídeo"). CTA "Quero experimentar" visível no topo da página, mesmo padrão de botão que nas outras marcas — mas este screenshot específico não captura o modal aberto, por isso não é possível confirmar aqui se os campos do formulário são idênticos aos das outras marcas (Nome/Apelidos/Telefone/E-mail/Concelho/reCAPTCHA); fica como pressuposto razoável por analogia, não como facto confirmado por esta imagem.

**Scorecard**
| Checkpoint | Resultado |
|-----------|-----------|
| CP1 Findability | Bom |
| CP2 Listing/stock | Aceitável |
| CP3 Preco visivel | Parcial - i5 M60/Touring com preco, i3 "A Consultar" |
| CP4 CTA | Presente ("Quero experimentar") |
| CP5 Pos-clique | Nao confirmado por screenshot (ver nota CP2) |
| CP6 Formulario | Nao confirmado por screenshot (ver nota CP2) |
| CP7 Mobile | Nao testado nesta reconstrucao - sem screenshot mobile de BMW em assets/bmw/funnel/ |
| CP8 Chat/callback | Nao testado nesta reconstrucao - sem screenshot correspondente |
| CP9 Campanhas | Ver sintese-modulo2.md: "BMW: 1 campanha (BMW Charging, soluções empresariais), sem data de validade visível — excepção à norma das restantes campanhas" |
| CP10 Conteudo EV | Ver sintese-modulo2.md: "BMW eléctrico... zero presença no hub EV central; não testado especificamente BMW eléctrico em Usados" |

**O que funciona:**
- Página de marca dedicada e bem indexada (/gama/bmw/)
- CTA de test-drive presente e consistente com outras marcas

**O que esta em falta:**
- Sem secção "Motorizações" na ficha do i3 (única marca sem esta secção, segundo a síntese)
- i3 sem preço "Desde X€" (classificado "A Consultar"), quebrando a consistência com os outros 2 modelos em destaque
- CP7, CP8: sem screenshots que permitam confirmar nesta reconstrução (ficam como lacuna a fechar, não como "resultado mau")

**Finding (uma frase):**
A BMW tem findability boa (1 clique, página dedicada), mas a ficha do modelo em destaque (i3) é a menos completa das 5 marcas observadas — sem secção de motorizações e sem preço fixo, o que destoa da força da marca no Módulo 1.

---

## Modulo 3 - Visibilidade Competitiva

> Preencher com base no protocolo: methodology/competitive-visibility-protocol.md
> [RECONSTRUIDO EM 07/07/2026 a partir dos 27 screenshots originais em assets/bmw/competitive/ - esta seccao estava vazia, apesar da recolha (7 pesquisas, linhas 1, 6, 11, 16, 21, 26, 31 de methodology/modulo3-tracking.md) e das sinteses (sintese-modulo3.md) ja existirem. Datas/horas nao estao registadas com precisao por pesquisa - a sessao BMW foi a primeira de cada distrito, em 01/07/2026, antes das restantes 4 marcas.]

**Sessao**
- Data: 01/07/2026 (mesma sessao das outras marcas, BMW pesquisada em primeiro lugar em cada distrito)
- Hora de inicio: nao especificada com precisao nas imagens

| Distrito | MatosCar organico | MatosCar maps | Anuncio pago | Concorrente principal |
|----------|:-----------------:|:-------------:|:------------:|----------------------|
| Castelo Branco | Sim (pos 1) | Knowledge Panel proprio | Nao | nenhum (Standvirtual so com scroll) |
| Evora | Sim (pos 1) | Local Pack completo (3 entradas MatosCar) | Nao | nenhum |
| Beja | Sim (pos 1) | Knowledge Panel de grupo (nao especifico BMW) | Nao | nenhum |
| Portalegre | Sim (pos 1) | Local Pack (2 entradas MatosCar + 1 concorrente intercalado) | Nao | PRcar |
| Guarda | Sim (pos 1) | Knowledge Panel proprio | Nao | nenhum |
| Abrantes | Nao (ausencia total) | Knowledge Panel generico vazio, nao MatosCar | Nao | Cremilcar / Carpego Automoveis |
| Santarem | Nao (ausencia total) | Knowledge Panel do concorrente | Nao | Anibal Carvalho & Filhos, S.A. |

**Finding (uma frase):**
A BMW domina 5 dos 7 distritos (Castelo Branco, Evora, Beja, Portalegre, Guarda) com Knowledge Panel ou Local Pack proprio e sem concorrencia directa, mas tem ausencia total em Abrantes e Santarem, onde concessionarios oficiais bem estabelecidos (Cremilcar/Carpego Automoveis e Anibal Carvalho & Filhos desde 1989) dominam sem contestacao - o mesmo padrao geografico ja identificado nas outras marcas para esta zona nova.

---

## Modulo 3 - Pesquisa: BMW Castelo Branco
Query: BMW Castelo Branco
Distrito / cidade: Beira Interior / Castelo Branco
Data: 01/07/2026

— ANUNCIOS PAGOS —
Existe anuncio pago: nao (nao visivel em nenhum dos 3 screenshots)

— RESULTADOS ORGANICOS —
Nota estrutural: Knowledge Panel proprio e correcto - "BMW - A MatosCar", 3,7 estrelas (31 avaliacoes), "Concessionario BMW em Castelo Branco - Aberto". Endereco: Zona Industrial de Castelo, R. G 0 1 1, 6005-438 Castelo Branco.
Resultado 1: Facebook - A MatosCar BMW (@AMatosCarBMW) - "Concessionario BMW na Guarda, Castelo Branco e Evora" - Car dealership - tel +351 245 095 090
Resultado 2: A MatosCar - amatoscar.pt - "A MatosCar: Compra e Venda de Carros Novos e Usados em Portugal"
Resultado 3: Standvirtual - standvirtual.com - "BMW Castelo Branco - Carros" (visivel so com scroll)
MatosCar aparece nos top 3 organicos: sim (posicao 1, via Knowledge Panel + resultados subsequentes)

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack classico: nao (substituido por Knowledge Panel de entidade unica)
Existe Knowledge Panel de entidade: sim
MatosCar e a entidade do Knowledge Panel: sim

— CONCORRENTES IDENTIFICADOS —
Nenhum dealer concorrente directo. Standvirtual e agregador, visivel apenas com scroll.

Screenshot: castelo-branco-bmw-1.png, castelo-branco-bmw-2.png, castelo-branco-bmw-3.png
Observacao livre: primeira pesquisa do modulo (referencia para as restantes marcas). Ja revela aqui o padrao do perfil de Facebook multi-distrito (Guarda + Castelo Branco + Evora servidos pela mesma unidade), confirmado depois nas pesquisas de Evora e Guarda.

## Modulo 3 - Pesquisa: BMW Evora
Query: BMW Evora
Distrito / cidade: Alentejo Central / Evora
Data: 01/07/2026

— ANUNCIOS PAGOS —
Existe anuncio pago: nao

— RESULTADOS ORGANICOS —
Resultado 1: BMW A MatosCar - amatoscar.pt (Home) - "Guer trate de um pequeno passeio ou de uma viagem mais longa..."
Resultado 2: BMW Premium Selection - bmwpremiumselection.pt - "A Matoscar - Veiculos usados" - listagem com STOCK REAL: BMW Serie 3 em Evora por 42.450 EUR | 48.267 km | A MatosCar Evora - unico caso em todo o modulo BMW com uma unidade concreta (preco e quilometragem) visivel directamente no SERP
Resultado 3: Facebook - A MatosCar BMW (@AMatosCarBMW) - "Concessionario BMW na Guarda, Castelo Branco e Evora" - 4,1 estrelas (5,4 mil seguidores) - tel +351 245 095 090
MatosCar aparece nos top 3 organicos: sim, posicao 1

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack classico: sim - 3 entradas, todas MatosCar:
  A. BMW - A MatosCar - R. da Barba Rala 1 A - Aberto
  B. Oficina BMW - A MatosCar - R. da Barba Rala 1a - Fecha em breve: 12:30
  C. BMW Motorrad Evora - A MatosCar - R. da Barba Rala 1a - Aberto ate 19:00
MatosCar aparece no Local Pack: sim, dominio total (3 de 3 posicoes)

— CONCORRENTES IDENTIFICADOS —
Nenhum concorrente directo identificado.

Screenshot: evora-bmw-1.png, evora-bmw-2.png, evora-bmw-3.png, evora-bmw-4.png
Observacao livre: unico distrito de todo o modulo BMW com stock real e concreto (unidade, preco, quilometragem) visivel directamente no SERP, via listagem BMW Premium Selection - achado forte, distinto dos restantes 6 distritos onde a visibilidade e institucional mas nao mostra inventario.

## Modulo 3 - Pesquisa: BMW Beja
Query: BMW Beja
Distrito / cidade: Baixo Alentejo / Beja
Data: 01/07/2026

— ANUNCIOS PAGOS —
Existe anuncio pago: nao

— RESULTADOS ORGANICOS —
Nota estrutural: Knowledge Panel e da entidade "Grupo A MatosCar" (generico, nao especificamente BMW) - 4,2 estrelas (25 avaliacoes), "Stand de automoveis em Beja - Fechado, abre as 16:30". Endereco: R. das Novas Tecnologias 4, 7800 Beja. Uma segunda entrada separada "BMW A MatosCar" surge com tel 933 729 493 e descricao de "Ponto de Servico Autorizado BMW".
Resultado 1: Standvirtual - standvirtual.com - "BMW Beja - Carros"
Resultado 2: OLX Portugal - olx.pt - "bmw - Comprar usados Carros Beja"
Resultado 3: Facebook - Nuno Ramos - A MatosCar BMW / BMW Motorrad | Beja
Resultado 4: BMW Portugal - bmw.pt - "BMW - Concessionarios BMW" (localizador oficial da marca)
Resultado 5: A MatosCar - amatoscar.pt
MatosCar aparece nos top 3 organicos: sim, posicao 1 (via Knowledge Panel de grupo)

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack classico: nao (substituido por Knowledge Panel)
Existe Knowledge Panel de entidade: sim (entidade de grupo, nao BMW especifica)
MatosCar e a entidade do Knowledge Panel: sim

— CONCORRENTES IDENTIFICADOS —
Nenhum dealer concorrente directo identificado. Standvirtual e OLX sao agregadores.

Screenshot: beja-bmw-1.png, beja-bmw-2.png, beja-bmw-3.png, beja-bmw-4.png
Observacao livre: unico dos 5 distritos "fortes" da BMW onde o Knowledge Panel dominante e do "Grupo A MatosCar" generico, nao de uma entidade BMW dedicada como em Castelo Branco, Evora ou Guarda - possivel sinal de perfil de Google Business menos especializado por marca neste distrito especifico.

## Modulo 3 - Pesquisa: BMW Portalegre
Query: BMW Portalegre
Distrito / cidade: Alto Alentejo / Portalegre
Data: 01/07/2026

— ANUNCIOS PAGOS —
Existe anuncio pago: nao

— RESULTADOS ORGANICOS —
Resultado 1: BMW A MatosCar - amatoscar.pt - "Sobre a Empresa" - "representante desde 2015 do BMW em Alentejo, o Grupo A MatosCar..."
Resultado 2: PRcar - "BMW Usados e Seminovos Premium - Portalegre" - "BMW usados e seminovos premium na PRcar Evora e Portalegre"
Resultado 3: Facebook - A MatosCar | Portalegre - mais de 24,1 mil seguidores, 4,0 estrelas (81 avaliacoes)
Resultado 4: BMW Portugal - bmw.pt - "Concessionarios BMW" (localizador oficial)
Resultado 5: Standvirtual - "BMW Portalegre - Carros"
Resultado 6: OLX Portugal - "BMW - Carros Portalegre" (2.950 EUR a 23.950 EUR)
MatosCar aparece nos top 3 organicos: sim, posicao 1

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack classico: sim - 3 entradas:
  A. A MatosCar - Comercio Auto... - Av. Francisco Fino 17 - Aberto, fecha 18:00
  B. PRcar - Automoveis Pedro Ru... - Zona Industrial, Av. Francisco Fino - Fechado (CONCORRENTE)
  C. Grupo A MatosCar - Av. Francisco Fino Industrial 35
MatosCar aparece no Local Pack: sim, mas com uma particularidade: as posicoes A e C sao AMBAS MatosCar (nomes ligeiramente diferentes - "A MatosCar - Comercio Auto" e "Grupo A MatosCar" -, mesma zona industrial), com o concorrente PRcar intercalado na posicao B entre as duas.

— CONCORRENTES IDENTIFICADOS —
1. PRcar - Automoveis Pedro Ru... - tambem presente em Evora (ver "BMW Usados e Seminovos Premium - Portalegre e Evora" no resultado organico 2)

Screenshot: portalegre-bmw-1.png, portalegre-bmw-2.png, portalegre-bmw-3.png, portalegre-bmw-4.png
Observacao livre: possivel duplicacao de perfil de Google Business Profile da MatosCar (2 entradas distintas no mesmo Local Pack, "A MatosCar - Comercio Auto" e "Grupo A MatosCar"), com o concorrente PRcar a aparecer fisicamente "no meio" das duas entradas MatosCar - vale a pena confirmar com o cliente se sao de facto 2 perfis GBP distintos por unificar, ou 2 negocios genuinamente distintos na mesma morada.

## Modulo 3 - Pesquisa: BMW Guarda
Query: BMW Guarda
Distrito / cidade: Beira Interior Norte / Guarda
Data: 01/07/2026

— ANUNCIOS PAGOS —
Existe anuncio pago: nao

— RESULTADOS ORGANICOS —
Nota estrutural: Knowledge Panel proprio - "BMW A MatosCar Guarda", 3,8 estrelas (117 avaliacoes), "Concessionario BMW na Guarda - Aberto, fecha as 19:00". Endereco: R. Vila de Mantiegas 1, 6300-617 Guarda. Tel 271 030 658.
Resultado 1: BMW Motorrad - bmw-motorrad.pt
Resultado 2: A MatosCar Guarda (Vehicle Sale) - tel 271 036 287
Resultado 3: Facebook - A MatosCar BMW (@AMatosCarBMW) - "Concessionario BMW na Guarda, Castelo Branco e Evora" - 4,1 estrelas (5,4 mil seguidores)
MatosCar aparece nos top 3 organicos: sim, posicao 1

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack classico: nao (substituido por Knowledge Panel de entidade unica)
Existe Knowledge Panel de entidade: sim
MatosCar e a entidade do Knowledge Panel: sim

— CONCORRENTES IDENTIFICADOS —
Nenhum concorrente directo identificado. Nota: "Usados BMW Santogal" aparece como pesquisa relacionada sugerida (grupo concessionario nacional), sem presenca directa nesta SERP.

Screenshot: guarda-bmw-1.png, guarda-bmw-2.png, guarda-bmw-3.png, guarda-bmw-4.png
Observacao livre: terceiro distrito consecutivo (apos Castelo Branco e Evora) coberto pela mesma entidade de Facebook multi-distrito - confirma que a mesma unidade de negocio serve os 3 distritos da Beira/Alentejo Central para BMW.

## Modulo 3 - Pesquisa: BMW Abrantes
Query: BMW Abrantes
Distrito / cidade: Santarem/Abrantes / Abrantes
Data: 01/07/2026

— ANUNCIOS PAGOS —
Existe anuncio pago: nao

— RESULTADOS ORGANICOS —
Nota estrutural: Knowledge Panel generico e vazio - "Bmw - Escritorio empresarial em Abrantes", sem classificacao, sem detalhe de negocio real, codigo postal 2200-383 Abrantes apenas.
Resultado 1: BMW Portugal - bmw.pt - "Concessionarios BMW" (localizador oficial)
Resultado 2: Cremilcar - cremilcar.pt - "Cremilcar Comercio de Viaturas Abril, Lda... empresa com sede em Abrantes"
Resultado 3: Standvirtual - "BMW Abrantes - Carros"
Resultado 4: Carpego Automoveis - carpego.pt - "Usados BMW | Carros Usados em Abrantes, Santarem" - Rua Vale do Roubam, 2200-205 Abrantes - tel 241332278 / 969589053
Resultado adicional (nao comercial): Medio Tejo - mediotejo.net - "Kartodromo de Abrantes recebe 'Trackday' dos classicos BMW" - artigo editorial local, sem relacao com concessionarios
MatosCar aparece nos primeiros organicos: nao - ausencia total
Aparece noutro ponto visivel sem scroll: nao

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack classico: nao (Knowledge Panel generico e vazio ocupa esse espaco)
MatosCar aparece: nao

— CONCORRENTES IDENTIFICADOS —
1. Cremilcar - Comercio de Viaturas Abril, Lda
2. Carpego Automoveis (carpego.pt) - usados BMW, endereco e telefone confirmados

Screenshot: abrantes-bmw-1.png, abrantes-bmw-2.png, abrantes-bmw-3.png, abrantes-bmw-4.png
Observacao livre: sexto distrito onde a BMW e pesquisada, mas o primeiro com ausencia total da MatosCar - o Knowledge Panel nem sequer aponta para um concorrente com dados, e simplesmente uma entidade generica vazia. Cremilcar e Carpego Automoveis confirmam-se como concorrentes ja conhecidos de outras marcas neste mesmo distrito (ver Audi Abrantes).

## Modulo 3 - Pesquisa: BMW Santarem
Query: BMW Santarem
Distrito / cidade: Santarem/Abrantes / Santarem
Data: 01/07/2026

— ANUNCIOS PAGOS —
Existe anuncio pago: nao

— RESULTADOS ORGANICOS —
Nota estrutural: Knowledge Panel e do concorrente - "BMW - Anibal Carvalho & Filhos, S.A.", 4,8 estrelas (429 avaliacoes) - a classificacao mais alta de todo o modulo BMW. "Concessionario BMW em Varzea - Aberto, fecha as 19:00". Endereco: R. do Matadouro Regional 21, 2005-002 Varzea. Tel 243 351 971.
Resultado 1: BMW Portugal - bmw.pt - "Veiculos Usados em Santarem" (BMW Premium Selection)
Resultado 2: Facebook - BMW - Anibal Carvalho & Filhos, SA | Santarem - mais de 11,1 mil seguidores
Resultado 3: Standvirtual
Resultado 4: Instagram - anibalcarvalhofilhos_bmw - mais de 3,1 mil seguidores
MatosCar aparece nos primeiros organicos: nao - ausencia total
Aparece noutro ponto visivel sem scroll: nao

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack classico: nao (substituido por Knowledge Panel do concorrente)
MatosCar aparece: nao

— CONCORRENTES IDENTIFICADOS —
1. Anibal Carvalho & Filhos, S.A. - concessionario BMW oficial desde 1989 no distrito de Santarem, presenca digital muito forte (429 avaliacoes Google, 11,1 mil seguidores Facebook, 3,1 mil Instagram)

Screenshot: santarem-bmw-1.png, santarem-bmw-2.png, santarem-bmw-3.png, santarem-bmw-4.png
Observacao livre: setimo e ultimo distrito do modulo BMW - ausencia total da MatosCar, tal como em Abrantes, mas aqui o concorrente e qualitativamente mais forte que em qualquer outro distrito de todo o modulo (429 avaliacoes, o volume mais alto identificado em toda a pesquisa BMW): a Anibal Carvalho & Filhos e um concessionario oficial estabelecido desde 1989, nao um dealer generico multimarca.

---

## Finding final desta BMW (para o relatorio)

> A BMW é a marca mais procurada das cinco (líder absoluto no comparativo nacional), mas a sua procura concentra-se no nome da marca e dilui-se ao nível do modelo — com uma excepção notável e por explicar: a Série 1 é a 2ª mais procurada do país no distrito de Portalegre.

---

## Query: BMW
Data da pesquisa: 07/07/2026
Janela: Ultimos 12 meses | Geografia: Portugal

### Volume
Indice medio: 81.3
Pico: semana de 2026-03-22, indice 100
Vale: semana de 2026-07-05, indice 69
Tendencia: Estavel (delta -2.4)

### Consultas relacionadas - Top (ate 5)
- bmw portugal - 100
- bmw e46 - 86
- bmw serie 1 - 74
- mercedes - 73
- x1 bmw - 71

### Consultas relacionadas - Em ascensao (ate 5)
- bmw i3 2026 - +4 350%
- bmw ix3 2026 - +2 600%
- bmw ix3 preço - +900%
- novo bmw ix3 - +850%
- novo bmw i3 - +450%

### Topicos relacionados - Top (ate 5)
- BMW - 98
- BMW - 65
- BMW - 64
- BMW Série 1 - 5
- Motocicleta - 4

### Topicos relacionados - Em ascensao (ate 5)
SEM DADOS SUFICIENTES (ficheiro relatedEntities.csv sem dados na exportacao)

### Top 5 nacional (sub-regiao)
1. Viseu - 100
2. Braga - 99
3. Vila Real - 96
4. Porto - 92
5. Viana do Castelo - 92

### Distritos MatosCar (lista fixa de 6 - gerado programaticamente, Setubal excluido por definicao)
- Castelo Branco: posicao 14, indice 69
- Évora: posicao 19, indice 57
- Beja: posicao 16, indice 68
- Portalegre: posicao 12, indice 73
- Guarda: posicao 9, indice 85
- Santarém: posicao 7, indice 89

### Observacao livre [RASCUNHO - rever]
6 de 6 distritos MatosCar com dados suficientes nesta query (20/20 regioes do pais no total). Face a sessao de 06/07/2026: Castelo Branco corrige de posicao 14 (estava mal calculado antes, seria 15 nos dados de ontem) e continua na mesma posicao 14 hoje - mas atencao, os indices subjacentes mudaram (69 hoje vs 70 ontem), por isso trata-se de coincidencia de posicao, nao persistencia do erro. [Sara: acrescentar leitura/contexto de mercado.]

### Screenshot
bmw-00.png; bmw-01.png

---

## Query: BMW Serie 1
Data da pesquisa: 07/07/2026
Janela: Ultimos 12 meses | Geografia: Portugal

### Volume
Indice medio: 52.6
Pico: semana de 2026-05-17, indice 100
Vale: semana de 2026-04-26, indice 0
Tendencia: Decrescente (delta -24.7)

### Consultas relacionadas - Top (ate 5)
- bmw serie 1 - 100
- serie 1 - 98
- bmw série 1 preço - 67
- mercedes - 35
- bmw série 1 usado - 32

### Consultas relacionadas - Em ascensao (ate 5)
- mercedes classe a - +300%

### Topicos relacionados - Top (ate 5)
- BMW - 100
- BMW Série 1 - 99
- BMW - 89
- BMW - 89
- used - 6

### Topicos relacionados - Em ascensao (ate 5)
- BMW 3 Series (E46) - Aumento
- Capô - Aumento
- Embraiagem - Aumento
- BMW Serie 1 120 - Aumento
- BMW Serie 1 116 - Aumento

### Top 5 nacional (sub-regiao)
1. Vila Real - 100
2. Portalegre - 94
3. Braga - 72
4. Viseu - 68
5. Porto - 59

### Distritos MatosCar (lista fixa de 6 - gerado programaticamente, Setubal excluido por definicao)
- Castelo Branco: posicao 9, indice 46
- Évora: posicao 13, indice 40
- Beja: posicao SEM DADOS SUFICIENTES, indice -
- Portalegre: posicao 2, indice 94
- Guarda: posicao SEM DADOS SUFICIENTES, indice -
- Santarém: posicao 8, indice 47

### Observacao livre [RASCUNHO - rever]
4 de 6 distritos MatosCar com dados suficientes nesta query (17/20 regioes do pais no total). Portalegre continua no topo (2o lugar nacional, era 1o em 06/07 - variacao normal, consistente com a instabilidade ja documentada nesta query). [Sara: acrescentar leitura/contexto.]

### Screenshot
bmw-serie1-00.png; bmw-serie1-01.png

---

## Query: BMW eletrico
Data da pesquisa: 07/07/2026
Janela: Ultimos 12 meses | Geografia: Portugal

### Volume
Indice medio: 26.2
Pico: semana de 2026-03-22, indice 100
Vale: semana de 2025-07-06, indice 0
Tendencia: Crescente (delta +43.1)

### Consultas relacionadas - Top (ate 5)
- carro elétrico - 100
- bmw eletrico - 89
- bmw elétrico i3 - 71
- bmw i3 - 70
- mercedes - 55

### Consultas relacionadas - Em ascensao (ate 5)
- ix3 - +300%
- bmw ix3 - +300%
- bmw x2 - +100%
- bmw ix1 - +90%
- byd - +50%

### Topicos relacionados - Top (ate 5)
- BMW - 100
- BMW - 78
- BMW - 77
- Preço - 34
- Elétrico - 32

### Topicos relacionados - Em ascensao (ate 5)
- Porsche - Aumento
- BMW X1 - Aumento
- Veículo híbrido - Aumento
- Plug-in - Aumento
- Motor elétrico - Aumento

### Top 5 nacional (sub-regiao)
1. Braga - 100
2. Viseu - 95
3. Viana do Castelo - 91
4. Aveiro - 88
5. Porto - 71

### Distritos MatosCar (lista fixa de 6 - gerado programaticamente, Setubal excluido por definicao)
- Castelo Branco: posicao SEM DADOS SUFICIENTES, indice -
- Évora: posicao SEM DADOS SUFICIENTES, indice -
- Beja: posicao SEM DADOS SUFICIENTES, indice -
- Portalegre: posicao SEM DADOS SUFICIENTES, indice -
- Guarda: posicao SEM DADOS SUFICIENTES, indice -
- Santarém: posicao 7, indice 51

### Observacao livre [RASCUNHO - rever]
1 de 6 distritos MatosCar com dados suficientes nesta query (12/20 regioes do pais no total). Santarem continua a ser o unico distrito MatosCar com sinal, consistente com a sessao anterior. BYD volta a aparecer como consulta em ascensao (+50%). [Sara: acrescentar leitura/contexto.]

### Screenshot
bmw-eletrico-00.png; bmw-eletrico-01.png

---

## Query: BMW concessionario
Data da pesquisa: 07/07/2026
Janela: Ultimos 12 meses | Geografia: Portugal

### Volume
Indice medio: 1.9
Pico: semana de 2026-06-21, indice 100
Vale: semana de 2025-07-06, indice 0
Tendencia: Estavel (delta 7.7)

### Consultas relacionadas - Top (ate 5)
SEM DADOS SUFICIENTES (ficheiro relatedQueries.csv sem dados na exportacao)

### Consultas relacionadas - Em ascensao (ate 5)
SEM DADOS SUFICIENTES (ficheiro relatedQueries.csv sem dados na exportacao)

### Topicos relacionados - Top (ate 5)
- BMW - 100
- BMW - 99
- Concessionária de automóveis - 91
- BMW - 72

### Topicos relacionados - Em ascensao (ate 5)
SEM DADOS SUFICIENTES (ficheiro relatedEntities.csv sem dados na exportacao)

### Top 5 nacional (sub-regiao)
1. Lisboa - 100
2. Aveiro - 20

### Distritos MatosCar (lista fixa de 6 - gerado programaticamente, Setubal excluido por definicao)
- Castelo Branco: posicao SEM DADOS SUFICIENTES, indice -
- Évora: posicao SEM DADOS SUFICIENTES, indice -
- Beja: posicao SEM DADOS SUFICIENTES, indice -
- Portalegre: posicao SEM DADOS SUFICIENTES, indice -
- Guarda: posicao SEM DADOS SUFICIENTES, indice -
- Santarém: posicao SEM DADOS SUFICIENTES, indice -

### Observacao livre [RASCUNHO - rever]
0 de 6 distritos MatosCar com dados suficientes nesta query (2/20 regioes do pais no total). Confirma o padrao ja documentado: "[marca] concessionario" nao e termo de pesquisa usado pelos portugueses para encontrar pontos de venda. [Sara: acrescentar leitura/contexto.]

### Screenshot
bmw-concessionario-00.png; bmw-concessionario-01.png

---
