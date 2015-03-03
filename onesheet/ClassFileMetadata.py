#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib

from os.path import split, splitext, getctime, getsize, getmtime
from time import ctime

VALID_VIDEO_FILE_EXTENSIONS = ['.avi', '.mov', '.mp4', '.mpeg', '.mpg', '.mkv']
VALID_AUDIO_FILE_EXTENSIONS = ['.wav', '.mp3', '.ogg']
VALID_IMAGE_FILE_EXTENSIONS = ['.bmp', '.gif', '.jpg', '.psd', '.tga', '.tif']
VALID_DOCUMENT_FILE_EXTENSIONS = ['.doc', '.docx', '.pdf', '.txt']


class FormatException(Exception):
    def __init__(self, value):
         self.value = value

    def __str__(self):
        return self.value


class FileMetadata(object):

    def __init__(self, sourcefile):
        self.___source = sourcefile
        self.___fileName = split(sourcefile)[1]
        self.___filePath = split(sourcefile)[0]
        self.___metadataDOM = None

    def __validateFileType(self):
        # check file extensions
        validation = True
        valid_extension = False
        file_extension = splitext(self.___source)[1]
        for extension in VALID_VIDEO_FILE_EXTENSIONS:
            if file_extension == extension:
                valid_extension = True
                break
        for extension in VALID_AUDIO_FILE_EXTENSIONS:
            if file_extension == extension:
                valid_extension = True
                break
        if not valid_extension:
            raise FormatException(file_extension + " is not an audio or video file.")
            # validation = False
        return validation



    def __sizeofHuman(self, num):
        num = int(num)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0


    @property
    def file_name(self):
        return self.___fileName

    @property
    def file_path(self):
        return self.___filePath

    @property
    def file_extension(self):
        return str(splitext(self.___source)[1])

    @property
    def format_type(self):
        #check if it's an audio format
        for extension in VALID_AUDIO_FILE_EXTENSIONS:
            if extension in self.___source:
                return "audio"

        #check if it's a video format
        for extension in VALID_VIDEO_FILE_EXTENSIONS:
            if extension in self.___source:
                return "video"
        return "unknown"

    @property
    def file_size(self):
        return getsize(self.___source)

    @property
    def file_size_human(self):
        return self.__sizeofHuman(getsize(self.___source))

    @property
    def date_created(self):
        return ctime(getctime(self.___source))

    @property
    def date_last_modified(self):
        return ctime(getmtime(self.___source))

    def getXML(self):
        pass

    def calculate_MD5(self):
        md5 = hashlib.md5()
        with open(self.___source,'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        return md5.hexdigest()


    def calculate_SHA1(self):
        sha1 = hashlib.sha1()
        with open(self.___source,'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                sha1.update(chunk)

        return sha1.hexdigest()


