# -*- coding: utf-8 -*-

class InvalidBetException(Exception):
    """Exception raised for invalid bets"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
