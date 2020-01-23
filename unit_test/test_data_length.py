import numpy as np
import pandas as pd
from my_project import view_point
import unittest
from my_project.utils.utility import *


class TestStringMethods(unittest.TestCase):
    def test_check_length(self):
        test_1 = pd.Series(
            [123, 456, 234, 567, 345, 123, 456, 789, 543, 234, 234, 234, 234, 234, 234, 234, 234, 234, 234, 1])
        expected_result_1 = ["NG", summary_for_check_length(test_1)]
        test_2 = pd.Series([123, 456, 234, 567, 345, 123, 456, 789, 543, None])
        expected_result_2 = ["NA", summary_for_check_length(test_2)]
        test_3 = pd.Series([123, 456, 234, 567, 345, 123, 456, 789, 543])
        expected_result_3 = ["OK", summary_for_check_length(test_3)]
        self.assertEqual(view_point.check_length(test_1), expected_result_1)
        self.assertEqual(view_point.check_length(
            test_2), expected_result_2)
        self.assertEqual(view_point.check_length(test_3), expected_result_3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
