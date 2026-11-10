# Plano do Reel de lançamento da Arara (v1, 04/11/2026)

Só plano. Nada foi produzido, instalado, agendado ou publicado. Pedido do Rodrigo em 04/11: planejar o lançamento da Arara em vídeo (Reels), usando o projeto `latent-spaces/brag` como fundamento, adaptado ao perfil de comunicação dele e ao da Arara. Isso amplia o escopo do guia de estilo (que dizia "sem reels por enquanto"): registro aqui como decisão nova e atualizo o guia só depois da aprovação deste plano.

## 1. Estado verificado em 04/11/2026

| Item | Estado | Fonte |
| --- | --- | --- |
| Lançamento | 15/12/2026 (terça), go/no-go 28/11, recuo 12/01/2027 | `devfluent-app/docs/PLANO_LANCAMENTO_DEZEMBRO_2026.md`, guia de estilo |
| Preço nas peças | não divulgar enquanto não houver preço público (regra do pré-lançamento) | guia de estilo |
| Idiomas do app | 16 (inglês, espanhol, francês, alemão, italiano, holandês, sueco, polonês, russo, turco, árabe, hebraico, hindi, mandarim, japonês, coreano) | `packages/shared/src/content/languages.ts` |
| Níveis | A1 a C1, só como referência ao QECR, sem equivalência com prova | `apps/web/src/data/home.ts`, guia |
| O app em uso | conversa por voz com a tutora de IA, por profissão ou objetivo, com correção explicada (frase original, frase corrigida e o porquê) | `home.ts` (`convs`, `demo`) |
| Material real reaproveitável | demo da home refeita em HTML (5 conversas fictícias), áudios da tutora em `apps/web/public/audio`, `arara.svg` e `arara-celebrate.svg` | repositório do app |
| Mascote para vídeo | 12 expressões aprovadas (04/11), mas só como cenas raster de 540x965 e folhas de 1629x965. Os SVGs oficiais têm 1 e 2 poses | `arara_social/stories_base`, web `public` |
| Alcance atual do perfil | 3 seguidores, alcance de 4, 0 cliques no link (semana de 02/11) | `arara_social/metrics_log.md` |
| Ferramentas na máquina | Node 24, FFmpeg 8.0.1, Chromium (Playwright). Geração de música via OpenRouter (Lyria 3) está configurada | verificado hoje |
| Publicação de vídeo | `publish.py` só publica imagem e carrossel. Reel exige `media_type=REELS` | `arara_social/publish.py` |

Consequência do último ponto de alcance: com 3 seguidores, o Reel é o primeiro formato capaz de chegar a quem ainda não segue a Arara (Reels são distribuídos para não seguidores). Por isso o gancho de 2 segundos vale mais aqui do que em qualquer post de feed.

## 2. O que aproveitamos do brag (e o que trocamos)

O brag é uma skill de agente que lê o projeto, planeja um vídeo de 15 a 25 s e entrega um MP4 pelo Hyperframes (HTML para vídeo, licença Apache-2.0). O valor dele para nós é o método, não o estilo "brag".

| Fundamento do brag | Como entra na Arara |
| --- | --- |
| Fluxo em 4 etapas com portões: inspecionar, planejar, compor, entregar | Mesmo fluxo, com aprovação nossa entre planejar e compor (guia: copy, visual, peça final e publicação são OKs separados) |
| O plano manda no roteiro, a ferramenta manda na mecânica | Plano e brief em `.md`; quem renderiza decide só animação e timing |
| Curto: 15 a 25 s | 24 a 28 s na versão principal; cortes de 10 a 12 s para story |
| Hook em 2 s decide tudo | Hook planejado primeiro (seção 4) |
| Mostre a coisa de verdade, reaproveitando componentes reais | A conversa real da demo do app, não uma explicação do app |
| Sem linguagem genérica de SaaS | Mesma regra do CLAUDE.md (sem "leve ao próximo nível", sem adjetivo vago) |
| Tempo de leitura: 0,8 s por rótulo, 0,3 s por palavra, mínimo 1,2 s por frase | Adotado como piso. Reels são muito vistos sem som, então a legenda na tela carrega a mensagem |
| Revelação em sequência e interação simulada (digitar, tocar) | Idiomas aparecendo um a um, correção surgindo na conversa |
| Música como cama, SFX esparsos, 1 a 3 batidas fortes travadas, reação sutil ao áudio | Igual, com música e SFX de licença limpa (seção 6) |
| `check` antes de renderizar, poster no quadro 0, texto de compartilhamento pronto | Igual, e o texto de compartilhamento vira a legenda do Reel |
| Nunca levar segredo ou dado pessoal para o vídeo | Só conversas fictícias, como já é a demo do app |
| Presets de tom | Criamos o preset **arara** (abaixo) |
| Áudio padrão com música CC BY (exige crédito) | Não usar: preferimos trilha própria para não depender de crédito |
| Narração desligada por padrão | Mantido desligado na v1 |

