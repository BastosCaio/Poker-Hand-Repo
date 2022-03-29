#!/usr/bin/env python3

from obs import PokerHand,Deck,Test

def get_int(prompt,*,min:int=1,max:int=100):
  """Essa função pega um input inteiro.
        
  Essa função pega um número inteiro como input do usuário dentro dos valores de mínimo e máximo especificados
  e, caso esse input não esteja dentro dos valores esperados, ela pede um input novamente, até que o valor
  colocado esteja dentro dos valores esperados.     

  Args:
      prompt(str): Mesnsagem que aparecerá no console.
      min(int): Valor mínimo.
      max(int): Valor máximo.
      
  Returns: 
      int: Valor digitado pelo usuário. 

  """
    
  get_input = True
  while get_input:
    try:
      value = int(input(prompt + " (" + str(min) + " -> " + str(max) + ") "))
      if value >= min and value <= max:
        get_input = False
        return value
    except:
      pass

if __name__ == "__main__":
    
    test_ask = get_int("In what mode do you want to play? 1 = Random hands, 2 = Specific Hands, 3 = Pre Implemented Tests ",min=1, max=3)
    
    if test_ask == 3:
        print('\n-------------- Welcome to the Pré Implemented Test mode --------------\n')
        print('In this mode you don\'t have to input anything, the Tests are going to happen following a predetermined list')
        Test(test_ask)
        
    elif test_ask == 2:
        print('\n-------------- Welcome to the Specific Hands mode --------------\n')
        print('In this mode you have to input 2 strings tha represent the hands that each of the two players will have')
        print('The strings must have the equivalent of 5 cards, each consisting of 2 characters the first being equivalent to the card\'s value and the second being equivalent to its suit.')
        print('A single space is used as the separator between the cards. Ex: \'TC TH 5C 5H KH\'')
        
        hand1 = input("Inform the hand of player 1: ")
        hand2 = input("Inform the hand of player 2: ")
        
        Test(test_ask, hand1, hand2)
        
        
    else:
        print('\n-------------- Welcome to the Random Hands mode --------------\n')
        print('This mode is like normal poker, each of the 2 players will draw a hand from a random pool of cards and the one with the best hand will win.')
        print('The only input needed is the number of games the two players are going to play.\n')
        
        num_decks = 1 # define o número de baralhos utilizados 
        num_cards = 5 # define o número de cartas de cada jogador
        num_players = 2 # define o numero de pessoas jogando (pode ser de 2 a 10) 
        num_shuffles = 1 # define o número de vezes que o baralho é embaralhado
        num_games = get_int("How many games?",max=500)
        
        
        #validation = get_int("How many games?",max=500)
            
        for i in range(1, num_games+1): # loop para cada jogo
            print("Game: " + str(i)) 
            shoe = Deck(num_decks) # cria um baralho que será usado durante o loop
            shoe.shuffle(num_shuffles) # embaralha o baralho criado
            players = [PokerHand() for i in range(num_players)] # Cria um objeto Hand para cada jogador, que vai conter as informações referentes à sua mão
            for i in range(num_cards): # loop de compra de cartas para abastecer as mãos
                for player in players: # Assim como no poker tradicional, nesse programa cada jogador recebe uma carta de cada vez
                    player.take_card(shoe.top_card())
            winner = (0,0,0,"") # é criada a tupla que vai armazenar as informações do vencedor       
            for count, player in enumerate(players, start=1):
                print("(%d)" % (count)) # imprime o número do jogador
                player.analyze_strength()
                print(player) # imprime a mão do jogador
                if player.strength > winner[1]: # se a mão do jogador for mais forte que o winner ele se torna o winner
                    winner = (count,player.strength,player.strength.highcard,player.get_strength()) 
                else:
                    if player.strength == winner[1]:
                        if player.strength.highcard > winner[2]:
                            winner = (count,player.strength,player.strength.highcard,player.get_strength())
                 
            print("Winner: Player " + str(winner[0]) + " with " + winner[3])
            print("\n")
            
            sorted1 = sorted(player.cards,reverse=True)
            sorted2 = sorted(player.cards)
            #print("Cards left: " + str(len(shoe)))

