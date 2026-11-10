LOTE: 11 (restante D01 a D04, W01 a W04)   VERSÃO: relatório 2 (após 2 rodadas de correção)
RESUMO: 6 de 8 peças aprovadas pela revisão independente. D02 e W03 repetiram a mesma falha depois de 2 correções: PARADO pela condição da 10.2.

PEÇAS (versão final, arquivo)
| peça | arquivo | revisão independente | pendências |
| D01 | datas/D01_carnaval_v2.png | APROVADA | menores: fresta branca de 10 px na axila, leve borrão azul ao lado do pé direito |
| D02 | datas/D02_festa_junina_v3.png | CORRIGIR (2ª vez) | fita verde translúcida sob a aba esquerda, ponta da fita amarela com fade esverdeado, franja da aba com lacunas translúcidas |
| D03 | datas/D03_fim_de_ano_v3.png | APROVADA | menores: ponta da haste parece colada, cauda um pouco curta |
| D04 | datas/D04_volta_as_aulas_v1.png | APROVADA | menores: lápis não pedido, um pé no vazio |
| W01 | widget/W01_comemorando_v1.png | APROVADA | confete entra no recorte |
| W02 | widget/W02_acenando_v1.png | APROVADA | nenhuma |
| W03 | widget/W03_carente_v3.png (melhor opção até aqui: v1 tem as 2 linhas sob os olhos e v3 tem o topete murcho) | CORRIGIR (2ª vez) | v3 ficou com 1 faixa navy opaca sob cada olho (canônica: 2); tufo lateral sai de trás da concha do fone; fundo #7D7C7D |
| W04 | widget/W04_dormindo_v1.png | APROVADA | cobertor toca as bordas, recorte com máscara manual |

MEDIÇÕES: medicoes.json (v1), medicoes_v2.json, medicoes_v3.json. Margens finais (esq/topo/dir/base): D01 v2 101/45/106/72; D02 v3 355/108/348/127; D03 v3 275/170/443/170; W03 v3 238/112/182/0 (close de busto, corte embaixo esperado). Fundo real entre #7D7C7D e #8A8888, não #8C8C8C chapado.
CUSTO: 15 gerações (8 v1, 4 v2, 3 v3), gpt-5.4-image-2, estimativa US$ 0,02 cada, cerca de US$ 0,30 no lote (teto US$ 1,00; diário US$ 3,00). Custo real não verificável (a ferramenta não devolve; OpenRouter 'Usage unavailable'). Nenhuma falha por saldo.
DÚVIDAS: como tratar D02 e W03 (opções abaixo).
RISCOS: comparação por inspeção visual, sem embedding; custo estimado.
REVISÃO INDEPENDENTE: 3 rodadas de revisão (v1, v2, v3) por subagente em contexto limpo; veredito final 6 APROVADA, 2 CORRIGIR, 0 REPROVADA.
STATUS: PARADO (condição 10.2: a mesma falha apareceu 2 vezes na mesma peça depois das correções, em D02 e em W03).

CAUSA E MUDANÇA DE ABORDAGEM PROPOSTA (10.5)
- Causa: o modelo de imagem refaz a peça inteira a cada edição e troca um defeito por outro (W03: corrigiu cílio e topete e perdeu uma linha sob os olhos; D02: não removeu os resíduos de fita).
- D02: limpar por código (sem custo): repintar com o fundo a região da fita verde e da ponta esverdeada e opacificar a franja da aba por máscara. Vira D02 v4, com nova revisão.
- W03: uma geração nova do zero, a partir da canônica, com o prompt completo de carência e a ordem explícita 'exactly two thin dark curved lines under each eye' (custo estimado US$ 0,02 a US$ 0,06), ou aceitar a v1 (2 linhas corretas, topete não murcho) com o topete tratado depois. Recomendo a geração nova.

ATUALIZAÇÃO 09/11/2026 ~02h25 UTC (após o 'ok' do Rodrigo)
- D02 v4 (por código, sem custo): arquivo personagens/rara/datas/D02_festa_junina_v4.png. Revisão: CORRIGIR leve. Resolvido: fita verde, folha solta e fade verde. Pendente: ponta da fita amarela mole e irregular com 2 manchas laranja minúsculas, e resíduo oliva de 12 px em (444-448, 328-330). Correção possível por código, sem custo.
- W03 v4 (geração nova do zero, US$ 0,02 estimados): arquivo personagens/rara/widget/W03_carente_v4.png. Revisão: CORRIGIR. Resolvido: 2 linhas sob cada olho e 3 cílios por olho. Pendente: topete com tufo lateral e volume (5.6 pede murcho); lágrimas em formato de haltere; fundo #7F7E7E.
- Custo total do lote 11: 16 gerações, cerca de US$ 0,32 estimados (teto US$ 1,00).
- STATUS: PARADO de novo (10.2: falha repetida). Opções: (a) aceitar D02 v4 e W03 v4 como 'aprovada com ressalva' e seguir a fila; (b) mais uma correção por código na D02 e uma nova geração da W03 com foco só no topete.
