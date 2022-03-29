from obs import PokerHand,Deck
import unittest


class Test(unittest.TestCase):          
    def __init__(self,testType,hand1 = None,hand2 = None):
        
        """Essa função realiza testes de performance do programa.
            
        Essa função realiza testes de performance do programa. Ela tem dois modos diferentes, o modo de
        mãos específicas e o modo de testes unitários pré programados. No modo de mãos específicas é 
        necessário o input de duas strings que representam as mãos dos jogadores e elas serão comparadas 
        entre si. Já no modo de testes unitários pré-programados não são necessários inputs, o programa irá
        comparar 26 duplas de mãos pré-selecionadas e exibirá os resultados no console.            

        Args:
            testType(int): Tipo de teste realizado, sendo: 2 -> Mãos específicas 3 -> Testes unitários pré-programados.
            hand1(str): Mão do jogador 1 no teste das mãos específicas.
            hand2(str): Mão do jogador 2 no teste das mãos específicas

        """
        
        num_decks = 10 # define o número de baralhos utilizados 
        num_cards = 5 # define o número de cartas de cada jogador
        num_players = 2 # define o numero de pessoas jogando (pode ser de 2 a 10)
        test_hands = ["TC TH 5C 5H KH","9C 9H 5C 5H AC","TS TD KC JC 7C","JS JC AS KC TD","7H 7C QC JS TS","7D 7C JS TS 6D","5S 5D 8C 7S 6H","7D 7S 5S 5D JS","AS AD KD 7C 3D","AD AH KD 7C 4S","TS JS QS KS AS","AC AH AS AS KS","TS JS QS KS AS","TC JS QC KS AC","TS JS QS KS AS","QH QS QC AS 8H","AC AH AS AS KS","TC JS QC KS AC","AC AH AS AS KS","QH QS QC AS 8H","TC JS QC KS AC","QH QS QC AS 8H","7H 8H 9H TH JH","JH JC JS JD TH","7H 8H 9H TH JH","4H 5H 9H TH JH","7H 8H 9H TH JH","7C 8S 9H TH JH","7H 8H 9H TH JH","TS TH TD JH JD","7H 8H 9H TH JH","JH JD TH TC 4C","JH JC JS JD TH","4H 5H 9H TH JH","JH JC JS JD TH","7C 8S 9H TH JH","JH JC JS JD TH","TS TH TD JH JD","JH JC JS JD TH","JH JD TH TC 4C","4H 5H 9H TH JH","7C 8S 9H TH JH","4H 5H 9H TH JH","TS TH TD JH JD","4H 5H 9H TH JH","JH JD TH TC 4C","7C 8S 9H TH JH","TS TH TD JH JD","7C 8S 9H TH JH","JH JD TH TC 4C","TS TH TD JH JD","JH JD TH TC 4C"]
        test_winners = [1,2,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,1]
        
        if testType == 2:
            num_tests = 1
            test_hands = [hand1,hand2]
        else:
            num_tests = len(test_winners)
        
        for i in range(1, num_tests+1): # loop para teste
            print("Teste: " + str(i)) 
            shoe = Deck(num_decks) # cria um baralho que será usado durante o loop
            shoe.shuffle(1) # embaralha o baralho criado
            players = [PokerHand() for i in range(num_players)] # Cria um objeto Hand para cada jogador, que vai conter as informações referentes à sua mão
            for count, player in enumerate(players, start=0): # loop de compra de cartas para abastecer as mãos e realizar os testes   
                for j in range(num_cards): 
                    player.take_card(shoe.specific_card(test_hands[(i-1)*2+count][0],test_hands[(i-1)*2+count][1])) # compra uma das cartas do array i-1 da lista de testes
                    test_hands[(i-1)*2+count] = test_hands[(i-1)*2+count][3:]
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
                            
            if testType==2:
                print("Winner: Player " + str(winner[0]) + " with " + winner[3])
                
            else:
                print("Winner: Player " + str(winner[0]) + " with " + winner[3] + ". And this result is: "+ str(winner[0] == test_winners[i-1])) 
                self.assertTrue(winner[0] == test_winners[i-1])

