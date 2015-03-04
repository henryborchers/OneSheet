#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet.AudioMetadata import *
# from onesheet.XMPAudioMetadata import XMPAudioMetadata


class AudioObject(AudioMetadata):
# class AudioObject(AudioMetadata, XMPAudioMetadata):

    def __init__(self, filename):
        AudioMetadata.__init__(self, filename)
