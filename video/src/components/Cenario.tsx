import React from 'react';
import { COR } from '../lib/tokens';

/**
 * Cenário em camadas com profundidade. `cam` é o deslocamento horizontal da câmera (px): cada camada anda numa velocidade (parallax).
 * Fundo distante (0,25), objetos do meio (0,6), chão e sombra de contato junto da Rara (1,0) e bokeh desfocado no primeiro plano (1,7).
 */
export const Fundo: React.FC<{ frame: number; cam: number; cor1?: string; cor2?: string; estudio?: boolean; chaoY: number }> = ({ frame, cam, cor1 = COR.creme, cor2 = '#FFE9C2', estudio = true, chaoY }) => {
  const circ = (x: number, y: number, d: number, bg: string, par: number, blur = 0) => (
    <div style={{ position: 'absolute', left: x - cam * par - d / 2, top: y - d / 2, width: d, height: d, borderRadius: 999, background: bg, filter: blur ? `blur(${blur}px)` : undefined }} />
  );
  // partículas de luz subindo devagar (meio-plano, parallax 0,6); posição só depende do quadro
  const motas = Array.from({ length: 16 }, (_, i) => {
    const sx = (i * 193) % 1080, v = 0.35 + ((i * 37) % 10) / 22, y = ((i * 311) % 1900 - frame * v * 1.4 + 3800) % 1900;
    return <div key={i} style={{ position: 'absolute', left: sx - cam * 0.6 + 14 * Math.sin(frame / 40 + i), top: y, width: 8 + (i % 4) * 4, height: 8 + (i % 4) * 4, borderRadius: 99, background: 'rgba(255,255,255,0.65)', filter: 'blur(1.5px)' }} />;
  });
  return (
    <div style={{ position: 'absolute', inset: 0, overflow: 'hidden' }}>
      <div style={{ position: 'absolute', inset: 0, background: `linear-gradient(180deg, ${cor1} 0%, ${cor2} 100%)` }} />
      {circ(180, 640, 760, 'rgba(255,255,255,0.55)', 0.25)}
      {circ(960, 1010, 860, 'rgba(255,200,61,0.20)', 0.25)}
      {estudio && (
        <>
          <div style={{ position: 'absolute', left: 60 - cam * 0.6, top: chaoY - 600, width: 160, height: 600, borderRadius: 30, background: 'rgba(8,18,38,0.07)', filter: 'blur(3px)' }} />
          <div style={{ position: 'absolute', left: 850 - cam * 0.6, top: chaoY - 400, width: 200, height: 400, borderRadius: 40, background: 'rgba(36,87,230,0.10)', filter: 'blur(3px)' }} />
          {circ(790, 520, 120, 'rgba(255,107,91,0.35)', 0.6, 1)}
        </>
      )}
      {motas}
    </div>
  );
};

/** Plano do sujeito: mesa de gravação (ou chão), microfone com LED e sombra de contato. Anda junto com a Rara. */
export const Plano: React.FC<{ frame: number; chaoY: number; sombra: { x: number; y: number; w: number; alto: number }; mesa?: boolean }> = ({ frame, chaoY, sombra, mesa = false }) => (
  <div style={{ position: 'absolute', inset: 0 }}>
    {mesa ? (
      <>
        <div style={{ position: 'absolute', left: -140, top: chaoY + 70, width: 1360, bottom: 0, background: 'linear-gradient(180deg, #E9C890 0%, #D9AE74 60%, #C99A62 100%)' }} />
        <div style={{ position: 'absolute', left: -140, top: chaoY, width: 1360, height: 78, borderRadius: '30px 30px 14px 14px', background: 'linear-gradient(180deg, #FBE7BE 0%, #F3D39A 100%)', boxShadow: '0 10px 0 rgba(120,80,30,0.18)' }} />
        <div style={{ position: 'absolute', left: -140, top: chaoY, width: 1360, height: 6, background: 'rgba(255,255,255,0.75)' }} />
        <div style={{ position: 'absolute', left: 168, top: chaoY - 24, width: 130, height: 28, borderRadius: 14, background: '#1A2B52' }} />
        <div style={{ position: 'absolute', left: 224, top: chaoY - 420, width: 18, height: 410, borderRadius: 9, background: '#2B3F70' }} />
        <div style={{ position: 'absolute', left: 190, top: chaoY - 640, width: 86, height: 236, borderRadius: 44, background: 'repeating-linear-gradient(0deg,#2B3F70 0 7px,#1A2B52 7px 14px)', border: '5px solid #0F1B3A' }} />
        <div style={{ position: 'absolute', left: 205, top: chaoY - 620, width: 20, height: 150, borderRadius: 10, background: 'rgba(255,255,255,0.22)' }} />
        <div style={{ position: 'absolute', left: 221, top: chaoY - 392, width: 24, height: 24, borderRadius: 99, background: '#FF6B5B', opacity: Math.floor(frame / 15) % 2 === 0 ? 1 : 0.25, boxShadow: '0 0 18px rgba(255,107,91,0.9)' }} />
      </>
    ) : (
      <>
        <div style={{ position: 'absolute', left: -140, width: 1360, top: chaoY, bottom: 0, background: 'linear-gradient(180deg, rgba(190,150,100,0.26) 0%, rgba(190,150,100,0.12) 20%, rgba(190,150,100,0.05) 100%)' }} />
        <div style={{ position: 'absolute', left: -140, width: 1360, top: chaoY - 2, height: 4, background: 'rgba(8,18,38,0.05)' }} />
      </>
    )}
    <div style={{ position: 'absolute', left: sombra.x - sombra.w / 2, top: sombra.y - 18, width: sombra.w, height: 36, borderRadius: '50%', background: 'radial-gradient(ellipse, rgba(8,18,38,0.38), rgba(8,18,38,0) 70%)', filter: 'blur(6px)', opacity: sombra.alto }} />
  </div>
);

/** Primeiro plano: círculos de luz desfocados passando mais rápido que a Rara. Dá escala e profundidade; ficam nas bordas, longe do rosto. */
export const PrimeiroPlano: React.FC<{ frame: number; cam: number }> = ({ frame, cam }) => {
  const b = (x: number, y: number, d: number, a: number, par: number, fase: number) => (
    <div style={{ position: 'absolute', left: x - cam * par - d / 2 + 22 * Math.sin(frame / 70 + fase), top: y - d / 2 + 14 * Math.cos(frame / 90 + fase), width: d, height: d, borderRadius: 999, background: `rgba(255,236,190,${a})`, filter: 'blur(26px)' }} />
  );
  return (
    <div style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
      {b(60, 1500, 300, 0.45, 1.7, 0)}
      {b(1020, 1380, 360, 0.38, 1.9, 2)}
      {b(980, 330, 220, 0.30, 1.5, 4)}
      <div style={{ position: 'absolute', inset: 0, background: 'radial-gradient(ellipse 75% 62% at 50% 52%, rgba(0,0,0,0) 55%, rgba(8,18,38,0.10) 100%)' }} />
    </div>
  );
};
