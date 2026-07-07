# Módulo 2 — Protocolo de Observação do Funil Digital
**amatoscar.pt · Junho 2026**

---

## Regras de observação — obrigatórias

1. **Browser:** Chrome, janela anónima (incógnito), cache limpa antes de cada sessão de marca.
2. **Viewport:** 390px de largura (simula iPhone 14). Todas as observações mobile-first. Repetir em desktop (1280px) apenas nos checkpoints 3 e 4 onde a diferença for relevante.
3. **Sequência fixa:** percorrer os 10 checkpoints pela mesma ordem para todas as marcas. Não saltar checkpoints mesmo que a resposta seja óbvia — o padrão de ausências é um finding em si.
4. **Data e hora:** registar no início de cada sessão por marca. Não fazer duas marcas com mais de 24h de intervalo se possível — o site pode mudar.
5. **Screenshots:** um screenshot por checkpoint com observação relevante. Guardar em `assets/[marca]/funnel/cp[número]-[descricao-curta].png`. Não é necessário capturar checkpoints sem nada a mostrar — só quando há algo a documentar (positivo ou negativo).
6. **Linguagem do registo:** português, directo, sem adjectivos. Descrever o que se vê, não o que se acha.

---

## Template de sessão — cabeçalho

```
Marca: [BMW / Audi / Volkswagen / BYD / Citroën]
Data da observação: [dd/mm/aaaa]
Hora de início: [hh:mm]
Browser: Chrome incógnito
Viewport inicial: 390px
URL de entrada: https://www.amatoscar.pt/
```

---

## Os 10 checkpoints

---

### CP1 — Findability a partir da homepage

**O que observar:** a partir de https://www.amatoscar.pt/, consegue-se chegar a conteúdo desta marca em 2 cliques ou menos, sem usar pesquisa interna?

