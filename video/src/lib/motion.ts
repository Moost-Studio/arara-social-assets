/**
 * Tokens de movimento da marca (frente M, tarefa M1; master 8.12d e 6.5).
 * Um conjunto único para app (Reanimated), site (CSS/GSAP) e reels (Remotion).
 * Código puro: nenhuma dependência de plataforma.
 *
 * VALORES A VALIDAR NOS REELS APROVADOS. Base: movimento mediano de cerca de
 * 10 quadros a 30 fps (~333 ms), do backlog M1. A escala em volta da base e os
 * atrasos são ajustes iniciais, não medidas dos reels.
 */

/** Curva bezier cúbica `[x1, y1, x2, y2]`, a mesma convenção do CSS. */
export type Bezier = readonly [number, number, number, number];

/** Nomes da escala de duração. */
export type DurationName = 'micro' | 'curto' | 'base' | 'longo' | 'comemoracao';
/** Nomes das curvas. */
export type CurveName = 'entrada' | 'saida' | 'padrao' | 'passada';
/** Nomes da escala de atraso entre itens de uma sequência. */
export type StaggerName = 'junto' | 'curto' | 'base' | 'longo';

/** Quadros por segundo do Remotion nos reels (master 6.5: 30 fps; 60 fps só com muito movimento da personagem). */
export const REEL_FPS = 30;

/** Teto da comemoração dentro da sessão (master 8.3, backlog D1/D3). */
export const CELEBRATION_MAX_MS = 1000;

/** Durações em ms. Base = ~10 quadros a 30 fps. A validar nos reels aprovados. */
export const DURATIONS: Readonly<Record<DurationName, number>> = {
  micro: 100,
  curto: 200,
  base: 333,
  longo: 500,
  comemoracao: CELEBRATION_MAX_MS,
};

/**
 * Curvas. Nada linear (master 6.5, "Easing: expo e back").
 * entrada: desacelera ao pousar (expo out). saida: acelera ao sair (expo in).
 * padrao: ease in-out suave. passada: entrada com leve passada e assentamento (back out).
 */
export const CURVES: Readonly<Record<CurveName, Bezier>> = {
  entrada: [0.16, 1, 0.3, 1],
  saida: [0.7, 0, 0.84, 0],
  padrao: [0.65, 0, 0.35, 1],
  passada: [0.34, 1.56, 0.64, 1],
};

/** Atrasos em ms entre itens de uma sequência (stagger). A validar nos reels aprovados. */
export const STAGGER: Readonly<Record<StaggerName, number>> = {
  junto: 0,
  curto: 40,
  base: 80,
  longo: 120,
};

/** Deslocamento inicial, em px, de quem entra em movimento. */
export const ENTER_OFFSET_PX = 24;

/**
 * Regras de composição como dados (master 6.5 e backlog M1). Consulta e documentação;
 * não são aplicadas automaticamente.
 */
export const COMPOSITION_RULES = {
  /** Pousar desacelera (curva `entrada`). */
  pousaDesacelerando: true,
  /** Sair acelera (curva `saida`), e saídas são mais curtas que entradas. */
  saiAcelerando: true,
  /** Quem entra já está se movendo (desloca `ENTER_OFFSET_PX`); fade sozinho não é entrada. */
  entraSeMovendo: true,
  /** O corte acontece com o movimento em andamento, nunca em corte seco sem intenção. */
  corteEmMovimento: true,
} as const;

/** Tokens completos, na forma consumida pelas plataformas. */
export interface Motion {
  /** `true` na versão estática ("reduzir movimento"). */
  reduced: boolean;
  durations: Readonly<Record<DurationName, number>>;
  curves: Readonly<Record<CurveName, Bezier>>;
  stagger: Readonly<Record<StaggerName, number>>;
  /** Deslocamento de entrada em px (0 quando reduzido). */
  enterOffsetPx: number;
}

const ZERO = <K extends string>(o: Readonly<Record<K, number>>) =>
  Object.fromEntries(Object.keys(o).map((k) => [k, 0])) as Record<K, number>;

const ANIMATED: Motion = {
  reduced: false,
  durations: DURATIONS,
  curves: CURVES,
  stagger: STAGGER,
  enterOffsetPx: ENTER_OFFSET_PX,
};

const STATIC: Motion = {
  reduced: true,
  durations: ZERO(DURATIONS),
  curves: CURVES,
  stagger: ZERO(STAGGER),
  enterOffsetPx: 0,
};

/**
 * Tokens para o modo atual. Com `reduced` verdadeiro devolve a versão estática:
 * todas as durações e atrasos 0 e nenhum deslocamento (o estado final aparece direto).
 */
export function motionFor(reduced: boolean): Motion {
  return reduced ? STATIC : ANIMATED;
}

/** Converte a curva para `cubic-bezier(x1, y1, x2, y2)` do CSS. */
export function toCssEasing(curve: Bezier): string {
  return `cubic-bezier(${curve.join(', ')})`;
}

/** Duração em ms para quadros inteiros (arredonda para o quadro mais próximo). Para o Remotion. */
export function framesAt(ms: number, fps: number = REEL_FPS): number {
  return Math.round((ms * fps) / 1000);
}

/** Quadros para ms (inverso de `framesAt`, a menos do arredondamento). */
export function msFromFrames(frames: number, fps: number = REEL_FPS): number {
  return (frames * 1000) / fps;
}
