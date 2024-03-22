from datetime import datetime


class Entry:
    def __init__(self, entry_id, title, body):
        self.id = entry_id
        self.title = title
        self.body = body
        self.date_created = datetime.now()

    def update_body(self, body):
        self.body = body

    def update_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body