**Como testar:**
- Abrir homepage
- Não usar a barra de pesquisa
- Tentar chegar à marca via navegação (menu, banners, filtros)
- Contar cliques

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Marca acessível em 1 clique (ex: menu directo) | Bom |
| Marca acessível em 2 cliques (ex: menu > submenu) | Aceitável |
| Mais de 2 cliques ou caminho não óbvio | Problema |
| Marca não encontrável sem pesquisa interna | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Caminho percorrido: [ex: menu "Novos" > filtro marca "BMW"]
Número de cliques: 
Screenshot: [s/n — se sim, nome do ficheiro]
Observação:
```

---

### CP2 — Página de modelo ou listing de stock

**O que observar:** existe uma página dedicada a esta marca com modelos listados ou stock disponível?

**Como testar:**
- A partir da página de marca, verificar se existe lista de modelos ou veículos disponíveis
- Verificar se o stock é real (tem VINs, matrícula, ou "disponível em [local]") ou genérico (apenas fichas técnicas do fabricante)

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Stock real listado com unidades concretas | Bom |
| Modelos listados mas sem stock concreto | Aceitável |
| Apenas redirecção para site do fabricante | Problema |
| Sem página de marca ou modelo | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
URL da página de marca/modelo encontrada:
Stock real visível: [s/n]
Número aproximado de unidades listadas (se aplicável):
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP3 — Preço visível no listing

**O que observar:** o preço aparece no listing sem necessidade de clicar num veículo específico ou preencher formulário?

**Como testar:**
- Abrir a lista de stock ou modelos desta marca
- Verificar se o preço aparece no card/linha de cada veículo
- Verificar tanto em mobile (390px) como desktop (1280px)
- Se o preço aparece só com condição (ex: "a partir de X com retoma"), registar isso

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Preço visível no listing sem clique adicional | Bom |
| Preço visível mas só dentro do detalhe do veículo | Aceitável |
| Preço condicionado (ex: "peça proposta") | Problema |
| Sem preço em nenhum ponto do funil | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Preço visível no card de listing: [s/n]
Preço visível no detalhe do veículo: [s/n]
Formato do preço (ex: "a partir de X€", "PVP X€", "peça proposta"):
Diferença mobile vs desktop: [s/n — se sim, descrever]
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP4 — CTA "Reservar" ou equivalente

**O que observar:** existe um call-to-action claro para avançar para compra ou reserva — e é visível sem scroll?

**Como testar:**
- No listing e no detalhe de um veículo desta marca, verificar se existe botão ou link com linguagem de acção (Reservar, Pedir proposta, Marcar test drive, Contactar, etc.)
- Verificar se é visível above the fold a 390px (sem scroll)
- Se existir mais do que um CTA, listar todos

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| CTA claro, acima do fold, linguagem de acção directa | Bom |
| CTA existe mas abaixo do fold ou linguagem passiva | Aceitável |
| CTA só na página de detalhe, não no listing | Problema |
| Sem CTA identificável | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Texto exacto do CTA:
Localização (listing / detalhe / ambos):
Visível above the fold a 390px: [s/n]
CTAs adicionais encontrados (texto exacto):
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP5 — O que acontece ao clicar o CTA

**O que observar:** o clique no CTA principal leva a um passo concreto de avanço no funil — ou é um beco sem saída?

**Como testar:**
- Clicar no CTA identificado no CP4
- Registar o que acontece: formulário, página de obrigado, chamada telefónica, WhatsApp, redirecção externa, etc.
- Se for formulário, avançar para CP6
- Se for redirecção para site do fabricante, registar como saída do funil

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Formulário interno com campos relevantes | Bom |
| WhatsApp ou chamada directa | Aceitável |
| Redirecção para site do fabricante | Problema |
| Erro, página em branco, ou sem resposta | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
O que acontece ao clicar:
URL de destino (se redirecção):
Sai do domínio amatoscar.pt: [s/n]
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP6 — Formulário de contacto

**O que observar:** existe um formulário funcional — e pede a informação certa sem pedir demasiado?

**Como testar:**
- Identificar o formulário associado a esta marca (pode ser genérico do site ou específico da marca)
- Listar todos os campos obrigatórios e opcionais
- Contar o número total de campos
- Verificar se o formulário tem campo de mensagem livre ou é fechado

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| 3-5 campos, inclui nome + contacto + mensagem livre | Bom |
| Formulário funcional mas campos excessivos (>8) ou desnecessários | Aceitável |
| Formulário genérico sem referência à marca ou modelo | Problema |
| Sem formulário | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Campos obrigatórios (listar):
Campos opcionais (listar):
Total de campos:
Tem campo de mensagem livre: [s/n]
É específico desta marca ou genérico:
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP7 — Mobile-friendly a 390px

**O que observar:** a experiência em mobile é utilizável — ou tem elementos partidos, texto ilegível, ou CTAs inacessíveis?

**Como testar:**
- Manter viewport a 390px
- Verificar: texto legível sem zoom, imagens não cortadas, botões clicáveis (mínimo 44px de altura), sem scroll horizontal
- Testar especificamente a página de listing e o formulário desta marca

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Experiência fluida, sem elementos partidos, CTAs acessíveis | Bom |
| Funcional mas com fricção menor (ex: texto pequeno, padding insuficiente) | Aceitável |
| Elementos partidos ou CTAs difíceis de clicar | Problema |
| Página inutilizável em mobile | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Texto legível: [s/n]
Sem scroll horizontal: [s/n]
CTAs clicáveis (mínimo 44px): [s/n]
Problemas específicos encontrados:
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP8 — Live chat ou callback

**O que observar:** existe uma forma de contacto síncrono ou quasi-síncrono — chat, WhatsApp, callback agendado?

**Como testar:**
- Verificar se existe widget de chat na página (canto inferior, geralmente)
- Verificar se existe link para WhatsApp
- Verificar se existe opção de callback ou "ligue-me"
- Registar se está activo ou apenas visível (ex: chat que diz "fora do horário")

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Chat activo ou WhatsApp com resposta esperada rápida | Bom |
| Chat visível mas fora de horário / sem indicação de tempo de resposta | Aceitável |
| Apenas número de telefone genérico | Problema |
| Sem opção de contacto síncrono | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Tipo de contacto síncrono encontrado (chat / WhatsApp / callback / nenhum):
Estado (activo / fora de horário / sem indicação):
Número de telefone visível: [s/n — se sim, qual]
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP9 — Campanhas activas para esta marca

**O que observar:** existe conteúdo de campanha visível e datado para esta marca — ou o site está parado?

**Como testar:**
- Verificar a secção "Campanhas" do site filtrada por esta marca
- Verificar se a homepage tem banner ou destaque para esta marca
- Verificar se as campanhas têm data de validade visível e estão dentro do prazo
- Registar se as campanhas encontradas têm CTA ou apenas são informativas

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Campanha activa, datada, com CTA, específica desta marca | Bom |
| Campanha genérica ou sem data clara | Aceitável |
| Campanha expirada ainda visível | Problema |
| Sem campanhas para esta marca | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Campanha encontrada: [s/n — se sim, título/descrição]
Data de validade visível: [s/n — se sim, qual]
Campanha dentro do prazo: [s/n]
Tem CTA: [s/n]
URL da campanha:
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

### CP10 — Conteúdo EV específico para esta marca

**O que observar:** existe conteúdo dedicado à versão eléctrica ou híbrida desta marca — ou o EV está invisível no funil?

**Como testar:**
- Procurar activamente por conteúdo EV para esta marca (modelo eléctrico, página de EV, campanha EV, filtro "eléctrico" no stock)
- Verificar se o modelo EV aparece no listing de stock
- Verificar se existe informação sobre incentivos, carregamento, ou autonomia

**Aplicável a:**
- BMW: i4, iX, iX1, iX2
- Audi: Q6 e-tron, A6 e-tron, e-tron GT
- Volkswagen: ID.3, ID.4, ID.5, ID.7
- BYD: toda a gama (marca 100% eléctrica/híbrida)
- Citroën: ë-C3, ë-C4

**Critérios:**

| Resultado | Classificação |
|-----------|--------------|
| Página ou secção dedicada ao EV desta marca, com stock e informação de produto | Bom |
| Modelo EV aparece no listing geral mas sem destaque ou conteúdo específico | Aceitável |
| EV só mencionado em campanhas, sem página de produto | Problema |
| Sem qualquer referência EV para esta marca | Falha |

**Registar:**
```
Resultado: [Bom / Aceitável / Problema / Falha]
Modelos EV encontrados no site:
Existe página/secção dedicada ao EV desta marca: [s/n]
Stock EV disponível no listing: [s/n — se sim, quantas unidades]
Informação sobre incentivos/carregamento/autonomia: [s/n]
URL de conteúdo EV (se existir):
Screenshot: [s/n — nome do ficheiro]
Observação:
```

---

## Template de síntese por marca

Preencher no final da sessão de cada marca.

```
Marca:
Data da observação:

