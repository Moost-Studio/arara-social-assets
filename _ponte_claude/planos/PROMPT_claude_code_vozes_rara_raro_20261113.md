# Prompt para o Claude Code: vozes da Rara e do Raro no app

Tarefa no `~/moost-projects/devfluent-app`. Faça `git pull` antes e leia o `CLAUDE.md` do projeto. Há dois arquivos não rastreados em `docs/` (`PLANO_PRECO_E_MINUTOS.md` e `PLANO_VOZ_POR_TURNOS_E_TEMPO_REAL.md`): são de outra frente, não os altere nem os apague.

## Decisões já tomadas pelo Rodrigo (fonte: `Moost-Studio/arara-identidade`, `arara_social/casting/resultado.md` e `arara_social/rara-sistema-de-marca.md`, itens B9, R5 e decisão 4)
- Voz da **Rara = Achernar** e voz do **Raro = Achird**, ambas do catálogo Gemini (`voice_name`). Escolha de 11/11/2026 17h36 UTC; Achird para o Raro confirmada em 12/11 ao ouvir "Senta que lá vem história".
- O Gemini é o provedor de voz padrão da Rara e do Raro, na leitura de texto (Gemini TTS) e na chamada (Gemini Live), com o mesmo `voice_name`. O modelo pode ser trocado depois, se o Rodrigo quiser.
- A chamada só migra do OpenAI Realtime para o Gemini Live se passar na bateria B11 (qualidade em pt-BR, custo por minuto, limites do modo preview). O OpenAI Realtime fica como plano B. **Trocar o provedor da chamada é refatoração e exige aprovação do Rodrigo.**
- Estilo de fala: usar literalmente os blocos [VOZ RARA] e [VOZ RARO] do master (seção 7.0 do prompt fundamental).

## Estado atual que eu encontrei (confira antes de editar, o código pode ter mudado)
- `apps/api/src/tts.service.ts`: `DEFAULT_VOICE = 'Achird'` ("a mais natural e amigável"), `ttsVoice(v?)` com a ordem opção, `TTS_VOICE`, padrão; TTS via OpenRouter `/audio/speech`; o `TONE` é um texto único de tutor, sem distinção entre Rara e Raro. A chave de cache já inclui a voz.
- `apps/api/src/starter.ts`: `STARTER_VOICES` padrão `Achird,Kore,Puck`.
- `apps/api/src/llm.ts` (cerca da linha 296): chamada com OpenAI Realtime, voz `VOICE_NAME` ou `marin`.
- `packages/shared/src/types.ts`: experimento A/B `voice: { variants: ['marin', 'cedar'] }`.
- Ou seja, a escolha do casting **ainda não está aplicada no app**: a Rara fala hoje com Achird (que é a voz do Raro).

## O que fazer
1. **Leitura de texto (Gemini TTS), parte de baixo risco:** a voz passa a depender do personagem. Rara usa Achernar; Raro usa Achird. Mantenha o override por `TTS_VOICE` e a opção `voice` por chamada. Troque o `TONE` único por um estilo por personagem, derivado dos blocos [VOZ RARA] e [VOZ RARO] do master, sem perder a regra de pronúncia nativa do idioma da aula. Descubra onde o personagem é conhecido no fluxo (tutor, Raro nas histórias e nas palavras) e passe-o até o `tts.service`. Confira o que `STARTER_VOICES` representa e ajuste só se for coisa de personagem; se não tiver certeza, pergunte em vez de mudar.
2. **Chamada (Gemini Live), só investigação:** monte e rode a bateria B11 com Achernar (Rara) e Achird (Raro): qualidade em pt-BR, custo por minuto, limites do modo preview e latência, comparando com o OpenAI Realtime atual. **Não troque o provedor, não remova `marin` e `cedar` e não encerre o experimento A/B da voz.** Entregue um relatório com os números e uma recomendação, para o Rodrigo decidir.
3. **Custo:** a bateria B11 gasta com a API. Estime antes e pare e peça autorização se passar de US$ 2. Use só dados sintéticos e contas de teste.
4. **Testes e docs:** atualize `apps/api/test/tts.test.ts` e os testes que fixam a voz; adicione teste de que a Rara resolve Achernar e o Raro resolve Achird; rode lint, typecheck, testes e build. Atualize a documentação afetada (`docs/`, variáveis de ambiente sem valores, o backlog B9 e R5 no repositório de identidade) e registre o relatório da B11 em `docs/`. Se a mudança não exigir doc em algum ponto, diga por quê.

## Restrições
- Nada de produção, segredos nos logs, banco real nem flags ligadas por você. Respeite as regras do projeto sobre telas e recursos só com flag ligada.
- Commits em Conventional Commits, com a minha identidade Git e sem Co-authored-by. Só faça push depois de lint, typecheck, testes e build.
- Se faltar informação (por exemplo, onde o personagem Raro fala no fluxo), pare e pergunte.

## Resposta final (curta)
(a) o que mudou em arquivos, (b) comandos e resultados reais de lint, typecheck, testes e build, (c) números da B11 e recomendação sobre o Gemini Live, (d) docs atualizadas, (e) pendências e riscos.
