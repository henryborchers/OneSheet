"""
OneSheet
========

OneSheet is a tool for extracting metadata from an Audio, Video, Image, or Document file.

OneSheet is designed for easily creating record generating scripts and scripts for validating files (such as
for quality assurance purposes)


To Install
----------

.. code::
    $ pip install OneSheet


"""


from setuptools import setup

setup(
    name='OneSheet',
    version='0.1.1',
    description='Easily access metadata for image, video, sound, and document file.',
    long_description=__doc__,
    url='https://github.com/henryborchers/OneSheet',
    license='GPL3',
    author='Henry Borchers',
    author_email='henryborchers@yahoo.com',
    packages=['onesheet'],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Programming Language :: Python',
                 'Topic :: Multimedia :: Sound/Audio :: Analysis'],
    keywords='metadata extraction'
)
