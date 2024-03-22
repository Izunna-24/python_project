from unittest import TestCase
from class_manipulation import Manipulation


class TestManipulation(TestCase):
    def test_string(self):
        string = Manipulation()
        string.get_string("philip")
        self.assertEqual("PHILIP", string.print_string())


