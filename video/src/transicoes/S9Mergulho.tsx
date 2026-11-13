/**
 * S9 Mergulho na tela genuina. Duracao 14 a 18 quadros, rampa `padrao`.
 * Quando usar: saida para a gravacao REAL do app (nunca uma tela inventada).
 * A cena de saida e o celular; a gravacao (cena seguinte) abre da area da tela do celular ate preencher o quadro,
 * sem mudar o conteudo capturado. Versao 2D; celular 3D em proporcao real pede @remotion/three (aguarda OK).
 * `tela` e o retangulo da tela do celular na cena anterior, em px de 1080x1920.
 */
import React from 'react';
import { interpolate } from 'remotion';
import type { TransitionPresentation, TransitionPresentationComponentProps } from '@remotion/transitions';
import { EASE } from './_util';

export type S9Props = { tela: { x: number; y: number; w: number; h: number; raio?: number } };

const Comp: React.FC<TransitionPresentationComponentProps<S9Props>> = ({ children, presentationDirection, presentationProgress: p, passedProps }) => {
  const { tela } = passedProps;
  const t = EASE.padrao(p);
  if (presentationDirection === 'exiting') {
    const s = interpolate(t, [0, 1], [1, 1920 / tela.h]);
    return <div style={{ position: 'absolute', inset: 0, transformOrigin: `${tela.x + tela.w / 2}px ${tela.y + tela.h / 2}px`, transform: `scale(${s})`, opacity: interpolate(p, [0.6, 1], [1, 0]) }}>{children}</div>;
  }
  const l = interpolate(t, [0, 1], [tela.x, 0]);
  const tp = interpolate(t, [0, 1], [tela.y, 0]);
  const r = interpolate(t, [0, 1], [1080 - tela.x - tela.w, 0]);
  const b = interpolate(t, [0, 1], [1920 - tela.y - tela.h, 0]);
  const raio = interpolate(t, [0, 1], [tela.raio ?? 56, 0]);
  return <div style={{ position: 'absolute', inset: 0, clipPath: `inset(${tp}px ${r}px ${b}px ${l}px round ${raio}px)` }}>{children}</div>;
};
export const mergulho_tela = (props: S9Props): TransitionPresentation<S9Props> => ({ component: Comp, props });
