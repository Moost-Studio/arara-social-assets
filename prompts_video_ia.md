# Prompts de vídeo com IA para os reels da Arara (05/11/2026)

Origem: os 6 prompts enviados pelo Rodrigo (os de número 5 e 6 chegaram idênticos). Nada foi gerado ainda. Preço consultado em 05/11/2026 na lista de vídeo do OpenRouter (https://openrouter.ai/api/v1/videos/models). Modelo candidato: `google/veo-3.1-fast`, de 4, 6 ou 8 s, a US$ 0,08 por segundo em 720p sem áudio e US$ 0,10 com áudio.

## Regras de produção
- A IA entrega o plano de fundo e a cena. Todo texto legível, logo, bandeira e interface do app é composto depois no motor de reels (HTML e GSAP), porque modelos de vídeo deformam letras e rostos de marca.
- O encerramento C (`reports/outro_c/encerramento_c.mp4`) fecha cada reel.
- Cada clipe é estudado como uma cena de 4 a 8 s e entra em um reel de 12 a 20 s, alternando com cartões de texto sóbrios.
- Gerar um clipe de teste de cada vez e aprovar antes do próximo. Usar `seed` para repetir.

## Mudanças que proponho nos prompts
- Descrever uma ação por faixa de tempo (0 a 2 s, 2 a 5 s, 5 a 8 s). Modelos de vídeo seguem melhor marcações de tempo que adjetivos.
- Pedir som ambiente, sem fala. O Veo gera áudio e inventa diálogo ininteligível se não for contido.
- Evitar "Apple-inspired" e "Apple". Citar a estética (estúdio escuro, vidro e alumínio) sem a marca de terceiros.
- Frases negativas ao fim: "no text, no logos, no subtitles, no watermarks, no extra fingers, no distorted faces".

## P1. Cafeteria, o travamento (vídeo 6 a 8 s, 9:16)
Cinematic commercial, 35mm lens, shallow depth of field. A young Brazilian professional in their late twenties sits at a window table in a modern coffee shop, talking with a colleague who stays out of frame. 0-2 s: speaks fluently, relaxed. 2-5 s: stops mid-sentence, eyes drift slightly up and to the side searching for a word, a small tight breath. 5-8 s: slow push-in toward the face, soft exhale, a faint self-aware smile. Warm natural window light, restrained color grading, natural skin texture. Ambient cafe sound only, no speech audible. Vertical 9:16. No text, no logos, no subtitles, no watermarks.
Observação: pessoa fotorrealista gerada por IA. Conferir a regra atual da Meta sobre aviso de conteúdo feito com IA antes de publicar (a decisão de 05/11 de não marcar foi tomada para a mascote).

## P2. Celular em estúdio (vídeo 6 a 8 s, 9:16)
Premium product cinematography. A modern smartphone floating in a deep midnight-blue studio, thin cyan light trails orbiting the device. The camera orbits about 40 degrees around the phone, then settles into a frontal close-up on the screen. The screen is a flat solid pure green (#00FF00) with no reflections on the glass surface, for chroma keying. Realistic aluminium and glass, precise shadows, minimal composition. No text, no logos, no hand, no watermarks. Vertical 9:16.
Observação: orbitar 180 graus impede compor a tela real com precisão. Limitar o giro e terminar de frente. A tela do app entra por chave de cor.

## P3. Tipografia que se corrige (não gerar por IA)
Modelos de vídeo escrevem letras erradas. Fazer no motor de reels: frase em branco sobre azul-noite, as palavras trocam de lugar até a frase certa, com destaque azul elétrico. Prompt para IA fica só para um plano de fundo de partículas e profundidade, sem letras.

## P4. Globo com balões de fala (vídeo 8 s, 9:16)
High-end 3D animation. A luminous translucent globe floating in a deep blue environment, soft speech bubbles orbiting it, each bubble containing abstract light patterns (no letters, no symbols, no flags). The camera circles slowly around the globe. Refined cyan and blue highlights with a few warm amber accents, realistic glass and light materials. Ambient music-free soft whoosh. Vertical 9:16, 8 s. No readable text, no flags, no logos.

## P5. Arara de marca (vídeo 6 a 8 s, 9:16, imagem para vídeo)
Decisão pendente. A mascote aprovada é uma arara azul de barriga amarela, cauda com verde, marquinhas brancas e estilo vetorial plano. O prompt do Rodrigo descreve uma arara realista em 3D, o que muda a identidade.
- Opção A (preserva a marca): animar a arte oficial por imagem para vídeo, mantendo o estilo plano, com giro de cabeça, piscar e abertura de asas.
- Opção B (nova identidade 3D realista): gerar, mas só depois de aprovar um novo guia visual da mascote.
Prompt da opção A: Animate the provided flat-vector macaw mascot exactly as drawn, keeping the same colors, proportions and style. 0-3 s: the head turns slowly toward the camera and blinks once. 3-6 s: the wings open gently and the tail feathers sway. Slow dolly-in on a dark navy studio background with a soft cyan rim light. No change to the character design, no text, no logos.
