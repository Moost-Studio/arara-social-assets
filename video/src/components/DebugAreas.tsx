import React from 'react';
import { SEGURA } from '../lib/tokens';
import { caixaRosto } from '../lib/rosto.js';

/** Área segura e caixa do rosto, só no Studio e nas prévias de conferência. Nunca na versão final. */
export const DebugAreas: React.FC<{ frame: number }> = ({ frame }) => {
  const r = caixaRosto(frame);
  return (
    <div style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
      <div style={{ position: 'absolute', left: SEGURA.x0, top: SEGURA.y0, width: SEGURA.x1 - SEGURA.x0, height: SEGURA.y1 - SEGURA.y0, border: '3px dashed #00B3FF' }} />
      {r && <div style={{ position: 'absolute', left: r[0], top: r[1], width: r[2] - r[0], height: r[3] - r[1], border: '4px solid #FF2D8D', background: 'rgba(255,45,141,0.12)' }} />}
    </div>
  );
};
