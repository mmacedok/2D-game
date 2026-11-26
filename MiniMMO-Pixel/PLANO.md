# Plano: mini-MMO RPG pixel (nome a definir)

Revisão de 26/11/2026. Versão anterior preservada em `PLANO.original.md`.

## 1. Visão e objetivo

Um RPG de navegador com o visual da vila aprovada: encontrar amigos, conversar, mostrar equipamentos
e sair em grupos de 1 a 4 jogadores para enfrentar monstros e buscar itens. O social se inspira em
Club Penguin/Habbo; combate e progressão, em Diablo.

O primeiro objetivo é provar este ciclo completo: **entrar → encontrar outro jogador → sair para a
floresta → derrotar monstros → receber e equipar um item → voltar → reconectar sem perder progresso**.

O jogo combina convivência em salas de vila e aventuras instanciadas. Não depende de colocar todos
os jogadores em uma única sala.

## 2. Escopo do primeiro protótipo online

Incluído:

- Uma vila sem combate, com ponto de nascimento e portal para a floresta.
- Cavaleiro com movimento em quatro direções e ataque básico.
- Grupo de 1 a 4 jogadores, com convite, aceite, saída e líder para iniciar a aventura.
- Uma floresta pequena e um tipo de monstro.
- Vida, morte, retorno à vila e progressão do nível 1 ao 5.
- Inventário de 20 itens, equipamento de arma e corpo e raridades comum e mágico.
- Loot individual e salvamento de identidade de teste, personagem, XP, inventário e equipamento.
- Comunicação por frases prontas no teste inicial.

Ficam para depois: Mago, Necromante, chefe, quatro poderes por classe, nível 30, outras áreas,
minigames, amigos persistentes, chat livre, loja, pagamentos, anúncios, trocas, PvP e casas.
Esses recursos não bloqueiam a validação do ciclo principal.

## 3. Regras de jogo e controles

### Vila, grupo e instâncias

- Salas de vila com limite configurável. Meta inicial de teste: 20 jogadores por sala; ampliar somente
  após medir servidor, rede e cliente. Permitir escolher a mesma sala dos amigos quando houver vaga.
- O líder solicita entrada na floresta; o servidor valida o grupo e transfere os membros presentes.
  Se o líder sair, a liderança passa a outro membro. Sair do grupo não apaga o progresso dos demais.
- Cada grupo recebe uma instância isolada. A aventura termina quando todos saem, depois de confirmar
  o salvamento. Monstros não reaparecem durante a mesma aventura no protótipo.
- Ao morrer, o jogador retorna à vila com vida restaurada e mantém os itens concedidos. Sem perda de
  XP ou moedas no protótipo. Pode reencontrar o grupo se a instância ainda existir.
- Na desconexão, remover o personagem do combate e reservar sua vaga por 60 segundos. Reconectar
  nesse prazo leva ao ponto de entrada da instância, se ainda existir; caso contrário, leva à vila.
  Efeitos já confirmados pelo servidor continuam válidos.
- Após reinício do servidor, retornar à vila com o último progresso confirmado no banco.

### Entrada e apresentação

- Validar primeiro no navegador de computador, com teclado e mouse. Celular entra depois com
  direcional e botões de toque próprios, seguido de teste real em aparelhos.
- Movimento: setas ou WASD. Ataque básico: espaço ou clique no alvo dentro de alcance.
- Os futuros quatro poderes usam **1, 2, 3 e 4**, evitando conflito entre W e o movimento em WASD.
- Manter resolução base 480×270, tiles 16×16, escala inteira e filtro nearest, conforme `AGENTS.md`.
  Usar barras quando necessário e definir tratamento para telas menores que a resolução base.
- Colisão usa uma área nos pés; o sprite segue a grade 32×32. Ordenar profundidade pela posição dos
  pés para permitir passar à frente e atrás dos objetos.

### Combate, recompensas e progressão

- O cliente envia intenções. O servidor valida movimento, velocidade, colisão, alcance, recarga,
  vida e alvo antes de aplicar efeitos. Nunca aceitar dano, XP, saldo ou item informado pelo cliente.
