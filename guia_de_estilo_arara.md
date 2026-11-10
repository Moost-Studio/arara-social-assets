# Guia de estilo da Arara (@falearara), preferências do Rodrigo

Compilado em 31/10/2026 a partir de tudo que o Rodrigo pediu, corrigiu e aprovou. Ler antes de escrever qualquer copy, legenda ou arte. Onde está marcado (inferido), é leitura minha e não pedido explícito.

## 1. Língua e tom
- Português do Brasil, fácil de entender, acessível para qualquer público. Nada de jargão.
- Escrita informal, conectada ao público jovem. Amigável, acolhedora, com humor leve.
- Falar com a pessoa: "você" e imperativo ("solte o bico", "salva este post"). Infinitivo só quando soar natural ("Pedir a conta").
- Frase elegante PARA o usuário. Não misturar primeira e terceira pessoa na mesma arte.
- Arte auto explicativa: quem vê não precisa ler a legenda. Texto com conectivos e contexto, nunca seco ou abrupto, nunca blocos soltos e desconexos.
- Sem travessão e sem dois pontos, nas artes e nas legendas.
- Emojis moderados e ligados ao tema da plataforma (🦜 🎤 😅 🎢 🍽️). Só na legenda. Na arte, quase nunca.
- Errar é normal: "acontece com todo mundo", "errar faz parte", "sem julgamento". Nunca humilhar quem erra.

## 2. Voz e vocabulário da marca
- Vocabulário próprio: bando, poleiro, pio, soltar o bico, voar, pousar certinho, muda de penas, ninho.
- Nunca: "bater asas" (é do Duolingo), "ficar arara", "papagaio" em sentido pejorativo.
- A tutora e a professora são femininas ("a tutora", "ela"). Nunca "o tutor".
- Fecho padrão de toda legenda: "Arara vai ser sua nova professora de idiomas. Entre no bando, em breve tem novidade 🦜". Rodapé só na legenda, nunca dentro da arte.
- Pré-lançamento (lançamento 15/12/2026, go/no-go 28/11, recuo 12/01/2027): sem preço, sem data nova, sem prometer o que o app não faz.
- Afirmações de produto sempre conferidas contra o app (idiomas, níveis, correção, indicação). Níveis A1 a C1 são referência, sem equivalência com TOEFL ou IELTS.

