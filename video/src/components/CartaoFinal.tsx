import React from 'react';
import { Img, spring, staticFile, useVideoConfig } from 'remotion';
import { COR, MOLA } from '../lib/tokens';
import { rampa } from '../lib/anim';

/** Cartão final: escurece em 0,3 s para Azul-Noite, o selo entra com mola e a pílula "falearara.com" depois. Um único movimento de entrada, sem salto duplo. */
export const CartaoFinal: React.FC<{ frame: number; inicio: number; mostrarTexto?: boolean }> = ({ frame, inicio, mostrarTexto = true }) => {
  const { fps } = useVideoConfig();
  const fundo = rampa(frame, inicio, inicio + 9, 0, 1);
  if (fundo <= 0) return null;
  const selo = spring({ frame: frame - (inicio + 5), fps, config: MOLA });
  const pil = spring({ frame: frame - (inicio + 20), fps, config: MOLA });
  return (
    <div style={{ position: 'absolute', inset: 0, background: `rgba(8,18,38,${fundo})` }}>
      <Img src={staticFile('assets/logo/selo.png')} style={{ position: 'absolute', left: 190, top: 560, width: 700, height: 700, opacity: Math.min(1, selo * 1.5), transform: `scale(${0.6 + 0.4 * selo})` }} />
      {mostrarTexto && (
        <div style={{ position: 'absolute', left: 0, right: 0, top: 1250, display: 'flex', justifyContent: 'center', opacity: Math.min(1, pil * 1.5), transform: `scale(${0.85 + 0.15 * pil})` }}>
          <div style={{ background: COR.creme, color: COR.noite, fontFamily: 'Nunito', fontWeight: 900, fontSize: 60, padding: '20px 52px', borderRadius: 999 }}>falearara.com</div>
        </div>
      )}
    </div>
  );
};
