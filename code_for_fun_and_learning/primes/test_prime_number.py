import unittest
from prime_numbers import is_prime

# Write this as a supplement to my blog post
# http://unstuck.grabyourfreedom.in/2018/01/why-unit-test-is-important.html


class TestPrimeNumber(unittest.TestCase):

    def test_valid_prime(self):
        prime = is_prime(7)
        self.assertTrue(prime)

    def test_composite_number(self):
        prime = is_prime(8)
        self.assertFalse(prime)

    def test_non_integer_input(self):
        prime = is_prime(2.1)
        self.assertFalse(prime)

    def test_string_input(self):
        prime = is_prime("2")
        self.assertFalse(prime)

    def test_is_two_prime(self):
        prime = is_prime(2)
        self.assertTrue(prime)

    def test_is_one_prime(self):
        prime = is_prime(1)
        self.assertFalse(prime)

    def test_input_negative_number(self):
        prime = is_prime(-234)
        self.assertFalse(prime)

    def test_bigger_composite(self):
        prime = is_prime(1000000008)
        self.assertFalse(prime)

    # Beware of this test. This test likely to take more time due to nature of
    # input (bigger prime). This test can be skipped by uncommenting the
    # immediate line of code
    # @unittest.skip("Removing from tests as it takes lot of time")
    def test_bigger_prime_number(self):
        prime = is_prime(1000000007)
        self.assertTrue(prime)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimeNumber)
    unittest.TextTestRunner(verbosity=2).run(suite)
