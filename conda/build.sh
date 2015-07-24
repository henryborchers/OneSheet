#!/bin/bash

#if [ ! -f /tmp/lame.tar.gz ]; then
#    echo "Downloading LAME";
#    wget -O /tmp/lame.tar.gz http://downloads.sourceforge.net/project/lame/lame/3.98.4/lame-3.98.4.tar.gz;
#else
#    echo "Found LAME";
#fi

#if [!$LIBRARY_BIN/ffprobe -h]; then
#    if [ ! -d /tmp/ffmpeg ]; then
#        git clone git://source.ffmpeg.org/ffmpeg.git /tmp/ffmpeg
#    else
#        echo "Found FFMPEG"
#        (cd /tmp/ffmpeg/; git pull)
#    fi
#
#    /tmp/ffmpeg/configure --prefix=${PREFIX} --disable-ffmpeg  --disable-ffplay --disable-ffserver --disable-doc --enable-small;
#    make;
#    make install;
#fi
#make clean;




$PYTHON setup.py install

# Add more build steps here, if they are necessary.

# See
# http://docs.continuum.io/conda/build.html
# for a list of environment variables that are set during the build process.
