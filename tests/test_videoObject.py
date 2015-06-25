from unittest import TestCase
from onesheet.VideoObject import *
__author__ = 'lpsdesk'


class TestVideoObject(TestCase):

    def setUp(self):
        self.f = VideoObject("/Volumes/DPLA0004/Manzanar/cainmnh_000034/cainmnh_000034_access.mov")

    def test_getVideoCodec(self):
        self.assertEquals(self.f.videoCodec, 'v210')

    def test_getVideoCodecLongName(self):
        self.assertEquals(self.f.videoCodecLongName, "Uncompressed 4:2:2 10-bit")

    def test_getVideoCodecTagString(self):
        self.assertEquals(self.f.videoCodecTagString, "v210")

    def test_getVideoCodecTag(self):
        self.assertEquals(self.f.videoCodecTag, '0x30313276')

    def test_getVideoFrameRate(self):
        self.assertEquals(self.f.videoFrameRate, 29.97)

    def test_getVideoColorSpace(self):
        self.assertEquals(self.f)

    def test_getVideoColorSampling(self):
        self.assertEquals(self.f)

    def test_getVideoBitRate(self):
        self.assertEquals(self.f.videoBitRate, 223724851)


    def test_getVideoBitRateH(self):
        self.assertEquals(self.f.videoBitRateH, '213.4 MB/s')


    def test_getVideoResolution(self):
        self.assertEquals(self.f.videoResolution, "720 x 486")

    def test_getVideoResolutionHeight(self):
        self.assertEquals(self.f.videoResolutionHeight, 486)

    def test_getVideoResolutionWidth(self):
        self.assertEquals(self.f.videoResolutionWidth, 720)


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
        self.assertEqual(self.f.totalRunningTimeRaw, 229.195854)

    def test_getTotalRunningTimeSMPTE(self):
        self.assertEquals(self.f.totalRunningTimeSMPTE, "00:03:49")

    def test_getTotalSeconds(self):
        self.fail()


    def test_colorDepth(self):
        self.assertEquals(self.f.videoColorDepth, 10)

    def test_colorSampling(self):
        self.assertEquals(self.f.videoColorSampling, '4:2:2')

    def test_audio_bit_depth(self):
        self.assertEquals(self.f.audioBitDepth, 24)

    def test_video_aspect_ratio(self):
        self.assertEquals(self.f.videoAspectRatio, "4:3")
    #
    def test_calculateMD5Checksum(self):
        self.assertEquals(self.f.calculate_MD5(progress=True), "dbf29b8d05c61ba53923ebb06c63377c")

    def test_calculateMD5ChecksumThread(self):
        self.f.calculate_MD5(progress=True, threaded=True)
        # print self.f.isMD5Calculating
        self.assertEquals(self.f.MD5_hash, "dbf29b8d05c61ba53923ebb06c63377c")
        # print self.f.isMD5Calculating
    pass