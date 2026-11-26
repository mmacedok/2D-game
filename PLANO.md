# Plano: mini-MMO RPG pixel (nome a definir)

## A ideia em uma frase

Um RPG online em pixel art, no navegador e no PC, com o visual da vila aprovada. Você tem um avatar e
encontra os amigos na vila (chat, minigames, skins, como Club Penguin/Habbo). Depois sai pelos portões
para um **mundo grande, contínuo e compartilhado**, onde farma monstros, itens, poderes e nível com
dezenas de outros jogadores, como Diablo.

## Metas de escala (definem a arquitetura)

| Meta | Número |
|---|---|
| Jogadores na mesma área, se vendo e lutando juntos | **50 a 60** |
| Mundo | **grande e conectado, sem tela de carregamento** entre vila e áreas |
| Combate | tempo real, com poderes, projéteis, área de efeito e invocações |
| Classes | 6 no lançamento (ver abaixo), mais depois |

## Laço do jogo

1. **Vila (social, sem combate):** praça central, lojas, quadro de missões, minigames e chat. É o ponto de
   encontro de todos.
2. **Mundo (combate, clima de Diablo):** os portões da vila dão direto no mapa, sem carregamento. Quanto
   mais longe da vila, mais escuro, sujo e perigoso (paleta da masmorra) e maior o nível dos monstros.
   Exemplos em `art/conceitos/`: Floresta Sombria, Cemitério Antigo e Minas Abandonadas.
3. **Masmorras de chefe:** a entrada fica no mundo aberto, e o interior é uma instância só do grupo
   (1–5 jogadores). É o único lugar com transição, que pode ser um fade curto de porta, não uma tela de
   carregamento.
4. **Volta:** vende, equipa, sobe de nível, mostra o item novo na vila.

## Classes (6 no lançamento)

| Classe | Papel | Visual | Poderes (1–4) |
|---|---|---|---|
| Cavaleiro | tanque corpo a corpo | prata e vermelho, escudo com leão | golpe em arco, escudo erguido, investida, grito de guerra |
| Mago | dano à distância em área | azul e dourado, cajado com orbe | bola de fogo, nova de gelo, teleporte curto, meteoro |
| Necromante | invocador | esqueleto roxo e dourado | erguer esqueleto, explosão de cadáver, maldição, exército |
| Arqueira | dano à distância rápido | verde e couro, capuz | flecha perfurante, chuva de flechas, armadilha, rolamento |
| Sacerdote | cura e suporte | branco e dourado | cura em área, escudo sagrado, ressuscitar, luz que fere mortos-vivos |
| Ladino | dano corpo a corpo rápido | cinza e preto, duas adagas | golpe pelas costas, veneno, sumir, chuva de facas |

Cada poder é um arquivo de dados (`Resource` do Godot) com custo, recarga, alcance, área, dano e efeito.
Balancear é editar números, não código.

## Progressão (estilo Diablo, simples)

- **Nível 1–30**, XP por monstro e missão. **XP compartilhado** por quem estava perto quando o monstro
  morreu, para ajudar estranhos dar vontade de jogar junto.
- **HUD de Diablo:** vida e mana numa barra embaixo, com 10 atalhos (1–0). Poderes nos atalhos 1–4, que
  destravam nos níveis 1, 3, 6 e 10; o resto fica para poções e itens.
- **Itens** em 6 espaços (arma, mão secundária, cabeça, corpo, botas, acessório), com raridade comum /
  mágico / raro / lendário e 1–3 atributos sorteados.
- **Loot pessoal:** cada jogador vê o próprio drop. Com 60 pessoas na área, isso evita roubo de item e briga.

## Minigames da vila (um por vez)

Pescaria no rio, tiro ao alvo, corrida em volta da praça e quiz. Rendem moeda da vila, nunca item de
combate, para o social não virar obrigação de farm.

## Stack técnica

| Parte | Escolha | Por quê |
|---|---|---|
| Engine | **Godot 4 + GDScript** | Grátis, ótima para 2D pixel, exporta para navegador e PC. C# não exporta para web |
| Tela | Interna 640×360, escala inteira (×3 = 1920×1080, ×4 = 1440p, ×6 = 4K) | Pixels nítidos em qualquer monitor |
| Mapas | `TileMapLayer`, tiles 16×16, mundo dividido em **pedaços (chunks) de 32×32 tiles** | Carrega só o que está perto |
| Rede | `WebSocketMultiplayerPeer` com **sincronização própria** (ver abaixo) | Funciona no navegador; o sync automático do Godot não aguenta 60 jogadores |
| Servidor | O próprio projeto exportado `--headless` | Um só código para cliente e servidor |
| Banco | SQLite no começo, Postgres depois | Contas, inventário, nível |
| Cliente | Export web (Cloudflare Pages / itch.io) e versão PC (Windows) | Entrar pelo link, ou baixar para rodar melhor |

