#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import XMPMetadata
from abc import ABCMeta

class PDFMetadata(XMPMetadata):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.___pdfKeywords = None
        self.___pdfPDFVersion = None
        self.___pdfProducer = None

    def getPdfKeywords(self):
        return self.___pdfKeywords

    def getPdfPDFVersion(self):
        return self.___pdfPDFVersion

    def getPdfProducer(self):
        return self.___pdfProducer

