#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib
import os

from os.path import split, splitext, getctime, getsize, getmtime
from sys import stdout
import threading
from time import ctime, sleep
from abc import ABCMeta
import thread
import sys
from OExceptions import FormatException, NoDataException

VALID_VIDEO_FILE_EXTENSIONS = ['.avi', '.mov', '.mp4', '.mpeg', '.mpg', '.mkv']
VALID_AUDIO_FILE_EXTENSIONS = ['.wav', '.mp3', '.ogg']
VALID_IMAGE_FILE_EXTENSIONS = ['.bmp', '.gif', '.jpg', '.psd', '.tga', '.tif']
VALID_DOCUMENT_FILE_EXTENSIONS = ['.doc', '.docx', '.pdf', '.txt']
BUFFER = 8192



class MD5_Generator(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.file = file
        self.total = getsize(file)
        self.isRunning = False
        self.completed = 0
        self.md5 = hashlib.md5()


    @property
    def running(self):
        return self.isRunning

    @property
    def progress(self):
        progress_lock = threading.Lock()
        with progress_lock:
            return self.completed

    @property
    def getChecksum(self):
        return self.md5.hexdigest()

    def run(self):

        self.isRunning = True
        with open(self.file, 'rb') as f:
            i = float(0)

            for chunk in iter(lambda: f.read(BUFFER), b''):
                i += BUFFER
                self.completed = int((i/self.total)*100)
                self.md5.update(chunk)

        self.isRunning = False



class FileMetadata(object):
    __metaclass__ = ABCMeta
    def __init__(self, sourcefile):
        if not os.path.exists(sourcefile):
            raise IOError(sourcefile + " not found")
        self.___source = sourcefile
        self.___fileName = split(sourcefile)[1]
        self.___filePath = split(sourcefile)[0]
        self.___metadataDOM = None
        self._calculation_progress = 0
        self._calculation = None
        self._MD5 = None

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
    def isMD5Calculating(self):
        if self._calculation:
            return self._calculation.isAlive()
        else:
            return False

    @property
    def calulation_progresss(self):
        return self._calculation_progress

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
        extension = os.path.splitext(self.___source)[1]
        if any(extension in x for x in VALID_AUDIO_FILE_EXTENSIONS):
            return "audio"

        #check if it's a video format
        elif any(extension in x for x in VALID_VIDEO_FILE_EXTENSIONS):
            return "video"
        else:
            raise FormatException(extension + " files are not currently supported.")


    @property
    def file_size(self):
        if self.___source is None or self.___source == "":
            raise NoDataException("No file not set")
        return getsize(self.___source)

    @property
    def file_size_human(self):
        if self.___source is None or self.___source == "":
            raise NoDataException("No file not set")

    @property
    def date_created(self):
        if self.___source is None or self.___source == "":
            raise NoDataException("No file not set")
        return ctime(getctime(self.___source))

    @property
    def date_last_modified(self):
        if self.___source is None or self.___source == "":
            raise NoDataException("No file not set")
        return ctime(getmtime(self.___source))

    @property
    def MD5_hash(self):
        if self._MD5:
            return self._MD5
        elif self._calculation.isAlive:
            self._calculation.join()
            # self._MD5 = self.calculation
            return self._MD5
        else:
            raise NoDataException("MD5 not calculated yet for " + self.___source)

    def getXML(self):
        pass


    def _calculate_MD5(self, progress):
        MD5 = hashlib.md5()
        # print "start"
        sleep(1)
        # total = self.file_size
        # checksum = MD5_Generator(self.___source, progress=True)
        checksum = MD5_Generator(self.___source)
        checksum.daemon = True
        checksum.start()
        # while checksum.running == True:
        while checksum.isRunning:
            # print checksum.running
            sleep(.25)
            self._calculation_progress = checksum.progress
            if progress == True:
                # print checksum.progress
                message = str(self._calculation_progress) + "%"
                # print(message),
                sys.stdout.write('\r' + message)
                sys.stdout.flush()
        checksum.join()
        if progress == True:
            sys.stdout.write("\r\033[K\r")
            sleep(.5)
            sys.stdout.flush()
        self._MD5 = checksum.getChecksum
        return self._MD5

    def calculate_MD5(self, progress=False, threaded=False):
        if self.___source is None or self.___source == "":
            raise NoDataException("No file not set")
        if threaded:
            self._calculation = threading.Thread(target=self._calculate_MD5, args=(progress,))
            self._calculation.daemon = True
            self._calculation.start()
        else:
            MD5 = self._calculate_MD5(progress)
            self._MD5 = MD5
            return MD5


    def calculate_SHA1(self, verbose=False):
        if self.___source is None or self.___source == "":
            raise NoDataException("No file not set")
        sha1 = hashlib.sha1()
        total = self.file_size
        with open(self.___source,'rb') as f:
            i = float(0)
            for chunk in iter(lambda: f.read(BUFFER), b''):
                if verbose:
                    i += BUFFER
                    completed = int((i/total)*100)
                    print str(completed) + "%"
                sha1.update(chunk)

        return sha1.hexdigest()

# TODO add a class for better progress reporting
