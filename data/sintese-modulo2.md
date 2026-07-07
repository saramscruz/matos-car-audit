# Síntese Módulo 2 — Observação do Funil Digital
**amatoscar.pt · Junho 2026**

> **Nota metodológica (07/07/2026):** esta síntese resulta de uma única sessão de observação, por um único investigador, maioritariamente em viewport mobile (390px). Ver `methodology/funnel-observation-checklist.md`, secção "Limitações a declarar no relatório", para as limitações completas antes de usar estas conclusões no relatório final.

---

## CP1 — Findability a partir da homepage — síntese das 5 marcas

**Resultado oficial (scorecard):** Bom em todas as 5 marcas — acesso em 1 clique de selecção via carousel de marcas na homepage, para uma página dedicada em /gama/[marca]/.

**Consistência estrutural positiva:** todas as 5 marcas seguem a mesma arquitectura — URL própria /gama/[marca]/, preço "Desde X€" visível no listing sem clique adicional, segmentação por modelo em abas horizontais.

**Achado 1 — Fricção real de descoberta mascarada pelo critério oficial:**
O carousel de marcas na homepage é automático/rotativo, não fixo. BMW e Audi apareceram por coincidência de timing no momento da observação. BYD e Citroën estavam em posições mais avançadas (4ª e 5ª) mas visíveis sem interacção. A Volkswagen — "âncora do portfólio" segundo o PRD — exigiu 12 cliques na seta antes do clique de selecção (13 cliques no total). O critério oficial de "1 clique" não captura esta fricção. Recomendação candidata: fixar posição da VW no carousel ou substituir por menu de marcas sempre visível.

**Achado 2 — Desalinhamento entre modelos em destaque e modelos pesquisados (Módulo 1):**
- BMW: query Série 1 vs destaques i3 / i5 M60 / i5 Touring
- Audi: query A3 vs destaques RS5 Limousine / RS5 Avant / S6 Sportback e-tron
- Volkswagen: query T-Roc vs destaques Tayron / ID.7 Tourer / ID.5
- BYD: query Atto 3 vs destaques Seal 6 DM-i Touring / Seal 6 DM-i / Atto 3 Evo (parcial overlap)
- Citroën: query C3 vs destaques ë-C5 Aircross / ë-SpaceTourer / ë-Berlingo — único caso onde o desalinhamento de modelo coexiste com alinhamento de categoria (EV), consistente com a liderança geográfica EV da marca identificada no Módulo 1.

**Achado 3 — Inconsistência na lógica de destaque EV entre marcas:**
Citroën destaca só eléctricos puros (3/3). VW mistura 2 eléctricos + 1 combustão. BYD mistura híbridos DM-i com eléctrico sem distinção visual clara. BMW e Audi não destacam nenhum EV apesar de terem gama disponível (i3, i5, e-tron, etc.). Não há critério consistente de selecção de destaque entre as 5 páginas de marca. Relevante para CP10.


## CP2 — Página de modelo ou listing de stock — síntese das 5 marcas

**Resultado oficial (scorecard):** Aceitável em todas as 5 marcas — modelos listados com URL própria por veículo (/carros-[marca]/[marca]-[modelo]/), mas sem stock concreto (sem VIN, matrícula real, quilometragem ou cor específica) em nenhuma das 5. Confirma-se de forma transversal que a MatosCar não expõe stock real no funil digital — todo o conteúdo de modelo é ficha genérica de catálogo do fabricante/distribuidor.

**Padrão estrutural comum:** todas as 5 marcas seguem a mesma arquitectura de página — hero com imagem, preço "Desde X€", CTA "Quero experimentar" (abre modal de pedido de test-drive, componente reutilizado e idêntico em todas as marcas: Nome/Apelidos/Telefone/E-mail obrigatórios, Concelho opcional, reCAPTCHA), bloco de texto promocional genérico (conteúdo varia por modelo, fornecido pelo fabricante/distribuidor), secção "Motorizações" com link "Solicitar oferta" por variante, galeria de fotos, vídeo, e formulário inline "Pedir informação" no fundo da página (Nome/Apelidos/E-mail/Telefone/Concelho obrigatórios + Comentários opcional, sem reCAPTCHA). "Solicitar oferta" e "Pedir informação" convergem para o mesmo mecanismo de contacto.

