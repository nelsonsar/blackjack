# -*- coding: utf-8 -*-

from exception import InvalidBetException

class Player(object):
    """Represents a blackjack player.
       A player can place a bet in a game and it also holds a Hand
       that will be used to define the winner
    """

    def __init__(self):
        self.hand = None

    def place_bet(self, bet, game):
        """Places a bet in given game"""

        if not bet:
            raise InvalidBetException("Invalid bet given")

        game.register_bet(bet)


class Game(object):
    """Game is responsible for the lifecycle of the application.
       It receives the player's bet, deal cards and resolve who is
       the winner.
    """

    def __init__(self):
        self.bets = []

    def register_bet(self, bet):
        """Add player bet to bet list"""
        self.bets.append(str(bet))

    def deal_cards(self):
        """Return a random Hand from Deck"""
        pass

    def resolve_bust(self):
        """Resolve the winner based on Players Hands"""
        self.result = "House wins!"

class Bet(object):
    """Simple object to hold player bet"""
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        """Return Bet object as the following string: '1 gil bet'"""
        return "%d gil bet" % self.amount
