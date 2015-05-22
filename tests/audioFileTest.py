import os

__author__ = 'California Audio Visual Preservation Project'
from onesheet.AudioObject import *
import sys
def main():
    print("\nONESHEET MODULE TEST PROGRAM\n")
    sys.stdout.flush()
    try:
        sys.argv[1]
    except IndexError:
        sys.stderr.write("Needs a file name to run test.\n")
        quit()

    if not os.path.exists(sys.argv[1]):
        sys.stderr.write(("Unable to find: " + sys.argv[1]))
        quit()
    print("Testing OneSheet AudioObject with: " + sys.argv[1])
    test = AudioObject(sys.argv[1])

    if not test.audioBitDepth:
        sys.stderr.write("Unable to calculate audioBitDepth\n")
    else:
        print("audioBitDepth: " + str(test.audioBitDepth))

    if not test.audioBitRate:
        sys.stderr.write("Unable to calculate audioBitRate\n")
    else:
        print("audioBitRate: " + str(test.audioBitRate))

    if not test.audioBitRateH:
        sys.stderr.write("Unable to calculate audioBitRateH\n")
    else:
        print("audioBitRateH: " + str(test.audioBitRateH))

    if not test.audioChannels:
        sys.stderr.write("Unable to calculate audioChannels\n")
    else:
        print("audioChannels: " + str(test.audioChannels))

    if not test.audioCodec:
        sys.stderr.write("Unable to calculate audioCodec\n")
    else:
        print("audioCodec: " + str(test.audioCodec))

    if not test.audioCodecLongName:
        sys.stderr.write("Unable to calculate audioCodecLongName\n")
    else:
        print("audioCodecLongName: " + str(test.audioCodecLongName))

    if not test.audioSampleRate:
        sys.stderr.write("Unable to calculate audioSampleRate\n")
    else:
        print("audioSampleRate: " + str(test.audioSampleRate))

    if not test.totalRunningTimeSMPTE:
        sys.stderr.write("Unable to calculate totalRunningTimeSMPTE\n")
    else:
        print("totalRunningTimeSMPTE: " + str(test.totalRunningTimeSMPTE))



if __name__ == '__main__':
    main()