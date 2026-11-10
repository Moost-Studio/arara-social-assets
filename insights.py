#!/usr/bin/env python3
"""Metricas do @falearara via Graph API (somente leitura).
Uso: insights.py [dias]   (padrao 7)
Mostra seguidores, alcance/visitas da conta e, por post recente, alcance, curtidas,
comentarios, salvamentos, compartilhamentos. Stories ativos entram com alcance e respostas."""
import json, sys, time, urllib.parse, urllib.request, urllib.error, pathlib

TOKEN = pathlib.Path("/home/rodrigo/.openclaw/workspace/.secrets/meta_arara_token.txt").read_text().strip()
IG = "17841450630484682"
API = "https://graph.facebook.com/v21.0"
dias = int(sys.argv[1]) if len(sys.argv) > 1 else 7


def get(path, **params):
    url = f"{API}/{path}?" + urllib.parse.urlencode({**params, "access_token": TOKEN})
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"erro": e.read().decode()[:300]}


def metricas(media_id, metricas_):
    r = get(f"{media_id}/insights", metric=metricas_)
    return {m["name"]: m["values"][0]["value"] for m in r.get("data", [])} if "data" in r else {"erro": r.get("erro")}


conta = get(IG, fields="username,followers_count,follows_count,media_count")
print(f"@{conta.get('username')}: {conta.get('followers_count')} seguidores, {conta.get('follows_count')} seguindo, {conta.get('media_count')} posts")

now = int(time.time())
ins = get(f"{IG}/insights", metric="reach,profile_views,website_clicks,accounts_engaged,total_interactions",
          metric_type="total_value", period="day", since=now - dias * 86400, until=now)
print(f"\nConta, ultimos {dias} dias:")
for m in ins.get("data", []):
    print(f"- {m['name']}: {m['total_value']['value']}")
if "erro" in ins:
    print("  (insights da conta indisponiveis:", ins["erro"], ")")

midias = get(f"{IG}/media", fields="id,caption,media_type,permalink,timestamp,like_count,comments_count", limit=20).get("data", [])
print("\nPosts recentes:")
for m in midias:
    if m["timestamp"] < time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(now - dias * 86400)):
        continue
    ins = metricas(m["id"], "reach,saved,shares,views")
    legenda = (m.get("caption") or "").split("\n")[0][:60]
    print(f"- {m['timestamp'][:10]} {m['media_type']} \"{legenda}\" | curtidas {m.get('like_count', 0)} comentarios {m.get('comments_count', 0)} | {ins} | {m['permalink']}")

print("\nComentarios recentes (para responder):")
achou = False
for m in midias[:10]:
    cs = get(f"{m['id']}/comments", fields="username,text,timestamp", limit=10)
    if "erro" in cs:
        print(f"- comentarios indisponiveis: {cs['erro']}")
        break
    for c in cs.get("data", []):
        achou = True
        print(f"- {c['timestamp'][:16]} @{c.get('username')}: {c.get('text')} ({m['permalink']})")
if not achou:
    print("- nenhum")

stories = get(f"{IG}/stories", fields="id,timestamp,permalink").get("data", [])
print(f"\nStories ativos: {len(stories)}")
for s in stories:
    print(f"- {s['timestamp']} | {metricas(s['id'], 'reach,replies,navigation')}")
