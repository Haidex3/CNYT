import unittest
import math
from library import add, subtract, multiply, divide, modulus, conjugate, polar, phase

class TestComplexFunctions(unittest.TestCase):

    # Test addition of complex numbers
    def test_add(self):
        self.assertEqual(add((2, 3), (1, -2)), (3, 1))
        self.assertEqual(add((0, 0), (4, 5)), (4, 5))

    # Test multiplication of complex numbers
    def test_multiply(self):
        self.assertEqual(multiply((2, 3), (1, -2)), (8, -1))
        self.assertEqual(multiply((0, 0), (4, 5)), (0, 0))

    # Test subtraction of complex numbers
    def test_subtract(self):
        self.assertEqual(subtract((2, 3), (1, -2)), (1, 5))
        self.assertEqual(subtract((0, 0), (4, 5)), (-4, -5))

    # Test division of complex numbers
    def test_divide(self):
        self.assertEqual(divide((2, 3), (1, -2)), (-0.8, 1.4))
        self.assertEqual(divide((4, 5), (0, 1)), (5, -4))

    # Test modulus (magnitude) of a complex number
    def test_modulus(self):
        self.assertAlmostEqual(modulus((3, 4)), 5.0, delta=1e-5)
        self.assertAlmostEqual(modulus((-2, 0)), 2.0, delta=1e-5)

    # Test conjugate of a complex number
    def test_conjugate(self):
        self.assertEqual(conjugate((2, 3)), (2, -3))
        self.assertEqual(conjugate((0, 0)), (0, 0))

    # Test polar representation of a complex number
    def test_polar(self):
        # The expected values and tolerances are adjusted
        self.assertAlmostEqual(polar((3, 4))[0], 3.0, delta=1e-5)
        self.assertAlmostEqual(polar((3, 4))[1], 4.0, delta=1e-5)

        self.assertAlmostEqual(polar((-1, 0))[0], 1.0, delta=1e-5)
        self.assertAlmostEqual(polar((-1, 0))[1], 0.0, delta=1e-5)

    # Test phase (argument/angle) of a complex number
    def test_phase(self):
        self.assertAlmostEqual(phase((1, math.sqrt(3))), math.pi / 3, places=5)
        self.assertAlmostEqual(phase((1, 0)), 0.0, places=5)


if __name__ == '__main__':
    unittest.main()
