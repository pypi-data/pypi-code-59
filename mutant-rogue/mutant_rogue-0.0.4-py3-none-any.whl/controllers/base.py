
from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
from pathlib import Path
import webbrowser
import requests
import uuid
import yaml
import time

VERSION_BANNER = """
Rogue Cli %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Rogue Cli'

        # text displayed at the bottom of --help output
        epilog = 'Usage: rogue command1 --foo bar'

        # controller level arguments. ex: 'rogue --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
    help='login'
    )
    def login(self):
        url = self.app.config.get('rogue','url')
        home = str(Path.home())
        token = str(uuid.uuid4())
        old_conf = self.app.config.get_dict()['rogue']
        
        new_conf = {
            'rogue': old_conf
        }

        new_conf['rogue']['token'] = token    

        with open(f'{home}/.rogue.conf', 'w') as outfile:
                yaml.dump(new_conf, stream=outfile, default_flow_style=False, indent=3)
        
        login_url = f'{url}/accounts/login?token={token}'
        browser = webbrowser.open(login_url)

        if not browser:
            self.app.render({'msg':f'You need to login: {login_url}'} ,'msg.jinja2')

        while True:
            
            r = requests.post(f'{url}/accounts/session', headers={'Authorization': f'token {token}'})
            print(r.json())
            if r.status_code == 200:
                self.app.render({'msg':f'You need to login: {login_url}'} ,'msg.jinja2')
                break
            else:
                time.sleep(5)
            
