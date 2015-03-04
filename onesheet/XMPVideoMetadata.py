#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import XMPMetadata
from abc import ABCMeta

class XMPVideoMetadata(XMPMetadata):
    __metaclass__ = ABCMeta
    def __init__(self):
        # TODO make class XMPVideoMetadata contstructor
        self.___xmpDMVideoFrameRate = None
        self.___xmpDMVideoFrameSize = None
        self.___xmpDMVideoPixelAspectRatio = None
        self.___xmpDMvideoPixelDepth = None
        self.___xmpDMvideoColorSpace = None
        self.___xmpDMVideoAlphaMode = None
        self.___xmpDMVideoAlphaPremultipleColor = None
        self.___xmpDMVideoUnityIsTransparent = None
        self.___xmpDMVideoCompressor = None
        self.___xmpDMVideoFieldOrder = None
        self.___xmpDMVideoPullDown = None
        self.___xmpDMVideoModDate = None

    def getXMPDMVideoFrameRate(self):
        # TODO Make getXMPDMVideoFrameRate method
        return self.___xmpDMVideoFrameRate

    def getXMPDMvideoColorSpace(self):
        # TODO Make getXMPDMVideoColorSpace method
        return self.___xmpDMvideoColorSpace

    def getXMPDMVideoAlphaMode(self):
        # TODO Make getXMPDMVideoAlphaMode method
        return self.___xmpDMVideoAlphaMode

    def getXMPDMVideoFrameSize(self):
        # TODO Make getXMPDMVideoFrameSize method
        return self.___xmpDMVideoFrameSize

    def getXMPDMVideoPixelAspectRatio(self):
        # TODO Make getXMPDMVideoAspectRatio method
        return self.___xmpDMVideoPixelAspectRatio

    def getXMPDMvideoPixelDepth(self):
        # TODO Make getXMPDMVideoPixelDepth method
        return self.___xmpDMvideoPixelDepth

    def getXMPDMVideoAlphaPremultipleColor(self):
        # TODO Make getXMPDMVideoAlphaPremultipleColor method
        return self.___xmpDMVideoAlphaPremultipleColor

    def getXMPDMVideoUnityIsTransparent(self):
        # TODO Make getXMPDMVideoUnityIsTransparent method
        return self.___xmpDMVideoUnityIsTransparent

    def getXMPDMVideoCompressor(self):
        # TODO Make getXMPDMVideoCompressor method
        return self.___xmpDMVideoCompressor

    def getXMPDMVideoFieldOrder(self):
        # TODO Make getXMPDMVideoFieldOrder method
        return self.___xmpDMVideoFieldOrder

    def getXMPDMVideoPullDown(self):
        # TODO Make getXMPDMVideoPullDown method
        return self.___xmpDMVideoPullDown

    def getXMPDMVideoModDate(self):
        # TODO Make getXMPDMVideoModDate method
        return self.___xmpDMVideoModDate

