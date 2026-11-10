# LOTE 13 — regras comuns do executor (DeepSeek) — 09/11/2026

Você é o EXECUTOR. O orquestrador (Claude) define a peça, recolhe a imagem, mede, aprova e registra. Você só MONTA O PROMPT e DISPARA UMA geração. Diretório: ~/.openclaw/workspace/arara_social. Arquivo mestre: rara_sistema_de_marca_v6.md.

## Antes de disparar
1. Leia no mestre os blocos fixos [STYLE], [RARA] (versão com 2 linhas sob os olhos) e [NEGATIVE] (seção 7.0 e linhas ~1040 a ~1115). Copie-os INTEIROS, palavra por palavra. O [STYLE] termina em "...children's-book polish but not childish." Não corte, não resuma.
2. NÃO escreva os rótulos "[STYLE]", "[RARA]", "[NEGATIVE]" nem sinais "+" nem aspas no prompt. Parágrafos separados por linha em branco.
3. Prompt = [STYLE] + [RARA] + cena oficial da peça + ADAPTAÇÃO COMUM (abaixo) + adaptação específica da peça (vem na tarefa) + [NEGATIVE], terminando com a frase de formato indicada na tarefa.
4. Em DESVIOS, declare com honestidade qualquer diferença em relação ao pedido, inclusive se o [STYLE] ("gentle rim light") conflitar com a instrução de silhueta limpa (mantenha o bloco inteiro e deixe a instrução da peça depois).

## ADAPTAÇÃO COMUM (inclua em frases claras, em inglês)
- "Very short stubby legs, almost completely hidden under the belly feathers, only the feet and a short bit of lower leg visible, no long thin visible yellow legs."
- Se a peça for de corpo inteiro: "Both yellow feet clearly planted on the ground with a soft, subtle contact shadow under each foot; the long tail is whole and clearly visible, resting on the ground or hanging with clear logic, never floating loose in the air."
- "Both wings visible with natural anatomy, feather tips like fingers, no claws and no mitten shape."
- "Three curved eyelashes on each open eye and the two thin curved lines under each eye clearly visible, coral blush, throat feather band, hooked beak, complete headset with coral boom mic."
- Para recorte em fundo cinza: "completely flat solid neutral gray #8C8C8C background, generous empty margins of at least 150 px on every side, soft even front lighting with NO rim light, NO glow, NO halo, NO cyan or light fringe around the feathers and NO bright outline; clean matte feather edges against the flat gray."
- Sem texto, letras, números, logos ou rabiscos legíveis em nenhum objeto (cadernos, cartões, placas ficam em BRANCO liso).

## Como disparar
- Ferramenta image_generate, model openrouter/openai/gpt-5.4-image-2, count 1, image = /home/rodrigo/.openclaw/workspace/arara_social/personagens/rara/rara_canonica_frente_v1.png (UMA referência), filename e parâmetros de formato (aspectRatio E size) conforme a tarefa, timeoutMs 300000.
- image_generate é ASSÍNCRONA. Dispare UMA vez. A resposta "Background task started" É o sucesso. Não dispare de novo, não espere, não faça polling, não tente copiar, medir nem logar: quem recolhe é o orquestrador. Termine o turno com a resposta final.
- Erro HTTP 402: reporte a mensagem literal e pare, sem retentativa. Se a ferramenta rejeitar size, reporte a mensagem literal e dispare UMA vez só com aspectRatio, informando em DESVIOS.
- Não escreva em nenhum arquivo. Nada de vídeo, música, publicação, mensagens externas, segredos.

## Resposta final (formato fixo, curta)
STATUS (disparada|erro); TASK_ID; PARAMETROS_ENVIADOS; PROMPT_COMPLETO (texto exato enviado); ERROS (literal ou "nenhum"); DESVIOS (honesto, ou "nenhum").

## REGRAS ADICIONAIS (aprendidas em SI01 a SI03, 09/11/2026)
- Sombra de contato: escreva "a soft dark elliptical contact shadow clearly visible on the gray ground under each foot" (nas três primeiras a sombra saiu quase invisível).
- Escala: a figura inteira ocupa cerca de 65% da altura do quadro, centrada, para sobrar margem de pelo menos 150 px em TODOS os lados, inclusive topo (crista) e base (pés e cauda). Escreva "the whole figure, including the crest, the tail tip and the feet, is small enough to leave at least 150 px of empty gray on the top, bottom, left and right".
- Asas que apontam ou acenam: "the raised wing shows distinct, separate feather tips like individual fingers, not a rounded mitten or glove blob".
- Peça cortada na borda do quadro (ex.: espiando): o corte deve ficar EXATAMENTE na borda do quadro, sem faixa cinza além do corte ("the figure is cut by the image border itself, no gray strip beyond the cut").

## REGRAS ADICIONAIS 2 (aprendidas em SI05 a SI10, 09/11/2026)
- SEM DENTES: toda boca que aparece abre como "the hooked beak open wide showing only a pink tongue and the dark navy beak, absolutely no teeth, no human teeth". NÃO use "clenched", "grimace", "teeth-baring" nem "gritted": nas SI05 v1 e v2 isso gerou dentes de humano; "open beak showing only a pink tongue" deu certo na SI09 e na SI10.
- SEM GARRAS NAS ASAS: as pontas das asas terminam em penas azuis macias e arredondadas; "absolutely no dark claws, no dark nails and no black tips on the wing feathers" (a SI08 e a SI09 saíram com pontas escuras de unha nas asas).
- Declare em DESVIOS só o que de fato mudou, em frases completas e legíveis (a SI05 v2 trouxe um trecho truncado).

