import random

from Card import OneCard


class DeckOfCards:
    """Initializes the deck of cards with 52 unique cards (13 for each suit: Diamond, Spade, Heart, Club)"""

    def __init__(self):
        self.cards_pack = []
        for i in range(1, 5):
            for j in range(1, 14):
                self.cards_pack.append(OneCard(j, i))

    def cards_shuffle(self):
        """Shuffles the deck of cards using shuffle() method from random module"""
        random.shuffle(self.cards_pack)

    def deal_one(self):
        """Deals (removes) a random card from the deck using randint() to pick random index pop it and print the card"""
        if len(self.cards_pack) > 0:
            card = self.cards_pack.pop(random.randint(0, len(self.cards_pack) - 1))
            return card

        return None
