// Rig por malha da Rara (porte do rig.py / reel4.html): 6 ossos com pesos suaves. JS puro, usado pelo Remotion (WebGL) e pelo QA (caixa do rosto).
import { RIG } from './rigdata.js';
export { RIG };
const clamp = (x, a = 0, b = 1) => Math.min(Math.max(x, a), b);
const sm = (e0, e1, v) => { const q = clamp((v - e0) / (e1 - e0)); return q * q * (3 - 2 * q); };
export const m3 = {
  mul: (a, b) => { const o = new Array(9).fill(0); for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) for (let k = 0; k < 3; k++) o[i * 3 + j] += a[i * 3 + k] * b[k * 3 + j]; return o; },
  trans: (dx, dy) => [1, 0, dx, 0, 1, dy, 0, 0, 1],
  rot: (deg, p) => { const t = deg * Math.PI / 180, c = Math.cos(t), s = Math.sin(t); return [c, -s, p[0] - c * p[0] + s * p[1], s, c, p[1] - s * p[0] - c * p[1], 0, 0, 1]; },
  scale: (sx, sy, p) => [sx, 0, p[0] - sx * p[0], 0, sy, p[1] - sy * p[1], 0, 0, 1],
};
export const PARAMS0 = { hop: 0, sq: 0, body: 0, head: 0, crest: 0, wl: 0, wr: 0, tail: 0 };
/** Matrizes dos 6 ossos [corpo, cabeça, topete, asa esq., asa dir., cauda] para os parâmetros a (graus e pixels da pose). */
export function matrizes(P, a) {
  const sy = 1 - a.sq, sx = 1 / Math.sqrt(sy);
  const B = m3.mul(m3.mul(m3.trans(0, -a.hop), m3.rot(a.body, P.feet)), m3.scale(sx, sy, P.feet));
  const H = m3.mul(B, m3.rot(a.head, P.neck));
  const C = m3.mul(H, m3.rot(a.crest, P.crest));
  const WL = P.wingL ? m3.mul(B, m3.rot(a.wl, P.wingL)) : B;
  const WR = P.wingR ? m3.mul(B, m3.rot(a.wr, P.wingR)) : B;
  const T = m3.mul(B, m3.rot(a.tail, P.tail));
  return [B, H, C, WL, WR, T];
}
/** Pesos por vértice [corpo, cabeça, topete, asaE, asaD, cauda] (soma 1). */
export function pesos(tipo, x, y, P) {
  if (tipo === 'arte') {
    let head = sm(P.neck[1] + 40, P.neck[1] - 40, y);
    const crest = head * sm(P.crest[1] + 90, P.crest[1] - 20, y);
    head -= crest;
    const tail = sm(P.tail[0] - 30, P.tail[0] + 60, x) * sm(P.tail[1] - 50, P.tail[1] + 20, y);
    const body = clamp(1 - head - crest - tail);
    return [body, head, crest, 0, 0, tail];
  }
  let head = sm(P.neck[1] + 35, P.neck[1] - 35, y); const crest = head * sm(P.crest[1] + 35, P.crest[1] - 30, y); head -= crest;
  const cx = 0.5 * (P.wingL[0] + P.wingR[0]), cy = 0.5 * (P.neck[1] + P.feet[1]);
  const ell = Math.sqrt(Math.pow((x - cx) / 150, 2) + Math.pow((y - cy) / 195, 2));
  const wband = sm(0.92, 1.12, ell) * sm(P.wingL[1] - 20, P.wingL[1] + 35, y) * sm(P.feet[1] - 10, P.feet[1] - 60, y);
  const wl = x < cx ? wband : 0, wr = x >= cx ? wband : 0, tail = sm(P.tail[1], P.tail[1] + 65, y);
  const body = clamp(1 - head - crest - wl - wr - tail);
  return [body, head, crest, wl, wr, tail];
}
const aplicaM = (m, x, y) => [m[0] * x + m[1] * y + m[2], m[3] * x + m[4] * y + m[5]];
/** Deforma um ponto da pose (px da imagem) com os pesos e as matrizes. */
export function deforma(tipo, P, M, x, y) {
  const w = pesos(tipo, x, y, P); let ox = 0, oy = 0;
  for (let k = 0; k < 6; k++) { if (!w[k]) continue; const [px, py] = aplicaM(M[k], x, y); ox += w[k] * px; oy += w[k] * py; }
  return [ox, oy];
}
/** Escala da pose: altura da figura em px de tela. */
export const escalaPara = (nome, altura) => altura / (RIG[nome].bbox[3] - RIG[nome].bbox[1]);
/** Posição de um ponto da imagem na tela: (d - pés) * escala + lugar (lugar = onde ficam os pés). */
export const paraTela = (nome, d, escala, lugar) => [(d[0] - RIG[nome].points.feet[0]) * escala + lugar[0], (d[1] - RIG[nome].bbox[3]) * escala + lugar[1]];
/** Caixa do rosto (olhos e bico) em px de tela, com os ossos aplicados nos 4 cantos e 40 px de margem. */
export function caixaRostoTela(nome, a, escala, lugar, margem = 40) {
  const D = RIG[nome], M = matrizes(D.points, { ...PARAMS0, ...a });
  const [x0, y0, x1, y1] = D.caixaRosto; const pts = [[x0, y0], [x1, y0], [x0, y1], [x1, y1]].map(([x, y]) => paraTela(nome, deforma(D.tipo, D.points, M, x, y), escala, lugar));
  const xs = pts.map((p) => p[0]), ys = pts.map((p) => p[1]);
  return [Math.min(...xs) - margem, Math.min(...ys) - margem, Math.max(...xs) + margem, Math.max(...ys) + margem];
}
/** Malha (grade de `passo` px sobre a caixa da figura + margem): posições, pesos e índices. */
export function malha(nome, passo = 18, m = 70) {
  const D = RIG[nome], [W, H] = D.tam, [x0, y0, x1, y1] = D.bbox;
  const ax = Math.max(0, x0 - m), ay = Math.max(0, y0 - m), bx = Math.min(W, x1 + m), by = Math.min(H, y1 + m);
  const nx = Math.ceil((bx - ax) / passo) + 1, ny = Math.ceil((by - ay) / passo) + 1;
  const pos = [], w0 = [], w1 = [], idx = [];
  for (let j = 0; j < ny; j++) for (let i = 0; i < nx; i++) { const x = Math.min(ax + i * passo, bx), y = Math.min(ay + j * passo, by); const w = pesos(D.tipo, x, y, D.points); pos.push(x, y); w0.push(w[0], w[1], w[2], w[3]); w1.push(w[4], w[5]); }
  for (let j = 0; j < ny - 1; j++) for (let i = 0; i < nx - 1; i++) { const a = j * nx + i, b = a + 1, c = a + nx, d = c + 1; idx.push(a, b, c, b, d, c); }
  return { pos: new Float32Array(pos), w0: new Float32Array(w0), w1: new Float32Array(w1), idx: new Uint16Array(idx) };
}
