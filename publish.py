#!/usr/bin/env python3
"""Publica um post do @falearara no Instagram via Graph API.

Uso: publish.py <id> [--dry-run]
--dry-run cria os containers (sem publicar) para validar URLs e legenda.

Protecoes (03/11/2026, depois de um 403 que veio com o post ja publicado):
- cada etapa vai para publish.log (sem o token), para sabermos qual chamada falhou;
- se media_publish der erro, confere no perfil se o post saiu antes de dar falha, e NUNCA chama media_publish de novo;
- se o mesmo post ja esta no ar (mesma legenda nas ultimas 24 h), nao publica outra vez.
"""
import json, sys, time, urllib.error, urllib.parse, urllib.request, pathlib
from datetime import datetime, timedelta, timezone

BASE = pathlib.Path(__file__).parent
TOKEN = pathlib.Path("/home/rodrigo/.openclaw/workspace/.secrets/meta_arara_token.txt").read_text().strip()
IG = "17841450630484682"
API = "https://graph.facebook.com/v21.0"
RAW = "https://raw.githubusercontent.com/Moost-Studio/arara-social-assets/main/img/"
LOG = BASE / "publish.log"


class ApiError(Exception):
    def __init__(self, code, body):
        super().__init__(f"ERRO {code}: {body}")
        self.code, self.body = code, body


def log(step, msg=""):
    with LOG.open("a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {step} {msg}\n")


def call(path, params=None, method="POST"):
    data = urllib.parse.urlencode({**(params or {}), "access_token": TOKEN}).encode()
    url = f"{API}/{path}"
    req = urllib.request.Request(url, data=data) if method == "POST" else urllib.request.Request(f"{url}?{data.decode()}")
    step = path.split("/")[-1] if "/" in path else "obj"
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            out = json.load(r)
        log(step, "ok")
        return out
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        log(step, f"HTTP {e.code} {body[:400]}")
        raise ApiError(e.code, body)


def wait_ready(cid):
    for _ in range(30):
        s = call(cid, {"fields": "status_code,status"}, "GET")
        if s.get("status_code") == "FINISHED":
            return
        if s.get("status_code") in ("ERROR", "EXPIRED"):
            raise SystemExit(f"container {cid} falhou: {s}")
        time.sleep(4)
    raise SystemExit(f"container {cid} nao ficou pronto")


def find_recent(caption, minutes):
    """Post do perfil com a mesma legenda publicado nos ultimos `minutes` minutos, ou None. Nao levanta erro: so consulta."""
    try:
        rows = call(f"{IG}/media", {"fields": "id,caption,timestamp,permalink", "limit": 10}, "GET").get("data", [])
    except ApiError:
        return None
    limite = datetime.now(timezone.utc) - timedelta(minutes=minutes)
    for r in rows:
        ts = datetime.strptime(r["timestamp"], "%Y-%m-%dT%H:%M:%S%z")
        if (r.get("caption") or "").strip() == caption.strip() and ts >= limite:
            return r
    return None


def main():
    pid = sys.argv[1]
    dry = "--dry-run" in sys.argv
    post = json.loads((BASE / "posts.json").read_text())[pid]
    imgs = [RAW + f for f in post["images"]]
    caption = post["caption"]
    log("inicio", f"{pid} dry={dry}")
    if not dry:
        ja = find_recent(caption, 24 * 60)
        if ja:
            print(f"JA PUBLICADO {pid}: {ja.get('permalink', ja['id'])} (nao publiquei de novo)")
            return
    try:
        if len(imgs) == 1:
            c = call(f"{IG}/media", {"image_url": imgs[0], "caption": caption})["id"]
            wait_ready(c)
        else:
            kids = []
            for u in imgs:
                k = call(f"{IG}/media", {"image_url": u, "is_carousel_item": "true"})["id"]
                wait_ready(k)
                kids.append(k)
            c = call(f"{IG}/media", {"media_type": "CAROUSEL", "children": ",".join(kids), "caption": caption})["id"]
            wait_ready(c)
    except ApiError as e:
        raise SystemExit(f"{e} (antes de publicar: nada saiu no perfil; detalhe em publish.log)")
    if dry:
        print(f"OK dry-run {pid}: container {c} pronto, nada publicado")
        return
    try:
        mid = call(f"{IG}/media_publish", {"creation_id": c})["id"]
    except ApiError as e:
        # O erro pode vir mesmo com o post publicado. Confere no perfil (2 tentativas) e nunca chama media_publish de novo.
        for espera in (10, 30):
            time.sleep(espera)
            achou = find_recent(caption, 15)
            if achou:
                log("confirmado", f"post existe apesar do erro {e.code}")
                print(f"PUBLICADO {pid}: {achou.get('permalink', achou['id'])} (a API devolveu erro {e.code} em media_publish, "
                      f"mas o post esta no perfil; detalhe em publish.log)")
                return
        raise SystemExit(f"{e}\nNAO CONFIRMADO: o post nao apareceu no perfil em 40 s. Nao tentei de novo para nao duplicar. "
                         f"Confira o perfil antes de qualquer nova tentativa.")
    try:
        info = call(mid, {"fields": "permalink"}, "GET")
    except ApiError:
        info = {}  # o post ja saiu; so nao deu para buscar o link
    print(f"PUBLICADO {pid}: {info.get('permalink', mid)}")


if __name__ == "__main__":
    main()
