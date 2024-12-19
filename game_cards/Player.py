from random import random
from random import randint
from Deck_Of_Cards import DeckOfCards
from Card import OneCard
from random import choice


class Player:
    """Initializes a player with a name and specified number pf cards, Defaults to 26 cards if the provided number is out of range"""
    def __init__(self, player_name, cards_per_player):
        if type(cards_per_player) != int:
            raise TypeError("Invalid type of character, only numbers")
        if cards_per_player > 26 or cards_per_player < 10:
            cards_per_player = 26
        if type(player_name) != str:
            raise TypeError("Invalid type of character, only string")
        self.player_name = player_name
        self.cards_per_player = cards_per_player
        self.player_cards = []

    def __str__(self):
        """Returns a string describing the player's name and the number of cards they have"""
        return f"player_name: {self.player_name}, amount of cards per player: {self.cards_per_player}"

    def __repr__(self):
        """similar to __str__ but meant for a more detailed representation of the player"""
        return f"player_name: {self.player_name}, amount of cards per player: {self.cards_per_player}"

    def set_hand(self, deck: DeckOfCards):
        """Deals a set number of cards to the player from the deck and adds them to their hand"""
        if type(deck) != DeckOfCards:
            raise TypeError("This is not the right class")
        for i in range(self.cards_per_player):
            card = deck.deal_one()
            self.player_cards.append(card)

    def get_card(self):
        """Returns and removes a random card from the player's card and prints the card"""
        card1 = choice(self.player_cards)
        self.player_cards.remove(card1)
        return card1

    def add_card(self, card: OneCard):
        """Adds a card to the player's hand"""
        if type(card) != OneCard:
            raise TypeError("This is not the right class")
        self.player_cards.append(card)












