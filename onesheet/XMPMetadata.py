#!/usr/bin/python
# -*- coding: UTF-8 -*-

from onesheet import DublinCoreMetadata
from onesheet.ClassFileMetadata import FileMetadata
from abc import ABCMeta
class XMPMetadata(FileMetadata, DublinCoreMetadata):
    __metaclass__ = ABCMeta
    def __init__(self):
        # TODO Make class XMPMetadata constructor
        self.___embeddedXMP = None
        self.___xmpAdvisory = None
        self.___xmpBaseURL = None
        self.___xmpCreationDate = None
        self.___xmpCreatorTool = None
        self.___xmpIdentifier = None
        self.___xmpLabel = None
        self.___xmpMetadataDate = None
        self.___xmpModifyDate = None
        self.___xmpNickname = None
        self.___xmpRating = None
        self.___xmpThumbnails = None
        self.___xmpidqScheme = None
        self.___xmpRightsCertification = None
        self.___xmpRightsMarked = None
        self.___xmpRightsOwner = None
        self.___xmpRightsUsageTerms = None
        self.___xmpRightsWebStatement = None
        self.___xmpMMDerivativedFrom = None
        self.___xmpMMDocumentID = None
        self.___xmpMMHistory = None
        self.___xmpMMInstanceID = None
        self.___xmpMMManagedFrom = None
        self.___xmpMMManager = None
        self.___xmpMMManageTo = None
        self.___xmpMMManageUI = None
        self.___xmpMMManagerVariant = None
        self.___xmpMMRenditionClass = None
        self.___xmpMMRenditionParams = None
        self.___xmpMMVersionID = None
        self.___xmpMMVersions = None
        self.___xmpMMLastURL = None
        self.___xmpMMRenditionOf = None
        self.___xmpMMSaveID = None
        self.___xmpBJJobRef = None
        self.___xmpTPgMaxPageSize = None
        self.___xmpTPgNPages = None
        self.___xmpTPgFonts = None
        self.___xmpTPgColorants = None
        self.___xmpTPgPlateNames = None
        self.___xmpDMProjectRef = None
        self.___xmpDMFileDataRate = None
        self.___xmpDMTapeName = None
        self.___xmpDMAltTapeName = None
        self.___xmpDMStartTimeCode = None
        self.___xmpDMAltTimeCode = None
        self.___xmpDMDuration = None
        self.___xmpDMScene = None
        self.___xmpDMShotName = None
        self.___xmpDMShotDate = None
        self.___xmpDMShotLocation = None
        self.___xmpDMLogComment = None
        self.___xmpDMMarkers = None
        self.___xmpDMContributedMedia = None
        self.___xmpDMMetadataModDate = None

    def embededXMPMetadata(self):
        pass

    def getXMPAdvisory(self):
        pass

    def getXMPBaseURL(self):
        pass

    def getXMPCreationDate(self):
        pass

    def getXMPCreatorTool(self):
        pass

    def getXMPIndentifier(self):
        pass

    def getXMPLabel(self):
        pass

    def getXMPMetadataDate(self):
        pass

    def getXMPModifyDate(self):
        pass

    def getXMPNickname(self):
        pass

    def getXMPRating(self):
        pass

    def getXMPThumnails(self):
        pass

    def getXMPidqScheme(self):
        return self.___xmpidqScheme

    def getXMPRightsCertification(self):
        return self.___xmpRightsCertification

    def getXMPRightsMarked(self):
        return self.___xmpRightsMarked

    def getXMPRightsOwner(self):
        return self.___xmpRightsOwner

    def getXMPRightsUsageTerms(self):
        return self.___xmpRightsUsageTerms

    def getXMPRightsWebStatement(self):
        return self.___xmpRightsWebStatement

    def getXMPMMDerivativedFrom(self):
        return self.___xmpMMDerivativedFrom

    def getXMPMMDocumentID(self):
        return self.___xmpMMDocumentID

    def getXMPMMHistory(self):
        return self.___xmpMMHistory

    def getXMPMMInstanceID(self):
        return self.___xmpMMInstanceID

    def getXMPMMManagedFrom(self):
        return self.___xmpMMManagedFrom

    def getXMPMMManager(self):
        return self.___xmpMMManager

    def getXMPMMManageTo(self):
        return self.___xmpMMManageTo

    def getXMPMMManageUI(self):
        return self.___xmpMMManageUI

    def getXMPMMManagerVariant(self):
        return self.___xmpMMManagerVariant

    def getXMPMMRenditionClass(self):
        return self.___xmpMMRenditionClass

    def getXMPMMRenditionParams(self):
        return self.___xmpMMRenditionParams

    def getXMPMMVersionID(self):
        return self.___xmpMMVersionID

    def getXMPMMVersions(self):
        return self.___xmpMMVersions

    def getXMPMMLastURL(self):
        return self.___xmpMMLastURL

    def getXMPMMRenditionOf(self):
        return self.___xmpMMRenditionOf

    def getXMPMMSaveID(self):
        return self.___xmpMMSaveID

    def getXMPBJJobRef(self):
        return self.___xmpBJJobRef

    def getXMPTPgMaxPageSize(self):
        return self.___xmpTPgMaxPageSize

    def getXMPTPgNPages(self):
        return self.___xmpTPgNPages

    def getXMPTPgFonts(self):
        return self.___xmpTPgFonts

    def getXMPTPgColorants(self):
        return self.___xmpTPgColorants

    def getXMPTPgPlateNames(self):
        return self.___xmpTPgPlateNames

    def getXMPDMProjectRef(self):
        return self.___xmpDMProjectRef

    def getXMPDMFileDataRate(self):
        return self.___xmpDMFileDataRate

    def getXMPDMTapeName(self):
        return self.___xmpDMTapeName

    def getXMPDMAltTapeName(self):
        return self.___xmpDMAltTapeName

    def getXMPDMStartTimeCode(self):
        return self.___xmpDMStartTimeCode

    def getXMPDMAltTimeCode(self):
        return self.___xmpDMAltTimeCode

    def getXMPDMDuration(self):
        return self.___xmpDMDuration

    def getXMPDMScene(self):
        return self.___xmpDMScene

    def getXMPDMShotName(self):
        return self.___xmpDMShotName

    def getXMPDMShotDate(self):
        return self.___xmpDMShotDate

    def getXMPDMShotLocation(self):
        return self.___xmpDMShotLocation

    def getXMPDMLogComment(self):
        return self.___xmpDMLogComment

    def getXMPDMMarkers(self):
        return self.___xmpDMMarkers

    def getXMPDMContributedMedia(self):
        return self.___xmpDMContributedMedia

    def getXMPDMMetadataModDate(self):
        return self.___xmpDMMetadataModDate

