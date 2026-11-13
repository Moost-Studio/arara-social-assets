import React from 'react';
import { AbsoluteFill, Audio, Img, Sequence, spring, staticFile, useCurrentFrame, useVideoConfig } from 'remotion';
import '../fonts';
import { COR, MOLA } from '../lib/tokens';
import { easeIn, janela, rampa } from '../lib/anim';
import { RaraCamadas, type Camadas } from '../components/RaraCamadas';
import { Equalizador, Palavras, Pilula, TextoCinetico } from '../components/Texto';
import { BorraoX, CameraViva } from '../components/Camera';
import { CartaoFinal } from '../components/CartaoFinal';
import { DebugAreas } from '../components/DebugAreas';
import { dyKit } from '../lib/rosto.js';
import type { R01PropsT } from '../schema';

// R01 "Perdi a voz" (15,0 s, 450 quadros a 30 fps). Roteiro: reels_plano_remotion_v1.md, seção 4.1.
// Quadros: cena 1 gancho 0 a 77, cena 2 nada 78 a 149, cena 3 chicote 150 a 164, cena 4 bilhete 165 a 269,
// cena 5 chá 270 a 374, cena 6 cartão final 375 a 449.
const sfx = (n: string) => staticFile(`assets/sfx/${n}.wav`);

const Fundo: React.FC = () => (
  <AbsoluteFill style={{ background: `linear-gradient(180deg, ${COR.creme} 0%, #FFEFD0 100%)` }}>
    <div style={{ position: 'absolute', left: -240, top: 260, width: 760, height: 760, borderRadius: 999, background: 'rgba(255,255,255,0.6)' }} />
    <div style={{ position: 'absolute', right: -260, top: 640, width: 820, height: 820, borderRadius: 999, background: 'rgba(255,200,61,0.20)' }} />
  </AbsoluteFill>
);

/** Camadas da Rara para os quadros 0 a 149 (todas por janela de 2 quadros). */
function camadasDo(f: number): Camadas {
  return {
    olhos_K03: janela(f, 12, 14),                                   // piscada
    topete_K06: janela(f, 30, 98),                                  // topete sobe na antecipação, fica até a sacudida
    bico_K02: janela(f, 46, 77),                                    // bico aberto de uma vez, sem som
    olhos_K05: janela(f, 80, 149),                                  // olhos para o lado, confusa
    topete_K08: janela(f, 99, 149),                                 // espiral, trocado escondido na sacudida (q96 a 100)
    bico_K01: Math.max(janela(f, 104, 111), janela(f, 122, 130)),   // duas tentativas de falar (curva escrita à mão)
  };
}
const giroCabeca = (f: number) => (f < 96 || f > 100 ? 0 : [0, 2, -2, 1.5, 0][f - 96]);

const Cena1e2: React.FC<{ f: number; p: R01PropsT }> = ({ f, p }) => (
  <AbsoluteFill>
    <Fundo />
    <CameraViva frame={f}>
      <RaraCamadas frame={f} camadas={camadasDo(f)} dy={dyKit(f)} giro={giroCabeca(f)} />
    </CameraViva>
    {!p.semTexto && f < 150 && (
      <>
        <Pilula frame={f} texto="Gravando a aula de hoje" y={250} />
        <Equalizador y={410} />
        {f >= 100 && <Palavras frame={f} inicio={100} passo={6} palavras={[{ t: 'Nada.' }, { t: 'Nem' }, { t: 'um' }, { t: 'pio.', marca: true }]} linhaDepois={[0]} y={520} tam={112} />}
      </>
    )}
  </AbsoluteFill>
);

const ArteCobertura: React.FC<{ nome: string }> = ({ nome }) => (
  <Img src={staticFile(`assets/artes/${nome}.png`)} style={{ position: 'absolute', left: -1, top: -1, width: 1082, height: 1923 }} />
);

