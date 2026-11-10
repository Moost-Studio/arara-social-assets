# Direção visual de posts e stories da Arara (proposta de 06/11/2026)

Status: PROPOSTA, aguardando aprovação do Rodrigo. Nada foi produzido, agendado ou alterado. Posts e stories já agendados de 06 a 15/11 seguem como estão.

## 1. O que já foi decidido e orienta tudo
- A mascote é a arara vetorial antiga (decisão de 05/11, 23h55). A versão 3D foi descartada.
- Direção dos vídeos de 06/11: "vídeos imersivos, motion arrojado, experiência 3D, mantendo a arara antiga". Para posts e stories, isso vira profundidade, luz e vida na personagem, sem redesenhá-la.
- Referência de atuação: aberturas da Pixar (olhar, antecipação, pausa). Em peça estática, isso vira expressão com intenção: a arara olha para o conteúdo, reage ao erro, comemora o acerto.
- Tom: personagem marcante com acabamento profissional. Não infantil, sem confete, sem elementos aleatórios, sem realismo.
- Interface real do app como linguagem visual (cartões, balões, botões).
- Regras da marca que continuam: sem travessão nem dois-pontos na copy das artes, sem emoji na arte, Baloo 2 e Nunito, no máximo 3 stories por dia, sem enquete, sem preço, sem mencionar concorrente.

## 2. Sistema visual proposto

### Cor
| Papel | Valor | Uso |
|---|---|---|
| Base | #07152F (azul-marinho) | fundo de capas, slides e stories |
| Acento principal | #245BFA (azul elétrico) | botões, selos, brilhos |
| Luz | #36C9F5 (ciano) | contorno de luz da mascote, halos, ondas de voz |
| Destaque de texto | #FFC928 (amarelo) | uma palavra-chave por título e o CTA |
| Texto | #FFFFFF | títulos e corpo sobre a base |
| Acerto | #34C77B | só feedback de acerto |
| Erro | #E5483F | só feedback de erro |
- O azul-claro em degradê deixa de ser fundo. Superfícies claras só aparecem dentro de cartões de interface, onde o contraste ajuda a leitura.
- Cores por idioma (`lang_theme.py`): passam a ser o acento da borda e do brilho do cartão do idioma, sem repintar o fundo. Ainda faltam cores para holandês, sueco, polonês, russo, turco, árabe, hebraico, hindi e coreano.

### Profundidade (3 camadas)
1. Fundo: degradê de #07152F para um azul um pouco mais claro, com luz volumétrica suave atrás da mascote.
2. Meio: cartões de interface elevados, com sombra projetada e borda fina.
3. Frente: mascote com sombra de contato e contorno de luz ciano, e o título.
- Sem estrelinhas, confete ou formas soltas decorativas (o visual atual tem estrelinhas nas poses).

### Mascote
- Arte vetorial oficial, sem mudança de desenho, cor ou proporção. Contorno de luz e sombra aplicados por fora, como tratamento.
- Uma pose por peça, escolhida pela emoção do conteúdo. Ocupa no máximo 40% do quadro, nunca cortada, sempre olhando para o ponto de atenção.
- Resolução: o recorte atual é 540x965 ampliado. Antes do lote, gerar um kit em alta resolução (pendência D7 do planejamento de reels).

### Tipografia
- Baloo 2 nos títulos e Nunito no texto, como hoje. Manrope e Inter, citadas na prancha de 05/11, não foram aprovadas.
- Título em até 8 palavras, com uma palavra-chave em amarelo. Um título por peça.

### Cartões
- Reproduzem os tokens do app (raios, bordas, sombras), com texto sempre legível em tamanho de celular.
- Balão com cauda para a fala da mascote. Botões de resposta nos exercícios.

## 3. Formatos

### Posts (4:5, 1080x1350)
- Capa: base azul-marinho, gancho em até 8 palavras, mascote com atuação. Uma ideia só.
- Carrossel: slide 1 gancho; miolo com cartões de interface, um conceito por slide; último slide com ação suave (salvar, comentar ou marcar). O fecho comercial fica só na legenda.
- Consistência de grid: toda capa em base azul-marinho; a pose e o acento de cor variam por tema.

