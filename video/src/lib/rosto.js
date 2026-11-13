// Caixa do rosto (olhos + bico + 40 px de margem) em coordenadas do quadro 1080x1920, por quadro de tempo.
// Compartilhado entre o Studio (DebugAreas) e o QA (scripts/qa-rosto.mjs). JS puro, sem dependências.
export const MARGEM = 40;
const S_KIT = 1080 / 1024;       // o kit entra com largura do quadro
const TOPO_KIT = 1920 - 1080;     // base do busto na borda de baixo
const BASE_KIT = [347, 190, 692, 513]; // união das máscaras de olhos e bico no quadro 1024 (K00)
export const CAIXAS_ARTE = { PV01: [380, 840, 700, 1060], PV04: [400, 980, 620, 1160] }; // marcadas à mão nas artes 1080x1920 (cobertura)
const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const rampa = (f, a, b, v0, v1) => v0 + (v1 - v0) * ease(Math.min(1, Math.max(0, (f - a) / (b - a))));
/** Zoom da câmera por quadro. */
export function zoom(f) {
  if (f < 150) return f < 46 ? 1 : f < 78 ? rampa(f, 46, 77, 1, 1.05) : rampa(f, 78, 149, 1.05, 1.06);
  if (f < 270) return rampa(f, 165, 269, 1, 1.04);
  return rampa(f, 270, 374, 1, 1.04);
}
/** Deslocamento vertical do corpo do kit (antecipação q30 a 45, volta no q46). */
export function dyKit(f) {
  if (f < 46) return rampa(f, 30, 45, 0, 32);
  return rampa(f, 46, 52, 32, 0);
}
function escala(b, z) { const cx = 540, cy = 960; return [cx + (b[0] - cx) * z, cy + (b[1] - cy) * z, cx + (b[2] - cx) * z, cy + (b[3] - cy) * z]; }
/** Caixa do rosto no quadro f, ou null quando a imagem está em transição (sem garantia). */
export function caixaRosto(f) {
  let b;
  if (f < 150) { const d = dyKit(f); b = [BASE_KIT[0] * S_KIT, TOPO_KIT + BASE_KIT[1] * S_KIT + d, BASE_KIT[2] * S_KIT, TOPO_KIT + BASE_KIT[3] * S_KIT + d]; }
  else if (f >= 165 && f < 266) b = CAIXAS_ARTE.PV01;
  else if (f >= 272 && f < 375) b = CAIXAS_ARTE.PV04;
  else return null;
  const e = escala(b, zoom(f));
  return [e[0] - MARGEM, e[1] - MARGEM, e[2] + MARGEM, e[3] + MARGEM];
}
export const intersecta = (a, b) => !(a[2] <= b[0] || b[2] <= a[0] || a[3] <= b[1] || b[3] <= a[1]);
