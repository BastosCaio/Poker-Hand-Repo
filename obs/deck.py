from random import shuffle
from .card import Card

class Deck:
    def __init__(self,num_of_decks:int=1):
        self.cards = []
        suits = ["S","D","C","H"]
        values = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
        for i in range(num_of_decks):
            for suit in suits:
                for value in values:
                    self.cards.append(Card(value,suit))
    
    def __str__(self) -> str:
        return str(len(self.cards)) + " cards left."

    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self,num_of_shuffles: int = 1):
        """Essa função embaralha o baralho.
        
        Essa função embaralha o baralho, randomizando a ordem das cartas 
        contidas nele um número de vezes igual ao valor de num_of_shuffles.
        
        Args:
            num_of_shuffles(int): Indica a quantidade de vezes que o baralho será embaralhado
        
        """
        
        for i in range(num_of_shuffles):
            
          shuffle(self.cards)

    def top_card(self) -> Card:
        """Essa função compra a carta do topo do baralho.
        
        Essa função compra a carta do topo do baralho, eliminando-a do baralho e adicionando à mão.
        
        Returns:
            Card: Retorna a carta do tipo Card que estiver no topo do Deck
        
        """
        return self.cards.pop(0)
    
    def specific_card(self,cardvalue: str,cardsuit: str) -> Card:
        """Essa função compra uma carta específica do baralho.
        
        Essa função compra uma carta específica do baralho, encontrando-a a partir 
        do seu valor e naipe eliminando-a do baralho e adicionando à mão.
        Para a função funcionar deve existir no baralho uma carta com valor e naipe especificados.
        
        Args:
            cardvalue(str): Indica o valor da carta ex. "A", "5", "T"
            cardsuit(str): Indica o naipe da carta, que pode ser: "S" "D" "C" "H"
        
        
        Returns:
            Card: Retorna a carta do tipo Card que tiver o naipe e valor especificados
        
        """
        value_reconv = {"A": "A","2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": "J", "Q": "Q", "K": "K"}        
        if isinstance(cardvalue, str):
            cardvalue = value_reconv[cardvalue]
        for i in range(len(self.cards)):
            if self.cards[i].suit == cardsuit and self.cards[i].value == cardvalue:
                return self.cards.pop(i) # para testar adicione escreva no console: player.take_card(shoe.specific_card('K','C'))
            
            
                