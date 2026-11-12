# Diário da Rara, semana 23 a 29/11: estado da produção (12/11/2026)

Roteiro aprovado: `../stories_diario_semana1_roteiro_v1.md`. Cenas geradas uma por episódio (9:16, parte superior vazia) e depois cortadas em 3 telas por código com o texto do roteiro. Teto: US$ 1 por semana somando posts e stories.

**Gerador:** a chave do OpenRouter bateu o limite (HTTP 402, exige US$ 1 de saldo), então as cenas saem pela ferramenta de imagem do OpenClaw (chave direta do Gemini), com a canônica como referência (`personagens/rara/rara_canonica_frente_v1.png` e `personagens/raro/raro_canonica_frente_v2.png`). Prompts prontos em `prompts/` (STYLE + personagem + cena + regras + NEGATIVE).

| Cena | Prompt | Arquivo de saída | Estado |
| --- | --- | --- | --- |
| seg_escritorio | prompts/seg_escritorio.md | geradas/seg_escritorio_v1.jpg | gerada 12/11, conferida por mim (cílios, pés no chão, asa sem objeto, topo livre, sem texto); aguarda composição |
| qua_call | prompts/qua_call.md | geradas/qua_call_v2.jpg | v2 mais natural gerada 12/11 (cadeira, três quartos, uma asa solta, ícone de mudo bem visível, olhos castanhos, pés na cadeira, sem texto); ressalva: a cabeça começa a cerca de 31% da altura, topo livre um pouco menor que 40%; aguarda OK do Rodrigo. (anterior v1:) | gerada 12/11, conferida por mim (rosto livre, pés pousados na mesa, asas sem objeto, topo livre, sem texto); ressalva: ícone de mudo no notebook é pequeno, vai ser reforçado por código na tela 2 |
| sex_fila | prompts/sex_fila.md | geradas/sex_fila_v1.jpg | gerada 12/11, conferida por mim (rosto livre, dois pés no chão, sacolas pousadas, asa sem objeto, sem texto); ressalva: a faixa da loja começa a cerca de 35% da altura, perto do espaço do texto; um lêmure e um outro bicho aparecem além da capivara |
| sab_raro | prompts/sab_raro.md | geradas/sab_raro_v3.jpg | v3 = v1 com só o topete corrigido (pedido do Rodrigo), conferida: topete só sob a aba, resto igual; ressalva herdada da v1: olhos azulados e sonolentos, pés visíveis e no chão. (anterior:) | v2 gerada 12/11: chapéu fechado, topete só sob a aba, olhos castanhos, asas sem objeto, topo livre, sem texto. RESSALVAS: pés escondidos atrás da mesa (não dá para confirmar pés no chão) e a cauda desce na frente das pernas da mesa; olhar ainda um pouco sonolento. Aguarda decisão do Rodrigo. (v1 REPROVADA por mim: o topete atravessa o topo do chapéu (a marca diz que só aparece sob a aba), os olhos saíram azul-claros e sonolentos (a marca pede calmo, não sonolento) e o rosto ficou diferente do canônico; regerar v2 |
| dom_resumo | prompts/dom_resumo.md | geradas/dom_resumo_v2.jpg | v2 = v1 com olhos castanhos e calendário sem números (edição pontual), conferida; pronta para compor. (anterior v1:) | v1 gerada 12/11: pés amarelos visíveis sobre o tapete, cauda pousada, xícara pousada, asas cruzadas sem objeto, topo livre. RESSALVAS: os olhos saíram azul-esverdeados (o canônico é castanho) e o calendário da parede tem numerais minúsculos (o prompt proibia números). Aguarda decisão |

Depois de cada geração: copiar o arquivo para a pasta, conferir (3 cílios, rosto sem balão, pés no chão, asa sem dedos nem objeto seguro, sem texto na imagem) e atualizar esta tabela. Com as 5 aprovadas na conferência, compor as telas, montar a folha de revisão para o Rodrigo e só então preparar o agendamento.

## Custo da semana (12/11, estimativa a US$ 0,068 por imagem, sem retorno de custo da ferramenta)
Seis imagens geradas (cinco cenas mais a regeração do Raro): cerca de US$ 0,41. Se regerar o Raro v3 e o domingo v2: cerca de US$ 0,55 no total, dentro do teto de US$ 1 por semana.

## Decisões do Rodrigo (12/11, ~21h25 UTC)
- **Raro (sáb 28/11):** a v1 era a preferida; "deixe tudo igual, só ajuste o topete". Fazer edição da v1 (sab_raro_v1.jpg) mudando SÓ o topete (sem penas atravessando o topo do chapéu). A v2 fica descartada.
- **"Cena de 15/11 artificial demais":** não há cena em 15/11; assumi 25/11 (a call, Rara de asas abertas na mesa). Regerar qua_call_v2 mais natural. Confirmar com o Rodrigo. O domingo 29/11 segue com defeitos (olhos azul-esverdeados, calendário com números) e sem decisão.

## Telas compostas (12/11, ~21h50 UTC)
15 telas 1080x1920 em `telas/{seg,qua,sex,sab,dom}_{1,2,3}.png`, geradas por `compor_telas.py` (HTML em `semana1/_scripts/diario_*.html`). Selo no topo ("DIÁRIO DA RARA" ou "HISTÓRIA DO RARO"), título na tela 1, balão com a fala aprovada sempre acima da cabeça (medido: pelo menos 117 px livres entre o balão e o topo do personagem), texto mínimo de 40 px. Limite: as 3 telas de cada episódio usam a MESMA cena (só uma imagem por episódio foi gerada); o que muda é o texto. Aguardam o OK do Rodrigo; nada agendado.
Atenção no texto aprovado: a tela 3 de segunda diz "amanhã eu conto por que ninguém chegou", mas terça 24/11 é modo carente, sem episódio; promessa sem entrega. Sugestão: "e até agora ninguém chegou".

## Retorno do Rodrigo (12/11, ~21h59 UTC): "as imagens estão boas, mas estão iguais em todos do carrossel; têm que ser diferentes e concordar com o texto"
Cada tela precisa de UMA IMAGEM PRÓPRIA que ilustre a fala. Já existem as 5 cenas da tela 1. Faltam 10 (duas por episódio), custo cerca de US$ 0,68 (US$ 0,068 por imagem). A semana já está em cerca de US$ 0,62 de stories, então o total dos stories iria a cerca de US$ 1,30, acima do teto de US$ 1 por semana (sem contar os posts da semana 23 a 29, que pedem mais US$ 0,30 a 0,45). **Parar e pedir aumento do teto antes de gerar.**

| Tela | Fala | Cena a gerar (edição da cena do episódio, mesmo personagem e cenário) |
| --- | --- | --- |
| seg 2 | ensaiei o japonês do trabalho em voz alta | Rara em reverência educada diante de uma cadeira vazia, crachá pendurado |
| seg 3 | só tem um detalhe / e até agora ninguém chegou | Rara olhando um relógio de parede sem números, cabeça inclinada, intrigada |
| qua 2 | falei por dez minutos / o microfone estava no mudo | Rara falando de forma intensa de perfil, os bichinhos da tela com cara de confusos, ícone de mudo grande |
| qua 3 | errou? treinou / agora eu confiro antes de falar | Rara determinada, a ponta da asa encostando no botão do microfone do notebook |
| sex 2 | aprendi duas palavras na fila | Rara na fila erguendo duas penas como se contasse "dois", olhar de quem aprendeu algo |
| sex 3 | no fim saí com um suporte de microfone | Rara saindo da loja, satisfeita, um suporte de microfone encostado ao lado e uma sacola pousada |
| sab 2 | vem do hebraico... grego e latim | Raro com a ponta da asa apontando uma linha do dicionário aberto, sobrancelha levantada |
| sab 3 | por isso sábado combina com rede | Raro deitado na rede, chapéu sobre os olhos, caneca por perto |
| dom 2 | errei na call, na fila e na hora de chegar | Rara no tapete, diante de três quadrinhos na parede (fone no mudo, sacolas, relógio) sem texto |
| dom 3 | e tudo bem, errou? treinou / segunda tem mais | Rara sorrindo para a câmera, de manta, com o nascer do sol pela janela |

## Decisão do Rodrigo (12/11, 23h52 UTC): "pode gerar as imagens e sobe o teto por essa semana"
Opção 1: gerar as 10 cenas extras, uma por vez, como EDIÇÃO da cena do episódio (mesmo personagem e cenário, só pose e enquadramento). Teto desta semana (23 a 29/11 de conteúdo, produzido em 12/11) subiu de US$ 1 para US$ 2 (valor que propus e ele aceitou sem corrigir); só vale para esta semana. Frase de segunda tela 3: trocar por "e até agora ninguém chegou" (recomendação; ele não objetou, confirmar no envio da folha).
Fila: seg2, seg3, qua2, qua3, sex2, sex3, sab2, sab3, dom2, dom3 (tabela acima). Depois de cada geração: copiar para `geradas/<ep>_<n>.jpg`, conferir (cílios, olhos castanhos, pés no chão, asa sem objeto, topo livre, sem texto), anotar aqui. Ao fim: atualizar `compor_telas.py` para usar uma imagem por tela e refazer a folha.
