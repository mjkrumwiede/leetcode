import unittest
from solutions import array_solutions as sol

class testTwoSum(unittest.TestCase):
    def test1(self):
        # Setup
        arr = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]

        # Execute
        ans = sol.twoSum(arr, target)

        # Assert
        self.assertEqual(ans, expected_output)
    
    def test2(self):
        # Setup
        arr = [2, 7, 11, 15]
        target = 22
        expected_output = [1, 3]

        # Execute
        ans = sol.twoSum(arr, target)

        # Assert
        self.assertEqual(ans, expected_output)

    def test3(self):
        # Setup
        arr = [2, 7, 11, 15, 37, 40, 28, 14, 2, 9]
        target = 47
        expected_output = [1, 5]

        # Execute
        ans = sol.twoSum(arr, target)

        # Assert
        self.assertEqual(ans, expected_output)
