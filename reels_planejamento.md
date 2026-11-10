# Planejamento de Reels da @falearara (05/11 a 20/12/2026)

Estado em 05/11/2026. Reels deixam de ser "não autorizados": o Rodrigo mandou publicar o primeiro e pediu cadência constante. Posts (12h) e stories seguem como estão. O reel vai além deles, não substitui nada.

## 1. Ponto de partida (verificado)
- Perfil: 3 seguidores, 5 publicações, alcance semanal de 4 (métricas de 02/11). Nenhum conteúdo de hoje chega a quem não segue. Reels são o único formato que o Instagram distribui para quem não segue, então é aqui que o perfil pode crescer.
- Melhor conteúdo até agora: o carrossel "Deu branco..." (30/10). O primeiro reel usa o mesmo gancho.
- Link da bio ativo (`falearara.com`), que serve a chamada "Lista de espera no link da bio".
- Lançamento do app em 15/12/2026 (go/no-go em 28/11, recuo para 12/01/2027). Até lá, sem preço e sem prometer o que o app não faz.
- Pipeline pronto: `reel_teste/` (composição em HTML e GSAP, mascote articulada, desfoque de movimento, encerramento do logo) e `publish_reel.py` (publica e valida sem publicar com `--dry-run`).

## 2. Objetivo e como medir
Meta de aprendizado, não de volume: descobrir em 6 semanas quais formatos fazem desconhecidos assistirem até o fim e clicarem no link. Com 3 seguidores não existe linha de base, então a régua é relativa.
- Métricas por reel (leitura em 48 h): visualizações, % que assiste até o fim, compartilhamentos e salvamentos, visitas ao perfil, cliques no link.
- Régua: o reel que superar o alcance do melhor post (14 views) já é sinal. Depois de 4 reels, repetir só os 2 formatos de maior retenção e cortar os outros.
- O `arara-relatorio-semanal` (segunda) deve passar a listar os reels. Proposta de alteração, não feita (é um job existente).

## 3. Cadência proposta
2 reels por semana, terça e sábado às 19h30 (Brasília), longe dos posts das 12h e dos stories. Datas comemorativas podem trocar o dia.
Produção em lote na sexta, junto das artes da semana seguinte, como já é a rotina.

## 4. Formatos (cada um vira um modelo reaproveitável)
| Formato | Duração | O que é | Custo de produção |
|---|---|---|---|
| A. Exercício | 12 a 15 s | Pergunta, 3 opções, resposta com a Arara reagindo | baixo |
| B. Situação real em N idiomas | 15 a 20 s | Uma cena de trabalho ou viagem dita em 4 idiomas, tradução em português fixa | médio (cartões de idioma já existem) |
| C. Falso amigo | 12 a 15 s | Palavra, o que parece que é, o que é de verdade | baixo |
| D. Humor da Arara | 8 a 12 s | Expressão da Arara + frase curta, sem interface | baixo |
| E. O app em 20 s | 18 a 25 s | Conversa por voz e correção, fiel à interface | médio (reaproveita as telas) |
| F. Data comemorativa | 12 a 15 s | Língua do dia, curiosidade, explicada em português | baixo |
Regra: gancho nos primeiros 2 s, cada reel com uma ideia só, mais curto que o primeiro (44 s). Quase todos devem ficar abaixo de 25 s, porque retenção cai com duração.
Todos terminam com o encerramento do logo, em versão curta (2,5 s) para não pesar nos reels de 12 s. A versão curta ainda não existe.

## 5. Calendário (19h30, Brasília)
Os temas se apoiam em posts já aprovados, mas em formato diferente.
| Data | Formato | Tema | Observação |
|---|---|---|---|
| Qui 05/11 | E/gancho | Lançamento "Deu branco?" | publicado em 05/11 e EXCLUÍDO pelo Rodrigo em 06/11 ("ficou péssimo"). Não republicar |
| Ter 10/11 | A | "Onde fica o banheiro?" (3 opções) | par do post do dia |
| Sáb 14/11 | C | Falsos amigos: actually, pretend, library, push | par do post de 13/11 |
| Ter 17/11 | B | Pedir a conta em 4 idiomas | par do post de 09/11 |
| Sáb 21/11 | F | Dia Mundial da Saudação: "olá" em 6 idiomas | data a conferir |
| Ter 24/11 | D | "Você quando acerta a frase e ninguém viu" | humor |
| Sex 27/11 | F | Black Friday em inglês: sale, discount, checkout | só vocabulário, sem venda |
| Ter 01/12 | D | Contagem regressiva: faltam 14 dias | depende do go/no-go de 28/11 |
| Sáb 05/12 | E | A conversa por voz em 20 s | |
| Ter 08/12 | B | Para quem é: trabalho, viagem, intercâmbio | |
| Sáb 12/12 | D | Conheça a tutora | tutora é feminina |
| Seg 14/12 | D | "Amanhã" | só se o lançamento mantiver 15/12 |
| Ter 15/12 | E | Lançamento | depende do go/no-go |
| Sex 18/12 | F | Dia da Língua Árabe | sem letras árabes na arte, só traços |
| 24 e 31/12 | F | Boas festas e meta de ano novo | versão laica, a confirmar |
Se o lançamento recuar para 12/01/2027, os reels de contagem e lançamento trocam por formatos A, B, C e D, e esta tabela é refeita.