## 3. Legendas
- Abre com gancho curto e relacionável, com um emoji.
- Corpo curto, em parágrafos separados, sem muralha de texto.
- Pede uma ação: salvar, comentar, marcar um amigo. Sempre uma só.
- Fecho padrão e 5 hashtags relevantes (#aprenderidiomas #ingles + temáticas).
- Eu escrevo e mostro para aprovação antes de agendar.

## 4. Direção de arte
- Referência de formato: Duolingo (telas de exercício, cartões "conheça o time", testes de personalidade, humor, dicas), adaptado com a identidade da Arara, sem cópia.
- Texto sobre a imagem deve parecer interface de app, não canvas: cartões, balões com cauda, badges, botões de resposta.
- Badge de título separado do badge de explicação. Raio de borda padrão e espaçamento generoso entre eles.
- Título nunca encostado no balão. Respiro entre os blocos.
- Tipografia arredondada e simpática, de acordo com a personalidade da Arara (hoje Baloo 2 para títulos e Nunito para corpo). Palavra-chave do título em destaque azul.
- Mascote: arara azul, barriga amarela, cauda com verde, marquinhas brancas nas bochechas, bico azul escuro, olhos grandes. Ilustração vetorial plana, arredondada. Sempre a mesma personagem.
- Paleta azul, amarelo e verde, fundo azul claro com brilhos amarelos.
- Cores por idioma (aprovado em 04/11/2026, "ficou melhor"): em artes de UM idioma, o fundo claro da ilustração e a cor de destaque da interface (selo, palavra em destaque do título, ícone de som, botões) seguem a língua. Inglês: fundo azul e destaque vermelho. Espanhol: amarelo-sol e vermelho. Francês: lavanda e azul cobalto. Italiano: verde menta e verde. Alemão: dourado e grafite. Português: verde-limão e verde. Japonês: rosa-claro e carmim. Chinês: vermelho-claro e vermelho. A mascote nunca muda de cor, e o verde de "acertou" continua verde. Capas com vários idiomas, humor, tutora e testes ficam no azul padrão. Implementação em `lang_theme.py`.
- Expressões da Arara (pedido de 04/11/2026): variar mais as expressões, misturando momentos sérios (foco, determinação, acolhimento) com humor e memes (deadpan, olhar de lado, sorriso forçado de "tá tudo bem", orgulho convencido), sem copiar memes reconhecíveis. A cena e a expressão devem combinar com a copy da arte.
- Ilustração sem texto e sem balão. Área superior vazia (mais de 52%) para o texto entrar depois. Mascote na metade de baixo, sem nada importante no rodapé.
- Cada tema ganha uma ilustração com cena e adereço relevantes (restaurante, tutora com fone, perfis do teste).
- Preferências de interface (herdadas do front-end): ícones lucide-react, sem emoji na UI, sem translateY em animações.

## 5. Formatos e cadência
- Posts e stories como antes. Reels autorizados em 05/11/2026 (primeiro publicado e cadência constante pedida). Planejamento em `reels_planejamento.md`: 2 por semana, terça e sábado às 19h30, a confirmar. O reel vai além do post do dia, não o substitui.
- 1 post por dia às 12h (Brasília), seguindo os temas dos stories.
- Sempre planejar junto os stories complementares do dia. Máximo 3 por dia, nunca enquete, quiz ou caixa de pergunta.
- Stories típicos: aviso de manhã ("já no feed"), complemento à tarde, exercício em duas partes (pergunta e resposta).
- Diversificar idiomas: frases úteis de cada língua, em rodízio. Listas de 6 idiomas funcionam.
- Pilares: frases úteis, exercícios, falsos amigos, gírias, humor de quem aprende idioma, conheça a tutora e a Arara, testes de perfil, como funciona o app.
- Toda data comemorativa tem post específico, incluindo datas das línguas que o app ensina (16 idiomas).
- Destaques do perfil feitos a partir de stories (Sobre, Como é, Frases, Lista), cobertas só depois que os stories estiverem no ar.

## 6. Como ele gosta de trabalhar comigo
- Primeiro o plano: copy e visual esperado para aprovar. Só depois a arte. Artes de uma semana são feitas na sexta.
- Aprovada a copy, eu já agendo a publicação automática. Nada vai ao ar sem o OK dele.
- Mostrar o resultado em folhas de revisão com tudo junto. Ele revisa e dá ajustes pontuais, que valem como regra daí em diante.
- Eu mesma confiro fatos e frases antes de entregar, em vez de pedir que ele confira.
- Proatividade e constância: sugerir melhorias, temas, oportunidades (estudo no exterior, trabalho, pesquisa), acompanhar engajamento e tendências.
- Subagentes: valem conforme o ~/.claude/CLAUDE.md (agentes especialistas por domínio, um ou dois por vez, brifados e revisados). Decisão de 31/10/2026, substitui o pedido de 27/10 de evitar subagentes. Custo do Opus no planejamento aprovado.
- Ações irreversíveis ou externas só com confirmação. Respostas diretas, sem enrolação corporativa e sem puxa-saquismo.

## 7. Reels: estilo visual aprovado (vídeo de teste v9, 04/11/2026)
Rodrigo viu o vídeo de teste e aprovou ("gostei do vídeo, vamos guardar o estilo visual para os próximos"). Isso vale como **estilo**: o escopo do calendário continua "só posts e stories" (seção 5) até ele autorizar Reels. Regras valem para qualquer vídeo da Arara.

**Formato e áudio.** 1080×1920, 30 fps, H.264 `yuv420p`, sem narração. Efeitos de interface CC0 (Kenney) e trilha instrumental gerada pelo OpenRouter (Lyria 3 Pro) com a chave do Rodrigo, autorizada em 05/11/2026 (`reel_teste/musica/gen_music.py` e `add_music.py`). Não marcar como conteúdo de IA no Instagram (decisão dele, 05/11/2026). Duração: quase todos abaixo de 25 s; o reel de lançamento tem 44 s.

**Roteiro-modelo (teaser "O branco").** Gancho "Deu branco?" → acolhimento ("Acontece com todo mundo. Aqui você treina falando.") → app em uso (missão, conversa por voz, correção) → "Situações reais em 16 idiomas." → trilha A1 a C1 → fecho "Solte o bico. Falta pouco." com chamada para a lista de espera.

**Cenas e transições.** Cada cena sai por completo antes da próxima entrar; entre elas aparece só o fundo. Cada troca tem movimento próprio (varredura com desfoque, iris, subida, clarão), nunca a mesma duas vezes seguidas.

**Mascote.** Sempre articulado por peças rígidas (cabeça, asas, rabo, mão, corpo, com pivôs), nunca deformando a imagem como bolha. A cabeça não infla (sem zoom no rosto, sem esticar o corpo). Sem tremor. Piscar, atraso da cabeça em relação ao corpo, molas na chegada, agachar antes do pulo, asas que sobem rápido e descem devagar. Giro 3D leve (até cerca de 60°) com paralaxe entre as peças e brilho atrás.

**Celular.** Proporção de celular de verdade (tela 540×1070 num quadro de 1080), moldura metálica, ilha da câmera, barra de status 9:41, reflexo, sombra no chão, entrada e giro 3D leves. Interface fiel ao app real (tokens de `themePalette.ts`). Conteúdo de exemplo da profissão do app (Hotelaria, "Ana"), nunca o de TI do ambiente de teste.

**Idiomas.** Nunca "Bom dia" (passa a ideia de que o app só ensina cumprimentos). Mostrar uma **situação profissional real do app** em vários idiomas (check-in com reclamação), com a tradução em português fixa embaixo, bandeira, cor do idioma e equalizador de voz; fechar com a grade das 16 bandeiras. Escolhas: inglês = Reino Unido, árabe = Egito, hebraico = Israel.

**Profundidade e vida.** Fundo em camadas com paralaxe, bokeh à frente, vinheta leve, câmera na mão discreta, texto que flutua de leve e entra desfocado. Evitar desfoque em contêineres grandes (deixa o render muito lento).

**Texto na tela.** Baloo 2 e Nunito, azul-noite com a palavra-chave em azul; pílula branca para legenda sobre fundos coloridos. Zonas seguras: nada importante nos 250 px do topo nem nos 380 px da base.

**Arquivos para reutilizar.** Pasta `arara_social/reel_teste/`: `index_v9_aprovado.html` (composição, linha do tempo GSAP e poses), `render_v9_aprovado.js`, `build_v9_aprovado.py`, `rig.py` (separa a mascote em camadas), `assets/rig/`. Passo a passo no `README.md` da pasta. Vídeo aprovado: `reports/arara_reel_teste_v9_*.mp4`.

**Imersão (v10, 04/11/2026, a confirmar).** Gancho com barra "Procurando a palavra em inglês…" que trava em 99%, antes do "Deu branco?". Na conversa por voz a câmera mergulha na tela do celular (zoom de cerca de 2×, a moldura sai de quadro) e volta ao tocar em Correções; balões verdes e amarelos ("Expressão usada", "Melhor assim", "1 correção") saltam da tela em primeiro plano. Legendas viram pílulas brancas por cima da cena. Idiomas com o nome do idioma repetido em letras gigantes ao fundo, deslizando. No fecho, penas gigantes e balões de fala ("Could you help me?", "¿Me puede ayudar?", "Pourriez-vous m'aider ?", "Mi può aiutare?") passam à frente da Arara. O encerramento do logo usa a cabeça da Arara saltando de um círculo azul. Arquivos: `reel_teste/index_v10.html`.

**Fluidez (v11, 05/11/2026, a confirmar).** O Rodrigo achou a v10 "robotizada" e pediu cenas "mais sexys, harmônicas" como nas referências. Causas identificadas: quadros nítidos sem desfoque de movimento, molas exageradas e letras entrando uma a uma com giro aleatório. Correções: desfoque de movimento real (4 sub-quadros por quadro, `render_mb.js` + `avg_mb.sh`, uns 15 min com 4 processos), molas limitadas, entradas de texto por subida suave (expo.out), trocas mais longas. Regra: uma coisa grande se move por vez, sem giros aleatórios.

**Encerramento do logo (aprovado como padrão em 04/11/2026, a confirmar após ver o resultado).** Todo reel termina com um clipe de 4,6 s: três pontos (azul, amarelo, verde) convergem num ponto que cresce e vira o ícone da Arara, com anéis e penas coloridas; o ícone desliza e a palavra "Arara" surge ao lado; depois "Converse por voz em 16 idiomas" e a pílula "falearara.com". Fundo azul-noite, referência: encerramento animado do Spotify enviado pelo Rodrigo. O reel escurece em 0,3 s antes do clipe (sem sobrepor cenas). Reaproveitar: `reel_teste/outro/index.html`, `render_outro.js`, `build_outro.py <reel_mudo> <reel_sfx>`.

**Pendências conhecidas.** Música; resolução da mascote (540×965 ampliada); link da bio ativo para o CTA; `publish.py` ainda não publica Reel.
