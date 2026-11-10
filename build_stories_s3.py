import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import story_compose_v4 as sc
B = pathlib.Path(__file__).parent
out = B / "stories_s3"; out.mkdir(exist_ok=True)
for s in json.load(open(B / "stories.json"))["stories"]:
    if s["id"] < 31: continue
    h = s.get("head") or [None, None]
    sc.compose(s["id"], str(B / "stories_base" / s["art"]), h[0], h[1], str(out / f"story_{s['id']}.png"))
print("ok")
