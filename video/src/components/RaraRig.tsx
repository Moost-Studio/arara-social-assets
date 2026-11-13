import React, { useLayoutEffect, useRef, useState } from 'react';
import { continueRender, delayRender, staticFile } from 'remotion';
import { RIG, PARAMS0, escalaPara, malha, matrizes } from '../lib/rig.js';

type Params = Partial<typeof PARAMS0>;
const VS = `#version 300 es
in vec2 aPos;in vec4 aW0;in vec2 aW1;uniform mat3 uM[6];uniform vec4 uP;uniform vec2 uPlace;uniform vec2 uSz;uniform vec2 uTex;out vec2 vUV;
void main(){vec3 v=vec3(aPos,1.0);vec2 d=aW0.x*(uM[0]*v).xy+aW0.y*(uM[1]*v).xy+aW0.z*(uM[2]*v).xy+aW0.w*(uM[3]*v).xy+aW1.x*(uM[4]*v).xy+aW1.y*(uM[5]*v).xy;
 vec2 s=(d-vec2(uP.y,uP.z))*uP.x+uPlace;gl_Position=vec4(s.x/uSz.x*2.0-1.0,1.0-s.y/uSz.y*2.0,0.0,1.0);vUV=aPos/uTex;}`;
const FS = `#version 300 es
precision mediump float;in vec2 vUV;uniform sampler2D uTexS;out vec4 o;void main(){o=texture(uTexS,vUV);}`;

type Ctx = { gl: WebGL2RenderingContext; prog: WebGLProgram; mesh: { vao: WebGLVertexArrayObject; n: number }; tex: Record<string, WebGLTexture>; loc: Record<string, WebGLUniformLocation | null> };

function carrega(url: string): Promise<HTMLImageElement> {
  return new Promise((ok, erro) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => erro(new Error('imagem ' + url)); i.src = url; });
}

/**
 * A Rara com o rig por malha (6 ossos), desenhada em WebGL no quadro inteiro 1080x1920.
 * `pose`: C01, E01, E06, E13, E09 (corpo inteiro, 1254 px) ou PV01_v1 e PV04_v2 (artes aprovadas recortadas).
 * `altura`: altura da figura em px de tela. `lugar`: onde ficam os pés (x, y) em px de tela. `params`: graus e pixels da pose.
 */
export const RaraRig: React.FC<{ pose: string; variante?: string; altura: number; lugar: [number, number]; params: Params }> = ({ pose, variante = '', altura, lugar, params }) => {
  const ref = useRef<HTMLCanvasElement>(null);
  const st = useRef<Ctx | null>(null);
  const [pronto, setPronto] = useState(0);
  const arquivo = variante ? `${pose}_${variante}` : pose;

  // cria o contexto e a malha uma vez; carrega as texturas (pose e variante) antes do primeiro desenho
  useLayoutEffect(() => {
    const h = delayRender('rig ' + arquivo);
    (async () => {
      const cv = ref.current!;
      if (!st.current) {
        const gl = cv.getContext('webgl2', { premultipliedAlpha: true, alpha: true, antialias: false, preserveDrawingBuffer: true }) as WebGL2RenderingContext | null;
        if (!gl) throw new Error('sem WebGL2');
        const sh = (t: number, s: string) => { const x = gl.createShader(t)!; gl.shaderSource(x, s); gl.compileShader(x); if (!gl.getShaderParameter(x, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(x) || 'shader'); return x; };
        const prog = gl.createProgram()!; gl.attachShader(prog, sh(gl.VERTEX_SHADER, VS)); gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, FS)); gl.linkProgram(prog);
        if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(prog) || 'link');
        const m = malha(pose); const vao = gl.createVertexArray()!; gl.bindVertexArray(vao);
        const buf = (arr: Float32Array, nome: string, n: number) => { const b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.bufferData(gl.ARRAY_BUFFER, arr, gl.STATIC_DRAW); const l = gl.getAttribLocation(prog, nome); gl.enableVertexAttribArray(l); gl.vertexAttribPointer(l, n, gl.FLOAT, false, 0, 0); };
        buf(m.pos, 'aPos', 2); buf(m.w0, 'aW0', 4); buf(m.w1, 'aW1', 2);
        const ib = gl.createBuffer(); gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ib); gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, m.idx, gl.STATIC_DRAW);
        const loc: Record<string, WebGLUniformLocation | null> = {}; for (const n of ['uM', 'uP', 'uPlace', 'uSz', 'uTex', 'uTexS']) loc[n] = gl.getUniformLocation(prog, n);
        st.current = { gl, prog, mesh: { vao, n: m.idx.length }, tex: {}, loc };
      }
      const c = st.current; const gl = c.gl;
      if (!c.tex[arquivo]) {
        const img = await carrega(staticFile(`assets/rig/${arquivo}.png`));
        const t = gl.createTexture()!; gl.bindTexture(gl.TEXTURE_2D, t); gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, true);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img); gl.generateMipmap(gl.TEXTURE_2D);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        c.tex[arquivo] = t;
      }
      setPronto((n) => n + 1);
      continueRender(h);
    })().catch((e) => { console.error(e); continueRender(h); });
  }, [arquivo, pose]);

  // desenho: síncrono, a cada quadro, depois que a textura existe
  useLayoutEffect(() => {
    const c = st.current; if (!c || !c.tex[arquivo]) return;
    const { gl, prog, mesh, loc } = c; const D = RIG[pose]; const P = D.points;
    gl.viewport(0, 0, 1080, 1920); gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT); gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
    gl.useProgram(prog);
    const M = matrizes(P, { ...PARAMS0, ...params }); const f = new Float32Array(54);
    M.forEach((m: number[], k: number) => { for (let col = 0; col < 3; col++) for (let r = 0; r < 3; r++) f[k * 9 + col * 3 + r] = m[r * 3 + col]; });
    gl.uniformMatrix3fv(loc.uM, false, f);
    gl.uniform4f(loc.uP, escalaPara(pose, altura), P.feet[0], D.bbox[3], 0);
    gl.uniform2f(loc.uPlace, lugar[0], lugar[1]); gl.uniform2f(loc.uSz, 1080, 1920); gl.uniform2f(loc.uTex, D.tam[0], D.tam[1]);
    gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, c.tex[arquivo]); gl.uniform1i(loc.uTexS, 0);
    gl.bindVertexArray(mesh.vao); gl.drawElements(gl.TRIANGLES, mesh.n, gl.UNSIGNED_SHORT, 0);
  }, [pronto, arquivo, pose, altura, lugar[0], lugar[1], JSON.stringify(params)]);

  return <canvas ref={ref} width={1080} height={1920} style={{ position: 'absolute', left: 0, top: 0, width: 1080, height: 1920 }} />;
};
