---
name: arara-reels
description: Produz reels da Arara (Rara e Raro) com IA, movimento 3D, transições próprias da marca, voz dos personagens e telas genuínas do app. Use para planejar, gerar, compor, conferir e enviar para aprovação qualquer reel ou vídeo curto da marca.
---

# Reels da Arara

Versão 2, 12/11/2026. Dono: agente OpenClaw. Aprovador único: Rodrigo, pelo Telegram (fluxo da seção 11 do manual de operação).

**Ideia central: a fala vira matéria.** A Arara é um app de conversa por voz. Nos reels, o que a Rara e o Raro falam aparece, ocupa espaço, quebra, se conserta e leva a câmera para a próxima cena. Isso é o que nenhum outro app de idioma faz e é o que torna o vídeo reconhecível sem o logo. As assinaturas que realizam essa ideia estão em `referencias/assinaturas.md` e são obrigatórias.

## 0. Estado e trava

- **Reels bloqueados até o estilo ser aprovado.** A única tarefa liberada é o **piloto de estilo** (seção 13). Nada de série, calendário ou publicação antes de Rodrigo escolher o estilo e este skill ser atualizado com a escolha.
- Depois do estilo aprovado, produzir é livre dentro do teto de gasto; **publicar ou agendar** sempre passa pela aprovação no Telegram (item POST, com hash do arquivo final).
- **Nenhum pio da Rara** em reel até Rodrigo aprovar o pio (HUM-24).

## 1. Antes de cada reel: sincronizar e inventariar

As artes são adicionadas ao GitHub o tempo todo. Nunca trabalhe com lista fixa, cópia antiga ou memória.

1. `git pull` em `Moost-Studio/arara-identidade` (**fonte oficial** das artes e dos documentos) e em `Moost-Studio/arara-social` (acervo: ferramentas, áudio, pipeline antigo; suas artes podem estar atrasadas, não use como fonte de personagem).
2. Confira `arara_social/personagens/CANONICAS.sha256`. Se a soma de alguma canônica (C01 a C08) mudou, pare e avise Rodrigo.
3. Gere o inventário do dia em `arara_social/video/_inventario/AAAA-MM-DD.json` com todas as poses aprovadas de `personagens/rara/`, `personagens/raro/`, `elenco/` e `logotipo/`. Ignore `_substituidas`, `_descartadas`, `_reprovadas`, `_fora_da_biblioteca`, `_originais`. Use sempre a versão mais alta (`_v2` vence `_v1`).
4. Pose que não existe sai **por edição de uma canônica** (regra do `CANONICAS.md`), como tarefa de arte separada com plano e custo. Nunca improvise personagem dentro do vídeo.
5. Releia no master (`rara-sistema-de-marca.md`): blocos **[RARA]**, **[RARO]**, **[NEGATIVE]**, **[VIDEO]**, **[VOZ RARA]**, **[VOZ RARO]** (parte 7), regras de reels (6.5), assinaturas visuais (5.5), estados do topete (5.6), bordões (3.3), cores e tipografia (5.x). Use os blocos **literalmente**; não reescreva a descrição dos personagens.

## 2. O que Rodrigo já reprovou (não repetir)

Do acervo (`docs/memoria_agente/`): animação monótona e slide que desliza; efeito de balão (deformar o contêiner inteiro em vez de mover o personagem); cabeça que incha; tremor; visual infantil com cartões chapados; interface diferente do app ou celular fora de proporção; encerramento com salto duplo; "bom dia em 16 idiomas"; o reel de lançamento de 05/11, que ele excluiu.

## 3. Linguagem visual

