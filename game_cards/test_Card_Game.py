from unittest import TestCase
from Player import Player
from Card_Game import Cardgame
from Deck_Of_Cards import DeckOfCards
from Card import OneCard


class TestCardgame(TestCase):

    def setUp(self):
        """Set up resources and objects needed for the tests"""
        print("this is a setup")
        self.gamer1 = Player("Dagmawit", 26)
        self.gamer2 = Player("Barbie", 24)
        self.deck = DeckOfCards()
        self.play = Player("brown", 26)
        self.game = Cardgame(self.gamer1.player_name, self.gamer2.player_name, 26)


    def tearDown(self):
        """Clean up resources after each test"""
        print("this is a teardown")

    def test_init_valid_player_name(self):
        """Test that player 1's name is correctly initialized"""
        self.assertEqual(self.gamer1.player_name, "Dagmawit")

    def test_init_valid_cards_amount1(self):
        """Test that player 1's card count is correctly initialized to 26"""
        self.assertEqual(self.gamer1.cards_per_player, 26)

    def test_new_game(self):
        """Test if new_game properly distributes cards"""
        self.assertTrue(len(self.game.player1.player_cards) == 26)
        self.assertTrue(len(self.game.player2.player_cards) == 26)
        self.assertEqual(len(self.game.deck.cards_pack), 0)

    def test_get_winner_player1(self):
        """Simulates a scenario where player 1 has more cads than player 2 and asserts that the winner is correctly determined"""
        self.game.player1.player_cards = [OneCard(value, suit) for suit in range(1,5) for value in range (1,8)]
        self.game.player2.player_cards = [OneCard(value, suit) for suit in range(1,5) for value in range (1,6)]
        winner = self.game.get_winner()
        self.assertEqual(winner, self.game.player1)

    def test_get_winner_player2(self):
        """Simulates a scenario where player 2 has more cads than player 1 and asserts that the winner is correctly determined"""
        self.game.player1.player_cards = [OneCard(value, suit) for suit in range(1, 5) for value in range(1, 6)]
        self.game.player2.player_cards = [OneCard(value, suit) for suit in range(1, 5) for value in range(1, 8)]
        self.assertEqual(self.game.get_winner(), self.game.player2)

    def test_get_winner_players_are_teko(self):
        """Simulates a scenario where both players have the same numbers of cards and asserts that no winner is determined and the method returns None for a tie"""
        self.game.player1.player_cards = [OneCard(value, suit) for suit in range(1, 5) for value in range(1, 8)]
        self.game.player2.player_cards = [OneCard(value, suit) for suit in range(1, 5) for value in range(1, 8)]
        self.assertIsNone(self.game.get_winner())