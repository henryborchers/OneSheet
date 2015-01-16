#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import AudioMetadata
from onesheet.XMPAudioMetadata import XMPAudioMetadata


class AudioObject(AudioMetadata, XMPAudioMetadata):

    def __init__(self, filename):
        AudioMetadata.__init__(self, filename)
