![Status](https://github.com/fxwrld0/rep/actions/workflows/main.yml/badge.svg)
import unittest

# Упрощенная функция конвертации для теста
def calculate(amount, curr):
    rates = {"RUB": 92.5, "EUR": 0.92}
    if curr in rates:
        return amount * rates[curr]
    return 0

class TestCurrency(unittest.TestCase):
    def test_rub(self):
        # 100 * 92.5 = 9250.0
        self.assertEqual(calculate(100, "RUB"), 9250.0)

    def test_eur(self):
        # 10 * 0.92 = 9.2
        self.assertEqual(calculate(10, "EUR"), 9.2)

if __name__ == "__main__":
    unittest.main()
   
