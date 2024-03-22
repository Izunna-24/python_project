from diary_pack.diary import Diary

from unittest import TestCase


class TestDiary(TestCase):
    def setUp(self):
        self.diary = Diary("password", "username")

    def test_diary_can_be_unlocked(self):
        diary = self.diary
        self.assertFalse(diary.is_locked)
        diary.lock_diary()
        self.assertTrue(diary.is_locked)
        diary.unlock_diary("password")
        self.assertFalse(diary.is_locked)

    def test_diary_is_unlocked_diary_can_be_locked(self):
        self.assertFalse(self.diary.is_locked)
        self.diary.unlock_diary("password")
        self.assertFalse(self.diary.is_locked)
        self.diary.lock_diary()
        self.assertTrue(self.diary.is_locked)

    def test_diary_is_unlocked_diary_can_take_entry(self):
        self.assertFalse(self.diary.is_locked)
        self.assertEqual(0, self.diary.diary_body())
        self.diary.create_entry("tittle", "body")
        self.assertEqual(1, self.diary.diary_body())

    def test_diary_is_unlocked_diary_can_delete_entry(self):
        self.assertEqual(0, self.diary.diary_body())
        self.diary.create_entry("tittle", "body")
        self.assertEqual(1, self.diary.diary_body())
        self.diary.delete_entry(1)
        self.assertEqual(0, self.diary.diary_body())

    def test_diary_is_unlocked_diary_can_update_entry(self):
        self.assertEqual(0, self.diary.diary_body())
        self.diary.create_entry("tittle", "body")
        self.assertEqual(1, self.diary.diary_body())
        self.assertEqual("tittle", self.diary.find_entry_by_id(1).get_title())
        self.assertEqual("body", self.diary.find_entry_by_id(1).get_body())
        self.diary.update_entry(1, "Exam", "Subjects")
        self.assertEqual("Exam", self.diary.find_entry_by_id(1).get_title())
        self.assertEqual("Subjects", self.diary.find_entry_by_id(1).get_body())