## REGRAS 13E (Falso amigo, cenas literais) — 09/11/2026
- Formato: vertical 4:5, `aspectRatio "4:5"` + `size "1024x1280"`, frase final "Vertical 4:5 portrait composition." Fundo: cor lisa e quente (cada peça indica), piso/superfície visível de outra tonalidade com sombra de contato.
- Rara de CORPO INTEIRO e GRANDE (cerca de 55% da altura), centralizada na metade de baixo; os 25% de cima do quadro ficam vazios (fundo liso, sem objetos) para o texto entrar depois. Folga de pelo menos 150 px em esquerda, direita e base.
- Aplique a ADAPTAÇÃO COMUM de corpo inteiro (pernas curtas, dois pés no chão com sombra elíptica escura visível, cauda inteira pousada, duas asas com penas azuis macias e arredondadas, sem unha escura, sem luva) e as REGRAS ADICIONAIS 1 e 2 (SEM DENTES: bico aberto só com a língua; bico fechado = "closed in a sly smile", nunca "clenched").
- Adereços (cartão, bandeja, placa, notas, livro, caderno) ficam TODOS lisos e em branco: sem letras, números, símbolos, logos ou rabiscos legíveis. Notas de dinheiro: verde liso sem nenhuma marca.
- Gente nunca realista: se a cena pedir outro personagem, use o elenco de apoio (capivara, onça, tucano) copiando o bloco oficial do personagem do mestre e passando também a imagem canônica dele; senão, sem outros personagens.
- Sem fundo cinza #8C8C8C nestas peças (não são recortes).

## REGRAS 13C (Rara pelo mundo, um cenário por idioma) — 09/11/2026
- Formato 4:5, `aspectRatio "4:5"` + `size "1024x1280"`, frase final "Vertical 4:5 portrait composition." Cenário cotidiano e cultural do idioma (comida, transporte, costume), em cor e luz próprias; piso/chão visível com sombra de contato.
- Regras do mestre: SEM bandeiras, SEM símbolos religiosos ou políticos, SEM monumentos ligados a governo. Sem texto, letras, números ou logos em nenhum objeto (relógio só com marcas, sem algarismos; táxi, trem, placas e cardápios lisos).
- Rara de corpo inteiro e grande (cerca de 55% da altura), centralizada na metade de baixo, ocupando o primeiro plano; o cenário atrás é simples e desfocado de leve. Os 25% de cima ficam livres de objetos importantes (céu, parede, teto lisos) para o texto entrar depois; folga de 150 px em esquerda, direita e base.
- Aplique a ADAPTAÇÃO COMUM de corpo inteiro (pernas curtas, dois pés no chão com sombra elíptica escura visível, cauda inteira pousada, duas asas com penas azuis macias, sem unha escura, sem luva) e as REGRAS ADICIONAIS 1 e 2 (SEM DENTES: bico aberto só com a língua; nunca "clenched/grimace").
- Comida e objetos pequenos nas asas: seguros por penas como dedos. Sem outros personagens (sem gente), salvo quando a cena pedir e o elenco de apoio existir.

## REGRAS 13C, ajustes (PM01 a PM04, 09/11/2026)
- A Rara saiu MUITO grande (75 a 80% da altura) em todas. Escreva: "Rara is SMALL in the frame: her whole body, from the crest to the feet and the tail tip, occupies only about 50% of the frame height, with a lot of environment visible around her" e mantenha o topo 25% do quadro vazio de objetos importantes.
- Veículos e objetos: placa de carro e emblemas DEVEM ser lisos: "the taxi has a plain blank license plate and a plain smooth grille without any emblem".
- A cauda longa pousada com folga: "the tail tip stays at least 150 px from every edge".

## REGRAS 13C v2 (após a revisão independente do lote 13, 09/11/2026 ~22h30 UTC)
O revisor reprovou PM03/PM04 e mandou corrigir PM02/PM05 por: asa que SEGURA objeto vira mão de dedos (polegar + 3 ou 4 lóbulos), indicador isolado ao apontar, cauda duplicada entre os pés, artefatos soltos. Para a v2:
- NENHUMA asa segura, empunha, pinça, agarra ou aponta com dedo. Objetos (prato, croissant, pretzel, sorvete, xícara) ficam APOIADOS sobre mesa, balcão, banco, suporte liso ou prato, ao lado da Rara. Escreva: "she holds nothing in her wings; every object rests on the table/counter/stand beside her".
- Gestos permitidos: asa inteira aberta em leque, asa levantada inteira (aceno), asa apoiada na mesa, asas cruzadas no peito, asa abraçando a barriga, asa cobrindo o rosto. Escreva: "each wing is a whole feathered limb ending in soft rounded blue feather tips, absolutely no thumb, no separated fingers, no fist, no mitten, no glove, no pointing finger, no dark claws, no dark nails".
- CAUDA: "one single long tail coming out from behind the hips, never passing between the feet, never duplicated".
- PEÇAS: nada de objeto flutuando, anel translúcido, pontinhos soltos ou fragmento de objeto no canto.
- FORMATO: 4:5 nativo, `aspectRatio "4:5"` + `size "1024x1280"` (deve sair 1122 x 1402), folga de pelo menos 150 px nas laterais.
- Microfone do headset azul-marinho liso, SEM esponja coral; garras dos pés azul-marinho escuro.
