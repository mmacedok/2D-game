# Regras para o Codex: arte e código do mini-MMO pixel

Leia este arquivo inteiro antes de gerar qualquer imagem ou código. O plano do jogo está em `PLANO.md`.
A lista do que gerar, na ordem, está em `prompts/lista-de-imagens.md`.

## 1. Visual aprovado

- **Referência única de estilo:** `art/referencia/vila-aprovada.jpg`. Medieval de fantasia, colorido,
  telhados azuis, pedra cinza, grama verde viva, estandartes vermelhos com flor-de-lis dourada, contorno
  escuro, luz vinda de cima à esquerda.
- **Grau de pixel que vale:** `art/referencia/vila-pixelizada-preview.png` (a mesma vila na grade real).
- **Câmera:** top-down 3/4 ortogonal. Telhados e topos vistos de cima, fachadas de frente.
  **Não** é isométrico e **não** é visão lateral.

## 2. Duas zonas, um estilo

O jogo tem o clima do Diablo: a vila é o lugar seguro e colorido, e o perigo fica fora dos portões.

| Zona | Onde | Paleta | Clima |
|---|---|---|---|
| **Vila** | `art/tiles`, `art/objetos`, `art/personagens`, `art/icones`, `art/ui` | `art/paleta.hex` (40 cores) | Alegre, saturado, limpo |
| **Masmorra / mundo** | `art/masmorra/tiles`, `art/masmorra/objetos`, `art/masmorra/monstros`, `art/masmorra/chefes` | `paleta.hex` + `paleta-masmorra.hex` | Terroso, sujo, sombrio: lama, madeira velha, musgo, pedra úmida, luz de tocha |

- Exemplo do clima da masmorra: `art/referencia/clima-masmorra-preview.png`. É a mesma vila com a paleta
  escura: **as formas, o contorno e o ângulo não mudam, só a luz e as cores.**
- **Personagens jogáveis, skins, ícones e UI usam só a paleta da vila**, também quando estão na masmorra.
  Assim o jogador fica colorido e fácil de achar no meio do escuro. O `check_art.py` recusa esses tipos
  dentro de `art/masmorra/`.
- Monstros ficam sempre em `art/masmorra/monstros/`. Brilho mágico (roxo do necromante, verde podre,
  laranja de tocha) é o único ponto de cor forte da masmorra.

## 3. Resolução e grade (números fixos, não mude)

| Coisa | Tamanho |
|---|---|
| **Resolução interna** | **640×360** |
| Na tela do jogador | ampliada por número inteiro: ×3 = 1920×1080, ×4 = 2560×1440, ×6 = 4K |
| Tile de chão/parede | 16×16 |
| Personagem jogável/NPC | corpo ~16×24 dentro de um quadro de 32×32, pés na linha y=30 |
| Monstro comum | quadro 32×32 |
| Chefe | quadro 64×64 |
| Casa | 3 a 5 tiles de largura (48–80 px) |
| Ícone de item/poder | 16×16 |
| HUD inteiro | cabe em 640×360; ver seção 6 |

A tela mostra cerca de 40×22 tiles, o que dá espaço para ver a vila cheia e grupos de monstros.

## 4. Como gerar imagem sem quebrar as regras

O gerador de imagem **não sabe** fazer pixel art de verdade: ele entrega uma imagem grande que só parece
pixel. Toda imagem passa por estes passos, sem pular nenhum:

1. Gere **um** asset por imagem, centralizado, sobre **fundo magenta chapado #FF00FF** (sem chão, sem sombra
   no fundo, sem moldura, sem texto). Use `prompts/asset.md` (vila) ou `prompts/asset-masmorra.md`.
2. Anexe sempre `art/referencia/vila-aprovada.jpg`. Na masmorra, anexe também
   `art/referencia/clima-masmorra-preview.png`. Para mais quadros do mesmo personagem, anexe o quadro já
   aprovado dele.
