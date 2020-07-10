#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################
# Name: setup.py
# Porpose: script to setup Videomass.
# Compatibility: Python3
# Platform: all
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2014-2020 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev: June.14.2020 *PEP8 compatible*
#########################################################

# This file is part of Videomass.

#    Videomass is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Videomass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Videomass.  If not, see <http://www.gnu.org/licenses/>.

#########################################################
from setuptools import setup, find_packages
from glob import glob
import os
from videomass3.vdms_sys.msg_info import current_release
from videomass3.vdms_sys.msg_info import descriptions_release

# ---- current work directory path ----#
PWD = os.getcwd()

# ---- Get info data ----#
cr = current_release()
RLS_NAME = cr[0]  # release name first letter is Uppercase
PRG_NAME = cr[1]
VERSION = cr[2]
RELEASE = cr[3]
COPYRIGHT = cr[4]
WEBSITE = cr[5]
AUTHOR = cr[6]
EMAIL = cr[7]
COMMENT = cr[8]

dr = descriptions_release()
LICENSE = dr[2]  # short license
DESCRIPTION = dr[0]
LONG_DESCRIPTION = dr[1]

# ---- categorize with ----#
CLASSIFIERS = [
        'Environment :: MacOS X :: Cocoa',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: GTK',
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Natural Language :: Italian',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Topic :: Utilities',
                ]
# ---------------------------------------------------------------------#


def glob_files(pattern):
    """
    Useful function for globbing that iterate on a pattern marked
    with wildcard and put it in a objects list
    """
    return [f for f in glob(pattern) if os.path.isfile(f)]
# ---------------------------------------------------------------------#


def source_build():
    """
    Source/Build distributions

    """
    INSTALL_REQUIRES = ["wxpython>=4.0.3; platform_system=='Windows' or "
                        "platform_system=='Darwin'",
                        "PyPubSub>=4.0.3",
                        "youtube_dl>=2020.1.1",
                        ]
    EXCLUDE = ['']

    DATA_FILES = [  # paths must be relative-path
                  ('share/applications', ['videomass3/art/videomass.desktop']),
                  ('share/pixmaps', ['videomass3/art/icons/videomass.png']),
                  ('share/man/man1', ['docs/man/man1/videomass.1']),
                  ]

    setup(name=PRG_NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=open('README.md').read(),
          long_description_content_type='text/markdown',
          author=AUTHOR,
          author_email=EMAIL,
          url=WEBSITE,
          license=LICENSE,
          platforms=["All"],
          packages=find_packages(exclude=EXCLUDE),
          data_files=DATA_FILES,
          package_data={"videomass3": ["art/icons/*", "locale/*"]
                        },
          exclude_package_data={"videomass3": ["art/videomass.icns",
                                               "art/videomass.ico",
                                               "locale/README",
                                               "locale/videomass.pot"
                                               ]},
          include_package_data=True,
          zip_safe=False,
          python_requires='~=3.7',
          install_requires=INSTALL_REQUIRES,
          setup_requires=["setuptools>=47.1.1",
                          "wheel>=0.34.2",
                          "twine>=3.1.1"
                          ],
          entry_points={'gui_scripts':
                        ['videomass = videomass3.Videomass3:main']},
          classifiers=CLASSIFIERS,
          )
# ---------------------------------------------------------------------#


if __name__ == '__main__':
    source_build()
