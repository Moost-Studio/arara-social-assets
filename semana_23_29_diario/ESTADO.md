# Diário da Rara, semana 23 a 29/11: estado da produção (12/11/2026)

Roteiro aprovado: `../stories_diario_semana1_roteiro_v1.md`. Cenas geradas uma por episódio (9:16, parte superior vazia) e depois cortadas em 3 telas por código com o texto do roteiro. Teto: US$ 1 por semana somando posts e stories.

**Gerador:** a chave do OpenRouter bateu o limite (HTTP 402, exige US$ 1 de saldo), então as cenas saem pela ferramenta de imagem do OpenClaw (chave direta do Gemini), com a canônica como referência (`personagens/rara/rara_canonica_frente_v1.png` e `personagens/raro/raro_canonica_frente_v2.png`). Prompts prontos em `prompts/` (STYLE + personagem + cena + regras + NEGATIVE).

| Cena | Prompt | Arquivo de saída | Estado |
| --- | --- | --- | --- |
| seg_escritorio | prompts/seg_escritorio.md | geradas/seg_escritorio_v1.jpg | gerada 12/11, conferida por mim (cílios, pés no chão, asa sem objeto, topo livre, sem texto); aguarda composição |
| qua_call | prompts/qua_call.md | geradas/qua_call_v2.jpg | v2 mais natural gerada 12/11 (cadeira, três quartos, uma asa solta, ícone de mudo bem visível, olhos castanhos, pés na cadeira, sem texto); ressalva: a cabeça começa a cerca de 31% da altura, topo livre um pouco menor que 40%; aguarda OK do Rodrigo. (anterior v1:) | gerada 12/11, conferida por mim (rosto livre, pés pousados na mesa, asas sem objeto, topo livre, sem texto); ressalva: ícone de mudo no notebook é pequeno, vai ser reforçado por código na tela 2 |
| sex_fila | prompts/sex_fila.md | geradas/sex_fila_v1.jpg | gerada 12/11, conferida por mim (rosto livre, dois pés no chão, sacolas pousadas, asa sem objeto, sem texto); ressalva: a faixa da loja começa a cerca de 35% da altura, perto do espaço do texto; um lêmure e um outro bicho aparecem além da capivara |
| sab_raro | prompts/sab_raro.md | geradas/sab_raro_v3.jpg | v3 = v1 com só o topete corrigido (pedido do Rodrigo), conferida: topete só sob a aba, resto igual; ressalva herdada da v1: olhos azulados e sonolentos, pés visíveis e no chão. (anterior:) | v2 gerada 12/11: chapéu fechado, topete só sob a aba, olhos castanhos, asas sem objeto, topo livre, sem texto. RESSALVAS: pés escondidos atrás da mesa (não dá para confirmar pés no chão) e a cauda desce na frente das pernas da mesa; olhar ainda um pouco sonolento. Aguarda decisão do Rodrigo. (v1 REPROVADA por mim: o topete atravessa o topo do chapéu (a marca diz que só aparece sob a aba), os olhos saíram azul-claros e sonolentos (a marca pede calmo, não sonolento) e o rosto ficou diferente do canônico; regerar v2 |
| dom_resumo | prompts/dom_resumo.md | geradas/dom_resumo_v1.jpg | v1 gerada 12/11: pés amarelos visíveis sobre o tapete, cauda pousada, xícara pousada, asas cruzadas sem objeto, topo livre. RESSALVAS: os olhos saíram azul-esverdeados (o canônico é castanho) e o calendário da parede tem numerais minúsculos (o prompt proibia números). Aguarda decisão |

Depois de cada geração: copiar o arquivo para a pasta, conferir (3 cílios, rosto sem balão, pés no chão, asa sem dedos nem objeto seguro, sem texto na imagem) e atualizar esta tabela. Com as 5 aprovadas na conferência, compor as telas, montar a folha de revisão para o Rodrigo e só então preparar o agendamento.

## Custo da semana (12/11, estimativa a US$ 0,068 por imagem, sem retorno de custo da ferramenta)
Seis imagens geradas (cinco cenas mais a regeração do Raro): cerca de US$ 0,41. Se regerar o Raro v3 e o domingo v2: cerca de US$ 0,55 no total, dentro do teto de US$ 1 por semana.

## Decisões do Rodrigo (12/11, ~21h25 UTC)
- **Raro (sáb 28/11):** a v1 era a preferida; "deixe tudo igual, só ajuste o topete". Fazer edição da v1 (sab_raro_v1.jpg) mudando SÓ o topete (sem penas atravessando o topo do chapéu). A v2 fica descartada.
- **"Cena de 15/11 artificial demais":** não há cena em 15/11; assumi 25/11 (a call, Rara de asas abertas na mesa). Regerar qua_call_v2 mais natural. Confirmar com o Rodrigo. O domingo 29/11 segue com defeitos (olhos azul-esverdeados, calendário com números) e sem decisão.
