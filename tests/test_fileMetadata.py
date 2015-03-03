from unittest import TestCase

from onesheet.ClassFileMetadata import *

__author__ = 'Henry Borchers'


class TestFileMetadata(TestCase):
    def setUp(self):
        self.f = FileMetadata("/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casjhsj_000061/casjhsj_000061_r1_prsv.mov")

    def test_getFileName(self):
        self.assertEqual(self.f.file_name, "casjhsj_000061_r1_prsv.mov")
    #
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

    # def test_getXML(self):
    #     self.fail()

    # def test_calculateMD5(self):
    #     self.assertEqual(self.f.calculate_MD5(), "dbf29b8d05c61ba53923ebb06c63377c")
    #
    # def test_calculateSHA1(self):
    #     self.assertEqual(self.f.calculate_SHA1(), "a0e33d68d98018376edccb952ead1e25ec9505f9")