### Stories (9:16, 1080x1920)
- Zona segura: 250 px no topo e 340 px no rodapé livres.
- Sequência do dia: 1) aviso com a pose da mascote e uma frase; 2) conteúdo ou exercício em cartões; 3) humor ou reforço. Máximo de 3.
- Story estático nesta fase. Versão animada, com a arara atuando, entra depois que o teste de atuação for aprovado.
- Datas sensíveis (por exemplo 20/11): story sóbrio, sem mascote em pose de brincadeira, sem CTA.

### Destaques e avatar
- Seis ícones (Sobre, Como usar, Idiomas, Dúvidas, Feedbacks, Novidades): círculo azul-marinho, ícone `lucide` branco com um detalhe amarelo.
- Avatar: manter a cabeça da arara vetorial sobre o círculo azul, enquanto o logo não for redefinido.

## 4. O que muda em relação ao visual atual
| Elemento | Hoje | Proposta |
|---|---|---|
| Fundo | azul-claro em degradê | azul-marinho com luz volumétrica |
| Profundidade | uma camada, sombra leve | três camadas com sombras e contorno de luz |
| Mascote | poses com estrelinhas | mesma arte, sem enfeites, com contorno de luz |
| Cartões | brancos chapados | interface do app com elevação |
| Cor do idioma | pinta o fundo | acento do cartão |
| Destaque do título | palavra em azul | palavra em amarelo |
| Pessoas | não usa | só com decisão específica (ver abaixo) |

## 5. Pessoas e fotografia
- Não usar pessoas geradas por IA em posts e stories nesta fase. O teste do café mostrou a voz e a boca fora de sincronia, e a regra de rótulo de conteúdo de IA da Meta precisa ser conferida.
- Se o Rodrigo quiser fotos de pessoas, o caminho é fotografia real licenciada ou própria, com autorização de uso de imagem.

## 6. O que reaproveita e o que falta
- Reaproveita: roteiro e copy aprovados, calendário, interface do app em HTML (já usada no encerramento C), `post_compose.py`, `lang_theme.py`, bandeiras em SVG, ícones `lucide`, as poses da mascote.
- Falta: fundo azul-marinho com luz, tratamento de contorno e sombra da mascote, novo modelo de cartão, kit da mascote em alta resolução, cores dos 9 idiomas pendentes e a seleção das poses por tema.
- Esforço e prazo: não medidos. A estimativa sai de uma peça de teste.

## 7. Transição proposta
- 06 a 15/11: sai como está agendado (artes aprovadas, nada a refazer).
- A partir de 16/11: novo visual, começando pela peça de pedir a conta (seg 16/11) em duas variações para escolha.
- Efeito colateral aceito: o feed mistura os dois visuais por uma semana. Alternativa, refazer 09 a 15/11 (cerca de 7 posts e 17 stories, com troca dos agendamentos).

## 8. Critérios de aceite por peça
- Legível em tela de celular, contraste adequado, margens respeitadas.
- Uma ideia e uma ação por peça. Palavra-chave única em amarelo.
- Mascote íntegra, no máximo 40% do quadro, sem enfeites.
- Interface fiel ao app. Nenhum recurso, número ou resultado inventado.
- Sem travessão nem dois-pontos na copy. Copy igual à aprovada no plano da semana.
- Revisão em folha com todas as peças do lote antes de qualquer agendamento.

## 9. Decisões pendentes do Rodrigo
1. Aprovar a base azul-marinho (A) ou manter fundo claro com mais profundidade (B).
2. Data de corte: 16/11 (recomendado) ou 09/11.
3. Pessoas: nenhuma por ora (recomendado) ou fotografia real.
4. Logo e avatar: manter o atual por ora (recomendado) ou redefinir.
5. Frase "Ensaie antes de falar": hoje só no encerramento do teste de reel. Usar em posts e stories exige aprovação separada.

## 10. Inovação de formato (pedido de 06/11/2026: "inovar")
Conceitos propostos para os posts e stories deixarem de parecer cartões estáticos. Todos mantêm a arara vetorial antiga e usam só recursos que o app tem (conversa por voz, correção em português, 16 idiomas, A1 a C1). Nenhum foi prototipado.

