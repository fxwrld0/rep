![Tests](https://github.com/fxwrld0/rep/actions/workflows/main.yml/badge.svg)
import unittest

def calculate(amount, curr):
    rates = {"RUB": 92.5, "EUR": 0.92}
    return amount * rates.get(curr, 0)

class TestSimple(unittest.TestCase):
    def test_rub(self):
        # Здесь целое число, ошибки нет
        self.assertEqual(calculate(10, "RUB"), 925.0)

    def test_eur(self):
        # Используем assertAlmostEqual для чисел с запятой
        # Это решит проблему с 9.200000000000001
        self.assertAlmostEqual(calculate(10, "EUR"), 9.2, places=2)

if __name__ == "__main__":
    unittest.main()
