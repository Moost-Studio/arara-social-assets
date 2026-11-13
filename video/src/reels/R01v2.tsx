import React from 'react';
import { AbsoluteFill, Audio, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import '../fonts';
import { COR, MOLA } from '../lib/tokens';
import { easeIn, rampa } from '../lib/anima.js';
import { RaraRig } from '../components/RaraRig';
import { Fundo, Plano, PrimeiroPlano } from '../components/Cenario';
import { Equalizador, Palavras, Pilula, TextoCinetico } from '../components/Texto';
import { BorraoX } from '../components/Camera';
import { CartaoFinal } from '../components/CartaoFinal';
import { camera, rara, caixaRosto } from './R01v2.timeline.js';
import { RIG, deforma, matrizes, escalaPara, paraTela, PARAMS0 } from '../lib/rig.js';
import { SEGURA } from '../lib/tokens';
import type { R01PropsT } from '../schema';

const sfx = (n: string) => staticFile(`assets/sfx/${n}.wav`);

/** Uma cena: cenário em camadas + Rara rigada, tudo dentro da câmera (zoom e parallax). */
const Cena: React.FC<{ f: number; tipo: 'estudio' | 'chá'; cor1?: string; cor2?: string; mesa?: boolean; children?: React.ReactNode }> = ({ f, tipo, cor1, cor2, mesa, children }) => {
  const r = rara(f); const c = camera(f);
  const altoSombra = Math.max(0.35, 1 - (r.params.hop || 0) / 120);
  const escala = escalaPara(r.pose, r.altura);
  const D = RIG[r.pose];
  const pesY = r.lugar[1] - (D.bbox[3] - D.points.feet[1]) * escala;   // linha dos pés na tela
  return (
    <AbsoluteFill>
      <div style={{ position: 'absolute', inset: 0, transform: `translateY(${-c.y}px) scale(${c.z})`, transformOrigin: '50% 50%' }}>
        <Fundo frame={f} cam={c.x} estudio={tipo === 'estudio'} cor1={cor1} cor2={cor2} chaoY={pesY + 4} />
        <div style={{ position: 'absolute', inset: 0, transform: `translateX(${-c.x}px)` }}>
          <Plano frame={f} chaoY={pesY + 4} mesa={mesa} sombra={{ x: r.lugar[0] - 10, y: pesY + 4, w: 420 * (r.altura / 900) * (0.55 + 0.45 * altoSombra), alto: altoSombra }} />
          <RaraRig key={r.pose} pose={r.pose} variante={r.variante} altura={r.altura} lugar={r.lugar as [number, number]} params={r.params} />
          {children}
        </div>
      </div>
      <PrimeiroPlano frame={f} cam={c.x} />
    </AbsoluteFill>
  );
};

/** Posição e giro do bilhete da PV01 na tela, seguindo o corpo da Rara (só o osso do corpo mexe nele). */
function bilhete(f: number) {
  const r = rara(f); const D = RIG.PV01_v1; const M = matrizes(D.points, { ...PARAMS0, ...r.params });
  const [bx0, by0, bx1, by1] = D.bilhete; const s = escalaPara('PV01_v1', r.altura);
  const c = deforma(D.tipo, D.points, M, (bx0 + bx1) / 2, (by0 + by1) / 2);
  const t = paraTela('PV01_v1', c, s, r.lugar);
  return { x: t[0], y: t[1], w: (bx1 - bx0) * s, h: (by1 - by0) * s, giro: r.params.body || 0 };
}

export const R01v2: React.FC<R01PropsT> = (p) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const aX = f < 150 ? 0 : rampa(f, 150, 157, 0, -1300, easeIn);
  const aBlur = f < 150 || f > 158 ? 0 : 26;
  const sB = spring({ frame: f - 156, fps, config: MOLA });
  const bX = f < 266 ? (f < 156 ? 1300 : (1 - sB) * 1300) : rampa(f, 266, 272, 0, -1300, easeIn);
  const bBlur = f < 156 ? 0 : f < 266 ? Math.max(0, (1 - sB) * 30) : f < 273 ? 26 : 0;
  const sC = spring({ frame: f - 268, fps, config: MOLA });
  const cX = f < 268 ? 1300 : (1 - sC) * 1300;
  const cBlur = f < 268 ? 0 : Math.max(0, (1 - sC) * 30);
  const topo = p.variante === 'dia20' ? 'VOLTO DIA 20.' : 'VOLTO LOGO.';
  const marcaDe = p.variante === 'dia20' ? 10 : 6;
  const sBil = spring({ frame: f - 175, fps, config: MOLA });
  const bil = f >= 155 && f < 280 ? bilhete(f) : null;
  const c = camera(f);
  const rosto = caixaRosto(f);

  return (
    <AbsoluteFill style={{ background: COR.creme, overflow: 'hidden' }}>
      {f < 160 && (
        <BorraoX id="bxa" qtd={aBlur}>
          <div style={{ position: 'absolute', inset: 0, transform: `translateX(${aX}px)` }}>
            <Cena f={f} tipo="estudio" mesa />
            {!p.semTexto && (
              <>
                <Pilula frame={f} texto="Gravando a aula de hoje" y={250} />
                <Equalizador y={410} />
                {f >= 100 && <Palavras frame={f} inicio={100} passo={6} palavras={[{ t: 'Nada.' }, { t: 'Nem' }, { t: 'um' }, { t: 'pio.', marca: true }]} linhaDepois={[0]} y={470} tam={112} />}
              </>
            )}
          </div>
        </BorraoX>
      )}

      {f >= 155 && f < 280 && (
        <BorraoX id="bxb" qtd={bBlur}>
          <div style={{ position: 'absolute', inset: 0, transform: `translateX(${bX}px)` }}>
            <Cena f={f} tipo="estudio" cor1="#FFF5E1" cor2="#FFE2B0">
              {!p.semTexto && f >= 175 && bil && (
                <div style={{ position: 'absolute', left: bil.x - bil.w / 2, top: bil.y - bil.h / 2, width: bil.w, height: bil.h, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: 'Nunito', fontWeight: 900, fontSize: 60, color: COR.noite, opacity: Math.min(1, sBil * 1.6), transform: `rotate(${bil.giro - 1}deg) scale(${0.8 + 0.2 * sBil})` }}>Perdi a voz.</div>
              )}
            </Cena>
            {!p.semTexto && f >= 200 && <TextoCinetico frame={f} inicio={200} texto={topo} marcaDe={marcaDe} y={330} tam={80} />}
          </div>
        </BorraoX>
      )}

      {f >= 266 && f < 385 && (
        <BorraoX id="bxc" qtd={cBlur}>
          <div style={{ position: 'absolute', inset: 0, transform: `translateX(${cX}px)` }}>
            <Cena f={f} tipo="chá" cor1="#F0B27A" cor2="#E39A60" />
            {!p.semTexto && f >= 285 && <Palavras frame={f} inicio={285} passo={4} palavras={[{ t: 'Até' }, { t: 'lá,' }, { t: 'eu' }, { t: 'falo' }, { t: 'por' }, { t: 'bilhete.', marca: true }]} linhaDepois={[3]} y={300} tam={96} />}
          </div>
        </BorraoX>
      )}

      <CartaoFinal frame={f} inicio={375} mostrarTexto={!p.semTexto} />
      {p.debug && (
        <div style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
          <div style={{ position: 'absolute', left: SEGURA.x0, top: SEGURA.y0, width: SEGURA.x1 - SEGURA.x0, height: SEGURA.y1 - SEGURA.y0, border: '3px dashed #00B3FF' }} />
          {rosto && <div style={{ position: 'absolute', left: rosto[0], top: rosto[1], width: rosto[2] - rosto[0], height: rosto[3] - rosto[1], border: '4px solid #FF2D8D', background: 'rgba(255,45,141,0.12)' }} />}
        </div>
      )}

      <Sequence from={3}><Audio src={sfx('toque_microfone')} volume={0.8} /></Sequence>
      <Sequence from={46}><Audio src={sfx('pop')} volume={0.25} /></Sequence>
      <Sequence from={78}><Audio src={sfx('pop')} volume={0.35} /></Sequence>
      <Sequence from={150}><Audio src={sfx('whoosh_saida')} volume={0.7} /></Sequence>
      <Sequence from={285}><Audio src={sfx('pop')} volume={0.35} /></Sequence>
      {p.trilha && <Sequence from={165}><Audio src={staticFile(p.trilha)} volume={(g) => rampa(g, 0, 35, 0.05, 0.5)} /></Sequence>}
    </AbsoluteFill>
  );
};
