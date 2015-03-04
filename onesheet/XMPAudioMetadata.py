#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import XMPMetadata

from abc import ABCMeta
class XMPAudioMetadata(XMPMetadata):
    __metaclass__ = ABCMeta
    def __init__(self):
        print "XMPAudioMetadata start"
        self._getAudioComments = None
        self.___xmpDMAudioSampleRate = None
        self.___xmpDMAudioSampleType = None
        self.___xmpDMAudioChannelType = None
        self.___xmpDMAudioCompressor = None
        self.___xmpDMAudioSpeakerPlacement = None
        self.___xmpDMAbsPeakAudioFilePath = None
        self.___xmpDMRealtivePeakAudioFilePath = None
        self.___xmpDMAudioModDate = None
        self.___xmpDMArtist = None
        self.___xmpDMAlbum = None
        self.___xmpDMTrackNumber = None
        self.___xmpDMGenre = None
        self.___xmpDMCopyright = None
        self.___xmpDMReleaseDate = None
        self.___xmpDMComposer = None
        self.___xmpDMEngineer = None
        self.___xmpDMTempo = None
        self.___xmpDMInstrument = None
        self.___xmpDMIntroTime = None
        self.___xmpDMOutCue = None
        self.___xmpDMRelativeTimestamp = None
        self.___xmpDMLoop = None
        self.___xmpDMNumberofBeats = None
        self.___xmpDMKey = None
        self.___xmpDMStretchMode = None
        self.___xmpDMTimeScaleParams = None
        self.___xmpDMResampleParams = None
        self.___xmpDMBeatSpliceParams = None
        self.___xmpDMTimeSignature = None
        self.___xmpDMScaleType = None

    def getXMPDMAudioSampleRate(self):
        # TODO Make getXMPDMAudioSampleRate method
        return self.___xmpDMAudioSampleRate

    def getXMPDMAudioSampleType(self):
        # TODO Make getXMPDMAudioSampleType method
        return self.___xmpDMAudioSampleType

    def getXMPDMAudioChannelType(self):
        # TODO Make getXMPDMAudioChannelType method
        return self.___xmpDMAudioChannelType

    def getXMPDMAudioCompressor(self):
        # TODO Make getXMPDMAudioCompressor method
        return self.___xmpDMAudioCompressor

    def getXMPDMAudioSpeakerPlacement(self):
        # TODO Make getXMPDMAudioSpeakerPlacement method
        return self.___xmpDMAudioSpeakerPlacement

    def getXMPDMAbsPeakAudioFilePath(self):
        # TODO Make getXMPDMAubsPeakAudio method
        return self.___xmpDMAbsPeakAudioFilePath

    def getXMPDMRealtivePeakAudioFilePath(self):
        # TODO Make getXMPRealtivePeakAudioFilePath method
        return self.___xmpDMRealtivePeakAudioFilePath

    def getXMPDMAudioModDate(self):
        # TODO Make getXMPAudioModData method
        return self.___xmpDMAudioModDate

    def getXMPDMArtist(self):
        # TODO Make getXMPRDMArtist method
        return self.___xmpDMArtist

    def getXMPDMAlbum(self):
        # TODO Make getXMPDMAlbum method
        return self.___xmpDMAlbum

    def getXMPDMTrackNumber(self):
        # TODO Make getXMPDMTrackNumber method
        return self.___xmpDMTrackNumber

    def getXMPDMGenre(self):
        # TODO Make getXMPDMGenre method
        return self.___xmpDMGenre

    def getXMPDMCopyright(self):
        # TODO Make getXMPDMCopyright method
        return self.___xmpDMCopyright

    def getXMPDMReleaseDate(self):
        # TODO Make getXMPDMReleaseDate method
        return self.___xmpDMReleaseDate

    def getXMPDMComposer(self):
        # TODO Make getXMPDMComposer method
        return self.___xmpDMComposer

    def getXMPDMEngineer(self):
        # TODO Make getXMPDMEngineer method
        return self.___xmpDMEngineer

    def getXMPDMTemp(self):
        # TODO Make getXMPMTemp method
        pass

    def getXMPDMInstrument(self):
        # TODO Make getXMPRDMInstrument method
        return self.___xmpDMInstrument

    def getXMPDMIntroTime(self):
        # TODO Make getXMPDMIntroTime method
        return self.___xmpDMIntroTime

    def getXMPDMOutCue(self):
        # TODO Make getXMPRDMOutCue method
        return self.___xmpDMOutCue

    def getXMPDMRelativeTimestamp(self):
        # TODO Make getXMPRealtiveTimestamp method
        return self.___xmpDMRelativeTimestamp

    def getXMPDMLoop(self):
        # TODO Make getXMPDMLoop method
        return self.___xmpDMLoop

    def getXMPDMNumberofBeats(self):
        # TODO Make getXMPNumberOfBeats method
        return self.___xmpDMNumberofBeats

    def getXMPDMKey(self):
        # TODO Make getXMPDMKeys method
        return self.___xmpDMKey

    def getXMPDMStretchMode(self):
        # TODO Make getXMPDStretchMode method
        return self.___xmpDMStretchMode

    def getXMPDMTimeScaleParams(self):
        # TODO Make getXMPDMTimeScaleParams method
        return self.___xmpDMTimeScaleParams

    def getXMPDMResampleParams(self):
        # TODO Make getXMPDResampleParams method
        return self.___xmpDMResampleParams

    def getXMPDMBeatSpliceParams(self):
        # TODO Make getXMPDMBeatSpliceParam method
        return self.___xmpDMBeatSpliceParams

    def getXMPDMTimeSignature(self):
        # TODO Make getXMPDMTimeSignature method
        return self.___xmpDMTimeSignature

    def getXMPDMScaleType(self):
        # TODO Make getXMPDMScaleTypes method
        return self.___xmpDMScaleType

