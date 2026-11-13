// R01 "Perdi a voz", versão 2 com a Rara rigada (corpo inteiro, 6 ossos). Tudo é função pura do quadro f, para o Remotion e para o QA do rosto.
import { clamp, easeIn, janela, rampa, repouso, soma, impulso, pulo } from '../lib/anima.js';
import { caixaRostoTela, escalaPara } from '../lib/rig.js';

export const DUR = 450;
const CX = 540, CY = 960;
/** Câmera: zoom e deslocamento (px) por quadro. */
export function camera(f) {
  let z;
  if (f < 150) z = f < 46 ? 1.0 : f < 78 ? rampa(f, 46, 77, 1.0, 1.05) : rampa(f, 78, 149, 1.05, 1.07);
  else if (f < 270) z = rampa(f, 165, 269, 1.0, 1.05);
  else z = rampa(f, 270, 374, 1.0, 1.05);
  // truck lateral lento (parallax: cada camada anda numa velocidade) + respiração de câmera na mão
  const tr = f < 150 ? rampa(f, 0, 149, -34, 30) : f < 280 ? rampa(f, 160, 269, 30, -30) : rampa(f, 270, 374, -30, 28);
  const x = tr + 1.6 * Math.sin(f / 7.3) + (f >= 214 && f <= 217 ? 2 * Math.sin(f * 3.1) : 0);
  const y = 5 * Math.cos(f / 41) + 1.2 * Math.cos(f / 5.1) + (f >= 214 && f <= 217 ? 2 * Math.cos(f * 2.3) : 0);
  return { z, x, y, dx: x, dy: y };
}
/** Estado da Rara por quadro: qual pose, variante de textura, tamanho, lugar dos pés e parâmetros do rig. */
export function rara(f) {
  if (f < 160) {
    const pose = f < 99 ? 'C01' : 'E06';
    let variante = '';
    if (pose === 'C01') variante = janela(f, 12, 14, 0, 0) ? 'blink' : (f >= 46 && f <= 77 ? 'beak' : (janela(f, 66, 68, 0, 0) ? 'blink' : ''));
    let p = repouso(f, 1);
    const crouch = rampa(f, 30, 45, 0, 0.055);
    // antecipação (q30 a 45): agacha, cabeça para trás, asas sobem; no q46 estica, pula e abre o bico de uma vez
    const sqAnt = f < 30 ? 0 : f < 46 ? crouch : f < 52 ? rampa(f, 46, 52, 0.055, -0.045) : f < 62 ? rampa(f, 52, 62, -0.045, 0) : 0;
    p = soma(p, { sq: sqAnt, head: f < 46 ? -4 * crouch / 0.055 : 0, wl: f < 46 ? 10 * crouch / 0.055 : 0, wr: f < 46 ? -10 * crouch / 0.055 : 0 });
    p = soma(p, { hop: pulo(f, 46, 11, 46), crest: impulso(f, 46, 16), tail: impulso(f, 46, 12, 16), wl: impulso(f, 46, 14, 10, 0.1), wr: -impulso(f, 46, 14, 10, 0.1) });
    // q78: o bico fecha; a cabeça cai um pouco
    p = soma(p, { head: rampa(f, 78, 92, 0, 3) });
    // sacudida de cabeça q96 a 100 (a troca para a pose confusa acontece escondida nela)
    p = soma(p, { head: f >= 96 && f <= 100 ? [0, 8, -8, 5, 0][f - 96] : 0 });
    if (f >= 100) {
      // confusa: cabeça inclinada, topete em espiral balançando, duas tentativas de falar (cabeça sobe e desce, peito infla)
      p = soma(p, { head: rampa(f, 100, 126, 0, 9), crest: 3 * Math.sin(f / 5) });
      for (const [a, b] of [[104, 111], [122, 130]]) { const t = clamp((f - a) / (b - a), 0, 1); if (t > 0 && t < 1) p = soma(p, { head: -7 * Math.sin(Math.PI * t), sq: -0.03 * Math.sin(Math.PI * t), hop: 6 * Math.sin(Math.PI * t) }); }
    }
    return { pose, variante, altura: 1060, lugar: [CX + 10, 1800], params: p };
  }
  if (f < 280) {
    const p = soma(repouso(f, 1.1, 15), { head: rampa(f, 175, 205, 0, 4.5), sq: 0 });
    // assenta ao chegar (q158 a 175): pequeno quique
    return { pose: 'PV01_v1', variante: '', altura: 1100, lugar: [CX - 6, 1680], params: soma(p, { hop: pulo(f, 160, 12, 18), crest: impulso(f, 160, 9) }) };
  }
  const p = soma(repouso(f, 1.2, 40), { head: f >= 300 ? 6 * Math.sin(Math.PI * clamp((f - 300) / 40, 0, 1)) : 0, sq: -0.01 * Math.sin(f / 9) });
  return { pose: 'PV04_v2', variante: '', altura: 1000, lugar: [CX + 10, 1680], params: soma(p, { hop: pulo(f, 272, 12, 12), crest: impulso(f, 272, 7) }) };
}
/** Caixa do rosto no quadro de vídeo (px), ou null durante o chicote (sem garantia). */
export function caixaRosto(f) {
  if ((f >= 150 && f < 165) || (f >= 266 && f < 274) || f >= 375) return null;
  const r = rara(f); const c = camera(f);
  const [x0, y0, x1, y1] = caixaRostoTela(r.pose, r.params, escalaPara(r.pose, r.altura), r.lugar, 0);
  const t = (x, y) => [CX + (x - c.x - CX) * c.z, CY + (y - c.y - CY) * c.z];
  const a = t(x0, y0), b = t(x1, y1);
  return [a[0] - 40, a[1] - 40, b[0] + 40, b[1] + 40];
}
