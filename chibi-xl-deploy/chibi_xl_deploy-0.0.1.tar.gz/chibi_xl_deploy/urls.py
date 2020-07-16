import requests
from chibi_xl_deploy.config import configuration
from chibi_requests import Chibi_url


base_url = Chibi_url(
    f"{configuration.xlr.schema}://{configuration.xlr.host}/api/v1/" )

base_url += requests.auth.HTTPBasicAuth(
    configuration.xlr.user, configuration.xlr.password )

base_url.headers.content_type = 'application/json'

templates = base_url + 'templates'
create_release = templates + '{templateId}/create'