### Preset de tom "arara" (a combinação dos dois perfis de comunicação)

Da Arara: informal, jovem e acolhedora, humor leve, fala com "você", vocabulário da marca (bando, poleiro, pio, soltar o bico, voar, pousar certinho), nunca "bater asas", nunca humilhar quem erra, sem travessão e sem dois-pontos na arte.

Do Rodrigo (como ele decide e se comunica): direto, sem hype, exato. Prova em vez de prometer, então a peça mostra a correção acontecendo em vez de afirmar que "funciona". Nenhum número, resultado ou depoimento inventado. Afirmação de produto só se estiver no app.

Regra do humor (a mistura que você pediu): a seriedade vem do produto (a correção real), o humor vem da dor do aprendiz ("deu branco") e da expressão da Arara. Nunca o contrário.

## 3. Conceitos (escolher um)

**A. "O branco" (recomendado).** Parte da dor mais relatável, mostra o app resolvendo e fecha com a Arara. É o conceito do carrossel que mais engajou (30/10, "Deu branco...").

**B. "16 idiomas, 16 cores".** Vitrine do sistema de cores por idioma. Visualmente forte, mas diz pouco sobre o que o app faz. Entra como trecho do A, não como vídeo inteiro.

**C. "Conversa de verdade".** Só a demo do app. Mais claro para quem já decidiu, mais fraco como gancho para quem não conhece.

## 4. Roteiro do conceito A (vertical 1080x1920, 30 fps, 27 s)

Cada tela de texto respeita o tempo mínimo de leitura. Textos sem travessão e sem dois-pontos.

| # | Tempo | O que se vê | Texto na tela | Expressão da Arara | Áudio |
| --- | --- | --- | --- | --- | --- |
| 1 | 0,0 a 2,6 s | Reunião por vídeo, a Arara de sorriso forçado com a gota de suor | "Deu branco?" | sorriso forçado | silêncio e um toque seco no corte |
| 2 | 2,6 a 6,6 s | A Arara muda para acolhedora, fundo azul padrão | "Acontece com todo mundo. Aqui você treina falando." (9 palavras, 4 s) | professora | a música entra |
| 3 | 6,6 a 13,6 s | O app em uso: a tutora fala, a pessoa responde com um errinho, a correção aparece com o porquê e a missão ganha o visto (cena real da demo, em inglês B2) | "Você fala. A tutora responde e corrige na hora." (9 palavras, 7 s com a interação) | concentrada, depois torcendo no visto | áudio real da tutora, cliques de interface |
| 4 | 13,6 a 19,6 s | Seis idiomas aparecendo um a um, cada um com a sua cor e a mesma frase útil | "Bom dia em 16 idiomas." e cada idioma com o nome na tela (0,9 s cada) | dançando | uma batida por item, só nos acentos |
| 5 | 19,6 a 23,0 s | Trilha do A1 ao C1 e as profissões (hotelaria, enfermagem, vendas) | "Do trabalho à viagem, no seu nível." | determinada | cama musical |
| 6 | 23,0 a 27,0 s | A Arara torcendo, asas para cima, confete nas cores da marca | "Solte o bico. A Arara chegou." (versão de lançamento) ou "Solte o bico. Falta pouco." (versão teaser) | torcendo | resolução da música, um acento |

O fecho padrão ("Arara vai ser sua nova professora de idiomas. Entre no bando...") fica **só na legenda**, como manda o guia, nunca dentro da arte.

Duas versões do mesmo vídeo, trocando só a tela 6 e o CTA da legenda:
- **Teaser** (antes do lançamento): CTA é a lista de espera, pelo link da bio.
- **Lançamento** (15/12): CTA é baixar na loja. Só sai se Apple e Google estiverem de fato publicadas.

