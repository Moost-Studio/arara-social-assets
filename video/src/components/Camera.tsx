import React from 'react';
import { zoom } from '../lib/rosto.js';

/** Aproximação lenta e deriva de 0,5 a 1 px (câmera viva). Nada linear: o zoom vem de lib/rosto.js, o mesmo usado no QA do rosto. */
export const CameraViva: React.FC<{ frame: number; children: React.ReactNode; tremer?: number }> = ({ frame, children, tremer = 0 }) => {
  const z = zoom(frame);
  const dx = 0.8 * Math.sin(frame / 23) + (tremer ? tremer * Math.sin(frame * 3.1) : 0);
  const dy = 0.6 * Math.cos(frame / 29) + (tremer ? tremer * Math.cos(frame * 2.3) : 0);
  return <div style={{ position: 'absolute', inset: 0, transform: `translate(${dx}px, ${dy}px) scale(${z})`, transformOrigin: '50% 50%' }}>{children}</div>;
};

/** Desfoque de movimento horizontal (chicote de câmera). */
export const BorraoX: React.FC<{ id: string; qtd: number; children: React.ReactNode }> = ({ id, qtd, children }) => (
  <>
    <svg width="0" height="0" style={{ position: 'absolute' }}><filter id={id} x="-20%" y="-5%" width="140%" height="110%"><feGaussianBlur stdDeviation={`${qtd} 0`} /></filter></svg>
    <div style={{ position: 'absolute', inset: 0, filter: qtd > 0.2 ? `url(#${id})` : undefined }}>{children}</div>
  </>
);
