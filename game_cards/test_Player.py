from unittest import TestCase
from Player import Player
from Deck_Of_Cards import DeckOfCards
from unittest import mock
from unittest.mock import patch
from Card import OneCard


class TestPlayer(TestCase):
    def setUp(self):
        """Set up a Player object and DeckOfCards object before each test"""
        print("this is a set up")
        self.play = Player("Dagmawit", 26)
        self.deck = DeckOfCards()

    def tearDown(self):
        """Clean up after each test"""
        print("this is a teardown")

    def test_init_valid_player_name(self):
        """Test that the Player is initialized with the correct name"""
        self.assertEqual(self.play.player_name,"Dagmawit")

    def test_init_valid_cards_amount(self):
        """Test that the Player is initialized with the correct number of cards"""
        self.assertEqual(self.play.cards_per_player, 26)

    def test_init_invalid_type_of_cards(self):
        """Test that initializing a Player with non-integer card count raises a TypeError"""
        with self.assertRaises(TypeError):
            gamer = Player("Barbie", "card")

    @mock.patch('Deck_Of_Cards.DeckOfCards.deal_one', return_value= OneCard(4,"Diamond"))
    def test_set_hands_deals_26_cards(self, mock_deal_one):
        """Test that the set_hand method assigns 26 cards to the player"""
        self.play.set_hand(self.deck)
        self.assertEqual(self.play.player_cards.count(OneCard(4, "Diamond")),26)

    def test_get_card_valid(self):
        """Test that the get_card method removes a card and returns None when cards are exhausted"""
        self.play.set_hand(self.deck)
        self.play.get_card()
        self.assertEqual(len(self.play.player_cards), 25)

    def test_add_card_add_one_card_valid(self):
        """Test that add_card correctly adds a single valid card to the player's hand"""
        gamer = Player("Dagi", 26)
        new_card = OneCard(5, "Diamond")
        gamer.add_card(new_card)
        self.assertIn(new_card, gamer.player_cards)
        self.assertEqual(len(gamer.player_cards), 1)



