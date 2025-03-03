# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:25:34 2022

@author: joyse
"""

import unittest
from search_lyrics import search_lyrics

tests = (
    (
        (
            "We're no strangers to love. You know the rules and so do I. A full commitment's what I'm thinking of.",
            "what ",
        ),
        True,
    ),
    (
        (
            "Mining away, I don't know what to mine, I'll mine this anyway, In this Minecraft day, So beautiful, mine further down.",
            "Fortnite",
        ),
        False,
    ),
    (("Are you cheating on this code submission?", "u cheat",), True,),
    (
        (
            "fmiwqpudlxryqsrkpdlueabjpftmlxalvunmimhddtkftjkscsjxtfckkpyd",
            "udlxryqsrkpd",
        ),
        True,
    ),
    (
        (
            "jordyufyyksxckxkvusdpktgmlqoxboijnpwrmpifrryhjemkisapsfwfecdduoptbmvmhhhodippsgarlryuivvmr",
            "isapsfwfeddduoptbm",
        ),
        False,
    ),
)


def check(test):
    args, staff_sol = test
    student_sol = search_lyrics(*args)
    return staff_sol == student_sol


class TestCases(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0]))

    def test_02(self):
        self.assertTrue(check(tests[1]))

    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)
