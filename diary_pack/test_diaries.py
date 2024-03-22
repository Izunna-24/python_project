from unittest import TestCase

from diaries import Diaries


class TestDiaries(TestCase):
    def test_diary_can_add(self):
        diaries = Diaries()
        diaries.add("username", "password")
        self.assertEqual(1, diaries.get_size())

    def test_diaries_can_delete_diary_entered(self):
        diaries = Diaries()
        diaries.add("username", "password")
        diaries.add("username2", "password2")
        self.assertEqual(2, diaries.get_size())
        diaries.delete_diary("username", "password")
        self.assertEqual(1, diaries.get_size())

    def test_that_deleting_diary_in_empty_diaries_throwsdiarynotfounderrorexception(self):
        diaries = Diaries()
