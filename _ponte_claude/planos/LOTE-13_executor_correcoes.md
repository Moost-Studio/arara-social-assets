# LOTE 13: tarefa-padrão do EXECUTOR nas correções (10/11/2026)

Você é o EXECUTOR (DeepSeek). Monte UM prompt e dispare UMA geração. Quem recolhe, mede, aprova e registra é o orquestrador.

## Leia antes
1. `/home/rodrigo/.openclaw/workspace/arara_social/_ponte_claude/planos/LOTE-13_regras_executor.md` inteiro (seções 13C v2 e adicionais valem para TODAS as peças, inclusive recortes e reações).
2. No mestre `/home/rodrigo/.openclaw/workspace/arara_social/rara_sistema_de_marca_v6.md` (seção 7.0 e linhas ~1040 a ~1115): blocos fixos [STYLE], [RARA] (versão com 2 linhas sob os olhos) e [NEGATIVE]. Copie-os INTEIROS, sem rótulos, sem sinais "+". Para elenco de apoio, copie também o bloco oficial do personagem.

## Estrutura do prompt
[STYLE] + [RARA] (+ bloco do elenco quando houver) + cena da peça + restrições abaixo + [NEGATIVE] + frase de formato.

## Restrições obrigatórias (aprendidas na revisão independente)
- Nenhuma asa segura, empunha, pinça, agarra, aponta com dedo ou faz joinha. Objetos ficam apoiados em superfície, no colo ou flutuam como adereço de cena. Cada asa é um membro inteiro de penas terminando em pontas azuis macias arredondadas: sem polegar, sem dedos separados, sem punho, sem luva, sem garra ou unha escura.
- Bico em gancho CURTO e canônico (nunca esticado ou deformado). Aberto mostra SÓ a língua rosa, sem dentes nem formas claras na mandíbula.
- Rosto completo: 3 cílios por olho, 2 linhas curvas sob cada olho, rubor coral, faixa azul-marinho na garganta, headset azul-marinho com detalhes coral e microfone AZUL-MARINHO liso (sem esponja coral). Cabeça e topete nas proporções canônicas.
- Pés amarelos plantados (ou assentados) com sombra de contato elíptica escura visível; pernas curtas; UMA única cauda, de trás do quadril, nunca entre os pés, nunca duplicada, com a ponta a pelo menos 150 px das bordas.
- Sem texto, letras, números, logos ou rabiscos; adereços lisos e em branco.
- Nada flutuando: sem objetos soltos, anéis translúcidos, pontinhos ou fragmentos nos cantos.
- Elenco: capivara, onça e tucano com patas/asas canônicas, sem mãos humanas, sem dedos separados, sem presas; ao copiar o bloco do tucano, declare depois "no surfboard and no shorts visible" (cena sentada) e, ao copiar o bloco da onça, que ela não segura currículo.
- Formato 4:5: `aspectRatio "4:5"` + `size "1024x1280"` (deve sair 1122 x 1402) e frase final "Vertical 4:5 portrait composition." Recortes SI e reações RE: ver o formato indicado na peça.

## Disparo
`image_generate`, model `openrouter/openai/gpt-5.4-image-2`, count 1, as imagens de referência indicadas na peça, filename indicado, timeoutMs 300000. Dispare UMA vez; "Background task started" é sucesso; não espere, não faça polling, não escreva arquivos. HTTP 402: reporte a mensagem literal e pare.

## Resposta final (formato fixo, curta)
STATUS; TASK_ID; PARAMETROS_ENVIADOS; PROMPT_COMPLETO; ERROS; DESVIOS (honesto, ou "nenhum").
