# Nova identidade da Arara (replanejamento de 05/11/2026)

## Direção vigente — 06/11/2026

**Feedback do teste do balão v1:** Rodrigo considerou o movimento ainda engessado e pediu mais vida, como na referência da Pixar. A v1 não valida a atuação; não expandir esse movimento para reels completos. Priorizar intenção, olhar, antecipação, peso e reações orgânicas, não complexidade de câmera. Uma alternativa de 6 s por vídeo generativo foi preparada em `reel_teste/imersao/teste_atuacao_v2.json`; ainda não gerada, estimativa consultada de US$ 0,48 e gasto novo pendente de autorização.

Rodrigo aprovou a referência de atuação da abertura da Pixar (peso, antecipação, pausas e personalidade) e pediu a execução do teste curto da arara com o balão. Produção isolada em `reel_teste/imersao/`, com a mascote original 2D em cena tridimensional. Não implica aprovação final do vídeo nem substituição do encerramento oficial.

Rodrigo quer reels mais imersivos, com motion arrojado e criativo, experiência única e 3D, **mantendo a arara antiga**. O caráter de mascote de app de idiomas deve ser preservado. A aprovação anterior da nova personagem 3D foi revogada; as decisões antigas abaixo são histórico quando conflitarem com esta atualização.

Interpretação criativa proposta, ainda não validada em novo render: combinar a mascote vetorial original com cenários e objetos 3D, profundidade e movimentos de câmera integrados à narrativa. Não confundir esse tratamento com autorização para modelar outra arara. Não reutilizar automaticamente os reels antigos como aprovados. Nenhuma publicação ou agendamento foi autorizado por esta definição.

**ATUALIZAÇÃO 05/11/2026, 23h55: o Rodrigo voltou atrás na mascote.** Disse que a mascote antiga (vetor plano) é mais bonita. A decisão das 22h37 (arara 3D oficial) está SUPERADA. A mascote oficial segue sendo a vetorial. Os arquivos da arara 3D ficam em `mascote_3d/` apenas como teste descartado. O que continua valendo da nova direção: paleta azul-noite, luz de estúdio, fotos/clipes de pessoas, texto sóbrio com palavra-chave em amarelo, encerramento C, frase 'Ensaie antes de falar.' no encerramento do teste. Ainda não decidido: música, voz do clipe do café.

Decisão do Rodrigo em 05/11/2026 às 22h37: a arara 3D da opção 1 vira a **mascote oficial**, e a identidade está sendo replanejada. A decisão substitui o estilo vetorial plano para os novos materiais. Os materiais já publicados e o logo atual (círculo azul com a cabeça) continuam como estão até nova decisão sobre o logo.

## Já decidido
- Mascote oficial: `mascote_3d/referencia_oficial_candidata.png` (arara 3D, sorriso fechado, olhar para cima, cabeça azul, peito amarelo, máscara clara, bico cinza). Folha de poses de teste em `mascote_3d/folha_poses_v1.png`.
- Direção visual: azul-noite #07152F, azul elétrico #245BFA, ciano #36C9F5, amarelo #FFC928, branco. Luz de estúdio, fotos reais de pessoas, sem confete, sem cara infantil.
- Encerramento dos reels: versão C (`reports/outro_c/encerramento_c.mp4`), aprovada. Ele ainda usa a cabeça da arara vetorial no logo e a tela atual do app.

## Ainda aberto
- Logo: manter o círculo com a cabeça (vetor) ou criar um símbolo novo. O exemplo do Rodrigo mostrava uma pena em curva.
- Cabeça 3D no logo e no avatar do Instagram.
- Tipografia: o app usa Baloo 2 e Nunito. A prancha propôs Manrope e Inter.
- Frases de marca novas (por exemplo "Ensaie antes de falar"): nenhuma foi aprovada.
- Fecho padrão das legendas e a regra de zero travessão nas artes: sem mudança até decisão contrária.
- Mascote fixa em clipes: precisa de teste de consistência em movimento. Um teste foi feito em 05/11 (ver reports/video_ia).
- Fundo transparente da mascote para composição nas artes e nos reels.
- Os 13 reels já renderizados (novembro e dezembro) usam o visual reprovado e não devem ser agendados.
- O guia `guia_de_estilo_arara.md` e as seções de estilo do README do pipeline ainda descrevem o vetor plano. Atualizar quando a identidade fechar.

## Como a produção funciona agora
Fotos e clipes de pessoas e cenas vêm de IA (Veo 3.1 Fast pelo OpenRouter, cerca de US$ 0,08 a 0,10 por segundo). Texto, interface do app, bandeiras, logo e encerramento ficam no motor de reels (HTML e GSAP), porque modelos de vídeo deformam letras. Detalhes em `prompts_video_ia.md`.

## Posts e stories (06/11/2026)
Proposta de direção visual em `direcao_visual_posts_stories_2026-11.md`, aguardando aprovação. Os agendamentos de 06 a 15/11 não foram alterados.

## Tom de voz (06/11/2026)
Proposta de tom de voz mais social, criativo, brasileiro e desajeitado em `tom_de_voz_arara_2026-11.md`, aguardando aprovação. O plano de 16 a 22/11 e os textos agendados não foram alterados.

## PAUSA DAS ARTES (06/11/2026, 9h03 BRT)
O Rodrigo pediu para pausar as artes da Arara enquanto reformula a identidade. Nenhuma arte nova é produzida até novo aviso (posts, stories, reels, protótipos). A situação das publicações já agendadas de 06 a 15/11 aguarda a decisão dele (ver conversa). Trabalho de planejamento já feito (direção visual, tom de voz, catálogo de formatos, protótipos) fica guardado como proposta.

## SISTEMA DE MARCA v6 RECEBIDO (06/11/2026, 11h37 BRT)
O Rodrigo enviou `rara-sistema-de-marca.md` (versão 6, 06/11/2026), salvo em `rara_sistema_de_marca_v6.md` (1.921 linhas). Declara substituir os documentos anteriores e define: marca Arara, personagem Rara (arara-canindé feminina, tutora de IA), secundário Raro, voz em portuglês com cargos e drama carinhoso, paleta livre por tema com quatro âncoras, tipografia Nunito Black e Mochiy Pop One, séries do feed, formatos de story e reel, campanha "A Rara perdeu a voz", prompt fundamental do agente (7.0), lotes 1 a 16 e plano de rebrand do app (parte 8).
Passa a ser a fonte da identidade. Substitui, nas redes, as propostas deste dia (direção visual, tom de voz). A pausa das artes continua até o Rodrigo liberar. O primeiro passo previsto pelo documento (7.20) é a canônica da Rara (C01) e a folha de giro (C02), com aprovação humana antes de seguir. Conflitos com regras em vigor listados na conversa e aguardando decisão.

## DECISÃO (06/11/2026, 11h39 BRT): "esse documento é a nova id"
O Rodrigo confirmou que o sistema de marca v6 é a nova identidade e prevalece sobre as regras antigas e sobre as propostas do dia (direção visual, tom de voz, paleta azul-noite, Baloo 2, limite de stories, regra de "papagaio"). A pausa das artes termina para o fluxo do documento (seção 7.20), que começa por C01 e C02, com aprovação humana antes de seguir. Peças com a identidade antiga continuam só até 15/11, como já agendado.
