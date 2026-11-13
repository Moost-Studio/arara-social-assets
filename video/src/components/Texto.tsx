import React from 'react';
import { spring, useVideoConfig } from 'remotion';
import { COR, MOLA } from '../lib/tokens';

type Palavra = { t: string; marca?: boolean };
/** Palavras que entram uma a uma (mola), em Nunito ExtraBold. A palavra-chave leva marca-texto amarelo atrás (fundo claro, v6 5.4). */
export const Palavras: React.FC<{ frame: number; inicio: number; passo: number; palavras: Palavra[]; x?: number; y: number; tam?: number; cor?: string; largura?: number; linhaDepois?: number[] }> = ({ frame, inicio, passo, palavras, x = 64, y, tam = 104, cor = COR.noite, largura = 856, linhaDepois = [] }) => {
  const { fps } = useVideoConfig();
  const linhas: Palavra[][] = [[]];
  palavras.forEach((p, i) => { linhas[linhas.length - 1].push(p); if (linhaDepois.includes(i)) linhas.push([]); });
  let n = 0;
  return (
    <div style={{ position: 'absolute', left: x, top: y, width: largura, fontFamily: 'Nunito', fontWeight: 900, fontSize: tam, lineHeight: 1.12, color: cor }}>
      {linhas.map((l, li) => (
        <div key={li} style={{ display: 'flex', gap: tam * 0.26, flexWrap: 'wrap' }}>
          {l.map((p) => {
            const i = n++;
            const s = spring({ frame: frame - (inicio + i * passo), fps, config: MOLA });
            return (
              <span key={i} style={{ position: 'relative', display: 'inline-block', opacity: Math.min(1, s * 1.6), transform: `scale(${0.82 + 0.18 * s})`, transformOrigin: '0 100%', padding: '0 10px', margin: '0 -10px' }}>
                {p.marca && <span style={{ position: 'absolute', inset: '8px 0 0 0', background: COR.amarelo, borderRadius: 14, zIndex: -1, transform: `scaleX(${s})`, transformOrigin: '0 50%' }} />}
                {p.t}
              </span>
            );
          })}
        </div>
      ))}
    </div>
  );
};

/** Punchline em Mochiy Pop One, caixa alta, letra a letra (só no punchline, v6 5.4). */
export const TextoCinetico: React.FC<{ frame: number; inicio: number; texto: string; marcaDe?: number; y: number; tam?: number; x?: number; passo?: number }> = ({ frame, inicio, texto, marcaDe = -1, y, tam = 88, x = 64, passo = 1.6 }) => {
  const { fps } = useVideoConfig();
  return (
    <div style={{ position: 'absolute', left: x, top: y, fontFamily: 'Mochiy', fontSize: tam, lineHeight: 1.15, color: COR.noite, whiteSpace: 'pre', display: 'flex' }}>
      {texto.split('').map((c, i) => {
        const s = spring({ frame: frame - (inicio + i * passo), fps, config: { damping: 12, mass: 0.6, stiffness: 160 } });
        const marca = marcaDe >= 0 && i >= marcaDe && c !== '.';
        return (
          <span key={i} style={{ position: 'relative', display: 'inline-block', opacity: Math.min(1, s * 2), transform: `scale(${0.7 + 0.3 * s}) rotate(${(1 - s) * -6}deg)`, transformOrigin: '50% 100%' }}>
            {marca && <span style={{ position: 'absolute', inset: '12% -2px 4% -2px', background: COR.amarelo, borderRadius: 10, zIndex: -1 }} />}
            {c}
          </span>
        );
      })}
    </div>
  );
};

/** Pílula branca com ponto coral piscando (ex.: "Gravando a aula de hoje"). */
export const Pilula: React.FC<{ frame: number; texto: string; y: number; ponto?: boolean }> = ({ frame, texto, y, ponto = true }) => (
  <div style={{ position: 'absolute', left: 0, right: 0, top: y, display: 'flex', justifyContent: 'center' }}>
    <div style={{ display: 'flex', alignItems: 'center', gap: 22, background: COR.branco, color: COR.noite, fontFamily: 'Nunito', fontWeight: 900, fontSize: 50, padding: '20px 40px', borderRadius: 999, boxShadow: '0 6px 0 rgba(8,18,38,0.12)' }}>
      {ponto && <span style={{ width: 26, height: 26, borderRadius: 999, background: COR.coral, opacity: Math.floor(frame / 15) % 2 === 0 ? 1 : 0.25 }} />}
      {texto}
    </div>
  </div>
);

/** Equalizador de 5 barras parado, em linha reta (a Rara sem voz). */
export const Equalizador: React.FC<{ y: number }> = ({ y }) => (
  <div style={{ position: 'absolute', left: 0, right: 0, top: y, display: 'flex', justifyContent: 'center', gap: 18 }}>
    {[0, 1, 2, 3, 4].map((i) => <span key={i} style={{ width: 22, height: 8, borderRadius: 8, background: COR.noite, opacity: 0.55 }} />)}
  </div>
);
