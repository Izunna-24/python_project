from diary import Diary
from DiaryNotFoundError import DiaryNotFoundError


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username, password):
        diary = Diary(username, password)
        self.diaries.append(diary)

    def get_size(self):
        return len(self.diaries)

    def find_by_username(self, username):
        for diary in self.diaries:
            if diary.get_username() == username:
                return diary

        raise DiaryNotFoundError("Diary not found")

    def delete_diary(self, username, password):
        diary = self.find_by_username(username)
        diary.unlock_diary(password)
        self.diaries.remove(diary)
