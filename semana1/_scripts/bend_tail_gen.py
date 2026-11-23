"""Curva o rabo de um recorte RGBA da Rara (qualquer pose em pé, rabo reto saindo dos pés).
Uso: /tmp/camenv/bin/python bend_tail_gen.py <entrada.png> <saida.png> <lado: d|e> [dx_rel=0.95] [dy_rel=0.8] [cy_rel=0.5]
O rabo é refeito ao longo de uma curva de Bézier (raiz reta, ponta aberta para o lado), sem alterar o corpo.
dx_rel, dy_rel e cy_rel são frações do comprimento do rabo. Nada é inventado: os pixels do rabo original são só deformados."""
import sys, numpy as np
from PIL import Image
src = dst = lado = None; dxr, dyr, cyr = 0.95, 0.8, 0.5
if __name__ == '__main__' and len(sys.argv) > 3:
    src, dst, lado = sys.argv[1], sys.argv[2], sys.argv[3]
    dxr = float(sys.argv[4]) if len(sys.argv) > 4 else 0.95
    dyr = float(sys.argv[5]) if len(sys.argv) > 5 else 0.8
    cyr = float(sys.argv[6]) if len(sys.argv) > 6 else 0.5
def bend_core(A, ys, lado, dxr=0.95, dyr=0.8, cyr=0.5, verbose=True, cxr=0.0, sq=1.0):
    """A: array float HxWx4 (RGBA) da Rara em pé; ys: linha onde o rabo começa a ser refeito (logo abaixo das garras).
    Devolve (res_RGBA_array_da_tela_toda_com_rabo_curvo, ox) onde ox é o deslocamento horizontal aplicado ao canvas."""
    H, W, _ = A.shape; al = A[..., 3]
    xc = np.zeros(H); hw = np.zeros(H)
    for y in range(ys - 6, H):
        cols = np.where(al[y] > 60)[0]
        if len(cols): xc[y] = (cols.min() + cols.max()) / 2; hw[y] = (cols.max() - cols.min()) / 2
        else: xc[y] = xc[y - 1]; hw[y] = 0
    Ls = H - ys; sign = 1 if lado == 'd' else -1
    R = np.array([xc[ys], float(ys)]); E = R + np.array([sign * dxr * Ls, dyr * Ls]); C = R + np.array([sign * cxr * Ls, cyr * Ls])
    t = np.linspace(0, 1, 500)[:, None]; P = (1 - t) ** 2 * R + 2 * (1 - t) * t * C + t ** 2 * E
    T = np.gradient(P, axis=0); T /= np.linalg.norm(T, axis=1, keepdims=True); N = np.stack([-T[:, 1], T[:, 0]], 1)
    s_ = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(P, axis=0), axis=1))]); Lc = s_[-1]
    if verbose: print(f'raiz=({R[0]:.0f},{R[1]:.0f}), rabo={Ls}px, arco={Lc:.0f}px (estica {Lc / Ls:.2f}x)')
    pad = 90
    x0, x1 = int(min(R[0], E[0]) - Ls * 0.5 - pad), int(max(R[0], E[0]) + Ls * 0.5 + pad)
    y0, y1 = int(ys - 12), int(P[:, 1].max() + pad)
    gx, gy = np.meshgrid(np.arange(x0, x1), np.arange(y0, y1)); pts = np.stack([gx.ravel(), gy.ravel()], 1).astype(float)
    def bil(yy, xx):
        x = np.clip(xx, 0, W - 1.001); y = np.clip(yy, 0, H - 1.001); xi = x.astype(int); yi = y.astype(int); fx = (x - xi)[:, None]; fy = (y - yi)[:, None]
        return A[yi, xi] * (1 - fx) * (1 - fy) + A[yi, xi + 1] * fx * (1 - fy) + A[yi + 1, xi] * (1 - fx) * fy + A[yi + 1, xi + 1] * fx * fy
    out = np.zeros((len(pts), 4))
    for i in range(0, len(pts), 12000):
        p = pts[i:i + 12000]; d2 = ((p[:, None, :] - P[None, :, :]) ** 2).sum(2); k = d2.argmin(1)
        rel = p - P[k]; v = (rel * N[k]).sum(1); along = (rel * T[k]).sum(1)
        ok = ~((k == 0) & (along < -7)) & ~((k == len(P) - 1) & (along > 1))
        u = s_[k] / Lc; kw = 1 + 0.15 * u
        ysrc = ys + u * Ls + np.where(k == 0, np.minimum(along, 0), 0); xsrc = xc[np.clip(ysrc.astype(int), 0, H - 1)] + v / (kw * sq)
        inb = ok & (ysrc < H - 1) & (xsrc >= 0) & (xsrc < W - 1) & (np.abs(v) / (kw * sq) <= hw[np.clip(ysrc.astype(int), 0, H - 1)] + 4)
        res = np.zeros((len(p), 4))
        if inb.any(): res[inb] = bil(ysrc[inb], xsrc[inb])
        out[i:i + 12000] = res
    tail = out.reshape(y1 - y0, x1 - x0, 4)
    ox = max(0, -x0); CW = max(W, x1) + ox + 10; CH = max(H, y1 + 10)
    can = np.zeros((CH, CW, 4)); body = A.copy(); body[ys - 3:, :, 3] = 0; can[:H, ox:ox + W] = body
    reg = can[y0:y1, x0 + ox:x1 + ox]; a = tail[..., 3:4] / 255; ra = reg[..., 3:4] / 255
    oa = a + ra * (1 - a); rgb = (tail[..., :3] * a + reg[..., :3] * ra * (1 - a)) / np.maximum(oa, 1e-6)
    can[y0:y1, x0 + ox:x1 + ox] = np.concatenate([rgb, oa * 255], 2)
    return can, ox

if __name__ == '__main__':
    im = Image.open(src).convert('RGBA'); A = np.asarray(im).astype(float); H, W, _ = A.shape
    al = A[..., 3]; lum = A[..., :3].mean(2)
    escuro = (al > 200) & (lum < 75)
    lin = [y for y in range(int(H * 0.55), int(H * 0.80)) if escuro[y].sum() >= 6]
    yc = max(lin) if lin else int(H * 0.70); ys = yc + 10
    print(f'{src}: claws y={yc}', end=' ')
    can, ox = bend_core(A, ys, lado, dxr, dyr, cyr)
    res = Image.fromarray(np.clip(can, 0, 255).astype('uint8'), 'RGBA'); bb = res.getbbox()
    res = res.crop((0, 0, max(bb[2], ox + W), bb[3])); res.save(dst)
    print('saída', dst, res.size, '| corpo começa em x =', ox)
