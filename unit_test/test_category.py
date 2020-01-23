import numpy as np
import pandas as pd
from my_project import view_point
import unittest
from my_project.utils.utility import *


class TestStringMethods(unittest.TestCase):
    def test_check_category(self):
        test_1 = ['A', 'B', 'C', 'A', 'A', 'A', 'A', 'B', 'B',
                  'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D']
        expected_result_1 = ["NG", summary_for_check_category(test_1)]
        test_2 = ['A', 'B', 'C', 'A', 'A', 'A', 'A', 'B', 'B',
                  'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
        expected_result_2 = ["OK", summary_for_check_category(test_2)]
        test_3 = [None, None, None]
        expected_result_3 = ["NA", "null"]
        test_4 = ['A', None, None, None]
        expected_result_4 = ["NA", "null"]
        self.assertEqual(view_point.check_category(test_1), expected_result_1)
        self.assertEqual(view_point.check_category(test_2), expected_result_2)
        self.assertEqual(view_point.check_category(test_3), expected_result_3)
        self.assertEqual(view_point.check_category(test_4), expected_result_4)


suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
