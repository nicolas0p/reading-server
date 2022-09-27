import unittest
from number_reader import Portuguese_number_reader as reader

class Portuguese_number_reader_test(unittest.TestCase):

    def test_all_digits(self):
        results = []
        correct_digits = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                'seis', 'sete', 'oito', 'nove']
        for number in range(len(correct_digits)):
            reading = reader.read_number(number)
            results.append(reading)
        self.assertListEqual(results, correct_digits)

    def test_all_tens(self):
        results = []
        correct_tens = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
                'sessenta', 'setenta', 'oitenta', 'noventa']
        for number in range(len(correct_tens)):
            reading = reader.read_number((number + 1) * 10)
            results.append(reading)
        self.assertListEqual(results, correct_tens)

    def test_regular_composite_ten(self):
        number = 83
        result = reader.read_number(number)
        correct = "oitenta e três"
        self.assertEqual(result, correct)

    def test_all_irregular_tens(self):
        results = []
        correct_irregular_tens = ['onze', 'doze', 'treze', 'quatorze', 'quinze',
                'dezesseis', 'dezessete', 'dezoito', 'dezenove']
        for number in range(len(correct_irregular_tens)):
            reading = reader.read_number(11 + number)
            results.append(reading)
        self.assertListEqual(results, correct_irregular_tens)

    def test_all_hundreds(self):
        results = []
        correct_hundreds = ['duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
                'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
        for number in range(len(correct_hundreds)):
            reading = reader.read_number((number + 2) * 100)
            results.append(reading)
        self.assertListEqual(results, correct_hundreds)

    def test_composite_one_hundred(self):
        number = 183
        result = reader.read_number(number)
        correct = "cento e oitenta e três"
        self.assertEqual(result, correct)

    def test_irregular_hundred(self):
        number = 100
        result = reader.read_number(number)
        correct = "cem"
        self.assertEqual(result, correct)

    def test_composite_thousand(self):
        number = 3254
        result = reader.read_number(number)
        correct = "três mil e duzentos e cinquenta e quatro"
        self.assertEqual(result, correct)

    def test_ten_thousand_alone(self):
        number = 18000
        result = reader.read_number(number)
        correct = "dezoito mil"
        self.assertEqual(result, correct)

    def test_ten_thousand_and_hundred(self):
        number = 10900
        result = reader.read_number(number)
        correct = "dez mil e novecentos"
        self.assertEqual(result, correct)

    def test_ten_thousand_and_ten(self):
        number = 40091
        result = reader.read_number(number)
        correct = "quarenta mil e noventa e um"
        self.assertEqual(result, correct)

    def test_one_thousand_alone(self):
        number = 1000
        result = reader.read_number(number)
        correct = "mil"
        self.assertEqual(result, correct)

    def test_one_thousand_and_digit(self):
        number = 1006
        result = reader.read_number(number)
        correct = "mil e seis"
        self.assertEqual(result, correct)

    def test_one_thousand_and_hundred(self):
        number = 1100
        result = reader.read_number(number)
        correct = "mil e cem"
        self.assertEqual(result, correct)

    def test_negative_one_thousand(self):
        number = -1000
        result = reader.read_number(number)
        correct = "menos mil"
        self.assertEqual(result, correct)

    def test_out_of_range_number(self):
        number = 150000
        self.assertRaises(ValueError, reader.read_number, number)
        number = -150000
        self.assertRaises(ValueError, reader.read_number, number)

    def test_negative_exceptions(self):
        number = -18
        result = reader.read_number(number)
        correct = "menos dezoito"
        self.assertEqual(result, correct)

if __name__ == '__main__':
    unittest.main()