Scorecard:
CP1 Findability:          [Bom / Aceitável / Problema / Falha]
CP2 Listing/stock:        [Bom / Aceitável / Problema / Falha]
CP3 Preço visível:        [Bom / Aceitável / Problema / Falha]
CP4 CTA:                  [Bom / Aceitável / Problema / Falha]
CP5 Pós-clique:           [Bom / Aceitável / Problema / Falha]
CP6 Formulário:           [Bom / Aceitável / Problema / Falha]
CP7 Mobile:               [Bom / Aceitável / Problema / Falha]
CP8 Chat/callback:        [Bom / Aceitável / Problema / Falha]
CP9 Campanhas:            [Bom / Aceitável / Problema / Falha]
CP10 Conteúdo EV:         [Bom / Aceitável / Problema / Falha]

O que funciona (máximo 2 pontos):
-
-

O que está em falta (máximo 2 pontos):
-
-

Finding desta marca em uma frase:
```

---

## Limitações a declarar no relatório

- **As observações das 5 marcas foram feitas por um único investigador, num único browser/dispositivo, sem repetição.** Não há verificação cruzada por segunda pessoa, sessão ou data diferente.
- **O site pode mudar entre sessões de marcas diferentes.** A regra 4 (não mais de 24h entre marcas) reduz mas não elimina este risco — conteúdo, preços e destaques observados são um retrato pontual, não uma média estável.
- **Viewport mobile-first (390px) é a base de quase todas as observações**, com desktop testado apenas nos checkpoints 3 e 4 quando relevante — as restantes conclusões não foram verificadas em desktop.
- **"Bom/Aceitável/Problema/Falha" são juízos qualitativos de um único avaliador**, aplicados de forma consistente entre marcas mas sem critério quantitativo nem segunda opinião — outro avaliador podia classificar o mesmo ecrã de forma diferente.

## Nota sobre o que este módulo não avalia

- **Velocidade de carregamento:** fora de âmbito sem ferramentas de diagnóstico (PageSpeed, GTmetrix)
- **SEO on-page:** fora de âmbito sem acesso a Search Console
- **Taxas de conversão:** sem acesso a Google Analytics
- **Stock em tempo real:** o que está listado pode não reflectir disponibilidade actual
- **Conteúdo de campanhas pagas:** sem acesso à conta Google Ads

Se qualquer um destes pontos levantar questões óbvias durante a observação, registar em "Observação livre" — pode ser relevante para a secção de próximos passos do relatório.
