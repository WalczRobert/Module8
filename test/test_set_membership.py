"""Robert Walczak"""

import unittest
from more_fun_with_collections import set_membership

class SetTest(unittest.TestCase):
    def test_in_set_true(self):
        set = {1, 2, 3, 4, 5}
        expected_result = True
        self.assertEqual(expected_result, set_membership.in_set(set, 3), True)

    def test_in_set_false(self):
        set = {1, 2, 3, 4, 5}
        expected_result = False
        self.assertEqual(expected_result, set_membership.in_set(set, 9), False)


if __name__ == '__main__':
    unittest.main()