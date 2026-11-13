import React from 'react';
import { Img, staticFile } from 'remotion';
import { rampa } from '../lib/anim';

// A Rara em camadas: o K00 é a base e os remendos (bico, olhos, topete, já recortados pela máscara) entram por cima.
// `camadas` guarda a opacidade (0..1) de cada remendo; quem calcula é o reel (troca em 2 quadros, nunca corte seco).
export type Camadas = Partial<Record<'bico_K01' | 'bico_K02' | 'olhos_K03' | 'olhos_K04' | 'olhos_K05' | 'topete_K06' | 'topete_K07' | 'topete_K08', number>>;
const kit = (n: string) => staticFile(`assets/kit/${n}.png`);
const TAM = 1080; // o quadro 1024 entra com a largura do quadro de vídeo

export const RaraCamadas: React.FC<{ frame: number; camadas: Camadas; dy?: number; giro?: number; topoY?: number }> = ({ frame, camadas, dy = 0, giro = 0, topoY = 1920 - TAM }) => {
  // respiração de 1,5% em 2,4 s e balanço de 1,5 grau em 3 s, pivô na base (v6 6.5)
  const resp = 1 + 0.015 * Math.sin((2 * Math.PI * frame) / 72);
  const bal = 1.5 * Math.sin((2 * Math.PI * frame) / 90);
  const estilo: React.CSSProperties = { position: 'absolute', left: 0, top: topoY + dy, width: TAM, height: TAM, transformOrigin: '50% 100%', transform: `rotate(${bal + giro}deg) scaleY(${resp})` };
  const img = (src: string, op = 1) => <Img key={src} src={kit(src)} style={{ position: 'absolute', inset: 0, width: TAM, height: TAM, opacity: op }} />;
  return (
    <div style={estilo}>
      {img('rara_quadro_K00')}
      {Object.entries(camadas).map(([k, v]) => {
        if (!v) return null;
        const [g, n] = k.split('_');
        return img(`rara_remendo_${g}_${n}`, v);
      })}
    </div>
  );
};
export { rampa };
