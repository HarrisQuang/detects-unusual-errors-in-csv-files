from my_project import view_point
import pandas as pd
import unittest


class TestStringMethods(unittest.TestCase):
    def test_check_numeric(self):
        test_1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
        expected_result_1 = ['OK', 1.00]
        test_2 = pd.Series([1, 2, None, None, None, None, None])
        expected_result_2 = ['NA', round(2/7, 2)]
        test_3 = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, None])
        expected_result_3 = ['NG', 0.95]
        self.assertEqual(view_point.check_numeric(
            test_1), expected_result_1)
        self.assertEqual(view_point.check_numeric(
            test_2), expected_result_2)
        self.assertEqual(view_point.check_numeric(
            test_3), expected_result_3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
