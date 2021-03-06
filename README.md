# Desafio Python: Poker Hand

Essa aplicação foi criada como parte de um desafio, de programação em python. As regras do desafio podem ser encontradas no arquivo desafio python v1.0.pdf. Em resumo, o desafio consiste em criar um programa que simule um jogo de poker entre duas pessoas. O programa, portanto, emula um jogo de poker. Para rodar o programa o usuário deve clonar este repositório em seu computador e rodar o programa main.py em um interpretador de python.

A aplicação tem três modos de funcionamento, o modo 1 -> Random Hands, o modo 2 -> Specific Hands e o modo 3 -> Pré Implemented Test e você pode escolher o modo que deseja utilizar na inicialização da aplicação, digitando o número correspondente ao modo desejado como input no console. O modo Random Hands é o modo mais clássico em que alguns jogadores de poker se enfrentam comprando cartas aleatóriamente do baralho até que cada jogador tenha 5 cartas, então o programa compara as mãos dos jogadores para definir qual foi o vencedor. Nesse modo é solicitado que o usuário faça o input do número de jogadores (de 2 a 10) e do número de jogos que serão jogados em seguida (de 1 a 500). 

Os outros dois modos de utilização da aplicação são modos de teste. No modo Specific Hands é pedido que o jogador digite duas strings de caracteres que representam as mãos de cada jogador e elas serão comparadas para determinar qual dos dois jogadores foi vitorioso. No modo Pré Implemented Test, por sua vez, não é necessário nenhum input do usuário. Após a escolha desse modo serão realizados vários testes unitários pré-programados que testam vários casos comuns de embates de mãos, para checar o funcionamento da aplicação. Esses testes são realizados com mãos previamente definidas e os resultados dos embates de cada mão são comparados com um array que contem o resultado correto de cada um desses testes. A função assertTrue da biblioteca unittest é utilizada para fazer essa comparação, fazendo com que, se um dos resultados não corresponda ao esperado, o programa dê erro e aborte sua execução.



# Pacotes necessários

- unnittest

Para poder rodar o modo 3 -> Pré Implemented Test é necessário instalar o pacote unnittest no seu computador.
