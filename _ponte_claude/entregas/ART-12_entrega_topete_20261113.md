# ART-12: topete separado da base (kit da Rara), entrega de 13/11/2026

**Entregue em `arara_social/exports_app/kit/rara/`:** `rara_base_sem_topete_{1024.png,512.webp,256.webp}` e `rara_topete_{1024.png,512.webp,256.webp}`. Quadro 1024x1024, alinhamento do K00, fundo transparente, borda suavizada.
**Pivô:** (489, 217) no quadro de 1024.
**QA:** `_qa/_qa_topete_kit.png` (base, topete, sobreposição, +8 e -8 graus, K00).

**DESVIO DO PEDIDO (aprovado pelo Rodrigo em 13/11/2026, "serve sim"):** o critério "ao pixel" NÃO foi atendido. A cabeça sem topete exigiu pintura nova (1 imagem gerada, cerca de US$ 0,07, mais 2 imagens de teste descartadas), porque a região sob o topete não existe em nenhum quadro do kit. Base + topete difere do K00 em cerca de 15,3 mil pixels com diferença acima de 2 níveis (7,2 mil acima de 40), concentrados na borda do topete e na banda do fone. O critério passou a ser visual: sem buraco com o topete girado de -8 a +8 graus.
**Limites:** a banda do fone da base não coincide ao pixel com a do K00; usar o par base + topete juntos. Nenhum arquivo existente do kit foi alterado.
**Custo:** 3 imagens (1 usada, 2 descartadas), cerca de US$ 0,21.