**Achado 1 — Inconsistência de profundidade entre fichas de modelo:**
A secção "Motorizações" varia de ausente a muito detalhada, sem relação aparente com a marca em si:
- BMW (i3): secção ausente — só galeria e vídeo
- Audi (RS5 Limousine): 1 motorização listada
- Volkswagen (Tayron): 5 motorizações listadas
- BYD (Seal 6 DM-i Touring): 2 motorizações listadas
- Citroën (ë-C5 Aircross): 5 motorizações listadas
Isto sugere desigualdade na actualização ou disponibilidade de dados por ficha individual, não um padrão por marca — relevante como achado accionável: há fichas de modelo desactualizadas ou incompletas que prejudicam a informação disponível ao consumidor, independentemente da marca.

**Achado 2 — Confusão terminológica eléctrico/híbrido isolada à Audi:**
A Audi RS5 Limousine (híbrido PHEV) é descrita no texto promocional como tendo "autonomia totalmente eléctrica" sem qualificação clara de que é um sistema híbrido — risco real de confundir um consumidor a comparar opções EV genuínas. Em contraste, BYD e Citroën etiquetam consistentemente "Híbrido" e "Eléctrico" nas suas secções de Motorizações, sem ambiguidade. Este achado é específico da Audi e não se observa nas restantes 4 marcas.

**Achado 3 — Defeito de qualidade de conteúdo na Citroën:**
Os nomes das variantes na secção "Motorizações" da Citroën (ë-C5 Aircross) aparecem truncados ("Elétri 230cv...", "Elétr 230cv...", "Elé 230cv..."), indicando um provável limite de caracteres mal configurado no sistema que gera o catálogo. Defeito técnico isolado, não observado nas outras 4 marcas, mas fácil de corrigir e com impacto directo na credibilidade da informação apresentada.

**Achado 4 — Diferencial de garantia, exclusivo da BYD:**
Só a página da BYD apresenta secção de garantia explícita (8 anos/150.000 km garantia de fabricante, 8 anos/200.000 km garantia da bateria) antes do formulário de contacto — não observado em nenhuma das outras 4 marcas. Consistente com estratégia típica de marcas chinesas a construir confiança em mercados onde têm menor histórico.


## CP3 — Preço visível no listing — síntese das 5 marcas

Data da observação: 30/06/2026
Hora de início: 16:37

Resultado: Bom (todas as 5 marcas)
Preço visível no card de listing: sim (confirmado em desktop nas 5 marcas via CP1; confirmado em mobile 390px via amostra BYD)
Preço visível no detalhe do veículo: sim (confirmado em desktop nas 5 marcas via CP2)
Formato do preço: "Desde X€" — consistente em todas as marcas, sem condição (ex.: não há "peça proposta" ou equivalente)
Diferença mobile vs desktop: nenhuma diferença estrutural observada na amostra testada (BYD) — preço mantém-se visível, legível e sem necessidade de scroll horizontal
Nota metodológica: teste mobile (390px, DevTools modo responsivo) realizado apenas na BYD como amostra representativa, dado que os CP1 e CP2 confirmaram template técnico partilhado entre as 5 marcas (mesma estrutura /gama/[marca]/ e /carros-[marca]/[modelo]/). Resultado assumido válido para as restantes 4 marcas por extensão directa do padrão observado, não por observação individual marca a marca.
Excepção identificada: BMW i3 não apresenta preço "Desde X€" no listing — está classificado "A Consultar" (observado no CP1), o que quebra parcialmente a consistência "Bom" para este modelo específico, embora os outros 2 modelos em destaque da BMW (i5 M60, i5 Touring) tenham preço visível normal.
Screenshot: assets/byd/funnel/cp3-mobile-listing-390px.png, assets/byd/funnel/cp3-mobile-ficha-modelo-390px.png


## CP4 — CTA "Reservar" ou equivalente — síntese das 5 marcas

