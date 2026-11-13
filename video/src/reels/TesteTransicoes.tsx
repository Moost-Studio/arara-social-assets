// Teste visual das 4 assinaturas com cenas de cor chapada (nao e reel; sem arte nem custo).
import React from 'react';
import { AbsoluteFill } from 'remotion';
import { TransitionSeries, linearTiming } from '@remotion/transitions';
import { solta_bico, balao_torto, pena_cortina, mergulho_tela } from '../transicoes';

const Cena: React.FC<{ cor: string; txt: string }> = ({ cor, txt }) => (
  <AbsoluteFill style={{ background: cor, color: '#fff', fontFamily: 'Nunito', fontSize: 120, fontWeight: 900, justifyContent: 'center', alignItems: 'center' }}>{txt}</AbsoluteFill>
);
const cores = ['#081226', '#2457E6', '#FFC83D', '#22B573', '#FF6B5B'];
export const TesteTransicoes: React.FC = () => (
  <TransitionSeries>
    <TransitionSeries.Sequence durationInFrames={30}><Cena cor={cores[0]} txt="A" /></TransitionSeries.Sequence>
    <TransitionSeries.Transition presentation={solta_bico({ bico: { x: 540, y: 900 } })} timing={linearTiming({ durationInFrames: 14 })} />
    <TransitionSeries.Sequence durationInFrames={30}><Cena cor={cores[1]} txt="B" /></TransitionSeries.Sequence>
    <TransitionSeries.Transition presentation={balao_torto({ origem: { x: 540, y: 700 } })} timing={linearTiming({ durationInFrames: 10 })} />
    <TransitionSeries.Sequence durationInFrames={30}><Cena cor={cores[2]} txt="C" /></TransitionSeries.Sequence>
    <TransitionSeries.Transition presentation={pena_cortina()} timing={linearTiming({ durationInFrames: 8 })} />
    <TransitionSeries.Sequence durationInFrames={30}><Cena cor={cores[3]} txt="D" /></TransitionSeries.Sequence>
    <TransitionSeries.Transition presentation={mergulho_tela({ tela: { x: 240, y: 380, w: 600, h: 1100 } })} timing={linearTiming({ durationInFrames: 16 })} />
    <TransitionSeries.Sequence durationInFrames={30}><Cena cor={cores[4]} txt="E" /></TransitionSeries.Sequence>
  </TransitionSeries>
);