- **3D com volume:** os personagens já são 3D estilizados. Câmera que orbita, dolly e push-in; paralaxe em 3 ou 4 camadas (fundo, palavras distantes, personagem, primeiro plano); profundidade de campo; luz de recorte; sombra de contato que cresce e encolhe com o pulo; motion blur real.
- **Personagem sempre vivo** (master 6.5): mola com amortecimento 12 a 15 e massa 0,6 a 0,8; antecipação de 0,1 s; topete e cauda com 2 a 4 quadros de atraso; respiração de 1,5% em ciclo de 2,4 s; piscadas irregulares a cada 2 a 5 s; squash de 6% a 10%, não em toda batida; troca de pose escondida dentro de um movimento; ação atravessando o corte na mesma direção. A Rara é rápida e um pouco desajeitada (tropeço leve na entrada). O Raro é calmo, gesto largo e lento, ajeita o chapéu.
- **Transições:** primeiro as assinaturas da marca (S1 a S11); depois a biblioteca das referências (`analise-referencias.md`, 2.1). Nunca slide, fade genérico ou corte seco sem motivo.
- **Uma cor dominante por vídeo** da paleta: Azul Canindé #2457E6, Amarelo Peito #FFC83D, Verde Cauda #22B573, Coral #FF6B57, Azul-Noite #081226, Creme #FFF5E1, Céu #DCEBFF.
- **Premium, não infantil:** humor de colega de trabalho engraçado, luz de estúdio, materiais com textura, grão leve.
- **Ritmo:** cenas de 0,5 a 1,5 s cortadas na grade da batida; o vídeo acelera no meio e respira antes do fim, com um momento de câmera lenta; primeiro quadro já em movimento; último quadro conversa com o primeiro para o loop.
- **Duração:** 10 a 20 s (master 6.5); até 30 s só quando a fala pedir. 30 fps; 60 fps quando houver muito movimento de personagem.

## 4. Ferramentas

| Etapa | Ferramenta | Regra |
| --- | --- | --- |
| Quadros-chave e storyboard | Gemini imagem (`tools/gemini_multiref.py`), editando canônicas e poses aprovadas | Molde de cena do master; fundo #8C8C8C quando for recortar |
| Clipes de personagem | Veo 3.1 (Google) via OpenRouter, imagem para vídeo. Base: `arara-social/arara_social/video_ia/gen_video.py`. `veo-3.1-fast` 720p para teste, versão completa 1080p só no corte final | Clipes de 4 a 8 s, primeiro quadro de pose aprovada |
| Voz | Gemini TTS `google/gemini-3.8-flash-tts` via OpenRouter `/audio/speech`: **Rara = Achernar, Raro = Achird** (`casting/resultado.md`), com o estilo dos blocos [VOZ RARA] e [VOZ RARO] | Nunca usar a voz gerada pelo modelo de vídeo |
| Composição, 3D gráfico, tipografia, transições | Remotion (decisão 18) com `@remotion/three`, `@remotion/transitions`, `@remotion/media-utils`, `@remotion/noise`. Projeto em `arara_social/video/` (decisão 20) | Tokens do `motion.ts` do app (receitas, seção 3) |
| Trilha e efeitos | `audio/trilhas`, `audio/trilhas_master`, `audio/sfx`. Trilha nova só com licença comercial conferida | Pio proibido até HUM-24 |

Antes do primeiro uso de cada modelo no dia, confirme no catálogo do OpenRouter (`GET /api/v1/models`) que o id existe e o preço atual; registre mudança no log. As receitas de cada etapa estão em `referencias/receitas-tecnicas.md`.

## 5. Desenho de som (metade da sensação de movimento)

- Toda transição tem som próprio: S1 com um "sopro" crescente, S3 com vidro leve e clique de encaixe, S4 com um "pop" grave, S6 com farfalhar de pena, S10 com página virando. Sem som, a transição parece barata.
- Trilha na grade de BPM (`beats.json`), abaixando 8 dB sob a fala (sidechain). Mix final -14 LUFS, pico -1 dBTP.
- Um silêncio de 4 a 8 quadros antes da frase principal aumenta o impacto.

## 6. Fala dos personagens

1. Texto do roteiro aprovado, na voz da personagem; bordões do master (Rara: "Solta o bico!", "Errou? Treinou.", "Bora ensaiar?", "Que coisa Rara!", "Guardei seu lugar."; Raro: "Bah, isso tem história.", "Senta que lá vem história."). Bordão novo só com aprovação.
2. Áudio pelo TTS com a voz fixa e instrução de estilo (euforia, drama, calma); voz normalizada a -16 LUFS.
3. Clipe do personagem **falando sem áudio** (bico abrindo e fechando em ritmo de fala, cabeça e asas gesticulando), na duração da fala mais 0,5 s.
4. Sincronia: ataques de sílaba alinhados às aberturas do bico; corte e velocidade entre 0,9x e 1,1x; diferença acima de 3 quadros reprova. No piloto, teste também um modelo de lip-sync, se o catálogo tiver, e Rodrigo escolhe o método.
5. A fala dirige a imagem: anéis do S1 e estalo do topete pela amplitude real da voz; palavras do S2 entram sílaba por sílaba.
6. Legenda sempre na tela (muita gente assiste sem som).
7. Reel sem fala é válido: o personagem reage e gesticula e a mensagem vai na tipografia.

