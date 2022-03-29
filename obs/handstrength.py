from collections import defaultdict

class HandStrength:
    def __init__(self,cards):
        self.cards = cards
        self.highcard = 0
        self.strength = self.analyze()
        
    def __str__(self):
        return self.human_readable()

    def __gt__(self,other):
        return self.strength > other

    def __lt__(self,other):
        return self.strength < other

    def __eq__(self,other):
        return self.strength == other

    def human_readable(self) -> str: # Usada para traduzir a pontuação da mão de um número, para o que ele representa 
        """Essa função transforma os valores de pontuação em valores string.
        
        Essa função transforma os valores de pontuação, que são interpretados como números pelo programa, 
        para valores verbais, como "Flush" e "Two Pairs" , de forma que sejam entendidos por humanos. 
        
        Returns:
            str. Valor de pontuação em formato de string.

        """
        
        human = {23: "Royal Straight Flush",22: "Straight Flush",21:"Four of a Kind",20:"Full House",19:"Flush",18:"Straight",17:"Three of a Kind",16:"Two pairs",15:"One Pair",14:"High Card"}
        return human[self.strength]

    def analyze(self) -> int:
        """Essa função analiza a mão em busca de sua pontuação.
        
        Essa é a função principal da classe HandStrength, ela checa qual a pontuação mais adequada para a mão 
        em questão, checando pontuação por pontuação, até encontrar uma que tenha as condições exatas e, caso 
        não encontre, assume que a pontuação é highcard, que é a menor pontuação possível.
        
        Returns:
            int. Valor de pontuação encontrado.

        """
        
        if self.check_royal_straight_flush(): return 23
        if self.check_straight_flush(): return 22
        if self.check_four_of_a_kind(): return 21
        if self.check_full_house(): return 20
        if self.check_flush(): return 19
        if self.check_straight(): return 18
        if self.check_three_of_a_kind(): return 17
        if self.check_two_pairs(): return 16
        if self.check_one_pairs(): return 15
        else: 
            self.set_highcard()
            return 14

    def get_highcard(self):
        """Essa função retorna o valor da carta mais forte como uma string.
    
        Returns:
            str. Valor da carta mais forte da mão, como string.

        """
        
        if type(self.highcard) is list:
            return " and ".join([str(card.get_value()) for card in self.highcard]) + ""
        return str(self.highcard.get_value()) + ("")
        
    def set_highcard(self):
        """Essa função pega o valor da carta de maior valor da mão (highcard).
        
        Essa função pega o valor da carta de maior valor da mão (highcard). Ela adiciona um parâmetro 
        chamado highcard dentro do parâmetro strenght que vai armazenar a carta de maior valor da mão,
        para fatores de desempate e para caso a pontuação da mão seja highcard.

        """
        
        self.highcard = sorted(self.cards,reverse=True)[0]
        
    def check_royal_straight_flush(self) -> bool:
        """Essa função checa se a mão tem um royal straight flush.
    
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
     
        suits = [card.suit for card in self.cards]
        values = [card.value for card in self.cards]
        if 10 in values and 'J' in values and 'Q' in values and 'K' in values and 'A'  in values and suits[0] == 'H':
           self.set_highcard()
           return True
        else:
           return False        

    def check_straight_flush(self) -> bool:
         """Essa função checa se a mão tem um straight flush.
        
         Returns:
             bool. True se for essa a pontuação adequada e False se não for.

         """
         if self.check_flush() and self.check_straight():
            return True
         else:
            return False

    def check_four_of_a_kind(self) -> bool:
        """Essa função checa se a mão tem um four of a kind.
        
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
        value_counts = defaultdict(lambda:0)
        for card in self.cards:
            value_counts[card.value]+=1
        if sorted(value_counts.values()) == [1,4]:
            winner = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)[0][0]
            winners = []
            for card in self.cards:
                if card.value == winner:
                    winners.append(card)
            highcard = 0
            for card in winners:
                if highcard == 0: highcard = card
                if highcard and card > highcard:
                    highcard = card              
            self.highcard = highcard
            return True
        return False

    def check_full_house(self) -> bool:
        """Essa função checa se a mão tem um full house.
        
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
        
        value_counts = defaultdict(lambda:0)
        for card in self.cards:
            value_counts[card.value]+=1
        if sorted(value_counts.values()) == [2,3]:
            sorted_hand = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)
            boat = sorted_hand[0][0]
            full_of = sorted_hand[1][0]
            boat_list = []
            full_of_list = []
            for card in self.cards:
                if card.value == boat:
                    boat_list.append(card)
                if card.value == full_of:
                    full_of_list.append(card)
            high_boat = 0
            high_full_of = 0
            for card in boat_list:
                if high_boat == 0: high_boat = card
                if high_boat and card > high_boat:
                    high_boat = card
            for card in full_of_list:
                if high_full_of == 0: high_full_of = card
                if high_full_of and card > high_full_of:
                    high_full_of = card
            self.highcard = [high_boat,high_full_of]
            return True
        return False

    def check_flush(self) -> bool:
        """Essa função checa se a mão tem um flush.
        
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
        suits = [card.suit for card in self.cards]
        value_counts = defaultdict(lambda:0)
        for card in self.cards:
            value_counts[card.value]+=1
        if len(set(suits))==1:
            self.set_highcard()
            return True
        else:
            return False

    def check_straight(self) -> bool:
        """Essa função checa se a mão tem um straight.
        
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
        card_strength = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10,"J":11, "Q":12, "K":13, "A":14}
        values = [card.value for card in self.cards]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v] += 1
        rank_values = [card_strength[str(i)] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range==4):
            self.set_highcard()
            return True
        else:
            #check straight with low Ace
            if set(values) == set(["A", "2", "3", "4", "5"]):
                self.set_highcard()
                return True
            return False

    def check_three_of_a_kind(self) -> bool:
        """Essa função checa se a mão tem um three of a kind.
        
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
        value_counts = defaultdict(lambda:0)
        for card in self.cards:
            value_counts[card.value]+=1
        if set(value_counts.values()) == set([3,1]):
            winner = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)[0][0]
            winners = []
            for card in self.cards:
                if card.value == winner:
                    winners.append(card)
            highcard = 0
            for card in winners:
                if highcard == 0: highcard = card
                if highcard and card > highcard:
                    highcard = card              
            self.highcard = highcard
            return True
        else:
            return False

    def check_two_pairs(self) -> bool:
        """Essa função checa se a mão tem um two pairs.
        
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
        value_counts = defaultdict(lambda:0)
        for card in self.cards:
            value_counts[card.value]+=1
        if sorted(value_counts.values())==[1,2,2]:
            sorted_hand = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)
            pair_one = sorted_hand[0][0]
            pair_two = sorted_hand[1][0]
            pair_one_list = []
            pair_two_list = []
            for card in self.cards:
                if card.value == pair_one:
                    pair_one_list.append(card)
                if card.value == pair_two:
                    pair_two_list.append(card)
            high_pair_one = 0
            high_pair_two = 0
            for card in pair_one_list:
                if high_pair_one == 0: high_pair_one = card
                if high_pair_one and card > high_pair_one:
                    high_pair_one = card
            for card in pair_two_list:
                if high_pair_two == 0: high_pair_two = card
                if high_pair_two and card > high_pair_two:
                    high_pair_two = card
            self.highcard = [high_pair_one,high_pair_two]
            return True
        else:
            return False

    def check_one_pairs(self) -> bool:
        """Essa função checa se a mão tem um oen pair.
        
        Returns:
            bool. True se for essa a pontuação adequada e False se não for.

        """
        
        value_counts = defaultdict(lambda:0)
        for card in self.cards:
            value_counts[card.value]+=1
        if 2 in value_counts.values():
            winner = sorted(value_counts.items(), key=lambda x: x[1], reverse=True)[0][0]
            winners = []
            for card in self.cards:
                if card.value == winner:
                    winners.append(card)
            highcard = 0
            for card in winners:
                if highcard == 0: highcard = card
                if highcard and card > highcard:
                    highcard = card              
            self.highcard = highcard
            return True
        else:
            return False
