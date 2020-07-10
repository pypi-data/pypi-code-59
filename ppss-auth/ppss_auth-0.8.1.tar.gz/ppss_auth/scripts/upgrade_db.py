import sys,os
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
import logging
l = logging.getLogger('ppssauth.scripts')
import subprocess
from ppss_auth import __path__

def main(argv=sys.argv):
  config_uri = argv[-1]
  setup_logging(config_uri)
  inihere = os.getcwd()
  here = os.path.join(str(__path__[0]),"..")
  #out = subprocess.Popen('alembic -x sqluri={} -x cwd={} upgrade head'.format(config_uri,inihere).split(" "), 
  #         stdout=subprocess.PIPE, 
  ##         stderr=subprocess.STDOUT,
  #         workingdir=here)
  #stdout,stderr = out.communicate()
  subprocess.call('alembic -x sqluri={} -x cwd={} upgrade head'.format(config_uri,inihere).split(" "), cwd = here)
