# Rig da Rara (fase 1, por código)

Pontos de articulação de cada pose usada nos reels, no quadro de 1254 x 1254 px das poses aprovadas.
Referência: seção 7.21 do arquivo de marca e `rig.py` (protótipo em Python).

## Arquivos

- `{pose}.json`: um por pose.
  - `points`: `feet` (pés, pivô do corpo), `neck` (pescoço, pivô da cabeça), `crest` (topete), `wingL` e `wingR` (ombros), `tail` (base da cauda), todos em `[x, y]`.
  - `bbox`: caixa da figura `[x0, y0, x1, y1]` no mesmo quadro.
  - `image`: recorte RGBA em 1254 px, em `semana1/recortes/rig/{pose}.png`.
- `_verificacao.png`: folha com os pontos desenhados sobre cada pose.

## Como foram marcados

`semana1/_scripts/rig_prep.py` parte dos pontos do `rig.py` (poses de pé, mesmo corpo em todas), ajusta o topete
pela geometria da figura e usa `OVERRIDE` quando o corpo muda de lugar. A única pose com override é a E02 (no ar,
pés e cauda 115 px acima). Os pontos de pescoço e ombros são os do corpo canônico. Os pontos são estimados e
conferidos na folha de verificação; não foram marcados à mão ponto a ponto.

## Uso no reel

`semana1/_scripts/rig_data_gen.py` junta os JSON em `rig_data.js`. O `reel4.html` carrega esse arquivo, monta a malha
de cada pose (grade de 18 px, 6 pesos por vértice) e deforma por 6 ossos no WebGL com a mesma animação do `rig.py`
(pulinho com squash no contato, balanço em ciclo de 2 batidas, cabeça com atraso, topete com continuação, asas
abrindo no ritmo, cauda com atraso), na grade de 120 BPM.

Piscada e bico aberto são variantes de textura (`{pose}_blink.png`, `{pose}_beak.png`, geradas por
`overlay_gen.py` com os olhos do K03 e o bico do K01). Só existem onde a cabeça da pose bate com o kit (correlação
de olhos acima de 0,62 e de bico acima de 0,78).

## Limites

Como diz a seção 7.21: o rig por malha balança, pula e abre um pouco as asas. Asa totalmente aberta, giro de corpo
e perfil usam clipes de IA ou a fase 2 (Rive). Poses de perfil (C05) ficaram de fora.
