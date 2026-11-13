// Pontos de articulação e caixa de cada pose (quadro de 1254 px). Origem: personagens/rara/rig/*.json
/** @type {Record<string, any>} */
export const RIG = {"C01": {"bbox": [432, 18, 818, 1229], "points": {"feet": [628, 840], "neck": [628.0, 395.0], "crest": [604.5, 150.0], "wingL": [505, 445], "wingR": [752, 445], "tail": [627.9719626168225, 865]}}, "E01": {"bbox": [382, 18, 871, 1229], "points": {"feet": [628, 840], "neck": [628.0, 395.0], "crest": [604.4935064935065, 150.0], "wingL": [505, 445], "wingR": [752, 445], "tail": [627.2971698113208, 865]}}, "E06": {"bbox": [366, 12, 881, 1229], "points": {"feet": [628, 840], "neck": [628.0, 395.0], "crest": [554.5, 144.0], "wingL": [505, 445], "wingR": [752, 445], "tail": [627.75, 865]}}, "E13": {"bbox": [245, 20, 971, 1213], "points": {"feet": [628, 840], "neck": [628.0, 395.0], "crest": [601.1941176470589, 152.0], "wingL": [505, 445], "wingR": [752, 445], "tail": [612.617924528302, 865]}}, "E09": {"bbox": [402, 32, 826, 1229], "points": {"feet": [628, 840], "neck": [628.0, 395.0], "crest": [626.25, 164.0], "wingL": [505, 445], "wingR": [752, 445], "tail": [627.5, 865]}}}
// Artes aprovadas do lote 15 recortadas (941x1672): articulações estimadas por mim sobre as imagens (tipo 'arte': corpo, cabeça, topete e cauda).
RIG.PV01_v1 = { tipo: 'arte', tam: [941, 1672], bbox: [179, 523, 841, 1502], points: { feet: [433, 1470], neck: [462, 935], crest: [430, 700], tail: [560, 1390] },
  caixaRosto: [320, 720, 630, 930], bilhete: [275, 1035, 585, 1195] };
RIG.PV04_v2 = { tipo: 'arte', tam: [941, 1672], bbox: [127, 704, 810, 1445], points: { feet: [440, 1400], neck: [462, 1045], crest: [395, 790], tail: [610, 1350] },
  caixaRosto: [360, 850, 575, 1000] };
for (const k of ['C01', 'E01', 'E06', 'E13', 'E09']) { RIG[k].tipo = 'canon'; RIG[k].tam = [1254, 1254]; RIG[k].caixaRosto = [520, 225, 740, 400]; }

