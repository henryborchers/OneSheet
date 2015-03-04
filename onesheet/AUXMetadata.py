#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta
class AUXMetadata(object):
    __metaclass__ = ABCMeta
    def getAuxLens(self):
        return self.___auxLens

    def getAuxSerialNumber(self):
        return self.___auxSerialNumber

    def __init__(self):
        self.___auxLens = None
        self.___auxSerialNumber = None