Resultado: Problema (todas as 5 marcas)
Texto exacto do CTA: "Quero experimentar" — presente em todas as 5 marcas, idêntico
Localização: visível acima do fold em todas as 5 marcas, junto ao título do modelo e ao preço, na página de detalhe individual de cada veículo
CTAs adicionais encontrados: link "Solicitar oferta" por variante na secção "Motorizações" (BMW: não aplicável, sem secção Motorizações; Audi: 1 ocorrência; VW: 5 ocorrências; BYD: 2 ocorrências; Citroën: 5 ocorrências) — todos apontam para o mesmo formulário "Pedir informação", não são CTAs distintos em função
Observação: nenhuma das 5 marcas usa linguagem de avanço directo para compra ("Reservar", "Comprar", "Encomendar"). O CTA principal é sempre "Quero experimentar", que é uma intenção de test-drive, não de compra — e os CTAs secundários ("Solicitar oferta") pedem orçamento, não reserva de unidade. Cai no critério "Problema" do protocolo: existe CTA visível e acima do fold, mas a linguagem é passiva/exploratória, não de avanço comercial directo.

## CP5 — O que acontece ao clicar o CTA — síntese das 5 marcas

Resultado: Bom (todas as 5 marcas)
O que acontece ao clicar: abre modal interno de pedido de test-drive (Nome, Apelidos, Telefone, E-mail obrigatórios, Concelho opcional, política de privacidade obrigatória, reCAPTCHA) — componente idêntico e reutilizado nas 5 marcas
URL de destino: não há redirecção — modal sobreposto à própria página
Sai do domínio amatoscar.pt: não, em nenhuma das 5 marcas
Observação: cumpre o critério "Bom" do protocolo (formulário interno com campos relevantes), apesar do CTA em si (CP4) não usar linguagem de avanço comercial. O percurso técnico é sólido — não há fuga para sites de terceiros nem erros — mas o destino funcional é sempre um pedido de contacto genérico, nunca uma reserva real de unidade.

## CP6 — Formulário de contacto — síntese das 5 marcas

Resultado: Bom (todas as 5 marcas, com nuance)
Existem 2 formulários distintos em cada página de modelo, ambos analisados:
(1) Modal "Quero fazer um test-drive": Nome, Apelidos, Telefone, E-mail obrigatórios (4), Concelho opcional (1) = 5 campos, sem campo de mensagem livre, reCAPTCHA presente
(2) Inline "Pedir informação": Nome, Apelidos, E-mail, Telefone, Concelho obrigatórios (5), Comentários opcional (1) = 6 campos, COM campo de mensagem livre, sem reCAPTCHA visível
Específico desta marca ou genérico: específico do modelo na página (URL e título da página identificam o modelo), mas o formulário em si não pede unidade, cor ou versão — é genérico dentro do contexto da página
Observação: ambos os formulários caem em "Bom" pela contagem de campos (3-5 e 5-6, dentro ou perto do intervalo ideal do protocolo). O formulário "Pedir informação" é ligeiramente mais completo (tem campo de mensagem livre, que o protocolo valoriza como critério de "Bom"). Nenhum dos dois formulários permite especificar a unidade de interesse além do modelo já identificado pela própria página — não há selecção de cor, ano ou versão dentro do formulário, mesmo quando a secção Motorizações lista várias variantes.


## CP7 — Mobile-friendly a 390px — síntese das 5 marcas

Data da observação: 30/06/2026
Hora de início: 17:14

