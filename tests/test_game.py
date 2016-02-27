# -*- coding: utf-8 -*-

import unittest
from blackjack.game import Game, Bet

class GameTest(unittest.TestCase):
    def test_register_bet(self):
        game = Game()
        bet = Bet(1)
        game.register_bet(bet)

        self.assertEquals(["1 gil bet"], game.bets)

class BetTest(unittest.TestCase):
    def test_to_string(self):
        bet = Bet(1)

        self.assertEquals("1 gil bet", str(bet))
