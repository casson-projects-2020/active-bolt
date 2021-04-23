# Skin Fork

É o nome codigo de um sistema de RPG.

O sistema é baseado em alguns principios:

<b>1o axioma - Redução de regras</b><br/>
O número de regras deve ser o menor possivel, desde que isso não reduza a qualidade do jogo

<b>2o axioma - A realidade não precisa ser simplificada</b><br/>
As regras não devem simular a realidade, elas devem conduzir o jogo

<b>3o axioma - as regras devem permitir estratégias complexas</b><br/>
Embora poucas, deve ser possível combinar as regras de formas complexas

<b>4o axioma - as regras devem enriquecer o jogo</b><br/>
As regras devem ser feitas de forma a auxiliar a criação dos momentos de jogo.

# Regras
O sistema é baseado nos conceitos de <b>capacidades</b>, <b>primais</b>, <b>padrões de personagem</b>, <b>interações</b> e <b>juras</b>.

## Capacidades
Todas as coisas que um jogador pode fazer devem estar definidas como <b>capacidades</b>, e deve existir uma ficha explicando como a capacidade funciona. 
Caso um jogador, durante um jogo, queira fazer algo para o qual não exista uma capacidade, o mestre e o jogador devem improvisar uma ficha.

O jogador tem a capacidade se tiver a ficha, e ele pode comprar fichas durante a montagem do personagem. Se durante o jogo ele tentar fazer
algo, mas nao tiver a ficha, isso não quer dizer que a ação é impossivel para ele. Nesses casos pega-se uma ficha da caixa e checa-se se ela 
tem um modo de uso livre, que permite que qualquer um, mesmo quem nao tenha a ficha, tente executar o ato (veja modo livre).

As capacidades devem ser fundamentais, não se deve criar novas capacidades que possam ser representadas por outras existentes (axioma 1).

Então por ex nao se deve criar "cavalgar" e "andar de camelo", mas sim "montar animais" e onde se concordar que conhecimentos diferentes são necessarios
(como montar um cavalo, um camelo, ou uma aguia gigante, etc) criam-se especializações na ficha (a forma de fazer isso é descrita na propria ficha).

Outro exemplo: não se deve criar "mecatronica", mas sim o jogador combinar "mecânica" e "eletronica".

As capacidades tem modos de uso: pessimo, ruim, medio, bom, excelente. O jogador que tem a ficha começa no "medio".

### Modo livre
Considera-se que qualquer um pode fazer qualquer coisa no nivel "ruim" (ou seja, o jogador que não tem a ficha começa no "ruim"), 
exceto se na propria ficha isso estiver proibido (o jogador por exemplo
nao poderia montar um circuito se nao tiver 'eletronica' como ficha propria).

Se o jogador decidir usar o modo livre de alguma ficha, jogar e for bem-sucedido (mestre e jogadores decidem se o uso pode ser chamado 
de bem-sucedido, mas a palavra final é do mestre) o jogador ganha a ficha (e portanto é considerado com inicio em "medio" a partir dai).

Na ficha deve existir, na area "ruim", a seção "(geral)", e isso indica uso livre. Se ela nao existir, o uso livre é proibido.

Por ex, em:
    + Natação
    + ruim (geral): vc engole muita agua, -1 saúde, morte é possível (primais)
    + ruim: vc engole agua, -1 de saude é possivel (primais)

É permitido então nadar a qualquer um como modo livre da natação, mas existe risco de vida (mais sobre saúde e primais adiante).

### Modo avançado
Chama-se de uso avançado se o jogador possui a ficha. Uma vez que ele possui a ficha, é preciso checar, quando for ser usada a capacidade,
em que nivel o jogador está. Ele começa no médio, e bonus ou penalidades deslocam em 1 para cima ou para baixo o uso.


## Primais
As primais são associadas a caracteristicas como força, inteligencia, carater, etc, e  são representados por cubinhos coloridos 
(cada cor representa um tipo) ou qualquer tipo de peça pequena.

Os jogadores coletam primais nas cenas, e gastam primais para pagar o uso de capacidades ou comprar capacidades que ainda não tenham.

As primais são:
- Mana
- Estamina
- Anima
- Arte
- Fortuna
- Bem (good)
- Mal (evil)

## Interações

Todas as vezes que existir uma interação (q pode ser entre jogadores, entre PCs e NPCs, ou entre jogadores e objetos, etc) o sistema de interações tem que ser
utilizado.

Ele é composto de:
- pool de dados
- cartas de fluxo

Os jogadores começam com um pool de 5 dados da mesma cor. 
Cartas de fluxo existem em (? - TODO: quantos tipos? ) diferentes. 

Nas mesas de jogo existirão então duas (? TODO: duas só? ) filas de fluxo. Uma para ações individuais e outra para ações em grupo.

Colocam-se então (? - TODO: quantas) cartas na fila individual, e (?) na fila coletiva, com a descrição virada para baixo para que não seja possivel ler.
As cartas de fluxo tem espaços para se colocar dados, com um valor especifico, em cima e em baixo da carta.

