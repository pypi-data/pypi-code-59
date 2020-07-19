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

import psycopg2
from ebi_eva_common_pyutils.config_utils import EVAPrivateSettingsXMLConfig


def get_pg_metadata_handle_for_eva_profile(eva_profile_name: str, settings_xml_file: str):
    config = EVAPrivateSettingsXMLConfig(settings_xml_file)
    xpath_location_template = '//settings/profiles/profile/id[text()="{0}"]/../properties/{1}/text()'
    # Format is jdbc:postgresql://host:port/db
    metadata_db_jdbc_url = config.get_value_with_xpath(
        xpath_location_template.format(eva_profile_name, "eva.evapro.jdbc.url"))[0]
    username = config.get_value_with_xpath(
        xpath_location_template.format(eva_profile_name, "eva.evapro.user"))[0]
    postgres_uri = metadata_db_jdbc_url.split("jdbc:")[-1]
    return psycopg2.connect(postgres_uri, user=username)
