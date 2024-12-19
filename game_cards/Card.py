class OneCard:
    """Initializes a card with a value and a suit"""

    def __init__(self, card_value, card_suit):
        if type(card_value) != int:
            raise TypeError("value must be integer")
        if type(card_suit) != int:
            raise TypeError("suit must be integer")
        if not (1 <= card_value <= 13):
            raise TypeError("card value must be between 1-13")
        if not (1 <= card_suit <= 4):
            raise TypeError("card suit must be between 1-4")
        self.value = card_value
        self.suit = card_suit

    def __str__(self):
        return f"card's value is : {self.value}, card's suit is {self.suit}"

    def __repr__(self):
        return f"card's value is : {self.value}, card's suit is {self.suit}"

    def __gt__(self, other):
        """Returns True if the current card's value and suit is greater than the other card's value and suit"""
        if self.value == 1 and other.value != 1:
            return True
        elif self.value != 1 and other.value == 1:
            return False
        elif self.value == other.value:
            return self.suit > other.suit
        else:
            return self.value > other.value

    def __eq__(self, other):
        """Returns True if both the value and the suit of the two cards are the same"""
        return self.value == other.value and self.suit == other.suit