3. Salve a imagem bruta em `art/rascunho/<nome>.png`.
4. Converta:
   `python tools/pixelize.py art/rascunho/<nome>.png art/<pasta>/<nome>.png --largura N --altura N`.
   A paleta é escolhida pela pasta de destino (qualquer coisa em `art/masmorra/` usa a paleta escura).
   Personagens e monstros: some `--corpo LxA` (personagem `--corpo 16x24` num quadro 32×32; chefe
   `--corpo 48x56` num quadro 64×64). O script recorta a figura, encaixa nesse tamanho e apoia os pés
   2 px acima da base, para todos ficarem na mesma escala.
5. Confira: `python tools/check_art.py`. **Só termina com 0 erros.** Se der erro, siga o texto do erro;
   não edite o script de checagem nem as paletas para passar.
6. Abra o `.preview8x.png` e compare com a referência. Se destoar (cor, contorno, ângulo, proporção), mova
   para `art/rejeitadas/` com o motivo no nome (`goblin-v1-angulo-lateral.png`) e gere de novo.
7. Mostre ao Raffel/Henrique antes de seguir para o próximo item da lista.

**Tiles de chão** (grama, pedra, lama) precisam emendar sem costura. Gere um bloco de 4×4 tiles
(64×64 no jogo) pedindo textura contínua, converta com `--largura 64 --altura 64` e confira montando 3×3
cópias lado a lado.

Nome dos arquivos: minúsculas com hífen (`cavaleiro-andar.png`, `ogro-bastiao-ataque.png`).

## 5. Folha de animação (personagens e monstros)

Uma folha por animação, quadros lado a lado. Linhas na ordem **baixo, esquerda, direita, cima**.

| Animação | Quadros por linha |
|---|---|
| parado | 2 |
| andar | 4 |
| atacar | 4 |
| levar dano | 1 |
| morrer (só a linha de baixo) | 3 |

- Cada quadro é gerado e convertido sozinho (32×32 no `pixelize.py`, salvo em `art/rascunho/quadros/`) e
  depois juntado: `python tools/montar_folha.py art/personagens/cavaleiro-andar.png --colunas 4 <quadros>`.
- A linha "direita" pode ser o espelho da "esquerda" quando nada fica numa mão só (o escudo, por exemplo).
- A IA muda o personagem de um quadro para outro. Gere a pose base, aprove, e gere os outros quadros
  editando a partir dela. O ajuste fino de quadro se faz à mão (Aseprite/LibreSprite).
- **Skins:** a mesma grade e os mesmos quadros da classe base, para trocar uma pela outra sem mexer no código.

## 6. HUD (estilo Diablo)

Tudo em `art/ui/`, paleta da vila, moldura de pedra escura com detalhe dourado.

- **Barra de baixo, centralizada** (~400×40 px): vida (vermelha) e mana (azul) lado a lado em cima, com
  número dentro (`100/100`); embaixo, **10 atalhos 1–0** de 18×18 com ícone 16×16 dentro.
  Os 4 primeiros são os poderes da classe; os outros, poções e itens.
- **À esquerda da barra:** botões de personagem, equipamento e missões.
- **À direita da barra:** botões de inventário, chat e opções.
- **Canto de cima à esquerda:** retrato, nome e nível. **Canto de cima à direita:** minimapa redondo.
- **Chefe:** barra de vida larga no topo, com o nome.
- Texto com fonte pixel de 8 px de altura (ex.: m5x7 ou similar de licença livre), sem gerar texto por IA.

## 7. Classes atuais

Seis classes, cada uma com uma cor dominante para ser reconhecida de longe no meio de 60 jogadores:
Cavaleiro (vermelho e prata, escudo com leão), Mago (azul e dourado, cajado com orbe azul), Esqueleto
Necromante (roxo e dourado, cajado de caveira), Arqueira (verde e couro, capuz, arco), Sacerdote (branco e
dourado, maça e livro), Ladino (cinza e preto, duas adagas, lenço no rosto). As fichas antigas em arte
grande valem só para cores e silhueta; o sprite real segue a grade acima. Poderes de cada classe: PLANO.md.

Os mockups de `art/conceitos/` mostram o clima de cada área do mundo. Eles **não** são assets: servem de
referência de cenário, como a vila aprovada.

## 8. Código (Godot 4 + GDScript)

