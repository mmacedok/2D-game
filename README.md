# Jogo 2D

Mini-MMO RPG em pixel art, no navegador e no PC (Godot 4 + GDScript): vila social estilo Club Penguin/Habbo
e um mundo grande e contínuo para farmar monstros, itens, poderes e nível, como Diablo.

- **[PLANO.md](PLANO.md):** o jogo, as classes, a escala (50–60 jogadores por área) e as fases.
- **[AGENTS.md](AGENTS.md):** regras de arte e código para quem gera imagens ou programa (humano ou IA).
- **[prompts/lista-de-imagens.md](prompts/lista-de-imagens.md):** o que gerar, na ordem.
- `tools/`: `pixelize.py` (imagem de IA → pixel art na grade e paleta), `check_art.py` (confere tudo em `art/`),
  `montar_folha.py` (junta quadros de animação).

## Rodar o lobby

Abra `project.godot` no Godot 4.7 e aperte F5: abre a vila (`cenas/vila-lobby.tscn`) com o Cavaleiro andando
em WASD ou setas. Resolução interna 640×360, escala inteira, filtro Nearest.

## Origem

- Plano, regras, ferramentas, arte e skills: pacote MiniMMO-Pixel (github.com/mmacedok/MiniMMO-Pixel).
- Lobby jogável em Godot (`project.godot`, `cenas/`, `assets/`): cópia completa do amigo de 2026-11-26.
- [docs/PLANO-versao-do-amigo.md](docs/PLANO-versao-do-amigo.md): o plano ampliado pelo Codex do amigo. Ele ainda
  fala em Phaser; a stack valendo é a do `PLANO.md` (Godot 4).

Antes de mandar arte: `python tools/check_art.py` precisa dar 0 erros.

As skills em `.agents/skills/`, `processes/` e `workspace/_shared/` são do
[Mr. Mak Workspace](https://github.com/witnesstodark/mr-mak-workspace) (MIT, ver `LICENSE` e `THIRD_PARTY_NOTICES.md`).
