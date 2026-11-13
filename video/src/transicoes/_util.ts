import { Easing } from 'remotion';
import { CURVES } from '../lib/motion';
const b = (c: readonly [number, number, number, number]) => Easing.bezier(c[0], c[1], c[2], c[3]);
/** Curvas da marca (motion.ts do app) prontas para interpolate(). */
export const EASE = { entrada: b(CURVES.entrada), saida: b(CURVES.saida), padrao: b(CURVES.padrao), passada: b(CURVES.passada) };
export const PALETA = { azul: '#2457E6', amarelo: '#FFC83D', verde: '#22B573', turquesa: '#1FB5C9', branco: '#FFFFFF' };