Resultado: Aceitável (todas as 5 marcas, por extensão da amostra BYD)
Texto legível: sim, sem necessidade de zoom em nenhum dos elementos testados (listing, ficha de modelo, modal de test-drive, formulário inline)
Sem scroll horizontal: sim, confirmado em listing e formulários
CTAs clicáveis (mínimo 44px): sim, aparentam ter altura adequada nos elementos testados (CTA "Quero experimentar", campos de formulário)
Problemas específicos encontrados: sobreposição visual do widget flutuante "Quanto vale o meu carro?" (ícone de áudio/avaliação) sobre o topo do campo "E-mail" no formulário inline "Pedir informação", a 390px. Confirmado que não impede o preenchimento do campo (sem impacto funcional), mas é fricção visual menor — o utilizador pode hesitar ou precisar de mais atenção para clicar no sítio certo.
Nota metodológica: teste realizado apenas na amostra BYD, por extensão do template partilhado confirmado nos CP1-CP3. Assume-se comportamento equivalente nas restantes 4 marcas, incluindo a mesma sobreposição do widget flutuante (que é elemento global do site, não específico de marca).
Screenshot: assets/byd/funnel/cp7-modal-testdrive-390px.png, assets/byd/funnel/cp7-formulario-pedirinfo-390px.png
Observação: cai em "Aceitável" segundo o critério do protocolo ("funcional mas com fricção menor") devido à sobreposição do widget flutuante — não chega a "Bom" porque há um elemento de UI a interferir visualmente com um campo obrigatório do formulário, ainda que sem bloquear o preenchimento.


## CP8 — Live chat ou callback — síntese (observação transversal, não por marca)

Data da observação: 30/06/2026
Hora de início: 17:21

Resultado: Bom (chat) / Problema (contacto telefónico por instalação)
Tipo de contacto síncrono encontrado: chatbot de IA ("Seezar"), presente como widget flutuante em todas as páginas observadas (confirmado em homepage e /contactos/)
Estado: activo, com sugestões pré-formatadas ("Podem ajudar-me a escolher um automóvel?", "Onde é que estão localizados?", "Gostaria de marcar uma visita à vossa oficina"), disclaimer de uso de IA presente, link de política de privacidade incluído
Número de telefone visível: sim, um único número central "245 035 090", fixo no header em todas as páginas — mas NÃO há número de telefone directo por instalação/stand físico, mesmo na página /contactos/ que lista múltiplas localizações (ex.: Volvo A MatosCar Évora, Volvo A MatosCar Castelo Branco)
Redes sociais: links para Facebook, LinkedIn e Instagram presentes no rodapé de todas as páginas — não são canais síncronos de contacto, mas reforçam a presença digital do grupo fora do website
Screenshot: assets/_geral/cp8-chatbot-seezar.png, assets/_geral/cp8-pagina-contactos-formulario.png
Observação: o chatbot Seezar cumpre bem o critério "Bom" do protocolo — está activo, com tempo de resposta instantâneo implícito, e cobre casos de uso relevantes (escolha de automóvel, localização, marcação de visita à oficina). Contudo, a ausência de contacto telefónico directo por instalação é uma fricção real: um utilizador que já sabe a que stand físico se quer dirigir (por exemplo, depois de ver no mapa que há um Volvo A MatosCar em Évora) não tem forma de ligar directamente para esse local — só pode usar a linha central do grupo, o formulário genérico "Entre em contacto connosco" (Nome, Apelidos, Telefone, E-mail obrigatórios, Concelho obrigatório, Comentários opcional — sem campo de selecção de marca ou instalação específica), ou o chatbot. As redes sociais (Facebook, LinkedIn, Instagram) estão presentes mas não foram avaliadas quanto a actividade ou tempo de resposta — fora de âmbito deste checkpoint, mas relevante anotar a existência para referência futura. Nota adicional: o mapa de instalações em /contactos/ confirma presença física do grupo com a marca Volvo (Évora, Castelo Branco) — fora do âmbito das 5 marcas analisadas neste audit, mas relevante como contexto da estrutura mais ampla do grupo MatosCar.


## CP9 — Campanhas activas para esta marca — síntese das 5 marcas

Data da observação: 30/06/2026
Hora de início: 17:32

