#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import ClassFileMetadata
from abc import ABCMeta

class ImageMetadata(ClassFileMetadata):
    __metaclass__ = ABCMeta
    def getImageResolutionHeight(self):
        pass

    def getImageResolutionWidth(self):
        pass

    def getImageResolution(self):
        pass

    def getImageColorDepth(self):
        pass

