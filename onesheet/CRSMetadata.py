#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta
class CRSMetadata(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.___crsAutoBrightness = None
        self.___crsAutoContrast = None
        self.___crsAutoExposure = None
        self.___crsAutoShadows = None
        self.___crsBlueHue = None
        self.___crsBlueSaturation = None
        self.___crsBrightness = None
        self.___crsCameraProfile = None
        self.___crsChromaticAberrationB = None
        self.___crsChromaticAberrationR = None
        self.___crsColorNoiseReduction = None
        self.___crsContrast = None
        self.___crsCropTop = None
        self.___crsCropLeft = None
        self.___crsCropRight = None
        self.___crsCropWidth = None
        self.___crsCropHeight = None
        self.___crsCropUnits = None
        self.___crsExposure = None
        self.___crsGreenHue = None
        self.___crsGreenSaturation = None
        self.___crsHasCrop = None
        self.___crsHasSetings = None
        self.___crsLuminanceSmoothing = None
        self.___crsRawFileName = None
        self.___crsRedHue = None
        self.___crsRedSaturation = None
        self.___crsSaturation = None
        self.___crsShadows = None
        self.___crsShadowTint = None
        self.___crsSharpness = None
        self.___crsTemperature = None
        self.___crsTint = None
        self.___crsToneCurve = None
        self.___crsToneCurveNae = None
        self.___crsVersion = None
        self.___crsVignetteAmount = None
        self.___crsVignetteMidpoint = None
        self.___crsWhiteBalance = None

    def getCrsAutoBrightness(self):
        return self.___crsAutoBrightness

    def getCrsAutoContrast(self):
        return self.___crsAutoContrast

    def getCrsAutoExposure(self):
        return self.___crsAutoExposure

    def getCrsAutoShadows(self):
        return self.___crsAutoShadows

    def getCrsBlueHue(self):
        return self.___crsBlueHue

    def getCrsBlueSaturation(self):
        return self.___crsBlueSaturation

    def getCrsBrightness(self):
        return self.___crsBrightness

    def getCrsCameraProfile(self):
        return self.___crsCameraProfile

    def getCrsChromaticAberrationB(self):
        return self.___crsChromaticAberrationB

    def getCrsChromaticAberrationR(self):
        return self.___crsChromaticAberrationR

    def getCrsColorNoiseReduction(self):
        return self.___crsColorNoiseReduction

    def getCrsContrast(self):
        return self.___crsContrast

    def getCrsCropTop(self):
        return self.___crsCropTop

    def getCrsCropLeft(self):
        return self.___crsCropLeft

    def getCrsCropRight(self):
        return self.___crsCropRight

    def getCrsCropWidth(self):
        return self.___crsCropWidth

    def getCrsCropHeight(self):
        return self.___crsCropHeight

    def getCrsCropUnits(self):
        return self.___crsCropUnits

    def getCrsExposure(self):
        return self.___crsExposure

    def getCrsGreenHue(self):
        return self.___crsGreenHue

    def getCrsGreenSaturation(self):
        return self.___crsGreenSaturation

    def getCrsHasCrop(self):
        return self.___crsHasCrop

    def getCrsHasSetings(self):
        return self.___crsHasSetings

    def getCrsLuminanceSmoothing(self):
        return self.___crsLuminanceSmoothing

    def getCrsRawFileName(self):
        return self.___crsRawFileName

    def getCrsRedHue(self):
        return self.___crsRedHue

    def getCrsRedSaturation(self):
        return self.___crsRedSaturation

    def getCrsSaturation(self):
        return self.___crsSaturation

    def getCrsShadows(self):
        return self.___crsShadows

    def getCrsShadowTint(self):
        return self.___crsShadowTint

    def getCrsSharpness(self):
        return self.___crsSharpness

    def getCrsTemperature(self):
        return self.___crsTemperature

    def getCrsTint(self):
        return self.___crsTint

    def getCrsToneCurve(self):
        return self.___crsToneCurve

    def getCrsToneCurveNae(self):
        return self.___crsToneCurveNae

    def getCrsVersion(self):
        return self.___crsVersion

    def getCrsVignetteAmount(self):
        return self.___crsVignetteAmount

    def getCrsVignetteMidpoint(self):
        return self.___crsVignetteMidpoint

    def getCrsWhiteBalance(self):
        return self.___crsWhiteBalance

