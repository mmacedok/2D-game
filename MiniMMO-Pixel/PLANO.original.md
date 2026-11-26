# Plano: mini-MMO RPG pixel (nome a definir)

## A ideia em uma frase

Um jogo de navegador com o visual da vila aprovada: você tem um avatar, encontra os amigos na vila
(chat, minigames, skins, como Club Penguin/Habbo), e sai pelos portões para o mundo farmar monstros,
itens, poderes e nível, como Diablo.

## Laço do jogo

1. **Vila (social, sem combate):** praça central, lojas, quadro de missões, minigames, chat. Todo mundo
   do servidor se vê aqui.
2. **Mundo (combate):** cada saída da vila leva a uma área (floresta, cemitério, minas...). Áreas são
   instâncias para o grupo (1 a 4 jogadores), como Diablo: monstros nascem, você mata, cai loot.
3. **Volta:** vende, equipa, sobe de nível, mostra o item novo na vila.

## Progressão (estilo Diablo, simples)

- **Nível 1–30**, XP por monstro e missão.
- **4 poderes por classe** nas teclas Q W E R, que destravam nos níveis 1, 3, 6 e 10. Mana e recarga.
- **Itens** em 4 espaços (arma, cabeça, corpo, acessório), com raridade comum / mágico / raro / lendário
  e 1–3 atributos sorteados (dano, vida, mana, velocidade).
- **Classes:** Cavaleiro (corpo a corpo, defesa), Mago (distância, área), Necromante (invoca esqueletos).

## Minigames da vila (um por vez)

Pescaria no rio, tiro ao alvo (já existe o alvo na vila), corrida em volta da praça e quiz. Todos rendem
moeda da vila, nunca item de combate, para o social não virar obrigação de farm.

## Stack técnica

| Parte | Escolha | Por quê |
|---|---|---|
| Cliente | **Phaser 3 + TypeScript + Vite** | Roda em qualquer navegador e celular, carrega rápido, pixel art nítida |
| Mapas | **Tiled** (tiles 16×16), exportado em JSON | O Phaser lê direto |
| Servidor | **Colyseus** (Node/TypeScript) | Salas prontas: 1 sala "vila" + 1 sala por instância do mundo |
| Banco | SQLite no começo, Postgres depois | Contas, inventário, nível |
| Hospedagem | Frontend na Cloudflare Pages (grátis), servidor num VPS de ~US$ 5–10/mês | Dá para algumas centenas de jogadores ao mesmo tempo |

Godot também faria o jogo, mas a versão web dele é pesada e tem problemas em alguns navegadores. Para um
jogo de "entrar pelo link e jogar", o Phaser é mais simples.

Regra de ouro: **o servidor decide tudo** (dano, drop, XP, moedas). O cliente só mostra e manda comandos.

## Fases (cada uma termina com algo jogável)

| Fase | Entrega | Pronto quando |
|---|---|---|
| 0. Arte base | Tiles da vila, o Cavaleiro andando nas 4 direções, 1 monstro | `check_art.py` com 0 erros e a vila montada no Tiled parecendo a referência |
| 1. Vila online | Login simples, vários jogadores andando na vila, chat com filtro | 2 navegadores se veem e conversam |
| 2. Primeira área | Floresta instanciada, 3 monstros, ataque básico, XP, loot | Grupo de 2 sai da vila, mata, volta com item |
| 3. Classes e poderes | Mago e Necromante, Q W E R, inventário e equipamento | As 3 classes jogáveis até o nível 10 |
| 4. Chefe | Ogro do Bastião com padrões de ataque (estilo Eldest Souls) | Dá para vencer em grupo, cai lendário |
| 5. Social e loja | 1 minigame, skins cosméticas, lista de amigos | Comprar skin troca a folha do personagem |

## Segurança, chat e dinheiro

- Chat aberto com criança exige, desde a fase 1: filtro de palavrões, botão de denunciar, mute e limite de
  mensagens. Considerar o modo do Club Penguin: frases prontas para menores e chat livre só para contas
  verificadas.
- **Monetização: só cosmético vendido direto (skins, emotes, enfeites de casa).** O ECA Digital
  (Lei 15.211/2025) proíbe loot box em jogos para crianças e adolescentes no Brasil, e vender poder de
  combate (arma paga que depois é nerfada) gera reclamação e risco. Anúncio com recompensa só para maiores
  e opcional. Conferir a lei atual antes de lançar.
