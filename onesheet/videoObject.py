#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from onesheet.XMPVideoMetadata import XMPMetadata
from onesheet.VideoMetadata import VideoMetadata
from onesheet.AudioMetadata import AudioMetadata

# class VideoObject(AudioMetadata, VideoMetadata, XMPVideoMetadata):
class VideoObject(VideoMetadata):

    def __init__(self, filename):
        VideoMetadata.__init__(self, filename)

    pass
