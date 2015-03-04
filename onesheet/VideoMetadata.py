#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet.TimeBasedMetadata import TimeBasedMetadata


class VideoMetadata(TimeBasedMetadata):

    def __init__(self, filename):
        TimeBasedMetadata.__init__(self, filename)
        pass

    def __convertFrameToNDF(self, aFrameNumber):
        pass

    def __convertFrameToDF(self, aFrameNumber):
        pass

    def __sizeofHuman(self, num):
        num = int(num)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    @property
    def videoCodec(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return stream.getAttribute("codec_name")

    @property
    def videoCodecLongName(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return stream.getAttribute("codec_long_name")
    @property
    def videoCodecTagString(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return stream.getAttribute("codec_tag_string")


    @property
    def videoCodecTag(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return stream.getAttribute("codec_tag")

    @property
    def videoFrameRate(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return stream.getAttribute("r_frame_rate")



    def getVideoColorSpace(self):
        # TODO Make getVideoColorSpace method
        pass

    def getVideoColorSampling(self):
        # TODO Make getVideoColorSampling method
        pass

    @property
    def videoBitRate(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return int(stream.getAttribute("bit_rate"))

    @property
    def videoBitRateH(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return self.__sizeofHuman(int(stream.getAttribute("bit_rate")))+"/s"

    @property
    def videoResolution(self):
            for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    height = stream.getAttribute("height")
                    width = stream.getAttribute("width")
                    return width + " x " + height

    @property
    def videoResolutionHeight(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return int(stream.getAttribute("height"))

    @property
    def videoRespolutionWidth(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "video":
                    return int(stream.getAttribute("width"))


