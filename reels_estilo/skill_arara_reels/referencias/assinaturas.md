# Assinaturas de movimento da Arara

O que torna os reels da Arara reconhecíveis sem o logo. As referências (`analise-referencias.md`) ensinam técnica; estas assinaturas são **nossas**, nascem do produto (conversa por voz) e das assinaturas visuais do master (5.5): "Solta o bico", balão de fala torto, topete-termômetro, acessórios de áudio, penas-dedo.

Princípio: **a fala vira matéria.** Nenhum app de idioma mostra a voz como coisa física. Na Arara, o que se fala aparece, ocupa espaço, quebra, se conserta e leva a câmera para a próxima cena.

Regra de uso: todo reel usa **pelo menos duas** assinaturas, e no máximo quatro (mais que isso vira catálogo). Tempos em quadros a 30 fps; curvas e molas do `motion.ts` do app (seção 3 de `receitas-tecnicas.md`).

---

## S1. Solta o bico (transição-assinatura)
**O quê:** a Rara abre o bico e as ondinhas de som saem como anéis que crescem e viram o portal para a cena seguinte.
**Como:** 3 a 5 anéis em Azul Canindé e Amarelo Peito, nascendo do bico com 3 quadros de intervalo, espessura e raio dirigidos pela amplitude real da voz (`visualizeAudio`). O último anel vira máscara circular e revela a próxima cena dentro dele (12 a 16 quadros, curva `saida`).
**Quando:** início de fala, virada do gancho, saída para a tela do app.
**Não fazer:** anel genérico de "ondas de rádio" sem vínculo com a voz; anel em cor fora da paleta.

## S2. Palavra que sai do bico
**O quê:** a palavra em inglês (ou no idioma da aula) que a Rara fala **sai do bico como letras 3D infladas** (Mochiy Pop One, caixa alta), cai com física, quica e para no chão; a Rara reage a ela (pisa, abraça, empurra).
**Como:** letras em `@remotion/three` com material emborrachado, mola `passada`, sombra de contato, entrada sílaba por sílaba em sincronia com o áudio da fala.
**Quando:** toda vez que o reel ensina uma palavra ou expressão.

## S3. Errou? Treinou. (quebra e reconstrução)
**O quê:** a frase errada aparece, **racha** em Coral #FF6B57 e se desfaz em cacos; os cacos voltam no ar e montam a frase certa, que acende em Verde Cauda #22B573.
**Como:** a frase é dividida em fragmentos (Voronoi ou recorte por letra), explosão de 8 a 10 quadros, pausa de 4 quadros, reconstrução de 12 quadros com mola. Som de vidro leve na quebra e "clique" de encaixe na reconstrução.
**Quando:** falso amigo, erro comum, "I am agree".

## S4. Balão torto (portal)
**O quê:** o balão de fala torto da marca (branco, levemente inclinado, rabicho meio torto, borda inferior mais grossa) cresce até encher a tela e a câmera **entra nele**; a cena seguinte acontece dentro do balão.
**Como:** escala do balão de 0,3 a 4,0 com curva `saida` em 10 quadros, câmera em push-in simultâneo, desfoque de movimento radial nos 3 quadros finais.
**Quando:** mudança de tempo ou lugar ("na call", "no aeroporto"), início de diálogo.

## S5. Topete-termômetro na batida
**O quê:** o topete mostra a emoção antes do rosto (master 5.6) e marca o ritmo: dá um estalo na batida forte da trilha; vira espiral na confusão; murcha no erro; fica em pé na conquista.
**Como:** camada própria do topete com atraso de 2 a 4 quadros em relação à cabeça; nos clipes de IA, pedir o movimento do topete no prompt do segundo exato.

## S6. Pena-cortina
**O quê:** uma pena da Rara (gradiente azul, turquesa e verde da cauda) atravessa a câmera em primeiro plano, girando, e esconde o corte.
**Como:** pena 3D a 0,5 m da câmera virtual, desfocada, 6 a 8 quadros cruzando a tela na diagonal, com leve rotação em dois eixos. Substitui qualquer corte seco entre clipes de IA.

## S7. Plano-sequência de voo
**O quê:** em vez de cortes, a câmera **segue a Rara voando** de uma cena para a outra, num único plano aparente.
**Como:** clipes de IA encadeados (último quadro do clipe aprovado vira o primeiro quadro do próximo), costuras escondidas por S6 ou por uma asa passando perto da câmera; fundo muda durante o voo (escritório, aeroporto, tela do app).
**Quando:** reels de "um dia com a Rara", viagem, lançamento.

## S8. Quarta parede vertical
**O quê:** a Rara **usa as bordas do vídeo**: aparece de baixo da linha de legenda, empurra o texto para cima com a asa, senta numa palavra, espia pela lateral, segura a borda como se fosse a janela.
**Como:** personagem com recorte (matte) sobre a composição; o texto é objeto de cena com física, não legenda solta.
**Não fazer:** imitar botões ou interface do Instagram ou do TikTok.

## S9. Mergulho na tela genuína
**O quê:** a câmera atravessa a tela do celular 3D e entra na **gravação real do app**, que preenche o quadro; na volta, a Rara sai da tela.
**Como:** celular 3D em proporção real, push-in de 14 a 18 quadros com rampa `padrao`, a tela vira o quadro inteiro sem mudar o conteúdo capturado.

## S10. Dicionário do Raro (página que vira)
**O quê:** assinatura só do Raro. Ele abre o dicionário de bolso, as páginas viram em 3D e cada página é a próxima cena. "Senta que lá vem história" troca a textura para papel quente e a câmera desacelera.
**Como:** page-turn 3D com marcadores coloridos do dicionário; ritmo do Raro é mais lento (cenas de 1 a 1,5 s).

## S11. Dueto de ritmos
**O quê:** quando os dois aparecem, o vídeo alterna o tempo: cenas da Rara cortam a cada 0,5 s com câmera nervosa; cenas do Raro duram 1 a 1,5 s com câmera parada e um único movimento. O contraste vira piada visual.

---

## Anticlichê (evitar mesmo que esteja na moda)
- RGB split e glitch digital genérico.
- Celular 3D girando sem motivo.
- Adesivo de meme (gato, rosto), emoji, figurinha de terceiros.
- Máquina de escrever em todo texto.
- Zoom com desfoque radial em todo corte.
- Mais de 3 clarões por segundo (também é regra de acessibilidade contra fotossensibilidade).
