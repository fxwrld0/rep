import unittest

def calculate(amount, curr):
    rates = {"RUB": 92.5, "EUR": 0.92}
    return amount * rates.get(curr, 0)

class TestSimple(unittest.TestCase):
    def test_rub(self):
        self.assertEqual(calculate(10, "RUB"), 925.0)
    def test_eur(self):
        self.assertEqual(calculate(10, "EUR"), 9.2)

if __name__ == "__main__":
    unittest.main()
