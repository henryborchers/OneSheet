#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta
class EXFMetadata(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.___exffExifVersion = None
        self.___exifFlashpixVersion = None
        self.___exifColorSpace = None
        self.___exifComponentsConfiguration = None
        self.___exifCompressedBitsPerPixel = None
        self.___exifPixelXDimension = None
        self.___exifPixelYDimension = None
        self.___exifUserComment = None
        self.___exifRelatedSoundFile = None
        self.___exifDateTimeOriginal = None
        self.___exifDateTimeDigitized = None
        self.___exifExposureTime = None
        self.___exifFNumber = None
        self.___exifExposureProgram = None
        self.___exifSpectralSensitivity = None
        self.___exifISOSpeedRatings = None
        self.___exifOECF = None
        self.___exifShutterSpeedValue = None
        self.___exifApertureValue = None
        self.___exifBrightnessValue = None
        self.___exifExposureBiasValue = None
        self.___exifMaxApertureValue = None
        self.___exifSubjectDistance = None
        self.___exifMeteringMode = None
        self.___exifLightSource = None
        self.___exifFlash = None
        self.___exifFocalLength = None
        self.___exifSubjectArea = None
        self.___exifFlashEnergy = None
        self.___exifSpacialFrequencyResponse = None
        self.___exifFocalPlaneXResolution = None
        self.___exifFocalPlaneYResolution = None
        self.___exifFocalPlaneResolutionUnit = None
        self.___exifSubjectLocation = None
        self.___exifExposureIndex = None
        self.___exifSensingMethod = None
        self.___exifFileSource = None
        self.___exifSceneType = None
        self.___exifCFAPattern = None
        self.___exifCustomRendered = None
        self.___exifExposureMode = None
        self.___exifWhiteBalance = None
        self.___exifDigitalZoomRatio = None
        self.___exifFocalLengthIn35mmFilm = None
        self.___exifSceneCaptureType = None
        self.___exifGainControl = None
        self.___exifContrast = None
        self.___exifSaturation = None
        self.___exifSharpness = None
        self.___exifDeviceSettingDescription = None
        self.___exifSubjectDistanceRange = None
        self.___exifImageUniqueID = None
        self.___exifGPSVersionID = None
        self.___exifGPSLatitude = None
        self.___exifGPSLongitude = None
        self.___exifGPSAltitudeRef = None
        self.___exifGPSAltitude = None
        self.___exifGPSTimeStamp = None
        self.___exifGPSSatelites = None
        self.___exifGPSStatus = None
        self.___exifMeasureMode = None
        self.___exifGPSDOP = None
        self.___exifGPSSpeedRef = None
        self.___exifGPSSpeed = None
        self.___exifGPSTrackRef = None
        self.___exifGPSTrack = None
        self.___exifGPSImgDirectionRef = None
        self.___exifGPSImgDirection = None
        self.___exifGPSMapDatum = None
        self.___exifGPSDestLatitude = None
        self.___exifGPSDestLongitude = None
        self.___exifGPSDestBearingRef = None
        self.___exifGPSDestBearing = None
        self.___exifGPSDestDistance = None
        self.___exifGPSProcessingMethod = None
        self.___exifGPSAreaInformation = None
        self.___exifGPSDifferential = None

    def getExifExifVersion(self):
        pass

    def getExifFlashpixVersion(self):
        return self.___exifFlashpixVersion

    def getExifColorSpace(self):
        return self.___exifColorSpace

    def getExifComponentsConfiguration(self):
        return self.___exifComponentsConfiguration

    def getExifCompressedBitsPerPixel(self):
        return self.___exifCompressedBitsPerPixel

    def getExifPixelXDimension(self):
        return self.___exifPixelXDimension

    def getExifPixelYDimension(self):
        return self.___exifPixelYDimension

    def getExifUserComment(self):
        return self.___exifUserComment

    def getExifRelatedSoundFile(self):
        return self.___exifRelatedSoundFile

    def getExifDateTimeOriginal(self):
        return self.___exifDateTimeOriginal

    def getExifDateTimeDigitized(self):
        return self.___exifDateTimeDigitized

    def getExifExposureTime(self):
        return self.___exifExposureTime

    def getExifFNumber(self):
        return self.___exifFNumber

    def getExifExposureProgram(self):
        return self.___exifExposureProgram

    def getExifSpectralSensitivity(self):
        return self.___exifSpectralSensitivity

    def getExifISOSpeedRatings(self):
        return self.___exifISOSpeedRatings

    def getExifOECF(self):
        return self.___exifOECF

    def getExifShutterSpeedValue(self):
        return self.___exifShutterSpeedValue

    def getExifApertureValue(self):
        return self.___exifApertureValue

    def getExifBrightnessValue(self):
        return self.___exifBrightnessValue

    def getExifExposureBiasValue(self):
        return self.___exifExposureBiasValue

    def getExifMaxApertureValue(self):
        return self.___exifMaxApertureValue

    def getExifSubjectDistance(self):
        return self.___exifSubjectDistance

    def getExifMeteringMode(self):
        return self.___exifMeteringMode

    def getExifLightSource(self):
        return self.___exifLightSource

    def getExifFlash(self):
        return self.___exifFlash

    def getExifFocalLength(self):
        return self.___exifFocalLength

    def getExifSubjectArea(self):
        return self.___exifSubjectArea

    def getExifFlashEnergy(self):
        return self.___exifFlashEnergy

    def getExifSpacialFrequencyResponse(self):
        return self.___exifSpacialFrequencyResponse

    def getExifFocalPlaneXResolution(self):
        return self.___exifFocalPlaneXResolution

    def getExifFocalPlaneYResolution(self):
        return self.___exifFocalPlaneYResolution

    def getExifFocalPlaneREsolutionUnit(self):
        pass

    def getExifSubjectLocation(self):
        return self.___exifSubjectLocation

    def getExifExposureIndex(self):
        return self.___exifExposureIndex

    def getExifSensingMethod(self):
        return self.___exifSensingMethod

    def getExifFileSource(self):
        return self.___exifFileSource

    def getExifSceneType(self):
        return self.___exifSceneType

    def getExifCFAPattern(self):
        return self.___exifCFAPattern

    def getExifCustomRendered(self):
        return self.___exifCustomRendered

    def getExifExposureMode(self):
        return self.___exifExposureMode

    def getExifWhiteBalance(self):
        return self.___exifWhiteBalance

    def getExifDigitalZoomRatio(self):
        return self.___exifDigitalZoomRatio

    def getExifFocalLengthIn35mmFilm(self):
        return self.___exifFocalLengthIn35mmFilm

    def getExifSceneCaptureType(self):
        return self.___exifSceneCaptureType

    def getExifGainControl(self):
        return self.___exifGainControl

    def getExifContrast(self):
        return self.___exifContrast

    def getExifSaturation(self):
        return self.___exifSaturation

    def getExifSharpness(self):
        return self.___exifSharpness

    def getExifDeviceSettingDescription(self):
        return self.___exifDeviceSettingDescription

    def getExifSubjectDistanceRange(self):
        return self.___exifSubjectDistanceRange

    def getExifImageUniqueID(self):
        return self.___exifImageUniqueID

    def getExifGPSVersionID(self):
        return self.___exifGPSVersionID

    def getExifGPSLatitude(self):
        return self.___exifGPSLatitude

    def getExifGPSLongitude(self):
        return self.___exifGPSLongitude

    def getExifGPSAltitudeRef(self):
        return self.___exifGPSAltitudeRef

    def getExifGPSAltitude(self):
        return self.___exifGPSAltitude

    def getExifGPSTimeStamp(self):
        return self.___exifGPSTimeStamp

    def getExifGPSSatelites(self):
        return self.___exifGPSSatelites

    def getExifGPSStatus(self):
        return self.___exifGPSStatus

    def getExifMeasureMode(self):
        return self.___exifMeasureMode

    def getExifGPSDOP(self):
        return self.___exifGPSDOP

    def getExifGPSSpeedRef(self):
        return self.___exifGPSSpeedRef

    def getExifGPSSpeed(self):
        return self.___exifGPSSpeed

    def getExifGPSTrackRef(self):
        return self.___exifGPSTrackRef

    def getExifGPSTrack(self):
        return self.___exifGPSTrack

    def getExifGPSImgDirectionRef(self):
        return self.___exifGPSImgDirectionRef

    def getExifGPSImgDirection(self):
        return self.___exifGPSImgDirection

    def getExifGPSMapDatum(self):
        return self.___exifGPSMapDatum

    def getExifGPSDestLatitude(self):
        return self.___exifGPSDestLatitude

    def getExifGPSDestLongitude(self):
        return self.___exifGPSDestLongitude

    def getExifGPSDestBearingRef(self):
        return self.___exifGPSDestBearingRef

    def getExifGPSDestBearing(self):
        return self.___exifGPSDestBearing

    def getExifGPSDestDistance(self):
        return self.___exifGPSDestDistance

    def getExifGPSProcessingMethod(self):
        return self.___exifGPSProcessingMethod

    def getExifGPSAreaInformation(self):
        return self.___exifGPSAreaInformation

    def getExifGPSDifferential(self):
        return self.___exifGPSDifferential

