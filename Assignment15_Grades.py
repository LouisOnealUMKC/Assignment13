import unittest
import Grades

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
    
    def test_total_returns_0(self):
        result = Grades.total([])
        self.assertEqual(result, 0, "The total function should return 0")

    def test_average_one(self):
        result = Grades.total([2,5,9])
        self.assertAlmostEqual(result, 5.33333, 3)

    def test_average_two(self):
        result = Grades.total([2,15,22,9])
        self.assertAlmostEqual(result, 12.0000, 4)

    def test_median_odd(self):
        result = Grades.median([2,5,1])
        self.assertEqual(result,2,"median should be 2")

    def test_median_even(self):
        result = Grades.median([5,2,1,3])
        self.assertAlmostEqual(result,2.5,2)

    def test_median_valueError(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])

unittest.main()

