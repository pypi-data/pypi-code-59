"""
Python package
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from xml.dom import minidom
from pykrete.io.file.rtf import Rtf
from pykrete.io.file import File


class NugetPackage:
    """NuGet package
    """
    __release_notes_element = 'releaseNotes'

    def __init__(self, nuspec_path):
        """Initialize this intance

        :param nuspec_path: Nuspec file path
        """
        self._nuspec_path = nuspec_path

    def update_release_notes(self, release_notes_rtf_path):
        """Update release notes in nuspec from the specified RTF file

        :param release_notes_rtf_path: RTF file path
        """
        nuspec_doc = minidom.parse(self._nuspec_path)
        rtf_text = Rtf(release_notes_rtf_path).text.strip()
        self._replace_release_notes(nuspec_doc, rtf_text)
        File(self._nuspec_path).write_doc(nuspec_doc)

    def _replace_release_notes(self, doc, text):
        release_notes = doc.getElementsByTagName(self.__release_notes_element)[0]
        cdata = doc.createCDATASection(text)
        release_notes.replaceChild(cdata, release_notes.firstChild)