## 6. Como produzir sem repetir 10 versões
O primeiro reel levou muitas rodadas porque o estilo ainda estava sendo definido. Para sustentar a cadência:
1. Fase 0 (antes de 10/11): transformar `reel_teste/index.html` em modelos por formato (A a F) e um arquivo de conteúdo por reel (textos, idioma, tempos). Entregar um reel de formato A como teste do modelo.
2. Rotina semanal: sexta, plano e copy de 2 reels para aprovar; sábado e domingo, produção; segunda, revisão; publicação agendada com `publish_reel.py`.
3. Cada reel passa por: copy aprovada, vídeo aprovado, agendamento (que só roda depois do OK). O texto de cada legenda segue o guia (gancho com emoji, 3 parágrafos curtos, uma ação, fecho padrão, 5 hashtags, sem travessão e sem dois pontos).
4. Render com desfoque de movimento leva uns 15 min para 44 s. Em 15 s deve levar uns 5 min.

## 7. Decisões do Rodrigo (05/11/2026)
- D1 cadência: aprovada (terça e sábado às 19h30). D2 regra de duração: aprovada ("pode ser").
- D3 música: autorizou usar a chave dele do OpenRouter. Funciona: `reel_teste/musica/gen_music.py` (Lyria 3 Pro via chat/completions com áudio). O modelo ignora a duração pedida e entrega 54 a 70 s, então a trilha é cortada e mixada com `reel_teste/add_music.py` (música sob os efeitos, -16 LUFS). Se a chave falhar, ele gera outra.
- D4 etiqueta de IA no Instagram: NÃO marcar.

## 8. Pendências (ainda abertas)
- D1. Cadência: 2 por semana, terça e sábado às 19h30. Confirma?
- D2. Duração: a regra "quase todos abaixo de 25 s" muda o formato do primeiro reel (44 s). Confirma?
- D3. Música. Sem música hoje: a geração do OpenClaw dá erro 401, e só uso a sua chave do OpenRouter com OK. Áudios em alta no Instagram só podem ser aplicados dentro do app, não por API; reels publicados por aqui levam o áudio do próprio arquivo. Escolher: continuar só com efeitos, gerar trilha original ou postar no app quando quiser áudio em alta.
- D4. Etiqueta de conteúdo feito com IA: a mascote e as cenas foram geradas com IA. O Instagram permite marcar. Decidir se marcamos.
- D5. Versão curta do encerramento do logo (2,5 s) para reels curtos.
- D6. O job `arara-plano-semanal` (quinta 10h) passar a incluir reels no plano. Não alterei.
- D7. Resolução da mascote (540x965 ampliada): vale gerar o kit em alta resolução antes do lançamento.

## 9. Produção imediata solicitada em 05/11/2026

Rodrigo pediu "gere todos os videos programados agora". Produção em andamento
de 13 peças novas: seis de novembro (10 a 27/11) e sete rascunhos de dezembro
(01 a 18/12). O teaser de 05/11 já existe e não é substituído por este lote.

Contagem de 14 dias, véspera e lançamento são arquivos condicionais à confirmação
de 15/12/2026. Criar o rascunho não decide o go/no-go de 28/11 nem autoriza a publicação.
As sugestões de 24 e 31/12 continuam fora do lote, pois não têm programação confirmada.

Fontes editáveis e operação: `reel_teste/README.md`. Entregas e validação incremental:
`../reports/arara_reels_novembro/` e `../reports/arara_reels_dezembro/`.
Todos os novos vídeos seguem pendentes de aprovação final; nenhum job foi criado
ou alterado por esta produção.

## 10. Atualização de 06/11/2026
- O reel de lançamento (v11) foi publicado em 05/11 às 19h30 e o Rodrigo o excluiu em 06/11, por considerá-lo ruim. O perfil está sem reels. A entrada `lancamento` em `reels.json` não deve ser publicada de novo.
- Não há nenhum job de reel agendado. O lote de novembro e dezembro (13 vídeos no visual antigo) está reprovado e parado.
- Os reels só voltam com o método novo: arara antiga com atuação, cenário em profundidade, encerramento C e som desenhado. Nada é agendado antes de um teste aprovado pelo Rodrigo.
- A cadência de terça e sábado fica suspensa até lá.
