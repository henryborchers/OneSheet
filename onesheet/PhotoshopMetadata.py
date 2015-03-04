#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta

class PhotoshopMetadata(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.___photoshopAuthorsPosition = None
        self.___photoshopCaptionWriter = None
        self.___photoshopCategory = None
        self.___photoshopCity = None
        self.___photoshopCountry = None
        self.___photoshopCredit = None
        self.___photoshopDateCreated = None
        self.___photoshopHeadline = None
        self.___photoshopInstructions = None
        self.___photoshopSource = None
        self.___photoshopState = None
        self.___photoshopSupplementalCategories = None
        self.___photoshopTransmissionReference = None
        self.___photoshopUrgency = None

    def getPhotoshopAuthorsPosition(self):
        return self.___photoshopAuthorsPosition

    def getPhotoshopCaptionWriter(self):
        return self.___photoshopCaptionWriter

    def getPhotoshopCategory(self):
        return self.___photoshopCategory

    def getPhotoshopCity(self):
        return self.___photoshopCity

    def getPhotoshopCountry(self):
        return self.___photoshopCountry

    def getPhotoshopCredit(self):
        return self.___photoshopCredit

    def getPhotoshopDateCreated(self):
        return self.___photoshopDateCreated

    def getPhotoshopHeadline(self):
        return self.___photoshopHeadline

    def getPhotoshopInstructions(self):
        return self.___photoshopInstructions

    def getPhotoshopSource(self):
        return self.___photoshopSource

    def getPhotoshopState(self):
        return self.___photoshopState

    def getPhotoshopSupplementalCategories(self):
        return self.___photoshopSupplementalCategories

    def getPhotoshopTransmissionReference(self):
        return self.___photoshopTransmissionReference

    def getPhotoshopUrgency(self):
        return self.___photoshopUrgency