export const R01: React.FC<R01PropsT> = (p) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Chicote 1 (cena 3): cena 1+2 sai para a esquerda; o bilhete entra pela direita e assenta com mola.
  const aX = f < 150 ? 0 : rampa(f, 150, 157, 0, -1300, easeIn);
  const aBlur = f < 150 || f > 158 ? 0 : 26;
  const sB = spring({ frame: f - 156, fps, config: MOLA });
  const bEntra = f < 156 ? 1300 : (1 - sB) * 1300;
  const bSai = f < 266 ? 0 : rampa(f, 266, 272, 0, -1300, easeIn);
  const bX = f < 266 ? bEntra : bSai;
  const bBlur = f < 156 ? 0 : f < 266 ? Math.max(0, (1 - sB) * 30) : f < 273 ? 26 : 0;
  // Chicote 2 (cena 4 para 5): corte em movimento para o chá
  const sC = spring({ frame: f - 268, fps, config: MOLA });
  const cX = f < 268 ? 1300 : (1 - sC) * 1300;
  const cBlur = f < 268 ? 0 : Math.max(0, (1 - sC) * 30);
  const tremer = f >= 214 && f <= 217 ? 2 : 0;

  const topo = p.variante === 'dia20' ? 'VOLTO DIA 20.' : 'VOLTO LOGO.';
  const marcaDe = p.variante === 'dia20' ? 10 : 6;
  const sBil = spring({ frame: f - 175, fps, config: MOLA });

  return (
    <AbsoluteFill style={{ background: COR.creme, overflow: 'hidden' }}>
      {f < 160 && <BorraoX id="bxa" qtd={aBlur}><div style={{ position: 'absolute', inset: 0, transform: `translateX(${aX}px)` }}><Cena1e2 f={f} p={p} /></div></BorraoX>}

      {f >= 155 && f < 280 && (
        <BorraoX id="bxb" qtd={bBlur}>
          <div style={{ position: 'absolute', inset: 0, transform: `translateX(${bX}px)`, background: COR.creme }}>
            <CameraViva frame={f} tremer={tremer}>
              <ArteCobertura nome="PV01_v1" />
              {!p.semTexto && f >= 175 && (
                <div style={{ position: 'absolute', left: 310, top: 1195, width: 370, height: 190, display: 'flex', alignItems: 'center', justifyContent: 'center', fontFamily: 'Nunito', fontWeight: 900, fontSize: 60, color: COR.noite, opacity: Math.min(1, sBil * 1.6), transform: `scale(${0.8 + 0.2 * sBil}) rotate(-1deg)` }}>Perdi a voz.</div>
              )}
            </CameraViva>
            {!p.semTexto && f >= 200 && <TextoCinetico frame={f} inicio={200} texto={topo} marcaDe={marcaDe} y={330} tam={80} />}
          </div>
        </BorraoX>
      )}

      {f >= 266 && f < 385 && (
        <BorraoX id="bxc" qtd={cBlur}>
          <div style={{ position: 'absolute', inset: 0, transform: `translateX(${cX}px)`, background: '#E8A870' }}>
            <CameraViva frame={f}><ArteCobertura nome="PV04_v2" /></CameraViva>
            {!p.semTexto && f >= 285 && <Palavras frame={f} inicio={285} passo={4} palavras={[{ t: 'Até' }, { t: 'lá,' }, { t: 'eu' }, { t: 'falo' }, { t: 'por' }, { t: 'bilhete.', marca: true }]} linhaDepois={[3]} y={300} tam={96} />}
          </div>
        </BorraoX>
      )}

      <CartaoFinal frame={f} inicio={375} mostrarTexto={!p.semTexto} />
      {p.debug && <DebugAreas frame={f} />}

      {/* Sons: toque do microfone, pop ao fechar o bico, chicote, pop ao entrar o texto do chá. Silêncio total do q46 ao q78. */}
      <Sequence from={3}><Audio src={sfx('toque_microfone')} volume={0.8} /></Sequence>
      <Sequence from={78}><Audio src={sfx('pop')} volume={0.35} /></Sequence>
      <Sequence from={150}><Audio src={sfx('whoosh_saida')} volume={0.7} /></Sequence>
      <Sequence from={285}><Audio src={sfx('pop')} volume={0.35} /></Sequence>
      {p.trilha && <Sequence from={165}><Audio src={staticFile(p.trilha)} volume={(g) => rampa(g, 0, 35, 0.05, 0.5)} /></Sequence>}
    </AbsoluteFill>
  );
};