## 7. Telas do app: só genuínas

- Capturadas do app real (TestFlight, teste interno ou staging) com conta de teste sem dado pessoal. Nunca redesenhar, mockar ou gerar interface por IA.
- Só recursos com flag ligada na semana (`operacao/flags/AAAA-MM-DD.json`). Sem a ficha da semana, nenhuma tela de recurso com flag entra.
- Podem ir para dentro de um celular 3D em **proporção real** e receber o mergulho (S9), sem retoque no conteúdo.
- Sem a captura, peça a Rodrigo pelo Telegram e siga com outra cena.

## 8. Prompt de clipe (modelo)

Em inglês, sempre com primeiro quadro de pose aprovada:

```
[bloco RARA ou RARO do master, literal]
Motion, second by second: [0-1 s ...] [1-3 s ...] [3-5 s ...]
Secondary motion: crest follows through 2-4 frames behind the head, tail and feathers settle after each move, natural irregular blinks, soft breathing.
Camera: [slow orbit | dolly in | push past the wing | locked], 3D depth, soft rim light, shallow depth of field.
Background: [solid #8C8C8C for matting | scene in brand colors].
[bloco VIDEO do master, literal]
[bloco NEGATIVE do master, literal] No audio.
```

Regras: um gesto principal por clipe; descreva o passo, nunca "dance" genérico; câmera e personagem sem direções conflitantes; clipe que deformar o personagem é descartado, não consertado em pós; no máximo 3 tentativas por clipe, e na terceira falha troque o plano (outra pose de partida, câmera mais simples) e registre por quê.

## 9. Texto na tela

- Nunito no texto, **Mochiy Pop One em caixa alta só no punchline**, sem ponto. Maiúscula só no início do título; linhas de apoio em minúscula, como mensagem.
- Texto só em Azul-Noite ou branco. Palavra-chave em Amarelo Peito sobre fundo escuro; sobre fundo claro, em Azul-Noite com marca-texto amarelo inclinado.
- Português do Brasil, com a frase no idioma da aula em destaque. Uma ideia por tela, até 7 palavras por vez, entrando na batida. Texto é objeto de cena (S2, S3, S8), não legenda solta.
- Sem emoji, travessão ou dois-pontos na arte; sem concorrente nem fornecedor de IA (`forbidden.ts`); sem número, nota de loja, depoimento ou promessa inventada.
- Zonas seguras em 1080x1920: nada importante nos 250 px de cima, nos 420 px de baixo e nos 120 px da direita.

## 10. Saída

- 1080x1920, H.264 High, yuv420p, AAC 48 kHz estéreo, -14 LUFS, pico -1 dBTP. Capa JPG 1080x1920.
- Encerramento com o logo animado (`reel_teste/outro/`, versão corrigida sem salto duplo) em até 2 s.
- Pasta `arara_social/video/reels/<id>/`: `roteiro.md` (com as assinaturas usadas), `beats.json`, `storyboard.png`, `animatic.mp4`, `clipes/`, `voz/`, `render/<id>_v<n>.mp4`, `capa.jpg`, `custos.json`, `qa.json`. Vídeos pesados podem ficar fora do git conforme Rodrigo definir; roteiro, storyboard, QA e custos vão sempre.
- Commits em Conventional Commits (`feat(reels): ...`), sem atribuição a IA. Chave nunca em arquivo versionado.

## 11. Conferência antes da aprovação

Rode a conferência automática (receitas, seção 9) e a folha de contato a cada 0,25 s. Refaça se qualquer item falhar:

