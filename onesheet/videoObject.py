#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import XMPVideoMetadata, VideoMetadata, AudioMetadata


class videoObject(AudioMetadata, VideoMetadata, XMPVideoMetadata):
    pass
