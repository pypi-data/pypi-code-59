# Copyright 2020 EMBL - European Bioinformatics Institute
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lxml import etree as et
from ebi_eva_common_pyutils.mongo_utils import MongoConfig
from urllib.parse import quote_plus


class EVAPrivateSettingsXMLConfig:
    config_data = None

    def __init__(self, settings_xml_file: str):
        with open(settings_xml_file) as xml_file_handle:
            self.config_data = et.parse(xml_file_handle)

    def get_value_with_xpath(self, location: str):
        etree = self.config_data.getroot()
        return etree.xpath(location)
