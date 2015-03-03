from unittest import TestCase

from onesheet.TimeBasedMetadata import *


__author__ = 'Henry Borchers'


class TestTimeBasedMetadata(TestCase):

    def setUp(self):
        self.f = TimeBasedMetadata("/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casacsh_000048/casacsh_000048_b_prsv.wav")

    def test_getFileName(self):
        self.assertEqual(self.f.file_name, "casacsh_000048_b_prsv.wav")
    #
    # def test_getFilePath(self):
    #     self.assertEqual(self.f.file_path, "/Users/lpsdesk/PycharmProjects/PBcore/sample_records/casjhsj_000061")
    #
    # def test_getFormatType(self):
    #     self.assertEqual(self.f.format_type, "video")
    #
    # def test_getFileExtension(self):
    #     self.assertEqual(self.f.file_extension, '.mov')
    #
    # def test_getFileSize(self):
    #     self.assertEqual(self.f.file_size, 6531678142)
    #
    # def test_getFileSizeH(self):
    #     self.assertEqual(self.f.file_size_human, "6.1 GB")
    #
    # def test_getDateCreated(self):
    #     self.assertEqual(self.f.date_created, "Thu Feb 26 16:09:24 2015")
    #
    # def test_getDateLastModified(self):
    #     self.assertEqual(self.f.date_last_modified, "Thu Jan 15 11:18:30 2015")
    #
    # def test_getTotalRunningTimeRaw(self):
    #     self.assertEqual(self.f.getTotalRunningTimeRaw(), "ddd")
    #
    # def test_getTotalRunningTimeSMPTE(self):
    #     self.fail()
    #
    # def test_getTotalSeconds(self):
    #     self.fail()