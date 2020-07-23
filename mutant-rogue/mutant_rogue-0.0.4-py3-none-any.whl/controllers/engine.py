from cement import Controller, ex
from cement import App
import requests
from termcolor import colored
from tabulate import tabulate
from .utils import auth_error

class Engine(Controller):
    class Meta:
        label = 'engine'
        stacked_type = 'nested'
        stacked_on = 'base'
        description = 'Rogue Cli'
        epilog = 'Usage: rogue engine command'


    @ex(help='show all running projects on rogue')
    def running(self):
        url = self.app.config.get('rogue','url')
        token = self.app.config.get('rogue','token')

        try:
            r = requests.get(f'{url}/projects/running',  headers={'Authorization': f'token {token}'})

            if r.status_code == 200:
                headers = ['Extension', 'Name', 'version']
                result = r.json()
                dev = result['dev']
                prd = result['prd']
                data = []

                for d in dev:
                    data.append([d,dev[d]['name'], 'dev'])

                for p in prd:
                    data.append([p,prd[p]['name'], prd[p]['version']])

                
                self.app.render({'table':tabulate(data, headers)},'table.jinja2')
            elif r.status_code == 401:
                auth_error(self.app)

        except requests.exceptions.ConnectionError as err:
            print(colored('A error on rogue-dialog-api ocurred','red'))

    @ex(help='show all running projects on rogue')
    def configure(self):
        # lala = input('oioi')
        # self.app.config.set('rogue','blah', True)
        # other_config = dict()
        # other_config['myapp'] = dict()
        # other_config['myapp']['foo'] = 'not bar'
        # self.app.config.merge(other_config)
        print(self.app.config.get('rogue','name'))
