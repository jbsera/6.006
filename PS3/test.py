# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:27:03 2022

@author: joyse
"""

import unittest
from flix_chill import FlixChillManager

class TestCases(unittest.TestCase):
    def test_01(self):
        f = FlixChillManager()
        f.insert(1, 100, 50)
        f.insert(2, 101, 40)
        f.insert(3, 102, 1)
        self.assertTrue(f.highest(10) == 1)

    def test_02(self):
        f = FlixChillManager()
        f.insert(1, 100, 50)
        f.insert(2, 101, 40)
        f.insert(3, 102, 1)
        self.assertTrue(f.highest(101) == 2)

    def test_03(self):
        f = FlixChillManager()
        f.insert(1, 100, 50)
        f.insert(2, 101, 40)
        f.insert(3, 102, 1)
        self.assertTrue(f.highest(102) == 3)

    def test_04(self):
        f = FlixChillManager()
        f.insert(1000, 228, 99)
        f.insert(1001, 229, 49)
        f.insert(1002, 130, 34)
        self.assertTrue(f.highest(200) == 1000)

    def test_05(self):
        f = FlixChillManager()
        f.insert(1000, 228, 99)
        f.insert(1001, 229, 49)
        f.insert(1002, 130, 340)
        self.assertTrue(f.highest(100) == 1002)
        
    def test_06(self):
        f = FlixChillManager()
        f.insert(1, 1, 99)
        f.insert(2, 2, 49)
        f.insert(3, 3, 340)
        f.insert(5, 4, 100)
        f.insert(6, 5, 3400)
        f.insert(7, 6, 3)
        f.insert(8, 7, 46)
        f.insert(9, 8, 17)
        f.insert(10, 9, -20)
        
        print('my answer', f.highest(9))
        print('--------------------')
        self.assertTrue(f.highest(9) == 10)
    
    def test_07(self):
        f = FlixChillManager()
        f.insert(1, 1, -1)
        f.insert(2, 2, -2)
        f.insert(3, 3, -3)
        f.insert(4, 4, -4)
        f.insert(5, 5, -5)
        f.insert(6, 6, -6)
        f.insert(7, 7, -7)
        f.insert(8, 8, -8)
        f.insert(9, 9, -9)
        f.insert(10, 10, -10)
        f.insert(11, 11, -11)
        f.insert(12, 12, -12)
        f.insert(13, 13, -13)
        f.insert(14, 14, -14)
        f.insert(15, 15, -15)
        f.insert(16, 16, -16)
        f.insert(17, 17, -17)
        f.insert(18, 18, -18)
        f.insert(19, 19, -19)
        f.insert(20, 20, -20)
        f.insert(21, 21, -21)
        f.insert(22, 22, -22) 
        f.insert(23, 23, -23)
        f.insert(24, 24, -24)
        f.insert(25, 25, -25)
        f.insert(26, 26, -26)
        f.insert(27, 27, -27)
        f.insert(28, 28, -28)
        f.insert(29, 29, -29)
        f.insert(30, 30, -30)
        f.insert(31, 31, -31)
        f.insert(32, 32, -32)
        f.insert(33, 33, -33)
        f.insert(34, 34, -34)
        f.insert(35, 35, -35)
        f.insert(36, 36, -36)
        f.insert(37, 37, -37)
        f.insert(38, 38, -38)
        f.insert(39, 39, -39)
        f.insert(40, 40, -40)
        f.insert(41, 41, -41)
        f.insert(42, 42, -42)
        f.insert(43, 43, -43)
        f.insert(44, 44, -44)
        f.insert(45, 45, -45)
        f.insert(46, 46, -46)
        f.insert(47, 47, -47)
        f.insert(48, 48, -48)
        f.insert(49, 49, -49)
        f.insert(50, 50, -50)
        f.insert(51, 51, -51)
        f.insert(52, 52, -52)
        f.insert(53, 53, -53)
        f.insert(54, 54, -54)
        f.insert(55, 55, -55)
        f.insert(56, 56, -56)
        f.insert(57, 57, -57)
        f.insert(58, 58, -58)
        f.insert(59, 59, -59)
        f.insert(60, 60, -60)
        f.insert(61, 61, -61)
        f.insert(62, 62, -62)
        f.insert(63, 63, -63)
        f.insert(64, 64, -64)
        f.insert(65, 65, -65)
        f.insert(66, 66, -66)
        f.insert(67, 67, -67)
        f.insert(68, 68, -68)
        f.insert(69, 69, -69)
        f.insert(70, 70, -70)
        f.insert(71, 71, -71)
        f.insert(72, 72, -72)
        f.insert(73, 73, -73)
        f.insert(74, 74, -74)
        f.insert(75, 75, -75)
        f.insert(76, 76, -76)
        f.insert(77, 77, -77)
        f.insert(78, 78, -78)
        f.insert(79, 79, -79)
        f.insert(80, 80, -80)
        f.insert(81, 81, -81)
        f.insert(82, 82, -82)
        f.insert(83, 83, -83)
        f.insert(84, 84, -84)
        f.insert(85, 85, -85)
        f.insert(86, 86, -86)
        f.insert(87, 87, -87)
        f.insert(88, 88, -88)
        f.insert(89, 89, -89)
        f.insert(90, 90, -90)
        f.insert(91, 91, -91)
        f.insert(92, 92, -92)
        f.insert(93, 93, -93)
        f.insert(94, 94, -94)
        f.insert(95, 95, -95)
        f.insert(96, 96, -96)
        f.insert(97, 97, -97)
        f.insert(98, 98, -98)
        f.insert(99, 99, -99)
        f.insert(100, 100, -100)
        
        
        for i in range(1,101):
            self.assertTrue(f.highest(i)==i)

    def test_08(self):
        f = FlixChillManager()
        f.insert(1, 1, 1)
        f.insert(2, 2, 2)
        f.insert(3, 3, 3)
        f.insert(4, 4, 4)
        f.insert(5, 5, 5)
        f.insert(6, 6, 6)
        f.insert(7, 7, 7)
        f.insert(8, 8, 8)
        f.insert(9, 9, 9)
        f.insert(10, 10, 10)
        f.insert(11, 11, 11)
        f.insert(12, 12, 12)
        f.insert(13, 13, 13)
        f.insert(14, 14, 14)
        f.insert(15, 15, 15)
        f.insert(16, 16, 16)
        f.insert(17, 17, 17)
        f.insert(18, 18, 18)
        f.insert(19, 19, 19)
        f.insert(20, 20, 20)
        f.insert(21, 21, 21)
        f.insert(22, 22, 22) 
        f.insert(23, 23, 23)
        f.insert(24, 24, 24)
        f.insert(25, 25, 25)
        f.insert(26, 26, 26)
        f.insert(27, 27, 27)
        f.insert(28, 28, 28)
        f.insert(29, 29, 29)
        f.insert(30, 30, 30)
        f.insert(31, 31, 31)
        f.insert(32, 32, 32)
        f.insert(33, 33, 33)
        f.insert(34, 34, 34)
        f.insert(35, 35, 35)
        f.insert(36, 36, 36)
        f.insert(37, 37, 37)
        f.insert(38, 38, 38)
        f.insert(39, 39, 39)
        f.insert(40, 40, 40)
        f.insert(41, 41, 41)
        f.insert(42, 42, 42)
        f.insert(43, 43, 43)
        f.insert(44, 44, 44)
        f.insert(45, 45, 45)
        f.insert(46, 46, 46)
        f.insert(47, 47, 47)
        f.insert(48, 48, 48)
        f.insert(49, 49, 49)
        f.insert(50, 50, 50)
        f.insert(51, 51, 51)
        f.insert(52, 52, 52)
        f.insert(53, 53, 53)
        f.insert(54, 54, 54)
        f.insert(55, 55, 55)
        f.insert(56, 56, 56)
        f.insert(57, 57, 57)
        f.insert(58, 58, 58)
        f.insert(59, 59, 59)
        f.insert(60, 60, 60)
        f.insert(61, 61, 61)
        f.insert(62, 62, 62)
        f.insert(63, 63, 63)
        f.insert(64, 64, 64)
        f.insert(65, 65, 65)
        f.insert(66, 66, 66)
        f.insert(67, 67, 67)
        f.insert(68, 68, 68)
        f.insert(69, 69, 69)
        f.insert(70, 70, 70)
        f.insert(71, 71, 71)
        f.insert(72, 72, 72)
        f.insert(73, 73, 73)
        f.insert(74, 74, 74)
        f.insert(75, 75, 75)
        f.insert(76, 76, 76)
        f.insert(77, 77, 77)
        f.insert(78, 78, 78)
        f.insert(79, 79, 79)
        f.insert(80, 80, 80)
        f.insert(81, 81, 81)
        f.insert(82, 82, 82)
        f.insert(83, 83, 83)
        f.insert(84, 84, 84)
        f.insert(85, 85, 85)
        f.insert(86, 86, 86)
        f.insert(87, 87, 87)
        f.insert(88, 88, 88)
        f.insert(89, 89, 89)
        f.insert(90, 90, 90)
        f.insert(91, 91, 91)
        f.insert(92, 92, 92)
        f.insert(93, 93, 93)
        f.insert(94, 94, 94)
        f.insert(95, 95, 95)
        f.insert(96, 96, 96)
        f.insert(97, 97, 97)
        f.insert(98, 98, 98)
        f.insert(99, 99, 99)
        f.insert(100, 100, 100)
        
        
        for i in range(1,101):
            print('i', i)
            self.assertTrue(f.highest(i)==100)
        
    

if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)