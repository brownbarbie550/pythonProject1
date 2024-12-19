
from Deck_Of_Cards import DeckOfCards
from Player import Player
from Card import OneCard


class Cardgame:
    """Initializes the game, creates players, a deck and starts the game by calling new_game() to deal cards"""
    def __init__(self, name1, name2, cards_per_player=26):
        if type(cards_per_player) != int:
            raise TypeError("invalid type of character, only numbers")
        if not (10 <= cards_per_player <= 26):
            raise ValueError("card value must be between 1-13")
        self.player1 = Player(name1, cards_per_player)
        self.player2 = Player(name2, cards_per_player)
        self.deck = DeckOfCards()

        self.start = True
        self.new_game()
        self.start = False

    def new_game(self):
        """calls set_hand() on both players to distribute cards from the deck"""
        if self.start:
            self.deck.cards_shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
        else:
            raise TypeError

    def get_winner(self):
        """determines the winner by comparing the number of remaining cards for each player"""
        if len(self.player1.player_cards) > len(self.player2.player_cards):
            return self.player1
        elif len(self.player2.player_cards) > len(self.player1.player_cards):
           return self.player2
        return None













