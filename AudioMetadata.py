#!/usr/bin/python
# -*- coding: UTF-8 -*-
from TimeBasedMetadata import TimeBasedMetadata


class AudioMetadata(TimeBasedMetadata):
    def __init__(self, filename):
        print "AudioMetadata start"
        # super(AudioMetadata, self).__init__(filename)
        TimeBasedMetadata.__init__(self, filename)
        print "AudioMetadata done"
        # pass

    def getAudioBitDepth(self):
        # TODO Make getAudioBitDepth Method
        pass

    def getAudioChannels(self):
        # TODO Make getAudioChannels Method
        pass

    def getAudioCodec(self):
        # TODO Make getAudioCodec Method
        pass

    def getAudioCodecLongName(self):
        # TODO Make getAudioCodecLongName Method
        pass

    def getAudioSampleRate(self):
        # TODO Make getAudioSampleRate Method
        pass



