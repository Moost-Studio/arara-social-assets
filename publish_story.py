#!/usr/bin/env python3
"""Publica um story do @falearara via Graph API.
Uso: publish_story.py <id> [--dry-run]
--dry-run cria o container de story (sem publicar) para validar URL e formato."""
import json, sys, time, urllib.parse, urllib.request, urllib.error, pathlib

TOKEN = pathlib.Path("/home/rodrigo/.openclaw/workspace/.secrets/meta_arara_token.txt").read_text().strip()
IG = "17841450630484682"
API = "https://graph.facebook.com/v21.0"
RAW = "https://raw.githubusercontent.com/Moost-Studio/arara-social-assets/main/img/stories/"


def call(path, params=None, method="POST"):
    data = urllib.parse.urlencode({**(params or {}), "access_token": TOKEN}).encode()
    req = urllib.request.Request(f"{API}/{path}", data=data) if method == "POST" else urllib.request.Request(f"{API}/{path}?{data.decode()}")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ERRO {e.code}: {e.read().decode()}")


def main():
    sid = int(sys.argv[1])
    dry = "--dry-run" in sys.argv
    c = call(f"{IG}/media", {"image_url": f"{RAW}story-{sid:02d}.jpg", "media_type": "STORIES"})["id"]
    for _ in range(30):
        st = call(c, {"fields": "status_code,status"}, "GET")
        if st.get("status_code") == "FINISHED":
            break
        if st.get("status_code") in ("ERROR", "EXPIRED"):
            raise SystemExit(f"container {c} falhou: {st}")
        time.sleep(4)
    else:
        raise SystemExit(f"container {c} nao ficou pronto")
    if dry:
        print(f"OK dry-run story {sid}: container {c} pronto, nada publicado")
        return
    mid = call(f"{IG}/media_publish", {"creation_id": c})["id"]
    print(f"PUBLICADO story {sid}: media {mid}")


main()
