from unittest import TestCase
from onesheet.VideoMetadata import *
__author__ = 'lpsdesk'


class TestVideoMetadata(TestCase):
    def setUp(self):
        self.f = VideoMetadata("/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casjhsj_000061/casjhsj_000061_r1_prsv.mov")

    def test_getVideoCodec(self):
        self.fail()

    def test_getVideoCodecLongName(self):
        self.fail()

    def test_getVideoCodecTagString(self):
        self.fail()

    def test_getVideoCodecTag(self):
        self.fail()

    def test_getVideoFrameRate(self):
        self.fail()

    def test_getVideoColorSpace(self):
        self.fail()

    def test_getVideoColorSampling(self):
        self.fail()

    def test_getVideoBitRate(self):
        self.fail()

    def test_getVideoBitRate(self):
        self.fail()

    def test_getVideoBitRateH(self):
        self.fail()

    def test_getVideoResolution(self):
        self.fail()

    def test_getVideoResolutionHeight(self):
        self.fail()

    def test_getVideoRespolutionWidth(self):
        self.fail()

    def test_getFilePath(self):
        self.assertEqual(self.f.file_path, "/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casjhsj_000061")

    def test_getFormatType(self):
        self.assertEqual(self.f.format_type, "video")

    def test_getFileExtension(self):
        self.assertEqual(self.f.file_extension, '.mov')

    def test_getFileSize(self):
        self.assertEqual(self.f.file_size, 6531678142)

    def test_getFileSizeH(self):
        self.assertEqual(self.f.file_size_human, "6.1 GB")

    def test_getDateCreated(self):
        self.assertEqual(self.f.date_created, "Thu Feb 26 16:09:24 2015")

    def test_getDateLastModified(self):
        self.assertEqual(self.f.date_last_modified, "Thu Jan 15 11:18:30 2015")

    def test_getTotalRunningTimeRaw(self):
        self.assertEqual(self.f.getTotalRunningTimeRaw(), "ddd")

    def test_getTotalRunningTimeSMPTE(self):
        self.fail()

    def test_getTotalSeconds(self):
        self.fail()