__author__ = 'California Audio Visual Preservation Project'
from abc import ABCMeta
from onesheet.ClassFileMetadata import FileMetadata

class TimeBasedMetadata(FileMetadata):
    __metaclass__ = ABCMeta
    def __init__(self, filename):
        FileMetadata.__init__(self, filename)