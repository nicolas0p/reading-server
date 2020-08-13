import unittest
from number_reader import portuguese_number_reader as reader

class Portuguese_number_reader_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.correct_digits = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                'seis', 'sete', 'oito', 'nove']

        cls.correct_tens = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
                'sessenta', 'setenta', 'oitenta', 'noventa']
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


if __name__ == '__main__':
    unittest.main()
