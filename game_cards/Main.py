from Deck_Of_Cards import DeckOfCards
from Player import Player
from Card import OneCard
from Card_Game import Cardgame


def display_game(game_one : Cardgame):
    """Displays each player's name and initial card"""
    print(f"{game_one.player1.player_name}'s cards: {game_one.player1.player_cards}")
    print(f"{game_one.player2.player_name}'s cards: {game_one.player2.player_cards}")

def play_round(game_one: Cardgame, round_num):
    """Simulates one round where both players play a card, the winner takes both cards"""
    card1 = game_one.player1.get_card()
    card2 = game_one.player2.get_card()

    print(f"{game_one.player1.player_name} plays: {card1}")
    print(f"{game_one.player2.player_name} plays: {card2}")

    if card1 > card2:
        game_one.player1.add_card(card2)
        game_one.player1.add_card(card1)
        print(f"{game_one.player1.player_name} wins this round")
    elif card2 > card1:
        game_one.player2.add_card(card1)
        game_one.player2.add_card(card2)
        print(f"{game_one.player2.player_name} wins this round")
    else:
        print("its a tie")

def play_game(game_one: Cardgame):
    """Playes up to 10 rounds or until a player runs out of cards, declares the winner"""
    for round_num in range(1, 11):
        if len(game_one.player1.player_cards) <= 0 or len(game_one.player2.player_cards) <= 0:
            print("a player has ran out of cards")
            break
        play_round(game_one, round_num)
    print(game_one.get_winner())

name1 = input("player1, enter your name: ")
name2 = input("player2, enter your name: ")
game = Cardgame(name1, name2, 26)
display_game(game)
play_game(game)




