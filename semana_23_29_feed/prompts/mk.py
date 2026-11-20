import json,sys
b=json.load(open('/home/rodrigo/.openclaw/workspace/arara_social/semana_23_29_feed/prompts/_blocos.json'))
scene=open(sys.argv[1]).read().strip()
print(b['STYLE']+"\n\n"+b['RARA']+"\n\n"+scene+"\n\n"+b['NEGATIVE'])
