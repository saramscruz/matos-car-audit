# Módulo 3 — Protocolo de Visibilidade Competitiva
**amatoscar.pt · Junho 2026**

---

## Regras de observação — obrigatórias

1. **Browser:** Chrome, janela anónima (incógnito), cache limpa antes de cada sessão.
2. **Viewport:** 390px de largura durante toda a sessão. A maioria das pesquisas locais acontece em mobile.
3. **Localização:** não activar localização do browser. O objectivo é simular um utilizador que pesquisa com intenção geográfica explícita na query — não um utilizador localizado fisicamente no distrito.
4. **Sequência:** percorrer por distrito, não por marca. Faz as 5 marcas de Castelo Branco, depois as 5 de Évora, etc. Mantém o contexto geográfico consistente dentro de cada sessão.
5. **Tempo entre pesquisas:** mínimo 30 segundos entre pesquisas para evitar resultados influenciados por histórico de sessão.
6. **Data e hora:** registar no início de cada bloco por distrito. Não fazer dois distritos com mais de 48h de intervalo.
7. **Screenshots:** um screenshot por pesquisa. Capturar sempre os primeiros 3 resultados orgânicos + qualquer anúncio pago visível acima do fold. Guardar em `assets/[marca]/competitive/[distrito]-[marca].png`.
8. **Não clicar nos resultados.** Registar apenas o que é visível na SERP. Clicar altera o histórico da sessão e pode influenciar pesquisas subsequentes.

---

## Template de sessão — cabeçalho por bloco de distrito

```
Distrito: [nome]
Capital pesquisada: [cidade]
Data da observação: [dd/mm/aaaa]
Hora de início: [hh:mm]
Browser: Chrome incógnito
Viewport: 390px
Localização do browser: desactivada
```

---

## As 35 pesquisas

### Formato das queries

| Distrito | Capital | Query BMW | Query Audi | Query VW | Query BYD | Query Citroën |
|----------|---------|-----------|------------|----------|-----------|---------------|
| Beira Interior | Castelo Branco | `BMW Castelo Branco` | `Audi Castelo Branco` | `Volkswagen Castelo Branco` | `BYD Castelo Branco` | `Citroën Castelo Branco` |
| Alentejo Central | Évora | `BMW Évora` | `Audi Évora` | `Volkswagen Évora` | `BYD Évora` | `Citroën Évora` |
| Baixo Alentejo | Beja | `BMW Beja` | `Audi Beja` | `Volkswagen Beja` | `BYD Beja` | `Citroën Beja` |
| Alto Alentejo | Portalegre | `BMW Portalegre` | `Audi Portalegre` | `Volkswagen Portalegre` | `BYD Portalegre` | `Citroën Portalegre` |
| Beira Interior Norte | Guarda | `BMW Guarda` | `Audi Guarda` | `Volkswagen Guarda` | `BYD Guarda` | `Citroën Guarda` |
| Santarém / Abrantes | Abrantes | `BMW Abrantes` | `Audi Abrantes` | `Volkswagen Abrantes` | `BYD Abrantes` | `Citroën Abrantes` |
| Santarém / Abrantes | Santarém | `BMW Santarém` | `Audi Santarém` | `Volkswagen Santarém` | `BYD Santarém` | `Citroën Santarém` |

**Total:** 5 marcas × 5 distritos originais = 25 + 5 marcas × 2 queries Abrantes/Santarém = 10 → **35 pesquisas**

*Nota: o Abrantes/Santarém corre em duplo formato — cidade nova (Abrantes) e capital de distrito (Santarém) — para detectar se a presença digital já existe em algum dos dois formatos de pesquisa.*

---

## Template de registo — por pesquisa

