# Lista de imagens (fase 0), na ordem

Uma imagem por vez, seguindo AGENTS.md seção 4. Só passe para a próxima depois de aprovada.
"Bloco" = gerar como textura contínua e cortar (AGENTS.md, tiles de chão).

## A. Primeiro teste do processo (faça antes de tudo)

| # | Arquivo final | Tamanho | Assunto |
|---|---|---|---|
| 1 | `art/personagens/cavaleiro-parado.png` | 64×128 (2 quadros × 4 direções) | Cavaleiro de armadura prata, capa e penacho vermelhos, escudo com leão dourado. Gere primeiro só o quadro de frente; se ficar bom depois do `pixelize`, faça o resto |

Se o cavaleiro não ficar legível em 32×32, pare e avise: pode ser preciso mudar a grade antes de gerar o resto.

## B. Vila

| # | Arquivo final | Tamanho | Assunto |
|---|---|---|---|
| 2 | `art/tiles/grama.png` | 64×64 (bloco) | grama verde viva, poucas flores |
| 3 | `art/tiles/calcada.png` | 64×64 (bloco) | calçamento de pedra cinza da praça |
| 4 | `art/tiles/terra.png` | 64×64 (bloco) | caminho de terra batida |
| 5 | `art/tiles/agua.png` | 64×64 (bloco) | rio azul com reflexo claro |
| 6 | `art/tiles/muralha.png` | 64×48 | trecho de muralha de pedra com ameias |
| 7 | `art/objetos/casa-azul.png` | 64×64 | casa enxaimel com telhado de ardósia azul |
| 8 | `art/objetos/ferreiro.png` | 80×64 | ferraria com forja acesa e placa de bigorna |
| 9 | `art/objetos/barraca-mercado.png` | 48×48 | barraca de toldo listrado vermelho e branco |
| 10 | `art/objetos/fonte-leao.png` | 48×48 | fonte redonda com estátua de leão |
| 11 | `art/objetos/arvore.png` | 32×48 | árvore redonda verde |
| 12 | `art/objetos/estandarte.png` | 16×32 | estandarte vermelho com flor-de-lis dourada |
| 13 | `art/objetos/poste-lampiao.png` | 16×32 | poste com lampião aceso |
| 14 | `art/objetos/alvo-treino.png` | 32×32 | alvo de tiro com boneco de palha (minigame) |
| 15 | `art/personagens/guarda.png` | 64×128 (parado) | guarda com lança, NPC do portão |

## C. Personagens jogáveis (andar, 4 direções)

| # | Arquivo final | Tamanho | Assunto |
|---|---|---|---|
| 16 | `art/personagens/cavaleiro-andar.png` | 128×128 | Cavaleiro andando |
| 17 | `art/personagens/mago-parado.png` | 64×128 | Mago de manto e chapéu azuis com dourado, barba branca, cajado com orbe azul |
| 18 | `art/personagens/mago-andar.png` | 128×128 | Mago andando |
| 19 | `art/personagens/necromante-parado.png` | 64×128 | Esqueleto de manto roxo e dourado, chamas roxas na cabeça, cajado de caveira |
| 20 | `art/personagens/necromante-andar.png` | 128×128 | Necromante andando |

## D. Primeira área do mundo: floresta sombria

| # | Arquivo final | Tamanho | Assunto |
|---|---|---|---|
| 21 | `art/masmorra/tiles/lama.png` | 64×64 (bloco) | chão de lama com marcas de roda e poças |
| 22 | `art/masmorra/tiles/grama-escura.png` | 64×64 (bloco) | grama alta e escura, musgo |
| 23 | `art/masmorra/objetos/arvore-morta.png` | 32×48 | árvore retorcida sem folhas |
| 24 | `art/masmorra/objetos/cerca-quebrada.png` | 48×16 | cerca de madeira podre |
| 25 | `art/masmorra/objetos/fogueira.png` | 16×16 | fogueira acesa (luz laranja) |
| 26 | `art/masmorra/monstros/lobo.png` | 128×128 (andar) | lobo cinza magro, olhos amarelos |
| 27 | `art/masmorra/monstros/goblin.png` | 128×128 (andar) | goblin verde com adaga enferrujada |
| 28 | `art/masmorra/monstros/zumbi.png` | 128×128 (andar) | camponês zumbi com forcado quebrado |
| 29 | `art/masmorra/chefes/ogro-bastiao.png` | 128×64 (parado, 2 quadros, só de frente) | ogro verde enorme com clava de espinhos e cinto de caveira |

## E. HUD (AGENTS.md seção 6)

| # | Arquivo final | Tamanho | Assunto |
|---|---|---|---|
| 30 | `art/ui/barra-inferior.png` | 400×40 | moldura de pedra escura com detalhes dourados, espaço para vida, mana e 10 atalhos (sem números, sem texto) |
| 31 | `art/ui/moldura-retrato.png` | 96×32 | moldura do retrato, nome e nível |
| 32 | `art/ui/moldura-minimapa.png` | 48×48 | anel de pedra e dourado do minimapa |
| 33–36 | `art/icones/cavaleiro-poder-1..4.png` | 16×16 cada | golpe em arco, escudo erguido, investida, grito de guerra |
| 37 | `art/icones/pocao-vida.png` | 16×16 | poção vermelha |

Números e textos do HUD são desenhados pelo jogo com fonte pixel, nunca pela IA.

## F. Classes novas (parado e andar, 4 direções)

| # | Arquivo final | Tamanho | Assunto |
|---|---|---|---|
| 38 | `art/personagens/arqueira-parado.png` / `-andar.png` | 64×128 / 128×128 | Arqueira de capuz verde e couro, arco curto |
| 39 | `art/personagens/sacerdote-parado.png` / `-andar.png` | 64×128 / 128×128 | Sacerdote de manto branco e dourado, maça e livro |
| 40 | `art/personagens/ladino-parado.png` / `-andar.png` | 64×128 / 128×128 | Ladino de cinza e preto, duas adagas, lenço no rosto |

## G. Mais áreas do mundo (use os mockups de `art/conceitos/` como referência de cenário)

| # | Arquivo final | Tamanho | Assunto |
|---|---|---|---|
| 41 | `art/masmorra/tiles/terra-cemiterio.png` | 64×64 (bloco) | terra escura com grama morta e névoa rasteira |
| 42 | `art/masmorra/objetos/lapide.png` | 16×32 | lápide torta de pedra |
| 43 | `art/masmorra/objetos/cripta.png` | 64×64 | cripta de pedra com porta aberta |
| 44 | `art/masmorra/monstros/esqueleto.png` | 128×128 (andar) | esqueleto com espada enferrujada |
| 45 | `art/masmorra/tiles/chao-mina.png` | 64×64 (bloco) | chão de rocha com trilho de vagonete |
| 46 | `art/masmorra/objetos/vagonete.png` | 32×32 | vagonete de mina com minério |
| 47 | `art/masmorra/objetos/cristal-azul.png` | 16×32 | cristal azul brilhante |
| 48 | `art/masmorra/monstros/aranha-caverna.png` | 128×128 (andar) | aranha gigante de caverna |
| 49 | `art/masmorra/chefes/cavaleiro-morto-vivo.png` | 128×64 (parado, só de frente) | cavaleiro morto-vivo com aura roxa (minichefe do cemitério) |
