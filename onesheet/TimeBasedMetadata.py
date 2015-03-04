#!/usr/bin/python
# -*- coding: UTF-8 -*-
from subprocess import Popen, PIPE, STDOUT
from re import search, DOTALL
from xml.dom.minidom import parseString

from onesheet.ClassFileMetadata import FileMetadata


class TimeBasedMetadata(FileMetadata):
    def __init__(self, filename):
        FileMetadata.__init__(self, filename)
        self.GET_XML_COMMAND = 'ffprobe -print_format xml -show_streams'.split()
        self.fileName = filename
        if self.format_type == 'audio' or self.format_type == 'video':
            command = self.GET_XML_COMMAND
            command.append(self.fileName)
            p = Popen(command, stdout=PIPE, stderr=STDOUT, bufsize=0)
            self.rawdata = p.communicate()[0]
            self.fileXML = str(search('(<\?xml).*(</ffprobe>)', self.rawdata, DOTALL).group(0))
            self.xmlDom = parseString(self.fileXML)

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

        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "audio":
                    seconds = float(stream.getAttribute("duration"))#TODO create SMPTE TRT return
                    break

        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return str(int(h)).zfill(2) + ":" + str(int(m)).zfill(2) + ":" + str(int(s)).zfill(0)
        pass

    @property
    def totalSeconds(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "audio":
                    return float(stream.getAttribute("duration"))
        pass

