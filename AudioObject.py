#!/usr/bin/python
# -*- coding: UTF-8 -*-
from AudioMetadata import AudioMetadata
from XMPAudioMetadata import XMPAudioMetadata


class AudioObject(AudioMetadata, XMPAudioMetadata):

    def __init__(self, filename):
        AudioMetadata.__init__(self, filename)
