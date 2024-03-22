from unittest import TestCase
import cornflakes_in_class


class Test(TestCase):
    def test_length_of_list(self):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = 10
        actual_output = cornflakes_in_class.length_of_list(number_list)
        self.assertEqual(expected_output, actual_output)

    def test_sum_of_even_positions(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = 130
        actual_output = cornflakes_in_class.sum_of_even_positions(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_sum_of_odd_positions(self):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = 105
        actual_output = cornflakes_in_class.sum_of_odd_positions(number_list)
        self.assertEqual(expected_output, actual_output)

    def test_return_list_of_string(self):
        names = ['hannah', 'bob', 'Charlie']
        expected_output = ['hannah', 'bob']
        actual_output = cornflakes_in_class.return_list_of_string(names)
        self.assertEqual(expected_output, actual_output)

    def test_multiply_elements_at_every_third_position(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = 11726
        actual_output = cornflakes_in_class.multiply_elements_at_every_third_position(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_average_of_list_elements(self):
        numbers = [1, 2, 3, 4]
        expected_output = 2.5
        actual_output = cornflakes_in_class.average_of_list_elements(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_get_the_largest_number(self):
        numbers = [1, 2, 4, 4, 5, 99, 19]
        expected_output = 99
        actual_output = cornflakes_in_class.get_the_largest_number(numbers)
        self.assertEqual(expected_output, actual_output)

    def test_get_the_smallest_number(self):
        numbers = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
        expected_output = 1
        actual_output = cornflakes_in_class.get_the_smallest_number(numbers)
        self.assertEqual(expected_output, actual_output)
