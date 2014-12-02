#!/usr/bin/python
# -*- coding: UTF-8 -*-
import XMPMetadata
import PhotoshopMetadata
import CRSMetadata
import AUXMetadata


class XMPImageMetadata(XMPMetadata, PhotoshopMetadata, CRSMetadata, AUXMetadata):
    pass
