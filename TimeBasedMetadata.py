#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os.path import split
from ClassFileMetadata import FileMetadata


class TimeBasedMetadata(FileMetadata):
    def __init__(self, filename):
        super(TimeBasedMetadata, self).__init__(filename)

    def getTotalRunningTimeRaw(self):
        return self.___totalRunningTimeRaw

    def getTotalRunningTimeSMPTE(self):
        #TODO create SMPTE TRT return
        pass

    def getTotalSeconds(self):
        #TODO Create a total number of seconds
        pass

