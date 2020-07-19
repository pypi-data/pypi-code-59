"""
.Net source project
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import os
import re
from pykrete.args import exiting_file
from pykrete.io.file import File
from pykrete.patterns import first_or_error
from .project_type import ProjectType


class Project:
    """Handle source-code projects in a solution
    """

    __test_project_type_guid = '3AC096D0-A1C2-E12C-1390-A8335801FDAB'

    @property
    def path(self):
        """
        :return: (string) the project's path
        """
        return self._path

    @property
    def directory(self):
        """
        :return: (string) the project's directory
        """
        return os.path.dirname(self._path)

    @property
    def name(self):
        """
        :return: (string) the project's name
        """
        return self._name

    @property
    def type(self):
        """
        :return: (ProjectType) the project's type
        """
        return self._type

    @property
    def output(self):
        """
        :return: (dict) a dictionary between {mode} and {output path}
        """
        return self._output

    @property
    def assembly_info(self):
        """
        :return: (File) the project's assembly info source file
        """
        return self._assembly_info

    @property
    def include(self):
        """
        :return: included artifacts, or '*' if none are defined
        """
        return self._include

    def __init__(self, path):
        """Initializes this instance

        :param path: project's path
        """
        self._path = exiting_file(path)
        self.__file = File(path)
        self.__file.read_contents()
        self._name = self.__locate_name()
        self._type = self.__locate_type()
        self._output = self.__locate_output()
        self._assembly_info = self.__locate_assembly_info()
        self._include = self.__extract_artifacts()
        self.__file.forget_contents()

    def __str__(self):
        """Returns a string representation of this object

        :return: a string representation of this object
        """
        return f'{self.name} [{self.directory}]'

    def __locate_name(self):
        return first_or_error(re.findall(r'<AssemblyName>(.*?)</', self.__file.get_contents()),
                              'AssemblyName not found in ' + self.path)

    def __locate_type(self):
        output_type = re.findall(r'<OutputType>(.+?)</OutputType>', self.__file.get_contents())[0]
        if output_type == "Library":
            if self.__test_project_type_guid in self.__file.get_contents():
                return ProjectType.UNIT_TEST
            if self.name.endswith("Tests") or self.name.endswith("Test"):
                return ProjectType.FLOW_TEST
            return ProjectType.LIBRARY
        if output_type.endswith("Exe"):
            return ProjectType.EXECUTABLE
        return ProjectType.UNKNOWN

    def __locate_output(self):
        mode_and_out_path = re.findall(
            r'<PropertyGroup Condition=" \'\$\(C.+?\)\|.+?\)\'.+_?\'(.+?)\|[\s\S]+?'
            r'<OutputPath>(.+?)<', self.__file.get_contents())
        return {mode: os.path.join(self.directory, out_path)
                for (mode, out_path) in mode_and_out_path}

    def __locate_assembly_info(self):
        return File(os.path.join(self.directory,
                                 first_or_error(
                                     re.findall(r'<Compile Include="(.*AssemblyInfo\.cs)"',
                                                self.__file.get_contents()),
                                     'AssemblyName not found in ' + self.path)))

    def __extract_artifacts(self):
        # doesn't seem to work for MuDi.Cli!
        include = re.findall(r'\[assembly: Artifact"\(.*\)"\]', self.assembly_info.read())
        return include if include else "*"
