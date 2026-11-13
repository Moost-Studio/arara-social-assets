# Receitas técnicas dos reels

Trechos de referência para o agente. Confira a versão instalada de cada pacote antes de usar e ajuste à API da versão. Nenhuma chave aparece em código, log ou commit.

## 1. Grade de batida da trilha
Toda mudança forte cai na batida. Gere `beats.json` antes da composição:

```bash
# aubio (pip install aubio) devolve os tempos de batida em segundos
aubio beat trilha.wav > beats.txt
```
Converta para quadros (`round(t * 30)`) e salve `{ "bpm": ..., "beats": [quadros] }`. Na composição, todo corte e toda entrada de palavra usam o quadro de batida mais próximo.

## 2. Movimento ligado à voz (audio-reactive)
```tsx
import { useAudioData, visualizeAudio } from '@remotion/media-utils';
import { staticFile, useCurrentFrame, useVideoConfig } from 'remotion';

/** Amplitude da voz no quadro atual (0 a 1), usada nos anéis do "Solta o bico" e no estalo do topete. */
export const useVoiceLevel = (src: string): number => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const audioData = useAudioData(staticFile(src));
  if (!audioData) return 0;
  const bins = visualizeAudio({ fps, frame, audioData, numberOfSamples: 16 });
  return Math.min(1, bins.slice(0, 6).reduce((a, b) => a + b, 0) / 2);
};
```

## 3. Tokens de movimento da marca
Os mesmos do app (`packages/shared/src/motion.ts` no `falearara-app`): durações 100, 200, 333, 500 e 1000 ms; curvas `entrada` [0.16, 1, 0.3, 1], `saida` [0.7, 0, 0.84, 0], `padrao` [0.65, 0, 0.35, 1], `passada` [0.34, 1.56, 0.64, 1]; atrasos 0, 40, 80, 120 ms. Personagem com mola (master 6.5): `spring({ frame, fps, config: { damping: 12 a 15, mass: 0.6 a 0.8 } })`. Copie os valores do arquivo do app no dia (ele ainda pode ser ajustado) em vez de confiar nesta lista.

```tsx
import { Easing, interpolate } from 'remotion';
const entrada = Easing.bezier(0.16, 1, 0.3, 1);
const x = interpolate(frame, [0, 10], [24, 0], { easing: entrada, extrapolateRight: 'clamp' });
```

## 4. Câmera viva
Deriva sutil de câmera na mão (0,5 a 1 px) com ruído, não com aleatório por quadro (aleatório treme):
```tsx
import { noise2D } from '@remotion/noise';
const dx = noise2D('camx', frame / 90, 0) * 1;
const dy = noise2D('camy', 0, frame / 90) * 1;
```

## 5. Transições como componentes
Use `@remotion/transitions` (`TransitionSeries`) e escreva as assinaturas S1, S4, S6 e S9 como *presentations* próprias, reutilizáveis, em `arara_social/video/src/transicoes/`. Uma transição = um arquivo, com docstring de duração, curva e quando usar.

## 6. Clipe de IA com fundo removível
Gere sobre cinza liso #8C8C8C (regra do master; nunca verde, porque a cauda tem verde). Depois:
```bash
mkdir -p q m
ffmpeg -i clipe.mp4 q/%04d.png
# remoção de fundo por quadro (rembg com modelo birefnet-general, por exemplo)
for f in q/*.png; do rembg i -m birefnet-general "$f" "m/$(basename "$f")"; done
ffmpeg -framerate 30 -i m/%04d.png -c:v libvpx-vp9 -pix_fmt yuva420p -b:v 0 -crf 24 clipe_alfa.webm
```
No Remotion: `<OffthreadVideo src={...} transparent />`. Confira as bordas da cauda e das penas da asa em 3 quadros por segundo; halo cinza reprova.

## 7. Encadear clipes (plano-sequência)
```bash
# último quadro do clipe aprovado vira o primeiro quadro do próximo
ffmpeg -sseof -0.05 -i clipe_01.mp4 -frames:v 1 -update 1 inicio_02.png
```
Se o endpoint de vídeo aceitar também o último quadro (`frame_type: last_frame` ou equivalente; confirme na documentação do OpenRouter no dia), use primeiro e último quadro para fechar a ponte entre duas poses aprovadas.

## 8. Voz
```bash
# TTS: modelo google/gemini-3.8-flash-tts via OpenRouter /audio/speech, voz Achernar (Rara) ou Achird (Raro)
# normalização da voz e mixagem final
ffmpeg -i fala.wav -af loudnorm=I=-16:TP=-1.5:LRA=7 fala_norm.wav
# trilha abaixa 8 dB quando há fala (sidechain)
ffmpeg -i trilha.wav -i fala_norm.wav -filter_complex "[0][1]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[t];[t][1]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1[a]" -map "[a]" mix.wav
```
Alinhamento do bico: detecte os ataques de sílaba (`aubio onset fala.wav`) e marque as aberturas do bico no clipe; ajuste corte e velocidade (0,9x a 1,1x) até a diferença ficar abaixo de 3 quadros.

## 9. Conferência automática
```bash
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt -of json final.mp4
ffmpeg -i final.mp4 -af ebur128=peak=true -f null - 2>&1 | tail -12
# folha de contato a cada 0,25 s
ffmpeg -i final.mp4 -vf "fps=4,scale=270:-2,tile=8x8" -frames:v 1 folha.jpg
# trechos parados (mais de 1,5 s sem mudança)
ffmpeg -i final.mp4 -vf "freezedetect=n=0.003:d=1.5" -map 0:v -f null - 2>&1 | grep freeze_
```
`freezedetect` acusando qualquer trecho reprova, exceto o quadro final do logo.
