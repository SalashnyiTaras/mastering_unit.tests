# test_<filename> - it is a convention to name file with unit tests

# be careful when naming tests - if a name of a test does not start with "test_",
# a unit-test will be simply skipped

# do not think that all tests being right in the order they were created: no, they do not
import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, 5), 15)  # need to choose appropriate assert from documentation
        self.assertEqual(calc.add(-1, 1), 0)  # need to choose appropriate assert from documentation
        self.assertEqual(calc.add(-1, -1), -2)  # need to choose appropriate assert from documentation

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 10), -5)
        self.assertEqual(calc.subtract(5, 4), 1)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 0), 0)
        self.assertEqual(calc.multiply(0, 10), 0)
        self.assertEqual(calc.multiply(-1, -1), 1)
        self.assertEqual(calc.multiply(-1, 4), -4)
        self.assertEqual(calc.multiply(11, -1), -11)
        self.assertEqual(calc.multiply(11, 11), 121)
        self.assertEqual(calc.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(10, -5), -2)
        self.assertEqual(calc.divide(-10, -5), 2)
        self.assertEqual(calc.divide(-5, 1), -5)
        self.assertEqual(calc.divide(1, 10), 0.1)

        # the best way to test exceptions
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if '__name__' == '__main__':
    unittest.main()
