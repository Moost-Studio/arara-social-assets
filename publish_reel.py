#!/usr/bin/env python3
"""Publica um Reel do @falearara via Graph API (media_type=REELS).

Uso: publish_reel.py <id> [--dry-run]     (dados em reels.json; video em img/reels/ do repo de assets)
--dry-run cria o container e espera o processamento, sem publicar (valida URL, formato e legenda).
Mesmas protecoes do publish.py: log por etapa, nunca chama media_publish duas vezes, confere o perfil antes de dar erro
e nao publica se a mesma legenda ja saiu nas ultimas 24 h.
"""
import json, sys, time, pathlib
import publish as P

BASE = pathlib.Path(__file__).parent


def wait_video(cid, tentativas=90, espera=5):
    for _ in range(tentativas):
        s = P.call(cid, {"fields": "status_code,status"}, "GET")
        if s.get("status_code") == "FINISHED":
            return
        if s.get("status_code") in ("ERROR", "EXPIRED"):
            raise SystemExit(f"container {cid} falhou: {s}")
        time.sleep(espera)
    raise SystemExit(f"container {cid} nao ficou pronto em {tentativas * espera} s")


def main():
    pid = sys.argv[1]
    dry = "--dry-run" in sys.argv
    r = json.loads((BASE / "reels.json").read_text())[pid]
    caption = r["caption"]
    url = P.RAW + r["video"]
    P.log("inicio-reel", f"{pid} dry={dry}")
    if not dry:
        ja = P.find_recent(caption, 24 * 60)
        if ja:
            print(f"JA PUBLICADO {pid}: {ja.get('permalink', ja['id'])} (nao publiquei de novo)")
            return
    try:
        c = P.call(f"{P.IG}/media", {"media_type": "REELS", "video_url": url, "caption": caption, "share_to_feed": "true",
                                    "thumb_offset": str(r.get("thumb_offset_ms", 0))})["id"]
        wait_video(c)
    except P.ApiError as e:
        raise SystemExit(f"{e} (antes de publicar: nada saiu no perfil; detalhe em publish.log)")
    if dry:
        print(f"OK dry-run {pid}: container {c} pronto, nada publicado")
        return
    try:
        mid = P.call(f"{P.IG}/media_publish", {"creation_id": c})["id"]
    except P.ApiError as e:
        for espera in (10, 30):
            time.sleep(espera)
            achou = P.find_recent(caption, 15)
            if achou:
                P.log("confirmado", f"reel existe apesar do erro {e.code}")
                print(f"PUBLICADO {pid}: {achou.get('permalink', achou['id'])} (a API devolveu erro {e.code} em media_publish, mas o reel esta no perfil)")
                return
        raise SystemExit(f"{e}\nNAO CONFIRMADO: o reel nao apareceu no perfil em 40 s. Nao tentei de novo para nao duplicar. Confira o perfil antes de qualquer nova tentativa.")
    try:
        info = P.call(mid, {"fields": "permalink"}, "GET")
    except P.ApiError:
        info = {}
    print(f"PUBLICADO {pid}: {info.get('permalink', mid)}")


if __name__ == "__main__":
    main()