| # | Conceito | Ideia | Por que é novo no perfil | Risco |
|---|---|---|---|---|
| 1 | Carrossel panorâmico | Uma única cena larga que continua de slide em slide. A arara aparece em um canto do slide 1 e a cena segue ao deslizar | O gesto de deslizar vira parte da história | Emenda entre slides precisa ser exata no recorte do Instagram |
| 2 | A frase que se transforma | Em cada slide a mesma frase troca de idioma, com as palavras mudando de lugar na mesma posição | Ensina comparando, sem texto longo | Palavras em idiomas de alfabeto não latino precisam de revisão |
| 3 | A correção como protagonista | Slides em formato de conversa: a fala errada aparece, é sublinhada e a correção em português se abre em cartão | Mostra o recurso central do app, em vez de só falar dele | Deve seguir a tela real e não inventar explicações |
| 4 | Arara em cenário 3D | Série "Arara por aí": a arara em situações reais (restaurante, aeroporto, hotel, reunião) dentro de uma cena com perspectiva, luz e sombra de contato | Cenário com profundidade e a mascote integrada, sem redesenhá-la | Exige montar cenas 3D em HTML e testar a integração da mascote |
| 5 | Sequência de stories com pergunta e resposta | Story 1 a situação, story 2 a frase, story 3 a correção, com a arara reagindo em cada um | Cria um mini enredo diário, sem enquete | O limite é de 3 stories por dia |

### Recomendação
- Começar por 4 e 3. O 4 entrega o "universo 3D com a arara antiga" que você pediu, e o 3 mostra o diferencial do produto. O 1 e o 2 entram depois como formatos de apoio.
- Teste proposto: o post de pedir a conta (seg 16/11) em dois protótipos, um por conceito (4 e 3), no visual da seção 2.
- Antes de qualquer peça: confirmar a base de cor (azul-marinho ou claro) e a data de corte.

## 11. Decisão do Rodrigo (06/11/2026, 10h44)
- Base: **A misturada com B**. Azul-marinho premium com luz como base, e do B vêm as superfícies claras de interface, a tipografia forte e a personalidade "concorrente do Duolingo". A combinação exata será definida pelo protótipo.
- Corte: **a partir de 16/11**. Posts e stories de 06 a 15/11 saem como estão agendados.
- Ainda abertos: pessoas, logo e avatar, uso de "Ensaie antes de falar" em posts e stories. Seguem como recomendado até decisão contrária (sem pessoas, logo atual, frase só no encerramento dos reels).

## 12. Protótipos do post da conta (16/11), 06/11/2026
Arquivos em `reports/proto_conta/` (código em `posts_novo/build_proto.py`). São protótipos visuais, sem copy aprovada para o conceito 3 e sem agendamento.
- Conceito 4 (Arara em cenário 3D): `c4_s1` capa e `c4_s2` frase em inglês. Cena em perspectiva feita em CSS (piso com grade, mesa, pratos, conta), mascote com contorno de luz ciano e sombra de contato. Não é 3D real.
- Conceito 3 (correção como protagonista): `c3_s1` conversa e `c3_s2` correção aberta, com a interface do app em perspectiva leve. O texto da conversa e da explicação é ilustrativo, não vem do app.
- A mascote usa as artes vetoriais oficiais com os brilhos e confetes removidos por filtro de componentes. O recorte vem do arquivo de 540x965 ampliado, então a nitidez é limitada.

## 13. Ajuste de cor e expressões (06/11/2026, pedido do Rodrigo: "muito azul, quero misturar mais cores e mais expressões da arara")
- A base deixa de ser só azul-marinho. Cada peça ganha uma cor de tema, em degradê rico com luz no canto superior e sombra no inferior. O azul-marinho fica como cor de produto e do encerramento.
- Cor por tema ou idioma (proposta): conta e restaurante em coral e laranja, inglês em azul, espanhol em vermelho, francês em roxo, italiano em verde. Ainda não definidos: alemão, japonês, humor, falsos amigos e as datas.
- A cor do idioma define o fundo, a borda do cartão e o botão de som. O destaque do título é amarelo, ou amarelo claro sobre fundos quentes.
- Expressões: 36 poses da mascote recortadas das ilustrações existentes (`posts_novo/cutouts/`, script `recortar.py`): ouvindo com fone, de óculos escuros, em dúvida, comemorando, acolhendo, surpresa, cansada, lendo, com lupa, com celular e outras. Cada slide usa uma pose diferente, escolhida pela emoção do conteúdo.
- Protótipo: `reports/proto_conta_cores/` (capa coral e quatro idiomas), gerado por `posts_novo/build_proto2.py`.
- Pendente de medir: contraste do amarelo claro sobre o coral da capa e a nitidez dos recortes em tamanho maior.