- **Configuração de pixel art, desde o primeiro dia** (Project Settings):
  - `display/window/size/viewport_width = 640`, `viewport_height = 360`
  - `display/window/stretch/mode = viewport`, `stretch/scale_mode = integer`
  - `rendering/textures/canvas_textures/default_texture_filter = Nearest`
  - `rendering/2d/snap/snap_2d_transforms_to_pixel = true`
  - mapas com `TileMapLayer` de 16×16
- **Só GDScript.** C# não exporta para navegador.
- **Online no navegador:** `WebSocketMultiplayerPeer` (ENet não roda no navegador). O servidor é o
  próprio projeto exportado sem tela (`--headless`) num VPS.
- **Escala (PLANO.md, "Como o mundo fica contínuo"):** mundo em chunks de 32×32 tiles carregados em
  segundo plano, sem tela de carregamento; sincronização própria em binário a 20 ticks com área de
  interesse, não `MultiplayerSynchronizer` por jogador; teste de carga com 60 clientes falsos.
- **O servidor decide tudo:** dano, drop, XP, moedas e inventário são calculados só no servidor. O
  cliente manda comandos ("andar para", "usar poder 2") e mostra o resultado.
- Teste a versão web cedo, num celular comum e num PC fraco.
- Erro repetido vira checagem (teste ou script), não mais uma linha neste arquivo.

## 9. Skills do Mr. Mak (workflow de assets)

O pacote traz as 20 skills oficiais do Mr. Mak Workspace (licença MIT, `LICENSE`; projeto original:
github.com/witnesstodark/mr-mak-workspace) em `.agents/skills/`, mais `processes/` e `workspace/_shared/`.
O Codex lê skills dessa pasta sozinho; se a sua versão não listar, abra o `SKILL.md` indicado à mão.

**Sempre, antes de gerar, pedir ou integrar qualquer asset:**
1. Leia `.agents/skills/3d-production-routing/SKILL.md` e escolha a skill da tabela dele.
2. Leia a skill escolhida inteira e `processes/creative-production.md`. Caminhos relativos dentro das
   skills (`../../../processes/...`) valem a partir da raiz deste projeto.
3. Siga as regras deste AGENTS.md por cima da skill: grade, paletas, `pixelize.py` e `check_art.py`
   continuam obrigatórios.

**Qual skill usar neste jogo:**

| Tarefa | Skill |
|---|---|
| Conceitos de área, telas, variações de um personagem | `image-reference-workflow` |
| Ficha de personagem (frente, lados, costas) antes das animações | `character-sheet-pipeline` |
| HUD, menus, ícones e retratos | `game-ui-workflow` |
| Efeitos de poder (bola de fogo, cura, invocação) | `game-vfx-workflow` |
| Montar a vila e as áreas do mapa | `game-level-design` |
| Sons de golpe, passo, interface e ambiente | `game-audio-workflow` |
| Ligar animações ao movimento e ao combate no Godot | `game-animation-integration` |
| Conferir no jogo rodando que a mudança visual ficou certa | `gameplay-visual-review` |
| Plano curto de uma tarefa grande | `plan` |
| Passar uma tarefa pela metade para outro agente | `feature-handoff` |

As skills de 3D (`img2threejs`, `blender-game-animation`, `materials-to-game`, `motion-reference-workflow`)
não servem para este jogo 2D. `fal-ai-generation` e `higgsfield-workflow` usam serviços **pagos**: só com
pedido explícito do Henrique ou do Raffel. Algumas skills citam arquivos em `docs/` do Mr. Mak que não vêm
no pacote; são todos de 3D, então ignore essas referências.

**Registro de cada entrega (regra do Mr. Mak):** toda leva de imagens vira um cartão em
`workspace/<assunto>/` com as aprovadas e as rejeitadas (com o motivo), o prompt, a IA e o modelo
usados e o veredito de cada uma, registrado em `workspace/workspace.json`, em português. Um cartão por
assunto; revisões novas entram no mesmo cartão. O formato está na skill `workspace-authoring`. Se o
Raffel instalar o app do Mr. Mak, esses cartões aparecem na janela Workspace.
