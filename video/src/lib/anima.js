// Funções puras de animação (JS, para o Remotion e para o QA).
export const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
export const easeInOut = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
export const easeOut = (t) => 1 - Math.pow(1 - t, 3);
export const easeIn = (t) => t * t * t;
export const rampa = (f, a, b, v0, v1, ease = easeInOut) => v0 + (v1 - v0) * ease(clamp((f - a) / (b - a), 0, 1));
export const janela = (f, de, ate, sobe = 2, desce = 2) => (f < de - sobe || f > ate + desce ? 0 : Math.min(clamp((f - (de - sobe)) / sobe, 0, 1), clamp((ate + desce - f) / desce, 0, 1)));
/** Impulso amortecido a partir do quadro f0: amp * e^(-d t) * sen(2π t / per) (t em quadros). */
export const impulso = (f, f0, amp, per = 14, d = 0.11) => (f < f0 ? 0 : amp * Math.exp(-d * (f - f0)) * Math.sin((2 * Math.PI * (f - f0)) / per));
/** Pulso de um pulo: 0 antes de f0, meia senoide de `dur` quadros com altura `alt`, depois 0. */
export const pulo = (f, f0, dur, alt) => (f < f0 || f > f0 + dur ? 0 : alt * Math.sin((Math.PI * (f - f0)) / dur));
/** Repouso vivo: respiração (2,4 s), balanço (3 s), cabeça, topete, cauda e asas; `amp` escala tudo. */
export function repouso(f, amp = 1, fase = 0) {
  const T = (2 * Math.PI * (f + fase)) / 30;
  return {
    sq: -0.022 * amp * Math.sin(T / 2.4),
    body: 2.2 * amp * Math.sin(T / 3),
    head: 3.6 * amp * Math.sin(T / 2.8 - 0.7),
    crest: 8 * amp * Math.sin(T / 2 - 1.5),
    tail: 9 * amp * Math.sin(T / 2.5 - 1.3),
    wl: 3.2 * amp * (1 + Math.sin(T / 2.3)),
    wr: -3.2 * amp * (1 + Math.sin(T / 2.3 + 0.8)),
    hop: 3 * amp * Math.max(0, Math.sin(T / 1.6)) ,
  };
}
export const soma = (a, b) => { const o = { ...a }; for (const k in b) o[k] = (o[k] || 0) + b[k]; return o; };
