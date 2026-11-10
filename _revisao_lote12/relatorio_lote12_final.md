# Relatório de revisão independente — Lote 12 (versão final)

Revisor: subagente de contexto limpo (não gerou nem corrigiu nada).
Data: 2026-11-09. Pasta das peças: `arara_social/stories_lote12/`. Referência: `personagens/rara/rara_canonica_frente_v1.png` (1254x1254). Regras: `rara_sistema_de_marca_v6.md` (10.3 e tabela 7.15).

## Método e limites (leia antes)

- Todas as 11 peças atuais e as 5 versões antigas foram abertas com view_image. Medi com Python+Pillow rodando de /tmp (sem -I): tamanho/razão, bbox por diferença de fundo (peças de fundo liso), amostras de cor, perfil de luminância sob os pés e sob a cauda, halo no recorte, cantos (marca d'água).
- Nas cenas complexas (M08 a M12) o bbox por cor não é confiável (fundo azul/roxo/madeira). Nelas os valores marcados com "~" são estimados sobre a imagem exibida (escala 941/675, erro de uns 10 px).
- LIMITE HONESTO: o view_image só abre arquivos dentro de pastas permitidas, e eu só podia criar o relatório. Fiz recortes ampliados em /tmp/rev12/ (fora do projeto, para tentar zoom), mas o view_image recusou o caminho. Resultado: rosto, cílios e linhas sob os olhos foram conferidos na imagem inteira (cerca de 675x1200 de exibição), não em zoom. A contagem exata de 3 cílios por olho é "visualmente consistente", não provada em ampliação. Os recortes em /tmp/rev12/ ficaram lá (scratch, nada no projeto foi tocado).
- Observação sobre o checklist: o item 6 diz "microfone coral". No canônico o microfone é Azul-Noite escuro (medido: 0 px coral na ponta do microfone; o coral está no aro das conchas do fone: 508 px coral na concha esquerda). Todas as peças seguem o canônico (microfone escuro), exceto MA03_v2, onde a ponta do microfone tem coral medido (156 px). Registrado abaixo.

## (a) Tabela-resumo

| ID | Formato | Veredito | Principal motivo |
|---|---|---|---|
| RP06_v1 | 1254x1254, razão 1,000 (OK 1:1) | APROVADA COM RESSALVAS | Base do meio corpo esfumada por ~95 px (não é corte limpo); fundo #888786 (levemente abaixo de #8C8C8C); asa-mão com "dedos" de pena |
| MA01_v2 | 941x1672, razão 0,5628 (OK) | APROVADA COM RESSALVAS | Ponta da cauda a 31 px da borda esquerda; asa que segura o microfone é uma mão/luva de pelúcia; piso com contraste muito baixo (ΔRGB 31); pernas visíveis (curtas) |
| MA02_v3 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Crista começa em 28,6% do alto (invade o terço de cima em ~79 px); cauda vista só de lado, curta e meio escondida |
| MA03_v2 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Ponta da cauda a 44 px da base (2,6%), dentro da zona de UI do story; asas-mão em luva ao segurar prancheta e lápis; ponta do microfone coral (diverge do canônico escuro) |
| MA04_v1 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Piso quase igual ao fundo (ΔRGB 11; só há horizonte leve + reflexo e sombra); crista a 33,7% (7 px de folga no limite do terço); asas formam o coração (pedido) |
| M07_v1 | 941x1672, 0,5628 (OK) | APROVADA | Pendurada pelas asas na borda do topo (pedido), cauda pendente inteira, rosto legível; sem texto |
| M08_v1 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Rara pequena (~32% do alto); lua no terço de cima; vários adereços de cena (arbustos com flores, pedras, vaga-lumes, capim); cauda a ~35 px da borda esquerda |
| M09_v1 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Rara só da cintura para cima (mesa) e pequena; asas-mão ao segurar a pena; mesa e lâmpada cortadas/coladas nas bordas; muitos papéis amassados e cadeira como adereços |
| M10_v1 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Espeto do guarda-chuva em ~32,4% (15 px dentro do terço de cima); haste do guarda-chuva corre colada ao rosto/boom do microfone; asas-mão no celular e no cabo; cauda diagonal na calçada |
| M11_v1 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Só um pé visível; cabeça de lado com o rosto parcialmente na sombra; abajur com carinha e almofada com estrela são adereços não pedidos |
| M12_v2 | 941x1672, 0,5628 (OK) | APROVADA COM RESSALVAS | Crista a 27,8% (dentro do terço de cima); pedido era "só metade do rosto visível" e o rosto aparece inteiro; porta/batente/rodapé/maçaneta como adereços |

Nenhuma peça recebeu CORRIGIR: nenhuma tem os defeitos que reprovaram BS02 e M12_v1 (flutuação, pernas de pernilongo, formato errado, Rara minúscula). Mas há ressalvas reais, listadas em (c).

## (b) Checklist por peça

Legenda: OK / FALHA / N-A. "Ressalva" = passa mas com ponto a registrar.

### RP06_v1 (repost, 1:1, meio corpo sobre cinza)
1. Formato: OK. 1254x1254, razão 1,000 (1:1). Mesmo tamanho do canônico.
2. Pés: N-A (meio corpo, recorte para o canto da tela).
3. Pernas: N-A.
4. Asas: OK com ressalva. As duas visíveis. A asa que aponta para cima à esquerda é longa, plausível, sem garras; termina em "dedos" de pena arredondados com uma pena-indicador esticada (leitura de mão, mas com textura de pena, não é luva lisa). A asa da frente, à direita, também tem uma pena apontando para o peito.
5. Cauda: N-A (meio corpo).
6. Rosto: OK. Cada olho com 3 cílios curvos e 2 linhas curvas finas sob o olho, rubor, faixa de penas escuras no pescoço, bico escuro com gancho (aberto, com língua rosa, sorriso aberto), fone escuro com aro coral nas conchas, microfone escuro como no canônico. Legível.
7. Composição: OK. bbox x 60 a 1121, y 107 a 1195. Folgas L 60 px, T 107 px, R 132 px, B 58 px. Rara ocupa 86,8% do alto. Ponta da asa a 60 px da borda esquerda (aperta, mas não corta). Ressalva: o terço de cima não vale para RP (é recorte).
8. Limpeza: OK com ressalva. Sem texto, letras ou logos. Halo: 0 px claros no anel externo (luminância média do anel 133,6 contra fundo 134,4; máximo 156): sem halo claro. Ressalva: a base do corpo não é cortada reta, é esfumada. A cor amarela cai de #FEC902 (y~1100) para fundo cinza entre y 1100 e y 1195 (~95 px de degradê). Em recorte sobre o cinza isso vira semitransparência suja se alguém remover o fundo.
9. Fundo e cena: OK. Pedido "apontando para cima à esquerda com sorriso largo": cumpre. Fundo cinza chapado, medido #888786 (canto superior esquerdo #8A8988), contra #8C8C8C da regra (diferença de 3 a 5 níveis por canal; variação interna de ±3). Não é problema prático, só registro.

### MA01_v2 (Chamada, fundo amarelo, microfone vintage)
1. Formato: OK. 941x1672, razão 0,5628 (9:16 = 0,5625; diferença de 0,0003).
2. Pés: OK. Os dois apoiados no piso, que é um tom mais escuro de amarelo (#F8C121) que a parede (#FCCE2C): contraste real mas baixo (soma de ΔRGB 31; degrau de luminância 167 para 157 no horizonte, y~1310 px). Sombra de contato medida sob os pés: -43 de luminância no contato, -16 aos 6 px, -12 aos 14 px, -8 aos 40 px. Sem flutuação.
3. Pernas: OK com ressalva leve. Curtas, mas as duas pernas amarelas finas aparecem por baixo da barriga (~45 px na imagem exibida). Muito mais curtas que MA02_v2 (reprovada), mas não "quase escondidas" como no canônico.
4. Asas: OK com ressalva. A asa direita da Rara (esquerda na imagem) segura o microfone e vira uma mão: 4 lóbulos azuis empilhados em volta do cabo, textura de pena muito suave. Não tem garra e é plausível para o gesto, mas é a leitura "luva". A outra asa fica dobrada junto ao corpo.
5. Cauda: OK com ressalva. Longa, em degradê azul a verde, inteira, pousada no piso e saindo para a esquerda. Folga da ponta até a borda esquerda: 31 px (3,3% da largura). Apertada, não cortada.
6. Rosto: OK. 3 cílios no olho visível de cada lado, 2 linhas sob cada olho, rubor, faixa escura no pescoço, bico escuro com gancho, fone escuro com aro coral, microfone escuro. Legível.
7. Composição: OK. Crista em y=570 (34,1%), logo abaixo do terço de cima. O microfone começa em ~43%. Folgas: L 31 (cauda), R 236, B 187. Rara com microfone ocupa 54,7% do alto. Pedido "personagem na metade de baixo": ela ocupa de 34% a 89%, centro em ~62%, aceitável.
8. Limpeza: OK. Sem texto, letras ou logos. A grade do microfone não forma glifos. Canto inferior direito sem marca d'água (desvio-padrão 0,86, igual ao vizinho). Adereços não pedidos: nenhum.
9. Fundo e cena: OK. Amarelo liso com piso em degradê leve, como no pedido. Microfone vintage grande estendido para o espectador, sorriso animado (bico quase fechado, sorriso pequeno). Espaço livre acima para a caixinha de texto.

### MA02_v3 (Ouvindo, fundo azul-noite, olhos fechados)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK. Dois pés no piso azul (#4577CC), bem diferente do fundo (#101F46, ΔRGB 275). Sombra de contato medida: coluna sob o pé esquerdo 43, 31, 15 contra 62 a 66 do piso de referência nos mesmos y. Contato claro, sem flutuação.
3. Pernas: OK. Curtas, quase só os pés aparecem sob a barriga.
4. Asas: OK. A asa que fica à esquerda da imagem sobe e a ponta encosta na concha do fone, como pedido; sem garra, sem luva (a ponta é de pena). A outra asa fica dobrada ao lado do corpo.
5. Cauda: OK com ressalva. A cauda aparece só pelo lado direito, atrás da asa e das pernas, com degradê azul a verde, pousada no piso. Parte dela fica escondida atrás do corpo; o comprimento visível (~265 px) é menor que o canônico proporcional (~365 px). Não é toco, mas é curta. Folga da ponta: 206 px à direita, 322 px até a base.
6. Rosto: OK. Olhos fechados mantendo cílios e as 2 linhas curvas sob cada olho; rubor; faixa escura no pescoço; bico escuro com gancho; fone escuro com aro coral; microfone escuro. Legível.
7. Composição: FALHA parcial. Crista em y=478 (28,6%): invade o terço de cima em ~79 px (4,7 pontos percentuais). Só a crista e o topo do fone, mas o critério pede terço livre. Folgas L 234, R 206, B 322. Rara ocupa 52,1% do alto (não minúscula).
8. Limpeza: OK. Sem texto/logos (a forma de onda é feita na edição). Sem adereços.
9. Fundo e cena: OK. Azul-noite com piso azul mais claro, olhos fechados, ouvindo atenta, uma asa na concha. Cumpre o pedido.

### MA03_v2 (Corrigindo, fundo verde-menta)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK. Dois pés no piso (#C1ECD3 contra fundo #A5DDB5, ΔRGB 39) com sombra de contato forte (luminância 92 no contato contra 216 de referência; -67 aos 6 px, -58 aos 14 px, -40 aos 40 px). Sem flutuação.
3. Pernas: OK. Curtas, quase escondidas.
4. Asas: OK com ressalva. As duas visíveis: uma segura a prancheta, a outra o lápis. Ambas são mãos de pelúcia com lóbulos de pena (leitura de luva suave, mas sem garra). A prancheta e o lápis são claramente reconhecíveis.
5. Cauda: OK com ressalva. Longa, degradê azul a verde, inteira, pendendo para baixo na frente do piso. A ponta fica a 44 px da base (2,6%): folga muito apertada e dentro da zona de UI inferior do story (botão de resposta). Há sombra suave ao lado da cauda (luminância de 217 caindo para 145 a 183 junto dela).
6. Rosto: OK. Um olho aberto com 3 cílios e um olho piscando com cílios e 2 linhas mantidas; rubor; faixa escura; bico escuro com gancho; fone escuro com aro coral. A ponta do microfone está coral (156 px medidos), enquanto o canônico tem microfone escuro. Se o checklist do projeto realmente quer microfone coral, passa; contra o canônico medido, é um desvio pequeno. Registro como ressalva baixa.
7. Composição: OK. Crista em y=613 (36,7%). Folgas L 237, R 240, B 44 (cauda). Rara ocupa 60,6% do alto.
8. Limpeza: OK. A prancheta está em branco (sem texto, números ou rabiscos legíveis), o lápis é liso. Sem outros adereços.
9. Fundo e cena: OK. Verde-menta liso com piso mais claro; segura prancheta e lápis e dá piscadinha; abre espaço acima para a correção com trocadilho.

### MA04_v1 (Agradecendo, fundo rosa, coração com as asas)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK com ressalva. Dois pés apoiados, com sombra de contato forte (luminância 59 no contato contra 201 de referência; -73 aos 6 px; -49 aos 14 px) e reflexo alaranjado abaixo. Mas o piso é quase da mesma cor do fundo: fundo #FDADB9, piso #FDB7C1 (ΔRGB 11; só 6 níveis de luminância). A superfície aparece por horizonte leve, reflexo e sombra, não por cor diferente. Não está flutuando, mas não cumpre com folga o "superfície de cor diferente do fundo".
3. Pernas: OK. Curtas, pouco visíveis.
4. Asas: OK. As duas se unem formando um coração, como pedido (o coração amarelo da barriga aparece no vão). Sem garras; pontas com textura de pena.
5. Cauda: OK. Longa, degradê azul a verde, inteira, pousada no piso e saindo para a esquerda. Folga da ponta: 97 px à esquerda.
6. Rosto: OK. 3 cílios por olho, 2 linhas sob cada olho, rubor, faixa escura, bico escuro com gancho e sorriso, fone escuro com aro coral, microfone escuro. Legível.
7. Composição: OK no limite. Crista em y=564 (33,7%): só 7 px abaixo do limite de 33,3%. Folgas L 97 (cauda), R 250, B 186 (pés; o reflexo vai até 107 px da base). Rara ocupa ~59% do alto contando o reflexo.
8. Limpeza: OK. Sem texto/logos. Sem adereços.
9. Fundo e cena: OK. Rosa liso em degradê, sorriso caloroso, coração com as duas asas.

### M07_v1 (pendurada na borda do topo, fundo rosa)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: N-A com lógica. Ela está pendurada pelas asas; os pés ficam soltos (esperado). Não é flutuação: o apoio está nas asas, que agarram a borda.
3. Pernas: OK. Curtas, só os pés aparecem sob a barriga.
4. Asas: OK com ressalva. As duas esticadas para cima, agarrando a faixa rosa mais clara que forma a borda do topo (y 0 a ~63 px) com pontas fechadas em lóbulos de pena (leitura de mão fechada). Sem garras. Anatomia plausível para o gesto.
5. Cauda: OK. Longa, degradê azul a verde, inteira, pendendo na vertical por gravidade, ponta livre a ~1144 px (527 px da base). Pendurada com lógica.
6. Rosto: OK. 3 cílios por olho, 2 linhas sob cada olho, rubor, faixa escura, bico escuro com gancho (aberto), fone escuro com aro coral, microfone escuro. Sobrancelhas inclinadas (olhar suplicante). Legível.
7. Composição: OK no contexto. Rara de 2,3% a 66% do alto: ocupa o topo porque o pedido é "pendurada na borda de cima"; o terço de cima não pode estar livre. Folgas L 221, R 219. O espaço abaixo da cauda (~31% do alto) fica livre para o texto "Tô aqui em cima. Esperando.".
8. Limpeza: OK. Sem texto/logos. O único adereço é a faixa/borda do topo (pedido).
9. Fundo e cena: OK. Rosa suave com a borda do topo; olhando para baixo com olhos pidões.

### M08_v1 (lagoa à noite, tons roxos)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK. Os dois pés pendem da borda de pedra e tocam a superfície da água com ondas concêntricas e reflexo das pernas amarelas (pedido: "pés na água"). Há contato visível. Não é flutuação.
3. Pernas: OK. Curtas, só pés e tornozelos visíveis.
4. Asas: OK. A asa esquerda aparece aberta e inclinada para trás; a direita fica parcialmente dobrada ao lado do corpo. Sem garras nem luva.
5. Cauda: OK com ressalva. Longa, degradê azul a verde, inteira, deitada sobre a grama e a borda de pedra para a esquerda. Folga da ponta até a borda esquerda: ~35 px (estimado).
6. Rosto: OK com ressalva. Olhos tristes com cílios e 2 linhas sob cada olho, rubor, faixa escura, bico escuro com gancho (aberto num suspiro), fone escuro com aro coral. Rosto menor (~190 px de largura), ainda legível; a verificação de contagem de cílios aqui é menos segura do que nas outras peças.
7. Composição: OK com ressalva. Crista em ~y=704 (42%). Rara ocupa só ~32% do alto (~537 px): é a peça em que a Rara é menor, mas não minúscula. A lua e as estrelas ficam no terço de cima (céu, não personagem). Folgas: tail L ~35 px; R ~190 px; base: pés a ~440 px da base, o reflexo ocupa a parte de baixo.
8. Limpeza: OK. Sem texto/logos. Adereços não pedidos (cenário coerente com "noite, lagoa, luar"): arbustos com hortênsias roxas, pedras, grama, vaga-lumes, nuvens, reflexo da lua. O reflexo da Rara na água mostra o rosto grande e de cabeça para baixo, plausível e sem texto.
9. Fundo e cena: OK. Sentada na beirada, pés na água, olhando o reflexo, suspiro dramático, luar, tons roxos.

### M09_v1 (carta com pena, abajur)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK com ressalva. Os pés aparecem por baixo da mesa, apoiados no assento da cadeira (~y 1275 px), parcialmente escondidos pela borda da mesa. Há sombra no assento. Não é flutuação.
3. Pernas: OK. Não aparecem (escondidas).
4. Asas: OK com ressalva. As duas visíveis sobre a mesa: uma segura a pena de escrever, a outra se apoia no papel. Pontas de pena com leitura de mão; sem garras.
5. Cauda: OK. Longa, degradê azul a verde, inteira, pendendo atrás da cadeira até perto do chão. Ponta em ~1540 px (folga de base ~131 px), tocando o nível do piso perto da perna da cadeira.
6. Rosto: OK. Lágrimas escorrendo; 3 cílios por olho, 2 linhas sob cada olho (as lágrimas passam por cima), rubor, faixa escura, bico escuro com gancho, fone escuro com aro coral, microfone escuro. Legível.
7. Composição: OK com ressalva. Crista em ~y=592 (35,4%). Rara visível só da cintura para cima e ocupa ~41% do alto; é a peça em que ela mais perde protagonismo, depois da M08. A mesa encosta nas duas bordas laterais (L ~30 px, R 0) e o abajur chega a ~17 px da borda direita: são cenário, não a Rara.
8. Limpeza: OK. A carta (tira de papel comprida) está em branco, sem texto ou rabisco legível; os papéis amassados também. Sem logos. Adereços além do pedido: mesa de madeira, cadeira, ~12 bolas de papel amassadas espalhadas, tira de papel até o chão, rodapé/parede (cenário coerente com "papéis amassados em volta, abajur aconchegante").
9. Fundo e cena: OK. Parede quente com abajur aceso; escrevendo com pena de ave, olhos com lágrimas.

### M10_v1 (chuva, guarda-chuva, celular)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK. Dois pés na calçada molhada, com reflexo e sombra de contato (luminância -32 aos 6 px e -22 aos 14 px, abaixo do piso de referência). Sem flutuação.
3. Pernas: OK. Curtas, pouco visíveis.
4. Asas: OK com ressalva. Uma segura o celular, a outra segura o cabo do guarda-chuva; ambas com leitura de mão de pelúcia (lóbulos de pena), sem garras.
5. Cauda: OK com ressalva. Longa, degradê azul a verde, inteira, descendo na diagonal para a direita sobre a calçada, com reflexo esverdeado abaixo da ponta (~1498 px, folga de base ~174 px). A diagonal "para fora" do corpo é pouco comum, mas apoia no chão com reflexo.
6. Rosto: OK. Olhar esperançoso e triste; 3 cílios por olho, 2 linhas sob cada olho, rubor, faixa escura, bico escuro com gancho, fone escuro com aro coral, microfone escuro. Ressalva: a haste do guarda-chuva desce colada ao lado do rosto e do boom do microfone, o que polui a silhueta da bochecha direita.
7. Composição: OK no limite. Espeto do guarda-chuva em ~y=541 (32,4%), 15 px dentro do terço de cima; a copa começa em ~565 (33,8%). Crista da Rara em ~690 (41%). Rara ocupa ~39% do alto. Folgas: R ~190 px (guarda-chuva a ~160 px da direita), L ~210 px.
8. Limpeza: OK. O celular está de tela preta, sem texto/logo. Os prédios e luzes de fundo são borrados, sem letras legíveis. Adereços não pedidos: poste/luzes bokeh, gotas, prédios (cenário coerente com "chuva, luzes da cidade borradas").
9. Fundo e cena: OK. Chuva fina, guarda-chuva pequeno e azul, olhando a tela do celular, rosto triste e esperançoso, luzes da cidade borradas.

### M11_v1 (dormindo em cima do celular)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK com ressalva. Um único pé aparece, curvado, apoiado na cama (sombra suave). O outro fica escondido atrás do corpo, plausível numa pose deitada. Não há flutuação.
3. Pernas: OK. Não aparecem.
4. Asas: OK. Uma asa azul grande e aberta sobre as costas, bem desenhada; a outra fica embaixo do corpo. Sem garras, sem luva.
5. Cauda: OK. Longa, degradê azul a verde, inteira, curvada sobre o colchão. Ponta à direita ~132 px da borda, base ~264 px.
6. Rosto: OK com ressalva. Olho de cima fechado com cílios e linhas, lágrima pequena visível, rubor, faixa escura, bico escuro com gancho (levemente aberto, ronco), fone escuro com aro coral e microfone escuro. A cabeça deitada de lado mostra a outra bochecha na sombra perto da concha, com leitura mais difícil. Ainda legível em tamanho de story.
7. Composição: OK. Cabeça/fone a partir de ~y=913 (54,6%): terço de cima totalmente livre. Rara larga: ~450/675 da largura. Folgas: L ~178 px (cabeça), R ~132 px (cauda), B ~264 px.
8. Limpeza: OK. Celular preto sem texto/logo (a face de trás não aparece). Adereços não pedidos: abajur de cabeceira com carinha sorridente, almofada roxa com estrela, cama/colchão. A carinha do abajur não é texto, mas é um rosto extra desnecessário.
9. Fundo e cena: OK. Quarto escuro azul-roxo, dormindo com a cabeça sobre o celular como travesseiro, lágrima pequena, fone ainda na cabeça.

### M12_v2 (espiando atrás do batente)
1. Formato: OK. 941x1672, 0,5628.
2. Pés: OK. Os dois pés no assoalho de madeira, com sombra de contato medida (-34 aos 6 px, -32 aos 14 px, -24 aos 24 px contra o piso de referência) e o piso em cor diferente do fundo (madeira alaranjada contra parede bege). Sem flutuação. Isso corrige o defeito de M12_v1.
3. Pernas: OK. Curtas, quase escondidas.
4. Asas: OK. Uma asa agarra o batente (só penas, sem garras), a outra fica dobrada junto ao corpo. Anatomia plausível.
5. Cauda: OK. Longa, degradê azul a verde, inteira, deitada no assoalho para a direita. Folga da ponta: ~181 px à direita.
6. Rosto: OK. 3 cílios por olho, 2 linhas sob cada olho, rubor, faixa escura, bico escuro com gancho, fone escuro com aro coral, microfone escuro. Olhar esperançoso e tímido. Legível.
7. Composição: FALHA parcial. Crista em ~y=464 (27,8%): dentro do terço de cima (~90 px). Folgas: R ~181 px, B ~257 px; o lado esquerdo é coberto pelo batente (esperado). Rara grande: ~57% do alto.
8. Limpeza: OK. Sem texto/logos. Adereços: porta, batente, maçaneta dourada, rodapé, assoalho, luz quente do corredor.
9. Fundo e cena: OK com ressalva. O pedido era "espiando por trás do batente com só metade do rosto visível". Em v2 o rosto aparece inteiro (ambos os olhos, bico, as duas conchas) e quase 3/4 do corpo fica à mostra. Lê como "espiando", mas é mais "aparecendo" do que "só metade do rosto". Luz quente, sorriso tímido e esperançoso: cumpre.

### Versões antigas reprovadas (só para registro)

| Versão | Formato | O que se vê / por que perdeu |
|---|---|---|
| MA01_v1 | 1024x1536, razão 0,6667 (FALHA: não é 9:16) | Cauda longa saindo na diagonal para a esquerda, solta no ar; sombra só sob os pés; asa-luva ao microfone; ponta da cauda a ~150 px da borda. |
| MA02_v1 | 1024x1536, razão 0,6667 (FALHA) | Pés em cima da cauda, sem poleiro visível: a Rara fica em pé sobre a própria cauda no meio do piso, com reflexo da ponta no chão. Leitura de flutuação (mesmo defeito de BS02). |
| MA02_v2 | 941x1672, 0,5628 (formato OK) | Pernas longas e finas, amarelas, de pernilongo (~130 px na exibição); corrigido em v3. |
| MA03_v1 | 1122x1402, razão 0,8003 (FALHA: não é 9:16) | Formato quase 4:5; piscadinha e prancheta corretas; foi refeita em v2 em 9:16. |
| M12_v1 | 941x1672, 0,5628 (formato OK) | Rara minúscula (só uma fresta de ~25% do alto da cena) e cauda pendendo na fresta da porta sem apoio legível; leitura de flutuação. Corrigido em v2. |

Todas as correções das versões antigas foram de fato feitas nas versões atuais: formato, pernas, flutuação e escala da Rara.

## (c) O que o orquestrador deixou passar (priorizado)

Prioridade alta (afeta o critério do Rodrigo):
1. Terço de cima invadido: MA02_v3 (crista a 28,6%, ~79 px dentro) e M12_v2 (crista a ~27,8%, ~90 px dentro). Nenhum dos dois estava marcado. MA04_v1 está a 33,7% (só 7 px de folga) e M10_v1 tem o espeto do guarda-chuva a ~32,4% (15 px dentro).
2. MA04_v1: o piso quase não tem cor diferente do fundo (ΔRGB 11, 6 níveis de luminância). Não flutua (sombra e reflexo fortes), mas a regra "superfície visível de cor diferente" está no limite. MA01_v2 também é baixo (ΔRGB 31).
3. Asas-mão: em MA01_v2, MA03_v2, M09_v1 e M10_v1 as asas que seguram objetos têm lóbulos empilhados com leitura de luva de pelúcia (sem garras, com textura de pena). O Rodrigo pode ver isso como "luva lisa". Não foi possível confirmar a textura em zoom. É o risco de rejeição mais provável do lote, no mesmo espírito do que ele já reprovou.

Prioridade média:
4. Cauda a 31 px (MA01_v2) e 44 px (MA03_v2, base) da borda, e ~35 px (M08_v1): apertadas. A de MA03_v2 cai dentro da zona de UI inferior do story.
5. M12_v2 não entrega "só metade do rosto": o rosto aparece inteiro. Desvio do pedido da tabela 7.15 que a revisão anterior não registrou.
6. M08_v1 e M09_v1 têm a Rara menor (32% e 41% do alto, M09 só da cintura para cima). Aceitável, mas são as peças onde o "Rara grande" (âncora 1) fica mais fraco.
7. RP06_v1: base esfumada por ~95 px em vez de corte limpo; fundo #888786 em vez de #8C8C8C.
8. MA03_v2: ponta do microfone coral, diferente do microfone escuro do canônico (e das outras peças). Já o texto do checklist deste lote pede "microfone coral": o canônico é que está em conflito com o checklist. Vale decidir qual vale.

Prioridade baixa:
9. Adereços não pedidos: M11_v1 (abajur com carinha, almofada com estrela), M08_v1 (arbustos, vaga-lumes, nuvens), M09_v1 (cadeira, papéis amassados, tira até o chão), M12_v2 (rodapé, maçaneta), M10_v1 (prédios e postes borrados). Todos coerentes com a cena; nenhum tem texto legível.
10. Nenhuma peça tem texto, números, logos ou marca d'água legíveis (cantos conferidos por energia de detalhe: sem anomalia). Prancheta de MA03_v2, carta de M09_v1 e celulares de M10_v1/M11_v1 estão em branco/pretos.
11. Nenhuma peça repete o defeito que reprovou BS02 ou M12_v1: não há pés flutuando, nem pernas de pernilongo, nem cauda solta no ar, nem Rara minúscula.

## (d) Recomendação por peça

| ID | Recomendação |
|---|---|
| RP06_v1 | Manter. Se for usar com remoção de fundo, pedir nova versão com a base do meio corpo cortada reta (sem degradê) e fundo exatamente #8C8C8C. |
| MA01_v2 | Manter. Se o Rodrigo reclamar da mão em luva, pedir nova versão: "wing wrapping the microphone with visible individual flight feathers, no fingers, no mitten shape" e cauda mais curta ou girada para deixar 80 px ou mais até a borda. |
| MA02_v3 | Manter, ou nova versão leve: "move the character 90 px lower so the crest starts below one third of the frame, longer visible tail on the right". Só se o terço de cima precisar estar livre para o texto. |
| MA03_v2 | Manter, com ressalva da cauda. Se precisar da base livre: "tail curling to the side on the floor, at least 120 px from the bottom edge". Decidir se o microfone fica coral ou escuro. |
| MA04_v1 | Manter. Se o piso importar para o Rodrigo: nova versão com "a clearly visible slightly darker pink floor plane with a soft horizon line", mantendo sombra e reflexo. |
| M07_v1 | Manter. |
| M08_v1 | Manter. Se quiser mais Rara: nova versão com enquadramento mais fechado ("character about 45% of the frame height"). |
| M09_v1 | Manter. Se quiser Rara maior: "closer framing, character larger", e um ângulo em que a mesa não encoste nas duas bordas. |
| M10_v1 | Manter. Opcional: nova versão com "umbrella fully below one third of the frame, umbrella shaft away from the face". |
| M11_v1 | Manter. Opcional: tirar a carinha do abajur ("plain warm night lamp, no face"). |
| M12_v2 | Manter, ou nova versão (v3) se o pedido de "só metade do rosto" importar: "more of her body behind the door frame, only half of her face visible, crest below one third of the frame". |

Nenhuma peça precisa ser refeita do zero.

