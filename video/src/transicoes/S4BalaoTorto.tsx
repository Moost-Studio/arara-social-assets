/**
 * S4 Balao torto (portal). Duracao 10 quadros, curva `saida`, push-in simultaneo e desfoque radial nos 3 finais.
 * Quando usar: mudanca de tempo ou lugar ("na call", "no aeroporto"), inicio de dialogo.
 * O balao branco, inclinado -4 graus, rabicho torto e borda inferior mais grossa, cresce de 0,3 a 4,0 e a cena seguinte acontece dentro dele.
 */
import React from 'react';
import { interpolate } from 'remotion';
import type { TransitionPresentation, TransitionPresentationComponentProps } from '@remotion/transitions';
import { EASE } from './_util';

export type S4Props = { origem: { x: number; y: number } };

const Comp: React.FC<TransitionPresentationComponentProps<S4Props>> = ({ children, presentationDirection, presentationProgress: p, passedProps }) => {
  const { origem } = passedProps;
  const e = EASE.saida(p);
  const escala = interpolate(e, [0, 1], [0.3, 4]);
  const final = p > 0.7;
  const filtro = final ? `blur(${interpolate(p, [0.7, 1], [0, 10])}px)` : undefined;
  const balao = (
    <div style={{ position: 'absolute', left: origem.x, top: origem.y, width: 520, height: 360, transform: `translate(-50%,-50%) rotate(-4deg) scale(${escala})`, transformOrigin: 'center' }}>
      <div style={{ position: 'absolute', inset: 0, background: '#fff', borderRadius: 120, borderBottom: '14px solid #E8EEF9' }} />
      <div style={{ position: 'absolute', left: 60, bottom: -70, width: 90, height: 90, background: '#fff', borderBottom: '14px solid #E8EEF9', clipPath: 'polygon(0 0, 100% 0, 30% 100%)', transform: 'rotate(8deg)' }} />
    </div>
  );
  if (presentationDirection === 'exiting')
    return <div style={{ position: 'absolute', inset: 0, transform: `scale(${1 + 0.15 * e})`, filter: filtro }}>{children}{balao}</div>;
  return (
    <div style={{ position: 'absolute', inset: 0, clipPath: `ellipse(${260 * escala}px ${180 * escala}px at ${origem.x}px ${origem.y}px)` }}>
      <div style={{ position: 'absolute', inset: 0, transform: `scale(${interpolate(e, [0, 1], [1.1, 1])})`, filter: filtro }}>{children}</div>
    </div>
  );
};
export const balao_torto = (props: S4Props): TransitionPresentation<S4Props> => ({ component: Comp, props });
