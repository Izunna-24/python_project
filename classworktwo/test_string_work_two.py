from unittest import TestCase
from classworktwo.string_work_two import upper_and_lower_case
from classworktwo.string_work import count_digits_and_letters


class Test(TestCase):
    def test_upper_and_lower_case(self):
        self.word = "Hello World"
        expected = (2, 8)
        actual = upper_and_lower_case(self.word)
        self.assertEqual(expected, actual)

    def test_count_digits_and_letters(self):
        self.word = "Hello World 123"
        expected = (3, 10)
        actual = count_digits_and_letters(self.word)
        self.assertEqual(expected, actual)
