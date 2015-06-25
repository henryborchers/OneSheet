from unittest import TestCase
from onesheet.AudioObject import *
# import onesheet
__author__ = 'lpsdesk'


class TestAudioMetadata(TestCase):

    def setUp(self):
        self.f = AudioObject("/Users/lpsdesk/PycharmProjects/audio_convert/ALLEY_B.mp3")

    def test_getAudioBitDepth(self):
        self.assertEquals(self.f.audioBitDepth, 16)

    def test_getDuration(self):
        self.assertEquals(self.f.totalRunningTimeSMPTE, "00:33:20.25")

    def test_getAudioChannels(self):
        self.assertEquals(self.f.audioChannels, 2)

    def test_getAudioCodec(self):
        self.assertEquals(self.f.audioCodec, 'MP3')

    def test_getAudioCodecLongName(self):
        self.assertEquals(self.f.audioCodecLongName, "MP3 (MPEG audio layer 3)")

    def test_getAudioSampleRate(self):
        self.assertEquals(self.f.audioSampleRate, 44100)