```
Query: [texto exacto]
Distrito / cidade: 
Data: [dd/mm/aaaa] Hora: [hh:mm]

— ANÚNCIOS PAGOS —
Existe algum anúncio pago nos resultados: [s/n]
Se sim:
  Anunciante 1: [nome / domínio visível]
  Anunciante 2: [nome / domínio visível — se existir]
  A MatosCar tem anúncio pago: [s/n]

— RESULTADOS ORGÂNICOS —
Resultado 1: [título visível na SERP + domínio]
Resultado 2: [título visível na SERP + domínio]
Resultado 3: [título visível na SERP + domínio]

A MatosCar aparece nos primeiros 3 resultados orgânicos: [s/n]
Se sim, posição: [1 / 2 / 3]
Se não, aparece noutro ponto visível da SERP sem scroll: [s/n — descrever se sim]

— GOOGLE MAPS / LOCAL PACK —
Existe Local Pack (bloco de mapas) nos resultados: [s/n]
Se sim:
  A MatosCar aparece no Local Pack: [s/n]
  Se sim, posição no Local Pack: [1 / 2 / 3]
  Outros dealers no Local Pack (nome + cidade):
    1.
    2.

— CONCORRENTES IDENTIFICADOS —
Dealers concorrentes visíveis nesta SERP (orgânico + pago + maps):
  1. [nome + domínio]
  2. [nome + domínio]
  3. [nome + domínio]

Screenshot: [nome do ficheiro]

Observação livre (uma frase — só se houver algo inesperado):
```

---

## Tabela de síntese — preencher à medida que avança

Preencher uma linha por pesquisa. Permite ver padrões sem reler 35 registos individuais.

| Marca | Distrito | MatosCar orgânico | MatosCar maps | Anúncio pago presente | MatosCar tem anúncio | Concorrente principal |
|-------|----------|:-----------------:|:-------------:|:---------------------:|:--------------------:|----------------------|
| BMW | Castelo Branco | | | | | |
| BMW | Évora | | | | | |
| BMW | Beja | | | | | |
| BMW | Portalegre | | | | | |
| BMW | Guarda | | | | | |
| BMW | Abrantes | | | | | |
| BMW | Santarém | | | | | |
| Audi | Castelo Branco | | | | | |
| Audi | Évora | | | | | |
| Audi | Beja | | | | | |
| Audi | Portalegre | | | | | |
| Audi | Guarda | | | | | |
| Audi | Abrantes | | | | | |
| Audi | Santarém | | | | | |
| Volkswagen | Castelo Branco | | | | | |
| Volkswagen | Évora | | | | | |
| Volkswagen | Beja | | | | | |
| Volkswagen | Portalegre | | | | | |
| Volkswagen | Guarda | | | | | |
| Volkswagen | Abrantes | | | | | |
| Volkswagen | Santarém | | | | | |
| BYD | Castelo Branco | | | | | |
| BYD | Évora | | | | | |
| BYD | Beja | | | | | |
| BYD | Portalegre | | | | | |
| BYD | Guarda | | | | | |
| BYD | Abrantes | | | | | |
| BYD | Santarém | | | | | |
| Citroën | Castelo Branco | | | | | |
| Citroën | Évora | | | | | |
| Citroën | Beja | | | | | |
| Citroën | Portalegre | | | | | |
| Citroën | Guarda | | | | | |
| Citroën | Abrantes | | | | | |
| Citroën | Santarém | | | | | |

**Legenda:** ✓ = presente · ✗ = ausente · ? = inconclusivo

---

## Template de síntese por marca

Preencher no final das 7 pesquisas de cada marca.

```
Marca:

Visibilidade orgânica:
  Distritos onde MatosCar aparece nos top 3: [listar]
  Distritos onde MatosCar está ausente: [listar]

Visibilidade no Local Pack (Google Maps):
  Distritos com Local Pack presente: [listar]
  Distritos onde MatosCar aparece no Local Pack: [listar]
  Distritos com Local Pack mas MatosCar ausente: [listar]

Presença paga:
  Existem anúncios pagos nestas SERPs: [s/n]
  Quem anuncia (se aplicável): [listar]
  MatosCar tem anúncios pagos: [s/n]

Concorrentes recorrentes identificados:
  1.
  2.

Abrantes/Santarém — nota específica:
  MatosCar aparece em "Abrantes": [s/n]
  MatosCar aparece em "Santarém": [s/n]
  Observação sobre presença digital da nova abertura:

Finding desta marca em uma frase:
```

