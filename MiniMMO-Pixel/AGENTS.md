# Regras para o Codex: arte e código do mini-MMO pixel

Leia este arquivo inteiro antes de gerar qualquer imagem ou código. O plano do jogo está em `PLANO.md`.

## 1. Visual aprovado

- **Referência única:** `art/referencia/vila-aprovada.jpg`. Tudo no jogo deve parecer que saiu dessa imagem:
  medieval de fantasia, colorido, telhados azuis, pedra cinza, grama verde viva, estandartes vermelhos com
  flor-de-lis dourada, contorno escuro e luz vinda de cima à esquerda.
- **Como fica no jogo:** `art/referencia/vila-pixelizada-preview.png` é a mesma vila reduzida para a grade
  real (512×341) com a paleta do jogo. É esse grau de pixel que vale, não o da imagem original.
- **Câmera:** top-down 3/4 ortogonal (estilo Stardew/Zelda). Telhados e topos vistos de cima, fachadas de
  frente. **Não** é isométrico, **não** é visão lateral.

## 2. Grade e tamanhos (números fixos, não mude)

| Coisa | Tamanho no jogo |
|---|---|
| Resolução base | 480×270, ampliada por número inteiro (×4 = 1920×1080), sempre com filtro *nearest* |
| Tile de chão/parede | 16×16 |
| Personagem jogável/NPC | corpo ~16×24 dentro de um quadro de 32×32, pés na linha y=30 |
| Monstro comum | quadro 32×32 |
| Chefe | quadro 64×64 (ou 96×96 se aprovado) |
| Casa | 3 a 5 tiles de largura (48–80 px) |
| Ícone de item/poder | 16×16 |

## 3. Paleta

- Só as 40 cores de `art/paleta.hex` (amostra em `art/paleta.png`), tiradas da vila aprovada.
- Sem gradiente, sem dithering, sem brilho/blur. Transparência só 0 ou 255.
- Cor nova só com aprovação do Henrique ou do Raffel; aí ela entra em `paleta.hex` e vale para todos.

## 4. Como gerar imagem sem quebrar as regras

O gerador de imagem **não sabe** fazer pixel art de verdade: ele entrega uma imagem grande que só parece
pixel. Por isso, toda imagem passa por estes passos, sem pular nenhum:

1. Gere **um** asset por imagem, centralizado, sobre **fundo magenta chapado #FF00FF** (sem chão, sem sombra
   no fundo, sem moldura, sem texto). Use o modelo de prompt de `prompts/`.
2. Anexe sempre `art/referencia/vila-aprovada.jpg` como referência de estilo. Para mais quadros do mesmo
   personagem, anexe também o quadro já aprovado dele.
3. Salve a imagem bruta em `art/rascunho/<nome>.png`.
4. Converta: `python tools/pixelize.py art/rascunho/<nome>.png art/<pasta>/<nome>.png --largura N --altura N`.
5. Confira: `python tools/check_art.py`. **Só termina com 0 erros.** Se der erro, siga o texto do erro; não
   edite o script de checagem para passar.
6. Abra o `.preview8x.png` e compare lado a lado com a vila. Se o asset destoar (cor, contorno, ângulo,
   proporção), mova a versão para `art/rejeitadas/` com o motivo no nome e gere de novo.

Pastas: `tiles/`, `objetos/`, `personagens/`, `monstros/`, `chefes/`, `icones/`, `ui/`. Nome em minúsculas,
com hífen: `cavaleiro-andar.png`, `ogro-bastiao-ataque.png`.

## 5. Folha de animação (personagens e monstros)

Uma folha por animação, quadros 32×32 lado a lado. Linhas na ordem **baixo, esquerda, direita, cima**.

| Animação | Quadros por linha |
|---|---|
| parado | 2 |
| andar | 4 |
| atacar | 4 |
| levar dano | 1 |
| morrer (só linha de baixo) | 3 |

A linha "direita" pode ser o espelho da "esquerda" quando não há item numa só mão (escudo, por exemplo).
Animação feita por IA costuma variar de quadro para quadro: gere a pose base primeiro, aprove, e gere os
outros quadros editando a partir dela. Ajuste fino de quadro se faz à mão (Aseprite/LibreSprite).

**Skins (cosméticos):** cada skin é uma folha com a mesma grade e os mesmos quadros da classe base, para
trocar uma pela outra sem mexer no código.

## 6. Classes atuais

Cavaleiro (vermelho/prata, escudo com leão), Mago (azul/dourado, cajado com orbe azul), Esqueleto Necromante
(roxo/dourado, cajado de caveira). As fichas antigas em arte grande valem só para cores e silhueta; o sprite
real segue a grade acima.

## 7. Código

- Siga a stack de `PLANO.md` (Phaser + Colyseus em TypeScript). Servidor é quem manda: dano, loot, XP,
  moedas e inventário são calculados só no servidor.
- Erro repetido vira checagem (teste, lint ou script), não mais uma linha neste arquivo.
