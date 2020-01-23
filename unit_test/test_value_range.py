from my_project import view_point
import pandas as pd
import numpy as np
import unittest


class TestStringMethods(unittest.TestCase):
    def test_check_range(self):
        test_1 = pd.Series([1, 1.1, 1.2, 1.3, 1.5, 1.7, 1.4, 1.9])
        expected_result_1 = ["OK", round(np.mean(test_1)/np.std(test_1), 2)]
        test_2 = pd.Series([1, 1.1, 1.2, 1.3, 1.5, 1.7, 1.4, 2])
        expected_result_2 = ["NG", round(np.mean(test_2)/np.std(test_2), 2)]
        test_3 = pd.Series([1, 2, 3, 4, None])
        expected_result_3 = ["NA", "null"]
        self.assertEqual(view_point.check_range(test_1), expected_result_1)
        self.assertEqual(view_point.check_range(test_2), expected_result_2)
        self.assertEqual(view_point.check_range(test_3), expected_result_3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
