# Piloto de estilo dos reels da Arara: plano e pedido de teto (13/11/2026)

**Estado: PLANO. Nada foi gerado.** Origem: `arara-reels-skill.zip` do Rodrigo (seção 13 do SKILL.md). O skill exige plano com custo e **teto do piloto aprovado por escrito pelo Rodrigo antes de começar**.

Legenda: **[FATO]** conferido hoje; **[ESTIMATIVA]** eu estimo e NÃO verifiquei o preço; **[PROPOSTA]** decisão minha, a aprovar.

## 1. O que é o piloto [FATO, do skill]
Um roteiro de 12 a 15 s em três versões para o Rodrigo escolher o estilo. Roteiro base: na call a pessoa trava ("Deu branco"); a Rara entra pela borda de baixo (S8), solta o bico (S1) e a palavra que faltava sai do bico em letras 3D (S2); mergulho numa tela genuína do app (S9); fecha com "Bora ensaiar?" e o logo. Voz da Rara = Achernar.
- **A. Cinema 3D:** clipes Veo encadeados (S7), costuras com pena-cortina (S6).
- **B. Motion 3D gráfico:** Remotion com celular 3D, letras infladas e anéis pela voz; a Rara em clipes curtos recortados.
- **C. Híbrido rápido:** cortes a cada 0,5 s, balão-portal (S4), frase que quebra e se reconstrói (S3), Rara gingando.

## 2. Mudanças que eu faria no roteiro [PROPOSTA]
- **Bordão da quebra (S3 e versão C):** trocar "Errou? Treinou." por "Bora de novo?" (decisão do Rodrigo em 13/11).
- **S9 depende de captura real do app** (TestFlight ou staging, conta de teste). Eu NÃO tenho essa captura. Sem ela, as versões A e B ficam sem a cena do app e eu uso uma tela de lista de espera real do site, ou o Rodrigo me manda uma gravação. **Decisão dele (pergunta 1).**
- **"Bora ensaiar?"** do fecho é bordão do master e fica.
- Sem pio da Rara (HUM-24).

## 3. Bloqueios reais de hoje [FATO]
1. **Saldo do OpenRouter US$ 0,82**, abaixo do mínimo de US$ 1 para imagem e vídeo; o catálogo do OpenRouter não lista mais `google/veo-3.1-fast`. O vídeo sai pelo Google direto (`veo-3.1-fast-generate-preview`, já configurado na ferramenta do OpenClaw, 4, 6 ou 8 s, uma imagem de entrada). A TTS (voz Achernar) também usa a chave do OpenRouter: **precisa de saldo** (ou outra rota).
2. **`rembg` e `aubio` não estão instalados.** `rembg` baixa um modelo de recorte (centenas de MB) e roda lento por quadro; `aubio` é para batida. Eu só instalo com o seu OK. Alternativa sem instalar: recorte por cinza chapado #8C8C8C com código, como já faço nos recortes de imagem (funciona, mas as bordas finas da cauda precisam de conferência).
3. **3D no Remotion** (`@remotion/three`) não está instalado no projeto `video/` (hoje só `remotion` 4.0.543). Instalar é gratuito (MIT), mas muda `package.json`.
4. O clipe de IA tem 8 s no máximo; um plano-sequência de 12 a 15 s (versão A) pede 2 clipes encadeados.

## 4. Custo [ESTIMATIVA, NÃO VERIFICADA]
O preço do Veo 3.1 não está no catálogo que consultei. Minha estimativa por segundo gerado, pela tabela pública que conheço (pode ter mudado): `veo-3.1-fast` na faixa de US$ 0,10 a 0,15 por segundo; versão completa por volta de US$ 0,40. **Vou ler o custo real na primeira geração e paro se passar do teto.** O skill pede 720p fast para teste.

| Versão | Clipes de IA | Tentativas | Custo estimado |
| --- | --- | --- | --- |
| A. Cinema 3D | 2 a 3 clipes de 6 a 8 s (cerca de 20 s) | até 3 por clipe | US$ 2 a 3 por rodada; US$ 6 a 9 no pior caso |
| B. Motion 3D | 2 clipes curtos de 4 s (recorte) | até 3 | US$ 1 a 1,5 por rodada; US$ 3 a 4,5 no pior caso |
| C. Híbrido | 1 clipe de 4 a 6 s | até 3 | US$ 0,5 a 1; US$ 1,5 a 3 no pior caso |
| Voz (TTS) | 1 fala, 3 estilos | | centavos |
| Imagens (poses e quadros-chave que faltarem) | 3 a 6 | | US$ 0,2 a 0,4 |
| **Total** | | | **US$ 5 a 8 esperado; US$ 12 a 18 no pior caso** |

## 5. Pedidos de decisão ao Rodrigo [PROPOSTA]
1. **Teto do piloto inteiro:** proponho **US$ 15** (cobre o pior caso com folga); passando disso, eu paro e peço aval. Pode ser outro valor.
2. **Saldo:** o OpenRouter precisa de recarga (pelo menos US$ 10) para a voz e para qualquer imagem. Ou me diga se prefiro outra rota (chave direta do Google para a voz). Eu não recarrego conta nem pago nada sozinho.
3. **Captura real do app** para o S9: você manda uma gravação de uma conversa (TestFlight ou staging) ou aceito um piloto sem essa cena?
4. **OK para instalar** `@remotion/three` (gratuito) no projeto de vídeo. `rembg` e `aubio` só se você quiser; senão uso o recorte por cinza chapado.
5. **Ordem:** quero começar pela versão C (a mais barata e só Remotion), depois B, e A por último. OK?

## 6. Entrega do piloto [FATO, do skill]
Pelo Telegram: as três versões, a folha de contato de cada, o custo real de cada, o método de boca usado (sincronia manual e, se existir, lip-sync por modelo) e a pergunta "qual estilo, e o que mudar". Nada é publicado ou agendado.