## 5. Direção de arte e motion

- Estilo de app, como nas artes do feed: cartões, balões com cauda, badges, botões de resposta. Títulos em Baloo 2, corpo em Nunito, palavra-chave em destaque na cor do idioma.
- Cores por idioma (aprovadas em 04/11) aparecem no vídeo na tela 4, e o azul padrão vale nas demais.
- Áreas seguras do Reels: texto dentro do miolo da tela, longe do topo e da base, onde ficam a interface do Instagram e a legenda. Medidas a conferir no próprio app antes da composição.
- Transições suaves e curtas (0,3 a 0,6 s), entrada rápida e permanência longa do texto. Pouso certinho da Arara no fim.
- **Gargalo de ativos**: as cenas atuais têm baixa resolução (540x965) e não dão para animar a mascote. Solução proposta: gerar as 12 expressões como **PNG transparente** em alta resolução, uma por chamada, com a mesma referência de mascote. Isso vira um kit reutilizável (vídeo, posts e stories) e permite trocar o fundo por idioma sem recolorir. Risco: consistência de uma imagem para outra; mitigado pelo teste de 3 poses antes de gerar as 12.
- A restrição "sem `translateY`" é da interface web da Arara. Para vídeo vou tratar como não aplicável, mas entradas por escala, opacidade e recorte já bastam para o estilo.

## 6. Áudio

- **Música**: trilha instrumental original gerada pelo modelo Lyria 3, via OpenRouter (já configurado), em torno de 100 a 110 BPM, alegre, sem vocal, 30 s. Gerar 2 opções para você escolher. **A conferir antes do uso comercial**: os termos de uso do OpenRouter e do Lyria para música usada em peça publicitária. Se houver dúvida, plano B é uma trilha de banco com licença comercial clara.
- **SFX**: pacote Kenney (CC0, não exige crédito), que o brag já usa. Poucos, ligados ao gesto (toque, entrada de cartão, visto de acerto).
- **Voz**: sem narração na v1. O som "falado" vem do áudio real da tutora na tela 3. Narração com voz humana ou sintética fica como decisão sua (D4).
- Batida: travar 1 a 3 momentos fortes na música (corte da tela 2, visto da tela 3, entrada da tela 6), como no brag. Reação sutil da luz ao áudio, sem barras de equalizador.

## 7. Ferramenta de montagem

| Opção | Vantagem | Ponto de atenção |
| --- | --- | --- |
| **Hyperframes** (a do brag) | Código aberto, Apache-2.0. HTML, CSS e GSAP viram MP4 de forma determinística. Nosso material já é HTML/React (a demo da home) e a Moost já usa GSAP | Ferramenta nova, precisa de um teste de renderização e velocidade |
| Remotion | React puro, muita documentação | Licença própria a conferir para uso comercial |
| Montagem própria (Playwright captura quadros, FFmpeg junta) | Total controle, sem dependência nova | Mais trabalho manual de sincronia e áudio |

Recomendação: **teste curto com o Hyperframes** (uma cena de 6 s com o componente real da demo, 1 SFX e a trilha), medindo qualidade, tempo de renderização e licença. Se falhar, cai na montagem própria. Não instalo nada antes do seu OK, e reviso o código da skill antes (CLAUDE.md: nada de comando remoto sem revisão).

Entrega técnica complementar: uma skill própria **`arara-reel`**, derivada do método do brag (4 etapas, leis de roteiro, preset arara, regras do guia, portão de aprovação). Fica no diretório de skills do workspace e só é criada com o seu OK.

## 8. Publicação (o que falta no código)

- `publish.py` precisa de um modo Reel (`media_type=REELS`, `video_url`, capa e `share_to_feed`), com o mesmo cuidado já aplicado: conferir se o post saiu antes de dar falha, nunca chamar `media_publish` duas vezes e rodar com `--dry-run` primeiro.
- O MP4 precisa de uma URL pública que o Instagram consiga baixar. O repositório de assets serve imagens bem; para vídeo, conferir o tipo de conteúdo e o limite de tamanho, e usar o S3 se o GitHub não servir. A conferir.
- Agendamento no horário padrão de 12h (Brasília). Reel conta como o post do dia ou entra além dele? Decisão sua (D7).

## 9. Fases e datas