- [ ] Personagem idêntico à canônica em todo quadro: marcas do rosto, cílios (só Rara), fone com detalhe coral (Rara) ou verde (Raro), chapéu, óculos e lenço do Raro, bico, proporções. Nenhum dedo humano, cauda dupla ou abaixo da linha dos pés, olho ou bico deformado, halo de recorte.
- [ ] Sem efeito de balão, cabeça inchando, tremor ou corpo derretendo.
- [ ] `freezedetect` limpo (nada parado mais de 1,5 s); primeiro quadro em movimento.
- [ ] Pelo menos duas assinaturas da marca; nenhum item da lista anticlichê.
- [ ] Toda transição com som; cortes na batida.
- [ ] Voz certa e boca sincronizada (menos de 3 quadros); legenda presente.
- [ ] Telas genuínas, só com flag ligada.
- [ ] Texto conferido pelo verificador de copy; zonas seguras.
- [ ] No máximo 3 clarões por segundo (fotossensibilidade).
- [ ] Sem pio; trilha com licença.
- [ ] Técnica e loudness conforme a seção 10; custo real dentro do teto.

## 12. Custo, aprovação e aprendizado

- Plano em `_ponte_claude/planos/` antes de gerar: clipes, modelos, durações, tentativas previstas e custo estimado. Respeite `TETO_POR_LOTE` e `TETO_DIARIO`; passou, pede aval no Telegram.
- Aprovação em duas etapas: (1) **storyboard e animatic** com a fala em áudio e as assinaturas marcadas; (2) **reel final** com folha de contato, custo e legenda.
- Log de cada geração no `rara_log_geracao.md`.
- **Biblioteca viva:** cada reel publicado registra em `arara_social/video/desempenho.json` as assinaturas e transições usadas e, na semana seguinte, a retenção nos 3 primeiros segundos, a retenção média, salvamentos e envios. No relatório semanal, mostre quais movimentos estão ligados aos melhores números e proponha promover ou aposentar movimentos. A proposta vai para Rodrigo; a mudança no skill só com o OK dele.
- Ganchos em teste: quando fizer sentido, produza duas aberturas do mesmo reel (só os 2 primeiros segundos mudam) para teste com quem não segue, se a conta tiver o recurso de reels de teste. Publicar continua exigindo aprovação.

## 13. Piloto de estilo (primeira e única tarefa agora)

Um roteiro de 12 a 15 s em três versões, para Rodrigo escolher o estilo.

**Roteiro base:** na call, a pessoa trava ("Deu branco"). A Rara entra pela borda de baixo (S8), solta o bico (S1) e a palavra que faltava sai do bico em letras 3D (S2). Mergulho na tela genuína de uma conversa do app (S9). Fecha com "Bora ensaiar?" e o logo. Fala da Rara com a voz Achernar.

- **A. Cinema 3D:** quase tudo em clipes Veo encadeados como plano-sequência (S7), costuras com pena-cortina (S6), câmera orbitando, profundidade de campo.
- **B. Motion 3D gráfico:** Remotion com celular 3D, letras infladas, anéis dirigidos pela voz; a Rara entra em clipes curtos recortados sobre o cenário.
- **C. Híbrido rápido:** cortes na batida a cada 0,5 s, balão torto como portal (S4), "Errou? Treinou." com a frase quebrando e se reconstruindo (S3), tipografia gigante ao fundo, Rara gingando no ritmo.

Entregue no Telegram: as três versões, a folha de contato de cada, o custo de cada, o método de boca usado (sincronia manual e, se houver, lip-sync por modelo) e a pergunta "qual estilo, e o que mudar". O teto de gasto do piloto inteiro é aprovado por Rodrigo antes de começar.

Depois da escolha: atualize as seções 3 e 13 deste skill, registre a decisão no master e só então proponha a série.

## 14. Referências do skill

- `referencias/assinaturas.md`: as 11 assinaturas de movimento da marca e a lista anticlichê.
- `referencias/receitas-tecnicas.md`: batida, voz dirigindo o movimento, tokens, câmera viva, transições como componentes, recorte de clipe, encadeamento, mixagem e conferência automática.
- `referencias/analise-referencias.md`: 21 vídeos de referência analisados e a tradução de cada técnica para a Arara.
- No repositório: `reels_plano_remotion_v1.md` (formatos e calendário de janeiro, conteúdo e não estilo, até o piloto); `personagens/rara/rig/` (rig 2D por código, para movimentos pequenos).
