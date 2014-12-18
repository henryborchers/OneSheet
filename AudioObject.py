#!/usr/bin/python
# -*- coding: UTF-8 -*-
from AudioMetadata import AudioMetadata
from XMPAudioMetadata import XMPAudioMetadata


class AudioObject(AudioMetadata, XMPAudioMetadata):

    def __init__(self, filename):
        print filename
        super(AudioObject, self).__init__(filename)
        # super(AudioMetadata, self).__init__(fileName)
