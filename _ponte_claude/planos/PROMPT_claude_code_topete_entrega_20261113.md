Resposta à sua tarefa "duas peças do kit da Rara para o site (E1/M3)". Faça `git pull` em `Moost-Studio/arara-identidade` (commit `49a353b`; cópia em `Moost-Studio/arara-social`, commit `c3ecce0`).

Entregue em `arara_social/exports_app/kit/rara/`:
- `rara_base_sem_topete_1024.png`, `rara_base_sem_topete_512.webp`, `rara_base_sem_topete_256.webp`
- `rara_topete_1024.png`, `rara_topete_512.webp`, `rara_topete_256.webp`
Mesmo quadro de 1024x1024 e mesmo alinhamento do K00, fundo transparente, borda suavizada. WebP com qualidade 90 e alfa. Nenhum arquivo existente foi alterado.

Pivô do giro do topete: x = 489, y = 217 (px no quadro de 1024), onde ele encosta na cabeça. Para os WebP de 512 e 256, escale o pivô pelo mesmo fator (244,5 / 108,5 e 122,25 / 54,25).

QA: `arara_social/exports_app/_qa/_qa_topete_kit.png` (fundo magenta, com base, topete, sobreposição, topete a +8 e a -8 graus, e o K00 original).

DESVIO DO SEU CRITÉRIO DE ACEITE (aprovado pelo Rodrigo em 13/11/2026): base + topete NÃO é igual ao K00 ao pixel. Você mandou parar se a cabeça sem topete exigisse pintura nova, e exigiu: a região sob o topete não existe em nenhum quadro do kit. Gerei a cabeça sem topete como edição do K00 (uma imagem) e usei o topete do próprio K00, recortado por cor. Medido: base + topete difere do K00 em cerca de 15,3 mil pixels com diferença acima de 2 níveis (7,2 mil acima de 40) de 1.048.576, concentrados na borda do topete e na banda do fone. O critério passou a ser visual: sem buraco na cabeça com o topete girado de -8 a +8 graus, conferido na folha de QA.

Limites que você precisa respeitar no código:
- A banda do fone da base foi pintada pela geração e não coincide ao pixel com a do K00. Use o par base + topete juntos. Não misture a base nova com o K00 original nem com os remendos de olhos e bico sem conferir a costura.
- O topete é o do K00 (topete caído sobre a testa). Os remendos K06, K07 e K08 trazem topetes diferentes. Nas expressões com remendo de topete, mantenha o comportamento atual (o remendo substitui o topete), e só use a camada nova nas demais.
- Se aparecer costura ou borda azul-clara visível na animação, descreva a expressão e a rotação em que aconteceu e peça ajuste ao agente de arte. Não retoque a arte.

Mudança de copy que afeta o site, de 13/11/2026: o bordão "Errou? Treinou" foi aposentado. O bordão novo é "Bora de novo?". Use-o em qualquer texto do site que cite o bordão antigo. O prompt do site (`PROMPT_claude_code_site_identidade_20261112.md`) já foi atualizado com isso.

Regras de sempre: sem emoji, `lucide-react`, sem `translateY` novo, sem merge e sem deploy. No final devolva o que foi trocado, os testes que rodou de verdade e o que ficou pendente.
