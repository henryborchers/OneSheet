#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import ClassFileMetadata
from abc import ABCMeta

class DocumentMetadata(ClassFileMetadata):
    __metaclass__ = ABCMeta
    def getDocumentType(self):
        return self.___documentType

    def setDocumentType(self, aDocumentType):
        """@ReturnType void"""
        self.___documentType = aDocumentType

    def __init__(self):
        self.___documentType = None

