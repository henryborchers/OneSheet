#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet import CRSMetadata, XMPMetadata, PhotoshopMetadata, AUXMetadata


class XMPImageMetadata(XMPMetadata, PhotoshopMetadata, CRSMetadata, AUXMetadata):
    pass
