import unittest
import leap



class TestLeapYear(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(leap.is_leap_year(1600), "1600 is a leap year!")
        self.assertEqual(leap.is_leap_year(1996), "1996 is a leap year!")
        self.assertEqual(leap.is_leap_year(2000), "2000 is a leap year!")

    def test_incorrect(self):
        self.assertEqual(leap.is_leap_year(1700), "1700 is not a leap year!")
        self.assertEqual(leap.is_leap_year(2100), "2100 is not a leap year!")
        self.assertEqual(leap.is_leap_year(2021), "2021 is not a leap year!")





if __name__ == "main":
    unittest.main()