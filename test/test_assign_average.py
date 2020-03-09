import unittest
from more_fun_with_collections import assign_average


class SetTest(unittest.TestCase):
    def test_assign_average_test_A(self):
        self.assertEqual(assign_average.switch_average('A'), 100)

    def test_assign_average_test_B(self):
        self.assertEqual(assign_average.switch_average('B'), 200)

    def test_assign_average_test_C(self):
        self.assertEqual(assign_average.switch_average('C'), 300)

    def test_assign_average_test_D(self):
        self.assertEqual(assign_average.switch_average('D'), 400)

    def test_assign_average_test_E(self):
        self.assertEqual(assign_average.switch_average('E'), 500)

    def test_assign_average_invalid_key(self):
        self.assertEqual(assign_average.switch_average('F'), KeyError)


if __name__ == '__main__':
    unittest.main()