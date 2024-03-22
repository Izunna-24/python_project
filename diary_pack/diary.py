from entry import Entry


class Diary:
    def __init__(self, username, password):
        self.is_locked = False
        self.password = password
        self.username = username
        self.entries = []
        self.number_of_entries = 0

    def is_locked(self):
        return self.is_locked

    def unlock_diary(self, password):
        if self.password == password:
            self.is_locked = False

    def lock_diary(self):
        self.is_locked = True

    def create_entry(self, title, body):
        entry_id = self.number_of_entries + 1
        entry = Entry(entry_id, title, body)
        self.entries.append(entry)

    def diary_body(self):
        return len(self.entries)

    def get_username(self):
        return self.username

    def delete_entry(self, entry_id):
        entry = self.find_entry_by_id(entry_id)
        self.entries.remove(entry)

    def find_entry_by_id(self, entry_id):
        for entry in self.entries:
            if entry.id == entry_id:
                return entry
        raise ValueError("Entry does not exist")

    def update_entry(self, entry_id, title, body):
        entry = self.find_entry_by_id(entry_id)
        entry.title = title
        entry.body = body
