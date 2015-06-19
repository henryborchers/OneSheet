__author__ = 'California Audio Visual Preservation Project'

class FormatException(Exception):
    def __init__(self, value):
         self.value = value

    def __str__(self):
        return self.value


class NoDataException(Exception):
    def __init__(self, value):
         self.value = value

    def __str__(self):
        return self.value