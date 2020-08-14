import unittest
from number_reader import portuguese_number_reader as reader

class Portuguese_number_reader_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.correct_digits = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                'seis', 'sete', 'oito', 'nove']

        cls.correct_tens = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
                'sessenta', 'setenta', 'oitenta', 'noventa']

        cls.correct_irregular_tens = ['onze', 'doze', 'treze', 'quatorze', 'quinze',
                'dezesseis', 'dezessete', 'dezoito', 'dezenove']

        cls.correct_hundreds = ['duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
                'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

        cls.filler = 'e'

    def test_all_digits(self):
        results = []
        for number in range(len(self.correct_digits)):
            reading = reader(number)
            results.append(reading)
        self.assertListEqual(results, self.correct_digits)

    def test_all_tens(self):
        results = []
        for number in range(len(self.correct_tens)):
            reading = reader((number + 1) * 10)
            results.append(reading)
        self.assertListEqual(results, self.correct_tens)

    def test_regular_composite_ten(self):
        number = 83
        result = reader(number)
        correct = "oitenta e três"
        self.assertEqual(result, correct)

    def test_all_irregular_tens(self):
        results = []
        for number in range(len(self.correct_irregular_tens)):
            reading = reader(11 + number)
            results.append(reading)
        self.assertListEqual(results, self.correct_irregular_tens)

    def test_all_hundreds(self):
        #import pdb; pdb.set_trace()
        results = []
        for number in range(len(self.correct_hundreds)):
            reading = reader((number + 2) * 100)
            results.append(reading)
        self.assertListEqual(results, self.correct_hundreds)

    def test_composite_one_hundred(self):
        number = 183
        result = reader(number)
        correct = "cento e oitenta e três"
        self.assertEqual(result, correct)

    def test_irregular_hundred(self):
        number = 100
        result = reader(number)
        correct = "cem"
        self.assertEqual(result, correct)



if __name__ == '__main__':
    unittest.main()
