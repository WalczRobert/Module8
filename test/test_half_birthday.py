import unittest
from more_fun_with_collections import half_birthday


class half_my_birthday(unittest.TestCase):
    def test_half_birthday(self):
        most_recent_birthday = half_birthday.date(2020, 3, 7)
        my_half_birthday = half_birthday.date(2020, 9, 5)
        self.assertEqual(half_birthday.half_birthday(most_recent_birthday), my_half_birthday)


if __name__ == '__main__':
    unittest.main()