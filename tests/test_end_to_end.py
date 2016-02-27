# -*- coding: utf-8 -*-

import unittest
from blackjack.game import Player, Game, Bet
from blackjack.exception import InvalidBetException

class TestEndToEnd(unittest.TestCase):
    def test_player_loses_with_null_bet(self):
        player = Player()
        game = Game()
        self.assertRaises(InvalidBetException, lambda: player.place_bet(None, game))

    def test_player_bet_and_lose(self):
        player = Player()
        game = Game()
        bet = Bet(1)

        player.place_bet(bet, game)

        player.hand = game.deal_cards()

        game.resolve_bust()

        self.assertEquals("House wins!", game.result)
