#!/usr/bin/env python3
"""Gera clipes de vídeo por IA via OpenRouter (API assíncrona /api/v1/videos). Chave lida do arquivo, nunca impressa.
Uso: gen_video.py <id> ... (ids de CLIPES). Saída: ../../reports/video_ia/<id>.mp4 e <id>.json (metadados, sem a chave)."""
import base64, io, json, pathlib, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
R = pathlib.Path(__file__).resolve().parent; OUT = R.parent.parent / "reports" / "video_ia"; OUT.mkdir(parents=True, exist_ok=True)
KEY = (R.parent.parent / ".secrets" / "openrouter_api_key.txt").read_text().strip()
API = "https://openrouter.ai/api/v1"
MODEL = "google/veo-3.1-fast"

def first_frame():
    from PIL import Image
    bg = Image.new("RGB", (720, 1280)); px = bg.load()
    for y in range(1280):
        t = y / 1279; c = (int(10 + 14 * (1 - abs(t - .45) * 1.6 if abs(t - .45) < .6 else 0)), int(22 + 30 * (1 - abs(t - .45) * 1.6 if abs(t - .45) < .6 else 0)), int(46 + 40 * (1 - abs(t - .45) * 1.6 if abs(t - .45) < .6 else 0)))
        for x in range(720): px[x, y] = c
    m = Image.open(R.parent / "reel_teste" / "assets" / "m2.png").convert("RGBA").crop((90, 840, 975, 1690))
    m = m.resize((int(m.width * 0.78), int(m.height * 0.78)))
    bg.paste(m, ((720 - m.width) // 2, 1280 - m.height - 250), m)
    b = io.BytesIO(); bg.save(b, "PNG"); (OUT / "primeiro_quadro_arara.png").write_bytes(b.getvalue())
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()

def frame_file(path):
    return "data:image/png;base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()

CLIPES = {
 "t_veo_arara_4s": dict(duration=4, generate_audio=False, model="google/veo-3.1-fast", frame_path=str(R.parent / "mascote_3d" / "primeiro_quadro_aceno_v2.png"), prompt="Animate the provided 3D macaw mascot with very small, natural motion only. The raised wing waves gently once, one natural blink, a slight breath in the chest, tail feathers move slightly. The character stays in the same three-quarter pose facing the same direction for the entire clip: do not rotate the body or head toward the camera, do not zoom, do not change the framing. Static camera. Identical colors, blue eyes, face, beak, feathers and proportions as the first frame. Deep navy studio background unchanged. No text, no logos."),
 "t_kling_arara_4s": dict(duration=4, generate_audio=False, model="kwaivgi/kling-v3.0-std", seed=False, frame_path=str(R.parent / "mascote_3d" / "primeiro_quadro_aceno_v2.png"), prompt="Animate the provided 3D macaw mascot with very small, natural motion only. The raised wing waves gently once, one natural blink, a slight breath in the chest, tail feathers move slightly. The character stays in the same three-quarter pose facing the same direction for the entire clip: do not rotate the body or head toward the camera, do not zoom, do not change the framing. Static camera. Identical colors, blue eyes, face, beak, feathers and proportions as the first frame. Deep navy studio background unchanged. No text, no logos."),
 "p6_arara3d_aceno": dict(duration=8, generate_audio=False, frame_path=str(R.parent / "mascote_3d" / "primeiro_quadro_aceno.png"), prompt="Animate the provided 3D stylized macaw mascot exactly as shown, keeping identical colors, feather pattern, face, beak and proportions. 0-3 s: the raised wing waves gently twice while the head turns slightly toward the camera with a warm smile and one natural blink. 3-6 s: the wing lowers slowly, the chest rises with a soft breath, tail feathers sway slightly. 6-8 s: calm confident hold looking at the camera. Smooth slow dolly-in, deep navy studio background with soft electric-blue rim light, subtle floor reflection. Keep the framing stable from the first frame, no sudden zoom or cut. Do not change the character design. No text, no logos, no watermarks."),
 "p1_cafe": dict(duration=8, generate_audio=True, prompt="Cinematic commercial, 35mm lens, shallow depth of field. A young Brazilian professional in their late twenties sits at a window table in a modern coffee shop, talking with a colleague who stays out of frame. 0-2 s: speaks fluently, relaxed. 2-5 s: stops mid-sentence, eyes drift slightly up and to the side searching for a word, a small tight breath. 5-8 s: slow push-in toward the face, soft exhale, a faint self-aware smile. Warm natural window light, restrained color grading, natural skin texture. Ambient cafe sound only, no speech audible. Vertical 9:16. No text, no logos, no subtitles, no watermarks."),
 "p4_globo": dict(duration=8, generate_audio=False, prompt="High-end 3D animation. A luminous translucent globe floating in a deep blue environment, soft speech bubbles orbiting it, each bubble containing abstract light patterns (no letters, no symbols, no flags). The camera circles slowly around the globe. Refined cyan and blue highlights with a few warm amber accents, realistic glass and light materials. Vertical 9:16, 8 s. No readable text, no flags, no logos."),
 "p5_arara": dict(duration=8, generate_audio=False, frame=True, prompt="Animate the provided flat-vector macaw mascot exactly as drawn, keeping the same colors, proportions and flat illustration style. 0-3 s: the head turns slowly toward the camera and blinks once. 3-6 s: the wings open gently and the tail feathers sway. 6-8 s: calm hold, a slight breathing motion. Slow dolly-in on a dark navy studio background with a soft cyan rim light. Do not change the character design. No text, no logos, no watermarks."),
}

def call(path, body=None):
    req = urllib.request.Request(API + path, data=json.dumps(body).encode() if body is not None else None, headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read())

def run(cid):
    c = CLIPES[cid]
    body = {"model": c.get("model", MODEL), "prompt": c["prompt"], "duration": c["duration"], "resolution": "720p", "aspect_ratio": "9:16", "generate_audio": c["generate_audio"]}
    if c.get("seed", True): body["seed"] = 7
    if c.get("frame_path"): body["frame_images"] = [{"type": "image_url", "image_url": {"url": frame_file(c["frame_path"])}, "frame_type": "first_frame"}]
    elif c.get("frame"): body["frame_images"] = [{"type": "image_url", "image_url": {"url": first_frame()}, "frame_type": "first_frame"}]
    try: job = call("/videos", body)
    except urllib.error.HTTPError as e: return cid, "ERRO envio %s: %s" % (e.code, e.read().decode()[:400])
    jid = job.get("id"); poll = job.get("polling_url") or f"{API}/videos/{jid}"
    t0 = time.time()
    while time.time() - t0 < 1500:
        time.sleep(15)
        try:
            req = urllib.request.Request(poll, headers={"Authorization": "Bearer " + KEY}); st = json.loads(urllib.request.urlopen(req, timeout=60).read())
        except Exception as e: continue
        if st.get("status") == "completed":
            req = urllib.request.Request(f"{API}/videos/{jid}/content", headers={"Authorization": "Bearer " + KEY})
            (OUT / f"{cid}.mp4").write_bytes(urllib.request.urlopen(req, timeout=300).read())
            (OUT / f"{cid}.json").write_text(json.dumps({"id": jid, "model": c.get("model", MODEL), "status": st, "prompt": c["prompt"]}, ensure_ascii=False, indent=1))
            return cid, "ok %s s de espera; custo: %s" % (int(time.time() - t0), json.dumps(st.get("usage") or st.get("cost") or "n/d"))
        if st.get("status") in ("failed", "cancelled", "expired"): return cid, "FALHOU: " + json.dumps(st)[:500]
    return cid, "tempo esgotado (job %s)" % jid

if __name__ == "__main__":
    ids = sys.argv[1:] or list(CLIPES)
    with ThreadPoolExecutor(len(ids)) as ex:
        for cid, msg in ex.map(run, ids): print(cid, msg, flush=True)
