# ART-12, teste da opção 1 (13/11/2026): cabeça sem topete gerada, derivação NÃO entregue

**Feito:** 1 imagem (edição do K00 sobre cinza, `exports_app/_teste_topete/rara_sem_topete_gerada.jpg`, cerca de US$ 0,07). Fora da máscara do topete, só 0,5% dos pixels mudaram (>40 de diferença), então o alinhamento ao K00 é bom e a cabeça nova (cúpula azul lisa, fone inteiro) é visualmente boa.

**Derivação por código (2 tentativas, `_qa/_qa_topete_teste.png`): REPROVADA.**
- Diferença contra o K00 depois de base + topete: milhares de pixels com diff > 40 (a meta do Claude Code era ao pixel, máximo 2 níveis). A banda do fone gerada não coincide com a do K00, então aparece costura onde o topete "solta".
- A base tem um trecho cinza (fundo vazado) sob a banda do fone, porque o recorte tratou o interior da cabeça como fundo.
- O topete extraído por diferença leva fragmentos da banda do fone; extraído por cor, fica com buracos onde cobria a cabeça.
- Com o topete girado ±8° o buraco e a costura aparecem.

**Arquivos de teste (não copiados para `kit/rara/`):** `_teste_topete/rara_base_sem_topete_1024.png`, `rara_topete_1024.png`.

**Caminhos reais (decisão do Rodrigo):**
A. Mais uma passada: gerar o topete isolado (mais uma imagem, cerca de US$ 0,07) e montar a base só no topo, com máscara à mão para a banda do fone. Não garante o critério "ao pixel"; o critério visual (sem buraco a ±8°) é viável.
B. Relaxar o critério para o Claude Code: topete por cima com pivô e sem exigir identidade ao pixel do K00.
C. Ficar como está (topete animado só nas expressões K06).

## Atualização, opção A (13/11/2026, ~00h35 UTC)
- O topete isolado gerado (`_teste_topete/rara_topete_isolado_gerado.jpg`) NÃO serve: saiu em outra posição, maior, com um "saiote" de penas inventado. Descartado (1 imagem, cerca de US$ 0,07).
- Terceira derivação por código, usando o topete do próprio K00 (recorte por cor com fechamento morfológico) e a cabeça gerada como base, com o vão entre o fone e a cabeça preenchido no azul da cabeça. Folha `_qa/_qa_topete_teste.png`.
- Medido contra o K00: base + topete difere em cerca de 12,9 mil pixels com diff > 2 e 6,1 mil com diff > 40 (de 1.048.576). O critério "ao pixel" NÃO é atendido; o visual (sem buraco, topete girado ±8°) fica aceitável, com um fio escuro de banda do fone no alto do topete.
- Arquivos em `_teste_topete/` (`rara_base_sem_topete_1024.png`, `rara_topete_1024.png`), pivô provisório (467, 231) no quadro de 1024. NÃO copiados para `kit/rara/` até o OK visual do Rodrigo e a decisão de relaxar o critério com o Claude Code.
