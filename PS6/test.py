# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:14:10 2022

@author: joyse
"""

import unittest
from disjoint_subsequences import disjoint_subsequences


tests = [
    (
        "abcde",
        "abcdeabcde",
        True,
    ),
    (
        "abcde",
        "abcdefbcdef",
        False,
    ),
    (
        "",
        "",
        False,
    ),
    (
        "",
        "weproicqunwyeproqwieuljsl",
        True,
    ),
    (
        "shortest path",
        "My **favorite** shortest path algorithm is *Dijkstra's*. What is *your* favorite path algorithm?",
        True,
    ),
]


class TestCases(unittest.TestCase):
    def test_01(self):
        X, Y, ans = tests[0]
        solution = disjoint_subsequences(X, Y)
        self.assertTrue(solution == ans)

    def test_02(self):
        X, Y, ans = tests[1]
        solution = disjoint_subsequences(X, Y)
        self.assertTrue(solution == ans)

    def test_03(self):
        X, Y, ans = tests[2]
        solution = disjoint_subsequences(X, Y)
        print('solution', solution)
        print('answer', ans)
        self.assertTrue(solution == ans)

    def test_04(self):
        X, Y, ans = tests[3]
        solution = disjoint_subsequences(X, Y)
        self.assertTrue(solution == ans)

    def test_05(self):
        X, Y, ans = tests[4]
        solution = disjoint_subsequences(X, Y)
        self.assertTrue(solution == ans)


if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)