- Começar com ataque básico; acrescentar uma habilidade do Cavaleiro após estabilizar o combate.
- XP vai para membros vivos do grupo, presentes na instância e próximos do combate, com raio
  configurável e valor fixo por participante por tipo de monstro no protótipo.
- Cada participante elegível recebe sua própria rolagem de loot. Cada item tem identificador único;
  uma recompensa deve ser registrada uma única vez, mesmo com pedidos repetidos.
- Inventário cheio envia o item para uma fila persistente de recompensas pendentes, acessível na vila.
  Definir limite e política dessa fila antes de testes públicos.
- Arma concede dano e corpo concede vida. Item mágico pode receber um atributo extra de uma tabela
  limitada. Fórmulas, limites e chances ficam em configuração versionada do servidor.
- Balancear com dados de teste; não exigir números finais para começar a implementação.

## 4. Direção de arte

`AGENTS.md` continua sendo a fonte das regras visuais: referência aprovada, paleta de 40 cores,
tamanhos, nomes, animações e revisão visual. Esta revisão não altera esses valores.

- Produzir apenas os tiles e objetos necessários para uma vila pequena, uma floresta, um Cavaleiro
  e um monstro. Validar escala e leitura em uma cena pequena antes de ampliar o conjunto.
- Aprovar a pose base antes de produzir as animações.
- `tools/check_art.py` verifica parte das regras técnicas; não comprova qualidade visual, poses,
  luz, alinhamento dos pés ou completude das animações. Manter a revisão visual obrigatória.
- Zero erros pode ocorrer sem assets de jogo. Cada fase precisa listar os PNGs exigidos e verificar
  sua existência e utilização na cena, além de executar o validador.
- O validador atual exige múltiplos de 64 para chefes. A exceção de 96×96 prevista em `AGENTS.md`
  exige aprovação e suporte explícito no validador antes de ser utilizada.

## 5. Arquitetura técnica

| Parte | Escolha | Responsabilidade |
|---|---|---|
| Cliente | Phaser 3 + TypeScript + Vite | Entrada, renderização, animação, interface e interpolação |
| Mapas | Tiled, JSON, tiles 16×16 | Camadas visuais, colisão, portais e pontos de nascimento |
| Servidor | Colyseus + Node.js + TypeScript | Salas, grupos, simulação, combate e recompensas |
| Banco inicial | SQLite | Identidades de teste, personagens, itens e progresso |
| Banco futuro | Postgres, se necessário | Evolução mediante necessidade medida e migração planejada |
| Cliente publicado | Hospedagem estática com HTTPS | Distribuição dos arquivos do cliente |
| Servidor publicado | Processo Node com WSS e banco persistente | Conexões, simulação, gravação e recuperação |

Organização proposta: `client/`, `server/`, `shared/` e `maps/`, mantendo `art/`, `prompts/` e `tools/`.
`shared/` guarda contratos e tipos. Fixar versões compatíveis e documentar instalação e execução
quando o código for criado.

Regras de implementação:

- Uma sala por vila e uma sala por aventura. Acesso à instância exige participação validada no grupo;
  conhecer o identificador da sala não basta.
- Separar estado temporário de persistente. Monstros e posições são temporários; XP, posse de itens
  e equipamento exigem gravação confirmada.
- Conceder recompensa e registrar sua operação na mesma transação, sem duplicação por repetição.
- Usar migrações desde o início; testar backup e restauração antes do teste público.
- Configurar frequências de simulação e sincronização e ajustá-las por medição. Testar movimento,
  colisão e combate com latência simulada.
- Validar formato e tamanho das mensagens e limitar comandos por conexão.
- A identidade de teste usa sessão emitida pelo servidor. Escolher um apelido não permite acessar
  outro personagem. Contas públicas, recuperação e encerramento de sessão entram antes do lançamento aberto.

## 6. Fases e critérios de conclusão

Cada fase termina com uma versão executável. Não expandir conteúdo enquanto o ciclo anterior
continuar incompleto ou perder dados.

