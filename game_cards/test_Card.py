from unittest import TestCase
from Card import OneCard



class TestOneCard(TestCase):

    def setUp(self):
        print("this is a set up")

    def tearDown(self):
        print("this is a teardown")

    def test_init_valid(self):
        """Test that OneCard instance is correctly initialized with valid value and suit"""
        card = OneCard(1,2)
        self.assertTrue(card.value == 1 and card.suit == 2)

    def test_init_invalid_value_type(self):
        """Test that initializing a card with an invalid value type raises a TypeError"""
        with self.assertRaises(TypeError):
            card = OneCard("card", "Diamond")

    def test_init_invalid_suit_type(self):
        """Test that initializing a card with an invalid suit type raises a TypeError"""
        with self.assertRaises(TypeError):
            card = OneCard(1, "Spade")

    def test_init_invalid_value(self):
        with self.assertRaises(TypeError):
            card = OneCard(20, "Diamond")

    def test_init_invalid_suit(self):
        with self.assertRaises(TypeError):
            card = OneCard(1, "none")

    def test_gt_valid_ace_card_comparisons(self):
        """Test that an ace card is greater than any King card"""
        ace_of_spades = OneCard(1, 2)
        king_of_hearts = OneCard(13, 3)
        self.assertTrue(ace_of_spades > king_of_hearts)

    def test_gt_valid_not_ace_card_comparisons(self):
        """Test that a King card is greater than a 10 card"""
        king_of_hearts = OneCard(13, 1)
        ten_of_spade = OneCard(10, 3)
        self.assertTrue(king_of_hearts > ten_of_spade)

    def test_gt_invalid_card_comparisons(self):
        """Test that comparing a valid card with an invalid card raises a TypeError"""
        with self.assertRaises(TypeError):
            ace_of_spades = OneCard(1, 3)
            king_of_hearts = OneCard("Club", "Heart")
            self.assertFalse(ace_of_spades > king_of_hearts)

    def test_gt_diff_value(self):
        card1 = OneCard(8, 4)
        card2 = OneCard(8, 1)
        self.assertFalse(card2 > card1)

    def test_equality_valid(self):
        """Test that two cards with the same value and suit are equal"""
        card1 = OneCard(8, 4)
        card2 = OneCard(8, 4)
        self.assertEqual(card1, card2)

    def test_equality_invalid(self):
        """Test that two cards with different values or suits are not equal"""
        card1 = OneCard(8, 2)
        card2 = OneCard(7, 2)
        self.assertFalse(card1 == card2)


