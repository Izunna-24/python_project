class Manipulation:
    def __init__(self):
        self._get_string = ""

    def get_string(self, input_collector):
        self._get_string = input_collector

    def print_string(self):
        return self._get_string.upper()
