#!/usr/bin/env python3
"""Varredura de assuntos do momento para o perfil da Arara (@falearara).

Fontes (todas gratuitas, sem chave):
  1. Google Trends, assuntos em alta por pais (RSS oficial trending/rss)
  2. Google News, buscas por oportunidades ligadas a idiomas (RSS)

Uso: trends_scan.py [--json]
Saida: texto em portugues com (a) em alta nos paises dos idiomas ensinados,
(b) em alta no Brasil que casam com palavras-chave, (c) noticias de oportunidades
(intercambio, bolsa, vaga, visto, certificacao) das ultimas 48h.
O trabalho de julgamento (o que vira post) fica com o agente, nao com o script."""
import json, re, sys, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

UA = {"User-Agent": "Mozilla/5.0"}
GEOS = {"BR": "Brasil", "US": "EUA (inglês)", "GB": "Reino Unido (inglês)", "ES": "Espanha (espanhol)",
        "FR": "França (francês)", "DE": "Alemanha (alemão)", "IT": "Itália (italiano)", "JP": "Japão (japonês)"}
KEYS = re.compile(r"idioma|inglês|ingles|english|espanhol|francês|frances|alemão|alemao|italiano|japonês|japones|"
                  r"intercâmbio|intercambio|bolsa|visto|enem|vestibular|toefl|ielts|duolingo|tradu|"
                  r"copa|olimp|festival|filme|série|serie|música|musica|viagem|turismo|pa[ií]s|"
                  r"emprego|vaga|trabalho|mestrado|doutorado|universidade|erasmus|chatgpt|gemini|ia generativa|inteligência artificial", re.I)
NEWS_QUERIES = [
    "intercâmbio bolsa de estudos brasileiros",
    "vagas exterior inglês fluente brasileiros",
    "visto estudante trabalho brasileiros",
    "certificação idioma TOEFL IELTS DELE DELF",
    "aprender idiomas inteligência artificial",
    "dia internacional idioma língua",
]


def get(url, timeout=25):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read()


def trending(geo):
    root = ET.fromstring(get(f"https://trends.google.com/trending/rss?geo={geo}"))
    ns = {"ht": "https://trends.google.com/trending/rss"}
    out = []
    for it in root.iter("item"):
        title = it.findtext("title", "").strip()
        traffic = it.findtext("ht:approx_traffic", "", ns)
        news = [n.findtext("ht:news_item_title", "", ns) for n in it.findall("ht:news_item", ns)][:2]
        out.append({"termo": title, "buscas": traffic, "noticias": news})
    return out


def news(query):
    q = urllib.parse.quote(query)
    root = ET.fromstring(get(f"https://news.google.com/rss/search?q={q}+when:2d&hl=pt-BR&gl=BR&ceid=BR:pt-419"))
    limite = datetime.now(timezone.utc) - timedelta(hours=48)
    out = []
    for it in root.iter("item"):
        try:
            if parsedate_to_datetime(it.findtext("pubDate")) < limite:
                continue
        except Exception:
            pass
        out.append({"titulo": it.findtext("title", "").strip(), "link": it.findtext("link", "")})
    return out[:5]


def main():
    res = {"gerado_em": datetime.now(timezone.utc).isoformat(), "em_alta": {}, "casam_br": [], "oportunidades": {}, "erros": []}
    for geo in GEOS:
        try:
            res["em_alta"][geo] = trending(geo)
        except Exception as e:
            res["erros"].append(f"trends {geo}: {e}")
    for t in res["em_alta"].get("BR", []):
        if KEYS.search(t["termo"] + " " + " ".join(t["noticias"])):
            res["casam_br"].append(t)
    for q in NEWS_QUERIES:
        try:
            res["oportunidades"][q] = news(q)
        except Exception as e:
            res["erros"].append(f"news '{q}': {e}")
    if "--json" in sys.argv:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return
    for geo, nome in GEOS.items():
        itens = res["em_alta"].get(geo, [])[:8]
        print(f"\n== Em alta: {nome} ==")
        for t in itens:
            print(f"- {t['termo']} ({t['buscas']})" + (f" | {t['noticias'][0]}" if t["noticias"] else ""))
    print("\n== Em alta no Brasil que combinam com a Arara ==")
    for t in res["casam_br"] or [{"termo": "(nenhum agora)", "buscas": "", "noticias": []}]:
        print(f"- {t['termo']} ({t['buscas']})")
    print("\n== Oportunidades (notícias das últimas 48h) ==")
    for q, itens in res["oportunidades"].items():
        print(f"[{q}]")
        for n in itens:
            print(f"- {n['titulo']}")
    if res["erros"]:
        print("\nErros:", *res["erros"], sep="\n- ")


main()