Numa interação, após o mestre dar sinal para o inicio, um jogador ou um grupo jogam seus dados. Uma vez definidos os valores dos dados, começa uma contagem de tempo.

Nesse tempo o jogador ou grupo devem escolher cartas e colocar os dados com numeros corretos em cima dos slots nas cartas, na parte de baixo.

Simultaneamente, o mestre (ou outro jogador em caso de disputas) deve posicionar com cuidado dados na parte de cima das cartas 
(qualquer acidente que movimente os dados de uma parte de forma que não se saiba mais os valores da rodada impedem que a parte coloque dados nas
cartas - os dados ficam todos fora dela, no pool, com os valores que tiverem)

Dados que não tenham sido colocados em cartas (opcionalmente ou por falta de tempo ou acidente) são considerados ainda "o pool" e podem afetar as
regras. Dados posicionados sobre as cartas nao são considerados no pool.

Uma vez encerrado o tempo, mesmo q todos os dados nao tenham sido posicionados, resolve-se a interação seguindo os passos:

- Cartas com mais dados de um lado do que do outro são "propriedade" da parte que colocou mais dados. 
    Nenhum dado no entanto deve ser removido e colocados de volta no pool, pq a quantidade de dados e diferença entre elas pode influenciar as regras
- Cartas com dados somente de uma parte também são de propriedade dela
- Cartas em empate são consideradas agindo sobre os dois grupos
- Cartas vazias são consideradas "cartas fracas"

Tendo sido feitas as atribuiçoes, viram-se as cartas e resolve-se os efeitos. 
Cada carta tem regras especificas (algumas são vagas e nesse caso devem ser interpretadas pelo Mestre e também pelos jogadores), 
e as cartas podem solicitar valores nos dados do pool (por ex, "com parte que tiver um 5 no pool acontece ..."), primais, estados de saude,
ou qualquer outra condição.

Cartas de propriedade de um grupo dizem se afetam os donos, ou as vezes dao a eles a escolha de dizer que sofre o efeito (cartas em empate
ainda permitem essa escolha se for de comum acordo, embora em geral afetem ambas as partes).

Cartas fracas devem ser usadas utilizando suas regras especificas para isso, ou enfraquecidas de alguma forma pelo mestre, caso elas
sejam ativadas mesmo sem dados (as cartas informam suas ativações).

A interação em grupo se faz da mesma forma, mas com varias partes de ambos os lados. Idealmente cada parte terá dados de cores especificas
para facilitar a atribuição de cartas.

Um efeito final é determinado e descrito na cena.

Então, após se decidir numa cena que a interação é necessária, os passos são:

- jogar os dados
- iniciar a contagem de tempo
- posicionar os dados
- atribuir as cartas no final do tempo
- ler e resolver as cartas

A interação continua numa proxima rodada até que todas as partes resolvam parar, ou que algum efeito das proprias cartas pare a interação.

Para continuar descartam-se as cartas da fila anterior, devolvem-se os dados, posicionam-se novas cartas e o processo se repete. 

### Interpretando resultados
A interpretação de resultados vagos ou dubios pode ser feita pelo Mestre ou pelos jogadores, mas tem que seguir as regras. Se uma carta diz algo como 
"alguma coisa sai ligeiramente errado", ou uma "alguma coisa sai errado" é uma carta fraca, os jogadores podem sugerir o que, mas tem que ser algo
que realmente saiu errado - as sugestões que obviamente tentarem tirar os jogadores de problemas indicados pelos fluxos não devem ser usadas.

A palavra final é sempre do mestre.

### Fluxos
Existem (? TODO: quantos tipos?) tipos de fluxos:

- Ação
- Sorte 
- Mente
- Tempo
- Destino
- Balanço

#### Ação
Fluxos de ação interferem com tentativas de se realizar alguma coisa. Elas falam sobre se aquilo que se quer fazer foi bem sucedido, se falhou, se ocorre
algo inesperado.

Exemplos:
- Funciona, mas...
- Funcionou?
- O resultado foi...

#### Sorte
Fluxos de sorte falam sobre como eventos que não se pode contar podem melhorar ou piorar uma situação.

Exemplos:
- Boa sorte
- Má sorte
- A sorte foi...

#### Mente
Fluxos da mente interferem com tarefas mentais de forma semelhante a como a Ação interfere com tarefas fisicas.

Exemplos:
- Distração
- Idéia
- Bloqueio
- Engano

#### Tempo
Fluxos de tempo falam sobre a passagem do tempo, se coisas devem continuar, se são acabam, se são interrompidas, etc.

Exemplos:
- Interrupção
- Fim
- Atraso
- Pode acabar agora, mas...

#### Destino
Fluxos de destino falam sobre consequencias duradouras.

Exemplos:
- Catastrofe
- Morte

#### Balanço
Fluxos de balanço falam para qual lado da interação tendem os acontecimentos.

Exemplos:
- Reviravolta




