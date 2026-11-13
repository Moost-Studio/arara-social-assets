/**
 * S6 Pena-cortina. Duracao 6 a 8 quadros, travessia diagonal em primeiro plano; o corte acontece escondido no meio.
 * Quando usar: no lugar de qualquer corte seco entre clipes de IA.
 * Versao 2D (SVG com gradiente azul, turquesa e verde da cauda, desfoque e rotacao). A versao com pena 3D real
 * pede @remotion/three e aguarda o OK do Rodrigo para instalar.
 */
import React from 'react';
import { interpolate } from 'remotion';
import type { TransitionPresentation, TransitionPresentationComponentProps } from '@remotion/transitions';
import { EASE, PALETA } from './_util';

const Comp: React.FC<TransitionPresentationComponentProps<Record<string, never>>> = ({ children, presentationDirection, presentationProgress: p }) => {
  const visivel = presentationDirection === 'entering' ? p >= 0.5 : p < 0.5;
  const t = EASE.padrao(p);
  const x = interpolate(t, [0, 1], [-500, 1600]);
  const y = interpolate(t, [0, 1], [-300, 2200]);
  const rot = interpolate(t, [0, 1], [-35, 55]);
  return (
    <div style={{ position: 'absolute', inset: 0 }}>
      {visivel && <div style={{ position: 'absolute', inset: 0 }}>{children}</div>}
      {presentationDirection === 'entering' && (
        <svg width={1080} height={1920} style={{ position: 'absolute', inset: 0, pointerEvents: 'none', filter: 'blur(3px)' }}>
          <defs>
            <linearGradient id="pena" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0" stopColor={PALETA.azul} /><stop offset="0.55" stopColor={PALETA.turquesa} /><stop offset="1" stopColor={PALETA.verde} />
            </linearGradient>
          </defs>
          <g transform={`translate(${x} ${y}) rotate(${rot}) scale(${interpolate(Math.sin(p * Math.PI), [0, 1], [1.2, 2.6])})`}>
            <path d="M0 -420 C 160 -300 190 40 0 420 C -190 40 -160 -300 0 -420 Z" fill="url(#pena)" />
            <path d="M0 -380 L0 400" stroke="#fff" strokeOpacity="0.35" strokeWidth="6" />
          </g>
        </svg>
      )}
    </div>
  );
};
export const pena_cortina = (): TransitionPresentation<Record<string, never>> => ({ component: Comp, props: {} });
