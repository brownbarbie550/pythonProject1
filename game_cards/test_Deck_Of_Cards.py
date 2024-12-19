from unittest import TestCase
from Deck_Of_Cards import DeckOfCards



class TestDeckOfCards(TestCase):

    def setUp(self):
        """Set up a fresh DeckOfCards instance before each test"""
        print("this is a set up")
        self.deck = DeckOfCards()

    def tearDown(self):
        """Clean up after each test"""
        print("this is a teardown")

    def test_init_valid(self):
        """Test that the deck is initialized with exactly 52 cards"""
        self.assertTrue(len(self.deck.cards_pack) == 52)

    def test_cards_are_unique(self):
        """Test that all crds in the deck are unique(no duplicates)"""
        uni_list = []
        for c in self.deck.cards_pack:
            if c not in uni_list:
                uni_list.append(c)
        self.assertEqual(len(uni_list), len(self.deck.cards_pack))


    def test_cards_are_shuffled(self):
        """Test that the deck's 'cards_pack' is shuffled after calling 'cards_shuffle'"""
        original = self.deck.cards_pack[:]
        self.deck.cards_shuffle()
        self.assertNotEqual(original, self.deck.cards_pack)

    def test_cards_amount_after_shuffle(self):
        """Test that shuffling the deck does not change the number of cards"""
        original = self.deck.cards_pack[:]
        self.deck.cards_shuffle()
        self.assertEqual(len(original), len(self.deck.cards_pack))

    def test_deal_one(self):
        """Test that calling 'deal_one' removes one card from the deck"""
        d_card = self.deck.deal_one()
        self.assertEqual(len(self.deck.cards_pack), 51)
        self.assertNotIn(d_card, self.deck.cards_pack)

    def test_deal_one_empty_deck(self):
        """Test that calling 'deal_one' on an empty deck returns 'None'"""
        for c in range(52):
            self.deck.deal_one()
        self.assertIsNone(self.deck.deal_one())





