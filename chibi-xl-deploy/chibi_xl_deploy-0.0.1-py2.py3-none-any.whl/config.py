import logging
from chibi.config import configuration


logger = logging( 'chibi_xl_deploy.config' )

if not configuration.github.host:
    configuration.github.host = 'api.github.com'
if not configuration.github.schema:
    configuration.github.schema = 'https'


#http://[host]:[port]/[context-root]/[service-resource]

if not configuration.lxr:
    logger.error( 'no esta configurado XLR con chibi' )
