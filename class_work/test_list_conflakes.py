from unittest import TestCase
import list_conflakes

class Test(TestCase):
    def test_that_function_creates_list(self):
        listing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected = len(listing)
        actual = list_conflakes.my_new_list(listing)
        self.assertEqual(expected, actual)

    def test_duplicate_my_new_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected = numbers * 2
        actual = list_conflakes.duplicate_my_new_list(numbers)
        self.assertEqual(expected, actual)

    def test_eliminate_duplicates_in_my_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15]
        expected = list(set(numbers))
        actual = list_conflakes.eliminate_duplicates_in_my_list(numbers)
        self.assertEqual(expected, actual)