class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        self.value_conv = {"A": "A",2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "T", "J": "J", "Q": "Q", "K": "K"}
        self.card_strength = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J":11, "Q":12, "K":13, "A":14}
        self.suit_strength = {"S":1,"D":2,"C":3,"H":4}
    
    def __str__(self) -> str:
        return self.value_conv[self.value] + " " + self.suit + " " 

    def get_value(self):
        """Retorna o valor da carta.

        Essa função retorna, em formato de string o valor da carta.

        Returns:
            str: Valor da carta.

        """
        return self.value_conv[self.value]

    def __lt__(self,card) -> bool:
        try:
            if self.card_strength[str(self.value)] < self.card_strength[str(card.value)]:
                return True
            if self.card_strength[str(self.value)] == self.card_strength[str(card.value)] and self.suit_strength[self.suit] < self.suit_strength[card.suit]:
                return True
        except:
            print(str(self) + " -> " + str(card))
        return False

    def __gt__(self,card) -> bool:
        if self.card_strength[str(self.value)] > self.card_strength[str(card.value)]:
            return True
        if self.card_strength[str(self.value)] == self.card_strength[str(card.value)] and self.suit_strength[self.suit] > self.suit_strength[card.suit]:
            return True
        return False