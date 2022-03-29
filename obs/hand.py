from .handstrength import HandStrength
from .card import Card

class PokerHand:
    def __init__(self):
        self.cards = []
        self.strength = False
    
    def __str__(self) -> str:
        return "\n".join([str(card) for card in self.cards]) + "\n" + str(self.strength) + ": " + str(self.strength.get_highcard()) + "\n"

    def __len__(self) -> int:
        return len(self.cards)
    
    def __getitem__(self,i) -> Card:
        return self.cards[i]

    def take_card(self,card: Card):
        """Essa função compra uma carta do baralho.
        
        Essa função compra uma carta do baralho, tirando ela do Deck e adicionando-a a mão

        Args:
            card: parâmetro da classe Card, que representa uma carta de poker.

        """
        if not (card is None):
            self.cards.append(card)
    
    def get_strength(self):
        """Essa função retorna a força da mão.
        
        Essa função retorna a força da mão em forma de string, para que seja visualizada no console depois.

        Returns:
            str: (força da carta): (Carta mais forte)

        """
        return str(self.strength) + ": " + self.strength.get_highcard()

    def sorted(self,*,reverse=False):
        """Essa função coloca as cartas em ordem de valor.
        
        Essa função coloca as cartas em ordem de valor a partir do porâmetro reverse.
        Se reverse for true as cartas ficarão em ordem decrescente de valor e se 
        reverse for false elas ficarão em ordem crescente. 
        

        Args:
            reverse(bool): Informa se a ordem das cartas deve ser crescente o decrescente.

        Returns:
            list. Lista de cartas em ordem crescente ou decrescente.

        """
        return ", ".join(sorted(self.cards,reverse=reverse))
    
    def analyze_strength(self):
        """Essa função obtem o falor de força da mão.
        
        Essa função obtem o falor de força da mão chamando a função HandStrength, que analiza cada
        possibilidade de pontuação no poker e usa a carta maior para desempatar, caso seja necessário.
        O valor de força da mão é definido e adicionado como parâmetro à mão, de forma que possa 
        ser chamado no meio do código.


        """
        if len(self.cards) == 5:
            self.strength = HandStrength(self.cards)