---

## Template de síntese transversal

Preencher no final de todas as 35 pesquisas. Este é o input directo para a página 9 do relatório.

```
DATA DE CONCLUSÃO DO MÓDULO 3: [dd/mm/aaaa]

VISIBILIDADE GERAL MATOSCAR:
Número de SERPs onde MatosCar aparece (orgânico): [X] de 35
Número de SERPs onde MatosCar aparece (maps): [X] de 35
Número de SERPs onde MatosCar tem anúncio pago: [X] de 35

MARCA COM MELHOR VISIBILIDADE: 
MARCA COM PIOR VISIBILIDADE: 

DISTRITO COM MELHOR COBERTURA MATOSCAR: 
DISTRITO COM PIOR COBERTURA MATOSCAR: 

CONCORRENTES MAIS FREQUENTES (top 3):
  1. [nome] — presente em [X] SERPs
  2. [nome] — presente em [X] SERPs
  3. [nome] — presente em [X] SERPs

ABRANTES/SANTARÉM — DIAGNÓSTICO:
  MatosCar visível em pesquisas "Abrantes": [X] de 5 marcas
  MatosCar visível em pesquisas "Santarém": [X] de 5 marcas
  Conclusão (uma frase):

FINDING TRANSVERSAL (uma frase — vai para página 9 do relatório):
```

---

## O que este módulo não avalia

- **Posições além do fold inicial.** Só se regista o que é visível sem scroll. Resultados na posição 4+ existem mas não são o comportamento típico do utilizador mobile.
- **Qualidade das páginas de destino dos concorrentes.** Ver quem aparece não é avaliar se são melhores ou piores — isso é outro engagement.
- **Histórico de visibilidade.** Uma pesquisa num dia é um snapshot, não uma tendência. Se houver variações inesperadas, podem reflectir flutuação normal das SERPs.
- **Resultados de pesquisa de imagem, vídeo ou notícias.** Foco exclusivo em resultados web + Local Pack.
- **Paid search da MatosCar.** Sem acesso à conta Google Ads, não é possível saber se existem campanhas activas mas com targeting geográfico diferente do testado.

Se durante as pesquisas aparecer algo inesperado — uma marca nova, um agregador de leads, um concorrente de fora da área — registar em observação livre. Pode ser relevante para a secção de próximos passos.

---

## Limitações a declarar no relatório

- **As 35 pesquisas foram feitas numa única sessão, por um único investigador, num único browser/IP, sem repetição.** Não há verificação cruzada por segunda pessoa, dispositivo ou dia diferente. Os resultados reflectem o estado da SERP nesse momento específico, não uma média estável ao longo do tempo.
- **A regra 3 (não activar localização do browser) não elimina a geolocalização por IP.** Confirmado empiricamente na pesquisa BYD Abrantes: a AI Overview referiu "carros da BYD perto de Fundão" — a localização real do investigador, não a cidade pesquisada — mesmo em janela anónima e sem nenhuma permissão de site activa. O pressuposto original do protocolo (query com intenção geográfica explícita = simulação válida de utilizador nesse distrito) não se confirma nos casos em que o Google usa geolocalização por IP em vez de, ou além de, interpretar a query. Sem VPN/proxy não há correcção viável dentro deste protocolo.
- **O Google personaliza e actualiza resultados de pesquisa de forma dinâmica.** O mesmo termo pode devolver SERPs diferentes por hora do dia, dia da semana, histórico da conta, ou simplesmente variação normal do algoritmo — não testado neste módulo.
- **Padrões descritos como "sem excepção" ou "consistente em todos os distritos" referem-se sempre ao que foi observado dentro desta amostra e desta sessão** — não devem ser lidos como uma garantia de que o mesmo resultado se replica noutro dia, dispositivo ou investigador.
