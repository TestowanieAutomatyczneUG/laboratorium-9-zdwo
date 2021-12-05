import unittest
from unittest.mock import *
from ..src.Environment import Environment
from ..src.Checker import Checker
from datetime import datetime

checker = Checker()


class TestChecker(unittest.TestCase):

    def test_reminder_played(self):
        checker.env.getTime = Mock('getTime')
        checker.env.getTime.return_value = datetime(2021, 12, 5, 17, 56, 55, 831364)
        checker.reminder()
        self.assertTrue(checker.played)

    def test_reminder_notPlayed(self):
        checker.env.getTime = Mock('getTime')
        checker.env.getTime.return_value = datetime(2021, 12, 5, 10, 56, 55, 831364)
        checker.reminder()
        self.assertFalse(checker.played)
