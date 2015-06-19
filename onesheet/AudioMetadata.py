#!/usr/bin/python
# -*- coding: UTF-8 -*-
from onesheet.TimeBasedMetadata import TimeBasedMetadata
from abc import ABCMeta
from OExceptions import NoDataException
AUDIO_CODECS = {"8svx_exp": "8SVX",
                    "8svx_fib": "8SVX",
                    "aac": "AAC",
                    "aac_latm": "AAC",
                    "ac3": "AC-3",
                    "ac3_fixed": "AC-3",
                    "adpcm_4xm": "ADPCM",
                    "adpcm_adx": "ADPCM",
                    "adpcm_afc": "ADPCM",
                    "adpcm_ct": "ADPCM",
                    "adpcm_dtk": "ADPCM",
                    "adpcm_ea": "ADPCM",
                    "adpcm_ea_maxis_xa": "ADPCM",
                    "adpcm_ea_r1": "ADPCM",
                    "adpcm_ea_r2": "ADPCM",
                    "adpcm_ea_r3": "ADPCM",
                    "adpcm_ea_xas": "ADPCM",
                    "g722": "G.722)",
                    "g726": "G.726",
                    "g726le": "G.726",
                    "adpcm_ima_amv": "AMV",
                    "adpcm_ima_apc": "CRYO APC",
                    "adpcm_ima_dk3": "Duck DK3",
                    "adpcm_ima_dk4": "Duck DK4",
                    "adpcm_ima_ea_eacs": "EACS",
                    "adpcm_ima_ea_sead": "SEAD",
                    "adpcm_ima_iss": "Funcom ISS",
                    "adpcm_ima_oki": "Dialogic OKI",
                    "adpcm_ima_qt": "QuickTime",
                    "adpcm_ima_rad": "Radical",
                    "adpcm_ima_smjpeg": "Loki SDL MJPEG",
                    "adpcm_ima_wav": "WAV",
                    "adpcm_ima_ws": "Westwood",
                    "adpcm_ms": "Microsoft",
                    "adpcm_sbpro_2": "Sound Blaster Pro 2-bit",
                    "adpcm_sbpro_3": "Sound Blaster Pro 2.6-bit",
                    "adpcm_sbpro_4": "Sound Blaster Pro 4-bit",
                    "adpcm_swf": "Flash",
                    "adpcm_thp": "THP",
                    "adpcm_vima": "VIMA",
                    "vima": "VIMA)",
                    "adpcm_xa": "XA",
                    "adpcm_yamaha": "Yamaha",
                    "alac": "ALAC",
                    "amrnb": "AMR-NB",
                    "libopencore_amrnb": "AMR-NB",
                    "amrwb": "AMR-WB",
                    "libopencore_amrwb": "AMR-WB",
                    "ape": "Ape",
                    "atrac1": "ATRAC1",
                    "atrac3": "ATRAC3",
                    "atrac3plus": "ATRAC3+",
                    "on2avc": "AVC",
                    "binkaudio_dct": "Bink(DCT)",
                    "binkaudio_rdft": "Bink(RDFT)",
                    "bmv_audio": "BMV",
                    "comfortnoise": "RFC 3389 comfort noise generator",
                    "cook": "RealAudio G2",
                    "dsd_lsbf": "DSD",
                    "dsd_lsbf_planar": "DSD",
                    "dsd_msbf": "DSD",
                    "dsd_msbf_planar": "DSD",
                    "dsicinaudio": "CIN",
                    "dca": "DTS",
                    "eac3": "E-AC-3",
                    "evrc": "EVRC",
                    "flac": "FLAC",
                    "g723_1": "G.723.1",
                    "g729": "G.729",
                    "gsm": "GSM",
                    "libgsm": "gsm",
                    "gsm_ms": "GSM",
                    "libgsm_ms": "gsm_ms",
                    "iac": "IAC",
                    "libilbc": "iLBC",
                    "imc": "IMC",
                    "interplay_dpcm": "DPCM",
                    "mace3": "MACE 3:1",
                    "mace6": "MACE 6:1",
                    "metasound": "MetaSound",
                    "mlp": "MLP",
                    "mp1": "MP1",
                    "mp1float": "MP1",
                    "mp2": "MP2",
                    "mp2float": "MP2",
                    "mp3": "MP3",
                    "mp3float": "MP3",
                    "mp3adu": "ADU",
                    "mp3adufloat": "MP3ADU",
                    "mp3on4": "MP3onMP4",
                    "mp3on4float": "MP3onMP4",
                    "als": "MPEG-4als)",
                    "mpc7": "Musepack SV7",
                    "mpc8": "Musepack SV8",
                    "nellymoser": "Nellymoser Asao",
                    "opus": "Opus",
                    "libopus": "libopus Opus",
                    "paf_audio": "paf",
                    "pcm_alaw": "PCM A-law",
                    "pcm_bluray": "PCM Blu-ray",
                    "pcm_dvd": "PCM DVD",
                    "pcm_f32be": "PCM 32-bit floating point big-endian",
                    "pcm_f32le": "PCM 32-bit floating point little-endian",
                    "pcm_f64be": "PCM 64-bit floating point big-endian",
                    "pcm_f64le": "PCM 64-bit floating point little-endian",
                    "pcm_lxf": "PCM signed 20-bit little-endian planar",
                    "pcm_mulaw": "PCM mu-law",
                    "pcm_s16be": "PCM 16-bit",
                    "pcm_s16be_planar": "PCM 16-bit",
                    "pcm_s16le": "PCM 16-bit ",
                    "pcm_s16le_planar": "PCM 16-bit",
                    "pcm_s24be": "PCM 24-bit",
                    "pcm_s24daud": "PCM D-Cinema 24-bit",
                    "pcm_s24le": "PCM 24-bit",
                    "pcm_s24le_planar": "PCM 24-bit",
                    "pcm_s32be": "PCM 32-bit",
                    "pcm_s32le": "PCM 32-bit",
                    "pcm_s32le_planar": "PCM 32-bit",
                    "pcm_s8": "PCM signed 8-bit",
                    "pcm_s8_planar": "PCM 8-bit ",
                    "pcm_u16be": "PCM 16-bit",
                    "pcm_u16le": "PCM 16-bit",
                    "pcm_u24be": "PCM 24-bit",
                    "pcm_u24le": "PCM 24-bit",
                    "pcm_u32be": "PCM 32-bit",
                    "pcm_u32le": "PCM 32-bit",
                    "pcm_u8": "PCM 8-bit",
                    "pcm_zork": "PCM Zork",
                    "qcelp": "QCELP",
                    "qdm2": "QDesign Music Codec 2",
                    "real_144": "RealAudio 1.0",
                    "real_288": "RealAudio 2.0",
                    "ralf": "RealAudio Lossless",
                    "roq_dpcm": "DPCM id RoQ",
                    "s302m": "SMPTE 302M",
                    "shorten": "Shorten",
                    "sipr": "RealAudio SIPR",
                    "smackaud": "Smacker audio",
                    "sol_dpcm": "Sol",
                    "sonic": "Sonic",
                    "libspeex": "Speex ",
                    "tak": "TAK (Tom's lossless Audio Kompressor)",
                    "truehd": "TrueHD",
                    "truespeech": "TrueSpeech",
                    "tta": "True Audio",
                    "twinvq": "VQF TwinVQ",
                    "vmdaudio": "VMD",
                    "vorbis": "Vorbis",
                    "libvorbis": "Vorbis",
                    "wavesynth": "Wave synthesis pseudo-codec",
                    "wavpack": "WavPack",
                    "ws_snd1": "Westwood Audio (SND1)",
                    "wmalossless": "Windows Media Audio Lossless",
                    "wmapro": "Windows Media Audio 9 Professional",
                    "wmav1": "Windows Media Audio 1",
                    "wmav2": "Windows Media Audio 2",
                    "wmavoice": "Windows Media Audio Voice",
                    "xan_dpcm": "DPCM Xan"}