| Fase | Entrega | Pronto quando |
|---|---|---|
| 0. Base visual e local | Projeto executável, cena pequena, colisão e Cavaleiro animado | Instalação reproduzível; movimento em quatro direções; assets exigidos existem; validador sem erros e revisão visual concluída |
| 1. Vila online | Sessões de teste, movimento sincronizado e frases prontas | Dois navegadores distintos se veem; um não controla o outro; reconectar preserva a identidade |
| 2. Aventura completa | Grupos, floresta, monstro, ataque, morte, XP, loot e equipamento | Dois jogadores saem juntos, lutam, equipam e voltam; terceiro fora do grupo não acessa a instância |
| 3. Persistência | Transações, reconexão, backup e limites | Repetir recompensa não duplica item; inventário cheio não perde loot; reiniciar preserva progresso confirmado; backup restaurado com sucesso |
| 4. Teste fechado | Ajustes de combate e carga | Testar 20 jogadores na vila e quatro instâncias simultâneas de quatro jogadores; registrar latência, memória, CPU e falhas; corrigir travamentos, perdas e duplicações |
| 5. Classes e poderes | Três monstros, Mago, Necromante e mais poderes | As três classes completam a aventura até o nível 10; invocações têm limites e autoridade no servidor |
| 6. Chefe e progressão | Ogro do Bastião, itens e áreas | Ataques com sinais legíveis; grupo consegue vencer; dificuldade e recompensas passam por teste de balanceamento |
| 7. Social e cosméticos | Um minigame, amigos e skins | Minigame concede apenas moeda social; skin respeita classe e animações, sem alterar atributos de combate |

A fase 4 é uma meta de teste, não uma promessa de capacidade. Estimar prazo e orçamento depois das
primeiras medições e da confirmação da equipe disponível.

## 7. Evolução após o protótipo

- Expandir nível 10 até o 30 somente com conteúdo e ritmo de avanço validados.
- Expandir equipamento para arma, cabeça, corpo e acessório; raridades comum, mágico, raro e lendário.
- Chegar a quatro poderes por classe, nos níveis 1, 3, 6 e 10, com mana e recarga.
- Implementar um minigame por vez: pescaria, tiro ao alvo, corrida ou quiz. Escolher após testar a vila.
  Recompensas sociais não concedem poder de combate.
- Skins seguem a grade e as animações da classe correspondente. Invocações do Necromante precisam
  de limites de quantidade, duração e custo de simulação.

## 8. Comunicação, público e monetização

Começar em grupo fechado com frases prontas. Antes do cadastro público, definir faixa etária,
países atendidos, dados coletados, regras de convivência e responsáveis pela moderação.

Chat livre exige denúncia, bloqueio, mute, limite de mensagens e processo de atendimento. Filtro de
palavrões sozinho não resolve moderação. Definir retenção e acesso a registros e tratamento de
abusos antes de abrir esse recurso.

Direção comercial: cosméticos vendidos diretamente, sem venda de atributos de combate e sem loot boxes.
Pagamentos e anúncios ficam fora do protótipo. Antes de monetizar ou atender crianças e adolescentes,
validar as obrigações vigentes de privacidade, proteção de menores e consumo com análise jurídica
atualizada. A referência à legislação no plano anterior deve ser verificada nessa etapa; esta revisão
não determina sua aplicabilidade nem a conformidade legal do jogo.

## 9. Hospedagem, custos e operação

A previsão anterior de centenas de jogadores em um VPS de US$ 5–10 era uma hipótese sem medição.
Não adotar esse valor como orçamento ou garantia. Capacidade e custo dependem dos testes da fase 4
e dos preços e limites vigentes na contratação.

Levantar custo de servidor, armazenamento, backups, tráfego, domínio e operação. Confirmar limites
da hospedagem estática e suporte a conexões persistentes no servidor.

Registrar erros, conexões, salas ativas, duração das gravações e uso de recursos. Definir limite de
vagas, comportamento quando o servidor estiver cheio e recuperação após falha. Segredos ficam fora
do cliente e do controle de versão. Teste público exige HTTPS/WSS e backup fora do processo do jogo.

## 10. Próxima ação

Executar a fase 0: preparar o projeto Phaser/Colyseus, documentar execução local e montar uma cena
pequena com Cavaleiro, colisão e assets mínimos. Registrar o que foi demonstrado, os problemas e o
esforço real para orientar as próximas fases. Esta revisão é de planejamento; a implementação dessas
fases ainda não foi executada.
