import os
from unittest import TestCase
from onesheet.AudioObject import *
__author__ = 'lpsdesk'


class TestAudioObject(TestCase):
    def setUp(self):
        target = '/Users/lpsdesk/PycharmProjects/OneSheet/csfpal_000021_t4_b_prsv.wav'
        if os.path.exists(target):
            self.f = AudioObject(target)
        else:
            print("Cannot find file")

    def test_getAudioBitDepth(self):
        self.assertEquals(self.f.audioBitDepth, 24)

    def test_getDuration(self):
        self.assertEquals(self.f.totalRunningTimeSMPTE, "00:05:03")

    def test_getAudioChannels(self):
        self.assertEquals(self.f.audioChannels, 1)

    def test_getAudioCodec(self):
        self.assertEquals(self.f.audioCodec, 'PCM 24-bit')

    def test_getAudioCodecLongName(self):
        self.assertEquals(self.f.audioCodecLongName, "PCM signed 24-bit little-endian")

    def test_getAudioSampleRate(self):
        self.assertEquals(self.f.audioSampleRate, 96000)

    def test_getAudioBitRate(self):
        self.assertEquals(self.f.audioBitRate, 2304000)

    def test_getAudioBitRateH(self):
        self.assertEquals(self.f.audioBitRateH, "2.2 MB")

    def test_checksum(self):
        self.assertEquals(self.f.calculate_MD5(progress=True), "c1056fc5a6dd7f79683e57a0e373225a")

