#!/usr/bin/python
# -*- coding: UTF-8 -*-
import ClassFileMetadata


class DocumentMetadata(ClassFileMetadata):
    def getDocumentType(self):
        return self.___documentType

    def setDocumentType(self, aDocumentType):
        """@ReturnType void"""
        self.___documentType = aDocumentType

    def __init__(self):
        self.___documentType = None