| Fase | Quando | Entrega | Aprovação sua |
| --- | --- | --- | --- |
| 0. Decisões | 04 a 06/11 | Respostas de D1 a D8 | sim |
| 1. Teste técnico | 09 a 10/11 | Cena de 6 s no Hyperframes, 3 poses transparentes, 2 trilhas | sim (ferramenta e trilha) |
| 2. Kit e animatic | 11 a 18/11 | 12 expressões transparentes, vídeo-rascunho em quadros fixos com som, copy e legenda | sim (copy, depois visual) |
| 3. Composição | 19 a 27/11 | Versões teaser e lançamento, com e sem legenda, testadas em tela de celular | sim (peça final) |
| 4. Go/no-go | 28/11 | Decide se o teaser sai e quando | sim |
| 5. Publicação | teaser conforme D6, lançamento 15/12 às 12h | Reel no ar, medição | sim (autorização de publicar) |

Folga: a fase 3 termina um dia antes do go/no-go e deixa duas semanas de margem até 15/12 para ajustes ou para o recuo de data.

## 10. Linha de sucesso e medição

Sem números inventados: o perfil tem 3 seguidores, então a linha de base é praticamente zero. Proponho fixar a meta depois de 2 semanas de dados do teaser. Medir sempre: reprodução até 3 s (força do gancho), retenção até o fim, salvamentos, compartilhamentos, visitas ao perfil e cliques no link da bio com UTM do Reel (para atribuir cadastros na lista de espera). O relatório de segunda-feira já traz alcance, visitas e cliques; entra uma coluna para o Reel.

## 11. Conferência de fatos antes de publicar (checklist)

- 16 idiomas e A1 a C1: conferir no app e no site no dia da publicação.
- Nenhuma frase que prometa fluência, nota, certificado ou prazo. Níveis só como referência.
- Não citar concorrentes nem fornecedores de IA, inclusive no áudio da tutora.
- Frases em outros idiomas conferidas (regra do guia para es, fr, it, de, ja e gírias).
- Lançamento só com as duas lojas publicadas. Sem isso, usar a versão teaser.
- Nome de exibição "Arara . Aprenda novos idiomas com IA" idêntico em todas as redes.

## 12. O que não fazer

- Não copiar o tom de "brag" nem o humor de startup do projeto original.
- Não usar a trilha CC BY do brag (exige crédito e destoa da marca).
- Não colocar preço, promessa de resultado ou o fecho padrão dentro da arte.
- Não publicar nem agendar antes das três aprovações (copy, visual, peça final).
- Não instalar o brag, o Hyperframes ou qualquer pacote sem o seu OK e sem revisar o código.
- Não usar dado de usuário real, nem capturas com e-mail ou nome verdadeiros.
- Não depender de narração gerada com voz que cite provedor de IA.

## 13. Decisões do dono (para você responder)

- **D1 Conceito**: A (recomendado), B ou C?
- **D2 Perfil e voz**: o Reel sai só no @falearara, com a voz Arara + exatidão do Rodrigo descrita na seção 2? Ou também num perfil seu e da Moost, com você aparecendo?
- **D3 Duração**: 27 s (recomendado) ou mais curto?
- **D4 Narração**: sem voz (recomendado) ou com voz?
- **D5 Música**: trilha original gerada (recomendado, com checagem de licença) ou trilha de banco licenciada?
- **D6 Teaser**: sai antes de 15/12? Sugestão: 07/12, já que o go/no-go é 28/11.
- **D7 Agenda**: o Reel substitui o post do dia ou vai além dele?
- **D8 Ferramenta**: posso fazer o teste curto com o Hyperframes depois de revisar o código?

## 14. Fontes

- `github.com/latent-spaces/brag` (README, `skills/brag/SKILL.md`, `skills/brag-slim/SKILL.md`, `references/step-2-plan.md`, `step-3-compose.md`, `audio.md`), lidos em 04/11/2026.
- `github.com/heygen-com/hyperframes` (descrição e licença Apache-2.0).
- `devfluent-app`: `docs/PLANO_LANCAMENTO_DEZEMBRO_2026.md`, `packages/shared/src/content/languages.ts`, `apps/web/src/data/home.ts`.
- `arara_social`: `guia_de_estilo_arara.md`, `metrics_log.md`, `publish.py`, expressões e cenas aprovadas em 04/11/2026.
