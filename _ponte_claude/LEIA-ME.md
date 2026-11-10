# Ponte Claude (planeja e avalia) e OpenClaw (executa)

Fluxo de cada lote, sempre nesta ordem:

1. **Plano** (Claude): o Rodrigo salva o plano em `planos/LOTE-XX_plano.md`, usando `_modelo_plano.md`.
2. **Execução** (OpenClaw): só começa depois que o plano existe e o Rodrigo confirma. Nada fora do plano.
3. **Entrega** (OpenClaw): ao terminar, escreve `entregas/LOTE-XX_entrega.md` (modelo `_modelo_entrega.md`) e para.
4. **Parecer** (Claude): o Rodrigo leva a entrega ao Claude, que responde aprovado, aprovado com ajustes ou reprovado. O Rodrigo salva em `pareceres/LOTE-XX_parecer.md` (modelo `_modelo_parecer.md`).
5. **Próximo lote** só depois de um parecer "aprovado". Com ajustes, o OpenClaw corrige só o que foi pedido e entrega de novo (versão `_v2`). Reprovado volta ao plano.

Regras fixas:
- O Rodrigo é quem carrega os arquivos entre o Claude e o OpenClaw. Não há ligação automática, e nada sai por rede.
- Nada é publicado sem OK do Rodrigo para o conteúdo final.
- Vídeos seguem em pausa até o Rodrigo liberar (registro em 08/11/2026).
- Fonte única da marca: `arara_social/rara_sistema_de_marca_v6.md`. Log de gerações: `arara_social/rara_log_geracao.md`.
