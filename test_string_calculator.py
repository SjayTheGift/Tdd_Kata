from string_calculator import StringCalculator
import unittest


class TestStringMethods(unittest.TestCase):
    calculate = StringCalculator()

    def test_empty_string(self):
        """it should return 0 if the string is empty"""
        value = self.calculate.add('')
        self.assertEqual(0, value)

    def test_add_two_CSVs(self):
        """it should add 2 numbers in a comma separated string"""
        value = self.calculate.add('1, 2')
        self.assertEqual(3, value)

    def test_add_multiple_CSVs(self):
        """it should an unknown amount of numbers in a comma separated string"""
        value = self.calculate.add('1, 2, 3')
        self.assertNotEqual(3, value)
        self.assertEqual(6, value)

    def test_new_line_as_delimiter(self):
        """it should be able to use new lines as delimiters"""
        value = self.calculate.add('1\n2,3')
        self.assertEqual(6, value)

    def test_different_delimiters(self):
        """it should be able handle different delimiters"""
        value = self.calculate.add('//;\n1;2')
        self.assertEqual(3, value)

    def test_negative_numbers_exception(self):
        """it should raise an exception containing all negative numbers if any are found"""
        with self.assertRaises(Exception) as context:
            self.calculate.add('-1, -2, -3, 1, 2, 3')
        self.assertTrue('negatives not allowed -1, -2, -3', context.exception)

    def test_bigger_than_1000(self):
        """it should ignore numbers bigger than 1000"""

        value = self.calculate.add('//;\n1000,1;2')
        self.assertEqual(3, value)

    def test_delimiters_any_length(self):
        """it should ignore numbers bigger than 1000"""
        value = self.calculate.add('//[***]\n1***2***3')
        self.assertEqual(6, value)

    def test_multiple_delimiters(self):
        """it should be able handle multiple delimiters"""
        value = self.calculate.add('//[*][%]\n1*2%3')
        self.assertEqual(6, value)

    def test_multiple_delimiters_length_longer_char(self):
        """it should be able handle multiple delimiters with length longer than one char"""
        value = self.calculate.add('//[**][%%]\n1**2%%3')
        self.assertEqual(6, value)


if __name__ == '__main__':
    unittest.main()