Configurações de pixel art: AGENTS.md, seção 8.

## Como o mundo fica contínuo e aguenta 60 jogadores

**Mapa sem carregamento**
- O mundo é uma grade de chunks de 32×32 tiles (512×512 px). O cliente mantém carregado o chunk onde o
  jogador está e os 8 vizinhos, e carrega os próximos em segundo plano
  (`ResourceLoader.load_threaded_request`) antes de o jogador chegar. Os que ficam longe são descarregados.
- A vila é só uma parte do mesmo mapa, cercada por muralha. Atravessar o portão não troca de cena.

**Servidor**
- **Começo: um servidor para o mundo todo.** Ele roda a simulação a 20 ticks por segundo. Monstros não
  usam física do Godot: colisão simples por círculo e busca de caminho numa grade, que é barato em GDScript.
- **Área de interesse:** o servidor divide o mundo em células e manda a cada jogador só o que está
  perto dele (cerca de 1,5 tela). Na vila lotada, cada um recebe só quem está visível.
- **Pacotes enxutos:** em vez de um nó sincronizado por jogador, o servidor manda um "retrato" do que
  mudou a cada tick, em binário (`PackedByteArray`): id, posição, direção, animação e vida.
  Estimativa: ~60 entidades visíveis × ~12 bytes × 20/s ≈ 15 KB/s por jogador, que qualquer internet aguenta.
- **Depois, se crescer:** um servidor por região do mapa, com passagem do jogador de um para outro na
  borda (o cliente só troca de conexão, sem carregamento). Só quando um servidor único não der mais conta.

**Combate em tempo real**
- O jogador vê o próprio movimento na hora (**previsão no cliente**) e o servidor corrige se discordar.
- Os outros jogadores aparecem com **interpolação** (~100 ms atrás), o que deixa o movimento liso mesmo
  com internet ruim.
- Ataques e poderes: o cliente manda "usei o poder 2 nesta direção"; o servidor confere mana, recarga e
  alcance, calcula o acerto e o dano, e avisa todo mundo perto. O cliente já toca a animação e o som na
  hora, para não parecer atrasado.
- **Limites de 60 pessoas na tela:** efeitos dos outros jogadores ficam mais transparentes e menores que
  os seus, números de dano só os seus e os do grupo, e há limite de invocações do Necromante por área.

**Hospedagem**
- Teste: VPS de ~US$ 5–10/mês. Com o mundo aberto e 60+ jogadores por área: ~US$ 20–40/mês
  (4 núcleos, 8 GB). Banda de ~1 MB/s com 60 jogadores, dentro do que esses planos incluem.

**Teste de carga obrigatório:** um script que abre 60 clientes falsos (sem tela) andando e lutando na
mesma área. A fase 2 só termina quando o servidor segura isso a 20 ticks e um cliente web fica a 60 fps.

Regra de ouro: **o servidor decide tudo** (dano, drop, XP, moedas). O cliente só mostra e manda comandos.

## Fases (cada uma termina com algo jogável)

| Fase | Entrega | Pronto quando |
|---|---|---|
| 0. Arte base | Itens A a E de `prompts/lista-de-imagens.md` | `check_art.py` com 0 erros e a vila montada no Godot parecendo a referência |
| 1. Vila online | Login simples, jogadores andando na vila, chat com filtro | 2 navegadores se veem e conversam |
| 2. Mundo e escala | Vila + Floresta Sombria contínuas (chunks), sync próprio, área de interesse, teste de carga | 60 clientes falsos na mesma área a 20 ticks; andar da vila à floresta sem carregamento |
| 3. Combate | Cavaleiro e Mago com 4 poderes, 3 monstros, XP, loot pessoal | Grupo de estranhos mata monstros junto e cada um recebe seu loot |
| 4. Classes e itens | As 6 classes, inventário, equipamento, raridades | Todas jogáveis até o nível 10 |
| 5. Chefe e mais áreas | Cemitério e Minas, 1ª masmorra instanciada com o Ogro do Bastião | Grupo de 5 vence o chefe e cai lendário |
| 6. Social e loja | 1 minigame, skins cosméticas, lista de amigos | Comprar skin troca a folha do personagem |

## Segurança, chat e dinheiro

- Chat aberto com criança exige, desde a fase 1: filtro de palavrões, botão de denunciar, mute e limite de
  mensagens. Considerar o modo do Club Penguin: frases prontas para menores e chat livre só para contas
  verificadas. Com 60 pessoas na área, o chat da área mostra só quem está perto.
- **Monetização: só cosmético vendido direto (skins, emotes, enfeites de casa).** O ECA Digital
  (Lei 15.211/2025) proíbe loot box em jogos para crianças e adolescentes no Brasil, e vender poder de
  combate (arma paga que depois é nerfada) gera reclamação e risco. Anúncio com recompensa só para maiores
  e opcional. Conferir a lei atual antes de lançar.
