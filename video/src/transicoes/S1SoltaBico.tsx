/**
 * S1 Solta o bico. Duracao 12 a 16 quadros a 30 fps, curva `saida` na mascara.
 * Quando usar: inicio de fala, virada do gancho, saida para a tela do app.
 * Aneis nascem do bico (props.bico) com 3 quadros de intervalo; a espessura segue `amplitude`
 * (0 a 1, vinda de visualizeAudio da fala). O ultimo anel vira a mascara circular que revela a cena seguinte.
 * Nao usar anel sem vinculo com a voz nem cor fora da paleta.
 */
import React from 'react';
import { interpolate } from 'remotion';
import type { TransitionPresentation, TransitionPresentationComponentProps } from '@remotion/transitions';
import { EASE, PALETA } from './_util';

export type S1Props = { bico: { x: number; y: number }; amplitude?: number; aneis?: number };

const Comp: React.FC<TransitionPresentationComponentProps<S1Props>> = ({ children, presentationDirection, presentationProgress: p, passedProps }) => {
  const { bico, amplitude = 0.7, aneis = 4 } = passedProps;
  const R = Math.hypot(1080, 1920);
  const raio = interpolate(p, [0, 1], [0, R], { easing: EASE.saida });
  if (presentationDirection === 'exiting') return <div style={{ position: 'absolute', inset: 0 }}>{children}</div>;
  return (
    <div style={{ position: 'absolute', inset: 0 }}>
      <div style={{ position: 'absolute', inset: 0, clipPath: `circle(${raio}px at ${bico.x}px ${bico.y}px)` }}>{children}</div>
      <svg width={1080} height={1920} style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
        {Array.from({ length: aneis }).map((_, i) => {
          const q = Math.max(0, p - (i * 3) / 14);
          const r = interpolate(q, [0, 1], [0, R * 0.9], { easing: EASE.saida, extrapolateRight: 'clamp' });
          const alpha = interpolate(q, [0, 0.1, 0.8, 1], [0, 1, 0.6, 0]);
          return <circle key={i} cx={bico.x} cy={bico.y} r={r} fill="none" stroke={i % 2 ? PALETA.amarelo : PALETA.azul} strokeWidth={6 + amplitude * 22} opacity={alpha} />;
        })}
      </svg>
    </div>
  );
};
export const solta_bico = (props: S1Props): TransitionPresentation<S1Props> => ({ component: Comp, props });
