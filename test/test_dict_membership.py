"""Robert Walczak"""

import unittest
from more_fun_with_collections import dict_membership


class DictTest(unittest.TestCase):
    def test_in_dict_true(self):
        dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        self.assertEqual(True, dict_membership.in_dict(dict, 'B'), True)

    def test_in_dict_false(self):
        dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
        self.assertEqual(False, dict_membership.in_dict(dict, 'X'), False)


if __name__ == '__main__':
    unittest.main()