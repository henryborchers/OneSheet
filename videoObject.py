#!/usr/bin/python
# -*- coding: UTF-8 -*-
import AudioMetadata
import VideoMetadata
import XMPVideoMetadata


class videoObject(AudioMetadata, VideoMetadata, XMPVideoMetadata):
    pass
