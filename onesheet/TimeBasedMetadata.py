#!/usr/bin/python
# -*- coding: UTF-8 -*-
from subprocess import Popen, PIPE, STDOUT
from re import search, DOTALL
from xml.dom.minidom import parseString

from onesheet.ClassFileMetadata import FileMetadata
from abc import ABCMeta

class TimeBasedMetadata(FileMetadata):
    __metaclass__ = ABCMeta
    def __init__(self, filename):
        FileMetadata.__init__(self, filename)
        self.raw_stderr = ""
        GET_XML_COMMAND = 'ffprobe -print_format xml -show_streams'.split()
        self.fileName = filename
        if self.format_type == 'audio' or self.format_type == 'video':
            command = GET_XML_COMMAND
            command.append(self.fileName)
            p = Popen(command, stdout=PIPE, stderr=PIPE, bufsize=0)
            for line in p.stderr.readlines():
                self.raw_stderr += line
            self.rawdata = p.communicate()[0]
            self.fileXML = str(search('(<\?xml).*(</ffprobe>)', self.rawdata, DOTALL).group(0))
            self.xmlDom = parseString(self.fileXML)

    @property
    def Rawdata(self):
        return self.rawdata


    @property
    def totalRunningTimeRaw(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "audio":
                    return float(stream.getAttribute("duration"))
        # print self.fileXML
    #     return self.___totalRunningTimeRaw
        pass

    @property
    def totalRunningTimeSMPTE(self):

        # for stream in self.xmlDom.getElementsByTagName('stream'):
        #     if stream.getAttribute("codec_type") == "audio":
        #         seconds = float(stream.getAttribute("duration"))#TODO create SMPTE TRT return
        #         break
        #
        # m, s = divmod(seconds, 60)
        # h, m = divmod(m, 60)
        # return str(int(h)).zfill(2) + ":" + str(int(m)).zfill(2) + ":" + str(int(s)).zfill(2)
        REGEX_DURATION_PATTERN = '(?<=(Duration: ))\d\d:\d\d:\d\d.\d\d(?=,)'
        # print self.raw_stderr
        results = search(REGEX_DURATION_PATTERN, self.raw_stderr)
        # print
        return results.group(0)
        pass

    @property
    def totalSeconds(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "audio":
                    return float(stream.getAttribute("duration"))
        pass

