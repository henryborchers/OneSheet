from unittest import TestCase

from onesheet.TimeBasedMetadata import *


__author__ = 'Henry Borchers'


class TestTimeBasedMetadata(TestCase):
    def setUp(self):
        self.f = TimeBasedMetadata("ALLEY_1A.wav")

    def test_getFilePath(self):
        self.assertEqual(self.f.file_path, "/Users/lpsdesk/PycharmProjects/Metadata/ALLEY_1A.wav")

    def test_getFormatType(self):
        self.assertEqual(self.f.format_type, "video")

    def test_getFileExtension(self):
        self.assertEqual(self.f.file_extension, '.avi')

    def test_getFileSize(self):
        self.assertEqual(self.f.file_size, 100573184)

    def test_getFileSizeH(self):
        self.assertEqual(self.f.file_size_human, "95.9 MB")

    def test_getDateCreated(self):
        self.assertEqual(self.f.date_created, "Fri Nov 14 21:58:51 2014")

    def test_getDateLastModified(self):
        self.assertEqual(self.f.date_last_modified, "Wed Aug 01 23:38:18 2012")

    def test_getXML(self):
        self.fail()

    def test_calculateMD5(self):
        self.assertEqual(self.f.calculate_MD5(), "8c1b38a56aa810f717dbae2fc20e119d")

    def test_calculateSHA1(self):
        self.assertEqual(self.f.calculate_SHA1(), "dbd2af5e2d1b3146ce8578fdd63488152405efcb")

    def test_getTotalRunningTimeRaw(self):
        self.assertEqual(self.f.getTotalRunningTimeRaw(), "ddd")

    def test_getTotalRunningTimeSMPTE(self):
        self.fail()

    def test_getTotalSeconds(self):
        self.fail()