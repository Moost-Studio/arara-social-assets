export const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
export const easeInOut = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
export const easeOut = (t: number) => 1 - Math.pow(1 - t, 3);
export const easeIn = (t: number) => t * t * t;
/** Interpola v0 a v1 entre os quadros a e b (ease aplicado ao progresso). */
export function rampa(frame: number, a: number, b: number, v0: number, v1: number, ease: (t: number) => number = easeInOut) {
  return v0 + (v1 - v0) * ease(clamp((frame - a) / (b - a), 0, 1));
}
/** Janela 0..1: sobe em `sobe` quadros antes de `de`, fica em 1 até `ate` e desce em `desce` quadros (troca de camada nunca é corte seco: 2 quadros). */
export function janela(frame: number, de: number, ate: number, sobe = 2, desce = 2) {
  if (frame < de - sobe || frame > ate + desce) return 0;
  return Math.min(clamp((frame - (de - sobe)) / sobe, 0, 1), clamp((ate + desce - frame) / desce, 0, 1));
}
