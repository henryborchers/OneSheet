#!/usr/bin/python
# -*- coding: UTF-8 -*-
from subprocess import Popen, PIPE, STDOUT
from re import search, DOTALL
from xml.dom.minidom import parseString

from onesheet.ClassFileMetadata import FileMetadata


class TimeBasedMetadata(FileMetadata):
    def __init__(self, filename):
        FileMetadata.__init__(self,filename)
        self.GET_XML_COMMAND = 'ffprobe -print_format xml -show_streams'.split()
        self.fileName = filename
        if self.getFormatType() == 'audio' or self.getFormatType() == 'video':
            command = self.GET_XML_COMMAND
            command.append(self.fileName)
            p = Popen(command, stdout=PIPE, stderr=STDOUT, bufsize=0)
            self.rawdata = p.communicate()[0]
            self.fileXML = str(search('(<\?xml).*(</ffprobe>)', self.rawdata, DOTALL).group(0))
            self.xmlDom = parseString(self.fileXML)


    def getTotalRunningTimeRaw(self):
        return self.___totalRunningTimeRaw

    def getTotalRunningTimeSMPTE(self):
        #TODO create SMPTE TRT return
        pass

    def getTotalSeconds(self):
        #TODO Create a total number of seconds
        pass