Resultado: Aceitável (geral) / Problema (Citroën especificamente)
Existe conteúdo de campanha visível e datado: sim, página /campanhas/ activa, com filtros funcionais (Ver Tudo / Após Venda / Vendas) e paginação (4 páginas, ~25 campanhas no total), maioria com data de validade explícita ("até DD/MM/AAAA")
Cobertura por marca (das 5 em âmbito):
- Volkswagen: cobertura forte, 7-8 campanhas distintas (vendas e após-venda)
- Audi: 2 campanhas
- BYD: 1 campanha (Atto 2 DM-i, desde 27.640€+IVA)
- BMW: 1 campanha (BMW Charging, soluções empresariais), sem data de validade visível — excepção à norma das restantes campanhas
- Citroën: 0 campanhas em qualquer uma das 4 páginas
Screenshot: assets/_geral/cp9-campanhas-pagina1.png, assets/_geral/cp9-campanhas-pagina2.png, assets/_geral/cp9-campanhas-pagina4-bmw.png
Observação: a funcionalidade de campanhas está claramente activa e bem mantida (datas presentes, conteúdo recente, cobre múltiplas marcas do grupo incluindo marcas fora do nosso âmbito como Nissan, Kia, Peugeot, Opel, Toyota, Skoda, Seat). Contudo, a distribuição por marca dentro do nosso âmbito de 5 é desigual: a Citroën, identificada no Módulo 1 como a marca com melhor hierarquia geográfica de procura entre as 5, não tem nenhuma campanha promocional visível — desalinhamento directo entre força de procura e investimento promocional. A BMW tem apenas 1 campanha, de produto B2B (carregamento para empresas), sem data de validade, o que destoa do padrão geral de campanhas datadas. Achado accionável forte para o relatório: a marca com maior procura orgânica (Citroën) é a que recebe menos atenção promocional activa no funil.


## Nota de correção — CP9, lista de screenshots

A lista de screenshots do CP9 fica corrigida para refletir as 4 páginas guardadas (não 3): assets/_geral/cp9-campanhas-pagina1.png, assets/_geral/cp9-campanhas-pagina2.png, assets/_geral/cp9-campanhas-pagina3.png, assets/_geral/cp9-campanhas-pagina4-bmw.png.


## CP10 — Conteúdo EV para esta marca — síntese das 5 marcas + ACHADO ESTRUTURAL MAIOR

Data da observação: 30/06/2026
Hora de início: 17:39

Resultado: Aceitável, com achado estrutural maior do que inicialmente identificado

Existe hub dedicado EV: SIM — /veiculos-eletricos/, acessível em 1 clique a partir da homepage. Tabela comparativa EV/HEV/PHEV clara (energia principal, autonomia eléctrica, carregamento, uso ideal) e FAQ educativo ("Qual a diferença entre um carro híbrido e um híbrido plug-in?", "Os carros eléctricos compensam?", "E se não tiver onde carregar?"). Os 3 modelos em destaque (Peugeot e-208, Kia PV5, Volvo EX30) são de marcas fora do âmbito das 5 analisadas.

ACHADO MAIOR (revisão directa do CP2/CP4/CP5): a MatosCar tem um mecanismo de e-commerce real e funcional — /reservar-carro/[modelo]/ — disponível em USADOS, com registo de conta, pagamento de sinal (300€, descontável do preço final), preço fixo (não "Desde"), unidade individualizada com matrícula real, quilometragem e ano. Confirmado directamente em 3 marcas distintas: Peugeot e-208 (26.950€, matrícula CH27AF), Mercedes Classe A (23.450€, 105.520km), Volkswagen Taigo (19.950€, 41.000km). O CTA nestas páginas é "Reservar" / "Quero reservar" — linguagem de avanço comercial directo, contrastando com o "Quero experimentar" das páginas de carros NOVOS por marca, classificado como Problema no CP4.

Implicação directa para a síntese do Módulo 2: a conclusão dos CP2, CP4 e CP5 ("sem stock real, sem CTA de reserva, formulário genérico") aplica-se especificamente às páginas de carros NOVOS das 5 marcas (/gama/[marca]/ e /carros-[marca]/[modelo]/), não ao site como um todo. A secção de USADOS (/carros-usados/) tem stock genuíno, preço fixo e fluxo de reserva completo, validado nas 5 marcas por extensão directa (confirmado em VW; presume-se extensível a BMW, Audi, BYD, Citroën dado o padrão técnico idêntico em 3 marcas diferentes do grupo).

