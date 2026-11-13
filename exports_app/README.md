# exports_app: pacote de arte para o app e o site (ART-5 e ART-10)

Gerado em 12/11/2026 por código (sem geração paga), a partir da arte **já aprovada** pelo Rodrigo. Os geradores estão em `_gerador/` e podem ser rodados de novo (`python3 exportar_app.py <humores|telas|loja|avatares>`, `python3 kit_mascaras.py [rara|raro]`, `python3 exportar_logotipo.py`; precisam de Pillow e numpy).

## Formato comum

- Cada peça sai em **PNG 1024 (master)** e **WebP 512, 256 e 128** (qualidade 90, com transparência). O sufixo diz o tamanho: `nome_1024.png`, `nome_512.webp`, `nome_256.webp`, `nome_128.webp`.
- O quadro é **quadrado e igual ao da arte original**: o recorte tira só o fundo cinza (#8C8C8C), sem cortar ao conteúdo. Assim as poses de uma mesma família mantêm o mesmo alinhamento e dá para trocar uma pela outra sem a Rara pular de lugar.
- Só o cinza **conectado às bordas** é removido (preenchimento por inundação), então olhos, bico e headset escuros ficam intactos. A borda ganha 3 px de suavização e perde a contaminação de cinza.
- Os tamanhos finais por família dependem do orçamento de peso (H9). Os quatro tamanhos servem de ponto de partida: o app escolhe, o resto sai do bundle.

## Pastas

| Pasta | Conteúdo | Nomes |
| --- | --- | --- |
| `humores/` | 18 humores (9 da Rara, 9 do Raro) | `{rara,raro}_humor_{feliz,euforia,dormindo,acolhendo,desafiando,valente,carente,triste,braba}` |
| `telas/` | Telas de estado A01 a A11, Rara e Raro (22) | `{rara,raro}_A01_boas_vindas` ... `A11_assinatura` |
| `loja/` | Visuais da loja (óculos, mochila, gorro, junina), Rara e Raro (8) | `{rara,raro}_loja_{oculos,mochila,gorro,junina}` |
| `avatares/` | 53 avatares (arara-1 a 30 e 23 sazonais), bustos com a Rara recortada | `arara-N`, `season-*` (ids do app) |
| `kit/rara/`, `kit/raro/` | Quadros recortados K00 a K09, máscaras fixas e remendos (ART-5) | ver abaixo |
| `logotipo/` | Candidatos de ícone, adaptativo, splash, favicon, PWA, e-mail, OG e arte do Play, a partir do selo oficial | ver abaixo |

Correspondência de humores: feliz = H01 (W02 acenando), euforia = H02, dormindo = H03, acolhendo = H04, desafiando = H05, valente = H06, carente = H07, triste = H08, braba = H09. Nas duas famílias, feliz, euforia, dormindo e carente são **bustos** (corpo cortado no quadro); acolhendo, desafiando, valente, triste e braba são de **corpo inteiro**. Confira em `_qa/qa_humores.png` (fundo magenta de teste).

## Kit da chamada (ART-5)

Em `kit/<personagem>/`:

- `<p>_quadro_K00..K09_1024.png`: cada quadro do kit recortado, mesmo alinhamento do K00.
- `<p>_mascara_<grupo>_1024.png`: máscara em tons de cinza da região que o grupo mexe (alfa suave). Grupos da Rara: `bico` (K01 e K02), `olhos` (K03 a K05), `topete` (K06 a K08). Grupos do Raro: `bico`, `olhos`, `chapeu` (K06 a K08).
- `<p>_remendo_<grupo>_<K>_1024.png`: a variação só dentro da máscara, com fundo transparente. O app desenha o K00 e troca o remendo por cima.

Como as máscaras foram feitas: união das diferenças entre cada variação e o K00, suavizada para ignorar deslocamentos de 1 px, com buracos preenchidos e limitada à cabeça. Limites que a revisão visual confirmou:

- **Rara: boas.** Bico, olhos e topete são regiões compactas, sem respingos.
- **Raro: só aproximadas.** Os quadros do kit do Raro foram gerados um a um e **não se alinham ao pixel** (a cabeça e o chapéu mudam de tamanho de um quadro para outro). O remendo do bico e dos olhos traz restos das bordas, e o do chapéu cobre a cabeça inteira. Para o Raro, use **crossfade entre quadros inteiros** (`raro_quadro_Kxx`), não remendos.
- Para variações que **encolhem** a região (topete murcho, chapéu abaixado), o K00 aparece por baixo do remendo. Nesses casos, use o quadro inteiro.
- O K09 (erro técnico) não tem máscara: é um quadro inteiro.

### Topete separado da base (ART-12, 13/11/2026)

Em `kit/rara/`: `rara_base_sem_topete_{1024.png,512.webp,256.webp}` e `rara_topete_{1024.png,512.webp,256.webp}` (mesmo quadro de 1024 e mesmo alinhamento do K00, fundo transparente, WebP qualidade 90).

- **Como foram feitos:** a cabeça sem topete é uma edição gerada do K00 (1 imagem, o resto do quadro vem do K00); o topete é o do próprio K00, recortado por cor. **Não são idênticos ao K00 ao pixel**: base + topete difere do K00 em cerca de 15 mil pixels (de 1.048.576), concentrados na borda do topete e na banda do fone. O critério passou a ser visual, aprovado pelo Rodrigo em 13/11/2026: sem buraco na cabeça com o topete girado de -8 a +8 graus.
- **Pivô do giro:** x = 489, y = 217 (px no quadro de 1024), onde o topete encosta na cabeça.
- **Limite:** a banda do fone da base foi pintada pela geração e não coincide ao pixel com a do K00. Em animação, usar o par base + topete juntos (não misturar a base nova com o K00 original). A QA está em `_qa/_qa_topete_kit.png` (fundo magenta: base, topete, sobreposição, +8 e -8 graus, K00 original).
- Os arquivos de teste da geração ficam em `_teste_topete/` e não devem ser usados no app.

## Logotipo (D7, H7, E5, E9)

Todos derivam do selo oficial aprovado (`personagens/logotipo/`). **Nada substitui os arquivos atuais do app**: a troca do ícone atual pelo selo ainda é decisão do Rodrigo.

| Arquivo | Uso |
| --- | --- |
| `icon-1024.png` | Ícone do app e da App Store (1024, **sem transparência**) |
| `icon-play-512.png` | Ícone do Google Play (512) |
| `android-icon-foreground.png`, `android-icon-background.png`, `android-icon-monochrome.png` | Ícone adaptativo (selo a 60% do quadro, dentro da zona segura; fundo azul-noite `#081226`). O monocromático é só a silhueta do balão: **provisório** |
| `splash-icon.png` | Splash (selo transparente; o fundo vem da cor do `expo-splash-screen`) |
| `favicon.ico`, `favicon-16/32/48.png`, `apple-touch-icon.png` (180), `icon-192.png`, `icon-512.png`, `icon-512-maskable.png` | Site e PWA. Em 16 px o selo vira uma mancha azul em forma de balão; o rosto só se lê a partir de 32 px |
| `email-arara.png`, `email-arara@2x.png` | Imagem de e-mail (160 e 320 px de altura) |
| `og.png` (1200×630) | Imagem de compartilhamento noturna com o manifesto "Papagaio repete. Arara conversa." em Mochiy Pop One. **Proposta**, aguarda OK |
| `play-feature-1024x500.png` | Arte de destaque do Google Play, mesma composição. **Proposta**, aguarda OK |

## O que não existe ainda

- As 5 capturas das lojas com a Rara (dependem das telas finais do app).
- Os pacotes por densidade para Android (mdpi a xxxhdpi) e iOS (@1x a @3x): dependem dos tamanhos que o H9 fixar. Os WebP 512/256/128 e o master 1024 cobrem o ponto de partida.
- Camadas de acessório da loja (ART-8, H5): os arquivos de `loja/` são a arte **completa** com o acessório, não camadas separadas.
- Versão monocromática verdadeira do selo: a Rara é raster.
