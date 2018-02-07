import random
class Deck_of_cards(object):
    def __inti__(self):
        self.amount = 52
        self.cards = []
        suits = ["hearts", "diamnods", "spades", "hearts"]

        for value in range(1,14):
            for suit in suits:
                new_card = Card(value, suits)
                self.cards.append(new_card)

    def deal(self):
        for deal in self.cards:
            random.randint(1,52)
            return deal

class Card(object):
    def __inti__(self, value, suit):
        self.suit = suit
        self.value = value