Síntese por marca, EV especificamente:
- BMW: gama EV existe mas sem destaque dedicado em Novos; i3 sem preço visível; zero presença no hub EV central; não testado especificamente BMW eléctrico em Usados
- Audi: erro terminológico confirmado em Novos (RS5 PHEV descrito como "autonomia totalmente eléctrica"); zero presença no hub EV central
- Volkswagen: melhor cobertura de gama ID. em Novos; campanha activa "Família ID."; CONFIRMADO mecanismo de reserva real em Usados (Taigo); zero presença no hub EV central
- BYD: terminologia correcta em Novos, garantia de bateria bem comunicada; zero presença no hub EV central apesar de ser marca nativamente EV/híbrida
- Citroën: terminologia "ë-" clara em Novos; zero campanhas; zero presença no hub EV central apesar de ser a marca com melhor alinhamento procura/oferta EV segundo o Módulo 1

Screenshot: assets/_geral/cp10-hub-veiculos-eletricos-hero.png, assets/_geral/cp10-hub-tabela-comparativa-destaques.png, assets/_geral/cp10-reserva-peugeot-e208.png, assets/_geral/cp10-ficha-usado-peugeot-e208-matricula.png, assets/_geral/cp10-reserva-mercedes-classea.png, assets/_geral/cp10-reserva-vw-taigo.png

Observação final: a recomendação central do Módulo 2 não é "a MatosCar não tem capacidade de venda online" — tem, e está bem implementada em Usados. A recomendação correcta é dupla: primeiro, replicar o mecanismo de reserva real (já existente e funcional) às páginas de carros Novos das 5 marcas, que actualmente ficam presas em "Quero experimentar" sem avanço comercial directo; segundo, integrar as 5 marcas no hub /veiculos-eletricos/, que tem o melhor conteúdo educativo do site mas está desligado das marcas que esta auditoria analisa. Estas duas correcções aproveitam infraestrutura já validada e funcional, sem exigir desenvolvimento de raiz — são quick wins de alto impacto.

---

# MÓDULO 2 — ENCERRADO

10 checkpoints completos (CP1 a CP10), nas 5 marcas, 30/06/2026.


## Nota adicional pós-encerramento — Secção de Notícias e bloco de acções rápidas (homepage)

Data da observação: 30/06/2026
Hora de início: 17:52

Observação fora do âmbito dos 10 checkpoints formais, registada por relevância directa para o relatório.

**Secção "Notícias" na homepage**, com 3 artigos em destaque:
- "Novo Nissan Leaf, o pioneiro eléctrico com 622 km" (30/06/2026) — marca fora do âmbito
- "A MatosCar inaugurou o novo polo de Abrantes" (29/06/2026) — PRIMEIRA confirmação visual e datada da abertura de Abrantes referida no PRD, com fotografia do corte de fita. Relevante directamente para o Módulo 3 (cobertura Abrantes/Santarém).
- "BYD Dolphin G DM-i, o novo compacto do mercado europeu" (29/06/2026) — conteúdo editorial sobre BYD, descreve "autonomia de até 1.040 km" para um modelo PHEV ("Tecnologia Super Híbrida DM 5.0") sem distinguir claramente autonomia total vs autonomia eléctrica pura — variante mais subtil da mesma imprecisão terminológica identificada na Audi (CP2). Nenhuma notícia equivalente para BMW, Audi, VW ou Citroën nesta secção — reforça a assimetria de visibilidade editorial entre marcas já identificada no CP9 (campanhas).

**Bloco de acções rápidas, abaixo das notícias**: Contacte-nos, Marcação de Revisão, Onde estamos, Newsletter. A existência de subscrição de newsletter ("Receba novidades, campanhas e conteúdos exclusivos da A MatosCar") não foi testada quanto a funcionalidade, frequência de envio ou conteúdo — fica como ponto em aberto para um eventual follow-up engagement (Módulo de email marketing / CRM), não avaliável no âmbito deste audit de funil digital.

Screenshot: assets/_geral/cp-extra-noticias-homepage-abrantes-byd.png