AUDIO_BIT_DEPTHS = {"u8": "8",
                    "s16": "16",
                    "s32": "24",
                    "flt": "32",
                    "dbl": "",
                    "u8p": "8",
                    "s16p": "16",
                    "s32p": "24",
                    "fltp": "32",
                    "dblp": ""}

class AudioMetadata(TimeBasedMetadata):
    __metaclass__ = ABCMeta
    AUDIO_CODECS = {"8svx_exp": "8SVX",
                    "8svx_fib": "8SVX",
                    "aac": "AAC",
                    "aac_latm": "AAC",
                    "ac3": "AC-3",
                    "ac3_fixed": "AC-3",
                    "adpcm_4xm": "ADPCM",
                    "adpcm_adx": "ADPCM",
                    "adpcm_afc": "ADPCM",
                    "adpcm_ct": "ADPCM",
                    "adpcm_dtk": "ADPCM",
                    "adpcm_ea": "ADPCM",
                    "adpcm_ea_maxis_xa": "ADPCM",
                    "adpcm_ea_r1": "ADPCM",
                    "adpcm_ea_r2": "ADPCM",
                    "adpcm_ea_r3": "ADPCM",
                    "adpcm_ea_xas": "ADPCM",
                    "g722": "G.722)",
                    "g726": "G.726",
                    "g726le": "G.726",
                    "adpcm_ima_amv": "AMV",
                    "adpcm_ima_apc": "CRYO APC",
                    "adpcm_ima_dk3": "Duck DK3",
                    "adpcm_ima_dk4": "Duck DK4",
                    "adpcm_ima_ea_eacs": "EACS",
                    "adpcm_ima_ea_sead": "SEAD",
                    "adpcm_ima_iss": "Funcom ISS",
                    "adpcm_ima_oki": "Dialogic OKI",
                    "adpcm_ima_qt": "QuickTime",
                    "adpcm_ima_rad": "Radical",
                    "adpcm_ima_smjpeg": "Loki SDL MJPEG",
                    "adpcm_ima_wav": "WAV",
                    "adpcm_ima_ws": "Westwood",
                    "adpcm_ms": "Microsoft",
                    "adpcm_sbpro_2": "Sound Blaster Pro 2-bit",
                    "adpcm_sbpro_3": "Sound Blaster Pro 2.6-bit",
                    "adpcm_sbpro_4": "Sound Blaster Pro 4-bit",
                    "adpcm_swf": "Flash",
                    "adpcm_thp": "THP",
                    "adpcm_vima": "VIMA",
                    "vima": "VIMA)",
                    "adpcm_xa": "XA",
                    "adpcm_yamaha": "Yamaha",
                    "alac": "ALAC",
                    "amrnb": "AMR-NB",
                    "libopencore_amrnb": "AMR-NB",
                    "amrwb": "AMR-WB",
                    "libopencore_amrwb": "AMR-WB",
                    "ape": "Ape",
                    "atrac1": "ATRAC1",
                    "atrac3": "ATRAC3",
                    "atrac3plus": "ATRAC3+",
                    "on2avc": "AVC",
                    "binkaudio_dct": "Bink(DCT)",
                    "binkaudio_rdft": "Bink(RDFT)",
                    "bmv_audio": "BMV",
                    "comfortnoise": "RFC 3389 comfort noise generator",
                    "cook": "RealAudio G2",
                    "dsd_lsbf": "DSD",
                    "dsd_lsbf_planar": "DSD",
                    "dsd_msbf": "DSD",
                    "dsd_msbf_planar": "DSD",
                    "dsicinaudio": "CIN",
                    "dca": "DTS",
                    "eac3": "E-AC-3",
                    "evrc": "EVRC",
                    "flac": "FLAC",
                    "g723_1": "G.723.1",
                    "g729": "G.729",
                    "gsm": "GSM",
                    "libgsm": "gsm",
                    "gsm_ms": "GSM",
                    "libgsm_ms": "gsm_ms",
                    "iac": "IAC",
                    "libilbc": "iLBC",
                    "imc": "IMC",
                    "interplay_dpcm": "DPCM",
                    "mace3": "MACE 3:1",
                    "mace6": "MACE 6:1",
                    "metasound": "MetaSound",
                    "mlp": "MLP",
                    "mp1": "MP1",
                    "mp1float": "MP1",
                    "mp2": "MP2",
                    "mp2float": "MP2",
                    "mp3": "MP3",
                    "mp3float": "MP3",
                    "mp3adu": "ADU",
                    "mp3adufloat": "MP3ADU",
                    "mp3on4": "MP3onMP4",
                    "mp3on4float": "MP3onMP4",
                    "als": "MPEG-4als)",
                    "mpc7": "Musepack SV7",
                    "mpc8": "Musepack SV8",
                    "nellymoser": "Nellymoser Asao",
                    "opus": "Opus",
                    "libopus": "libopus Opus",
                    "paf_audio": "paf",
                    "pcm_alaw": "PCM A-law",
                    "pcm_bluray": "PCM Blu-ray",
                    "pcm_dvd": "PCM DVD",
                    "pcm_f32be": "PCM 32-bit floating point big-endian",
                    "pcm_f32le": "PCM 32-bit floating point little-endian",
                    "pcm_f64be": "PCM 64-bit floating point big-endian",
                    "pcm_f64le": "PCM 64-bit floating point little-endian",
                    "pcm_lxf": "PCM signed 20-bit little-endian planar",
                    "pcm_mulaw": "PCM mu-law",
                    "pcm_s16be": "PCM 16-bit",
                    "pcm_s16be_planar": "PCM 16-bit",
                    "pcm_s16le": "PCM 16-bit ",
                    "pcm_s16le_planar": "PCM 16-bit",
                    "pcm_s24be": "PCM 24-bit",
                    "pcm_s24daud": "PCM D-Cinema 24-bit",
                    "pcm_s24le": "PCM 24-bit",
                    "pcm_s24le_planar": "PCM 24-bit",
                    "pcm_s32be": "PCM 32-bit",
                    "pcm_s32le": "PCM 32-bit",
                    "pcm_s32le_planar": "PCM 32-bit",
                    "pcm_s8": "PCM signed 8-bit",
                    "pcm_s8_planar": "PCM 8-bit ",
                    "pcm_u16be": "PCM 16-bit",
                    "pcm_u16le": "PCM 16-bit",
                    "pcm_u24be": "PCM 24-bit",
                    "pcm_u24le": "PCM 24-bit",
                    "pcm_u32be": "PCM 32-bit",
                    "pcm_u32le": "PCM 32-bit",
                    "pcm_u8": "PCM 8-bit",
                    "pcm_zork": "PCM Zork",
                    "qcelp": "QCELP",
                    "qdm2": "QDesign Music Codec 2",
                    "real_144": "RealAudio 1.0",
                    "real_288": "RealAudio 2.0",
                    "ralf": "RealAudio Lossless",
                    "roq_dpcm": "DPCM id RoQ",
                    "s302m": "SMPTE 302M",
                    "shorten": "Shorten",
                    "sipr": "RealAudio SIPR",
                    "smackaud": "Smacker audio",
                    "sol_dpcm": "Sol",
                    "sonic": "Sonic",
                    "libspeex": "Speex ",
                    "tak": "TAK (Tom's lossless Audio Kompressor)",
                    "truehd": "TrueHD",
                    "truespeech": "TrueSpeech",
                    "tta": "True Audio",
                    "twinvq": "VQF TwinVQ",
                    "vmdaudio": "VMD",
                    "vorbis": "Vorbis",
                    "libvorbis": "Vorbis",
                    "wavesynth": "Wave synthesis pseudo-codec",
                    "wavpack": "WavPack",
                    "ws_snd1": "Westwood Audio (SND1)",
                    "wmalossless": "Windows Media Audio Lossless",
                    "wmapro": "Windows Media Audio 9 Professional",
                    "wmav1": "Windows Media Audio 1",
                    "wmav2": "Windows Media Audio 2",
                    "wmavoice": "Windows Media Audio Voice",
                    "xan_dpcm": "DPCM Xan"}

    AUDIO_BIT_DEPTHS = {"u8": "8",
                        "s16": "16",
                        "s32": "24",
                        "flt": "32",
                        "dbl": "",
                        "u8p": "8",
                        "s16p": "16",
                        "s32p": "24",
                        "fltp": "32",
                        "dblp": ""}

    def __init__(self, filename):
        TimeBasedMetadata.__init__(self, filename)

    def __sizeofHuman(self, num):
        num = int(num)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    @property
    def audioBitDepth(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
            if stream.getAttribute("codec_type") == "audio":
                data = int(AUDIO_BIT_DEPTHS[stream.getAttribute("sample_fmt")])
                if data == 0:
                    raise NoDataException("cannot find the bit depth for " + self.file_name)
                return data

    @property
    def audioChannels(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
                if stream.getAttribute("codec_type") == "audio":
                    data = int(stream.getAttribute("channels"))
                    if data == 0:
                        raise NoDataException("Cannot find any audio channels for " + self.file_name)
                    return data

    @property
    def audioCodec(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
            if stream.getAttribute("codec_type") == "audio":

                data = str(AUDIO_CODECS[stream.getAttribute("codec_name")])
                if data is None or data == "":
                    raise NoDataException("Cannot find any audio codec for " + self.file_name)
                return data


    @property
    def audioCodecLongName(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
            if stream.getAttribute("codec_type") == "audio":
                data = str(stream.getAttribute("codec_long_name"))
                if data is None or data == "":
                    raise NoDataException("Cannot find any audio codec long name for " + self.file_name)
                return data
    @property
    def audioSampleRate(self):
        # TODO Make audioSampleRate Method
        for stream in self.xmlDom.getElementsByTagName('stream'):
            if stream.getAttribute("codec_type") == "audio":
                data = int(stream.getAttribute("sample_rate"))
                if data == 0:
                    raise NoDataException("Cannot find a sample rate for " + self.file_name)
                return data

    @property
    def audioBitRate(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
            if stream.getAttribute("codec_type") == "audio":
                data = int(stream.getAttribute("bit_rate"))
                if data == 0:
                    raise NoDataException("Cannot find a bit rate for " + self.file_name)
                return data

    @property
    def audioBitRateH(self):
        for stream in self.xmlDom.getElementsByTagName('stream'):
            if stream.getAttribute("codec_type") == "audio":
                data = self.__sizeofHuman(int(stream.getAttribute("bit_rate")))
                if data is None or data == "":
                    raise NoDataException("Cannot find a bit rate for " + self.file_name)
                return data
