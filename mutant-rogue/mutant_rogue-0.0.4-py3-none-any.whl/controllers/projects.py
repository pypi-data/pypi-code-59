from cement import Controller, ex
from cement import App
import requests
from termcolor import colored
from tabulate import tabulate


class Projects(Controller):
    class Meta:
        label = 'projects'
        stacked_type = 'nested'
        stacked_on = 'base'
        description = 'Rogue Cli'
        epilog = 'Usage: rogue project command'

        
        # arguments = [
        #     # list of tuples in the format `( [], {} )`
        #     ( [ '-n', '--name' ],
        #       { 'help' : 'name of project' } ),
        # ]



    # @ex(help="second-controller default command", hide=True)
    # def _default(self):
    #     print(self.app.pargs)
    #     print("Inside SecondController.default()")

    @ex(help='List all projects')
    def ls(self):
        try:
                
            url = self.app.config.get('rogue','url')
            r = requests.get(f'{url}/projects')
            json_s = r.json()

            projects = list(map(lambda x: [x['name']], json_s))

            headers = ['name']

            self.app.render({'table':tabulate(projects, headers)},'table.jinja2')
        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')} ,'msg.jinja2')

    @ex(help='create new project',
    arguments=[
        (['name'],
        {'help': 'project name'}),
        (['template'],
        {'help': 'template name'}),
        (['email'],
        {'help': 'owner email'})
    ]
    )
    def new(self):
        url = self.app.config.get('rogue','url')

        try:

            body = {
                "name": self.app.pargs.name,
                "template": self.app.pargs.template,
                "email": self.app.pargs.email
            }	

            r = requests.post(f'{url}/projects', json=body)
            

            if r.status_code == 201:
                self.app.render(r.json(),'project.jinja2')
            else:
                error = {
                    'msg': colored(r.json()['message'],'red')   
                }
                self.app.render(error ,'msg.jinja2')
                # print(colored(r.json()['message'], 'red'))

        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')} ,'msg.jinja2')

    @ex(help='describe project',
    arguments=[
        (['name'],
        {'help': 'project name'}),
        (['-v', '--versions'],
        {'help': 'show versions of project','action':'store_true'}),
    ]
    )
    def describe(self):
        try:
            url = self.app.config.get('rogue','url')

            if self.app.pargs.versions:
                r = requests.get(f'{url}/projects/{self.app.pargs.name}/version')

                if r.status_code == 200:

                    headers = ['version', 'published']
                    data = []
                    for j in r.json():
                        published = 'YES' if j['published'] else 'NO'
                        data.append([j['version'],published])

            
                    self.app.render({'table':tabulate(data, headers)},'table.jinja2')
                else:
                    error = {
                        'msg': colored(r.json()['message'],'red')   
                    }
                    self.app.render(error ,'msg.jinja2')
                    
            
            else:
                print('No describe yet!')

        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')

    @ex(help='generate new version of project',
    arguments=[
        (['name'],
        {'help': 'project name'})
    ]
    )
    def new_version(self):
        try:
            url = self.app.config.get('rogue','url')
            r = requests.post(f'{url}/projects/{self.app.pargs.name}/version')

            if r.status_code == 202:
                msg = {
                        'msg': colored('A new versions is generating...')   
                }
                self.app.render(msg ,'msg.jinja2')
                    
            else:
                error = {
                        'msg': colored(r.json()['message'],'red')   
                }
                self.app.render(error ,'msg.jinja2')
                    
        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')


    @ex(help='publish project version',
    arguments=[
        (['name'],
        {'help': 'project name'}),
        (['version'],
        {'help': 'version project'}),
        (['extension'],
        {'help': 'extension of project', 'type': int}),
        (['-f', '--force'],
        {'help': 'override extension in use','action':'store_true'}),
    ]
    )
    def publish(self):
        url = self.app.config.get('rogue','url')
        try:

            # TODO: VALIDAR ANTES DE PUBLICAR
            arguments = self.app.pargs
            body = {
                        "extension": arguments.extension,
                        "override": arguments.force
                }

            r = requests.post(f'{url}/projects/{arguments.name}/{arguments.version}', json=body)

            if r.status_code == 200:
                self.app.render({'msg': f'Version {arguments.version} published!'},'msg.jinja2')
            elif r.status_code == 409:
                self.app.render({'msg': colored(f"{r.json()['message']}, -f parameter can force",'yellow')},'msg.jinja2')
            else:
                self.app.render({'msg': colored(r.json(),'red')},'msg.jinja2')

        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')

    @ex(help='validate project',
    arguments=[
        (['name'],
        {'help': 'project name'}),
        (['-a', '--audios'],
        {'help': 'validate with audios','action':'store_true'}),
    ]
    )
    def validate(self):
        try:
            url = self.app.config.get('rogue','url')
            arguments = self.app.pargs
            body = {
                "validateAudios": arguments.audios
            }

            r = requests.post(f'{url}/projects/{arguments.name}/validate', json=body)
            if r.status_code == 200:
                result = r.json()
                errors = 0
                warnings = 0
                obj = {
                    'states': []
                }

                for r in result:
                    state = {}
                    state['name'] = r
                    state['status'] = colored('OK', 'green')
                    state['messages'] = []
                    for s in result[r]['state']:

                        if s['type'] == 'error':
                            errors += 1
                            state['status'] = colored('NOK', 'red')
                            pre_txt = colored('[Error] ','red')
                        else:
                            warnings += 1
                            pre_txt = colored('[Warning] ','yellow')

                        cell = f':{s["cell"]}' if 'cell' in s else ''
                        state['messages'].append(f"{pre_txt}{s['message']}{cell}")
                    
                    for p in result[r]['prompts']:

                        if p['type'] == 'error':
                            errors += 1
                            state['status'] = colored('NOK', 'red')
                            pre_txt = colored('[Error] ','red')
                        else:
                            warnings +=1
                            pre_txt = colored('[Warning] ','yellow')

                        cell = f':{p["cell"]}' if 'cell' in p else ''
                        state['messages'].append(f"{pre_txt}{p['message']}{cell}")

                    for t in result[r]['transitions']:

                        if t['type'] == 'error':
                            errors += 1
                            state['status'] = colored('NOK', 'red')
                            pre_txt = colored('[Error] ','red')
                        else:
                            warnings +=1
                            pre_txt = colored('[Warning] ','yellow')


                        cell = f':{t["cell"]}' if 'cell' in t else ''
                        state['messages'].append(f"{pre_txt}{t['message']}{cell}") 

                    obj['states'].append(state)

                obj['errors'] = errors
                obj['warnings'] = warnings
                
                self.app.render(obj,'validate.jinja2')           
            else:
                self.app.render({'msg': colored(r.json(),'red')},'msg.jinja2')
        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')

    @ex(help='get schema for integration',
    arguments=[
        (['name'],
        {'help': 'project name'})
    ]
    )
    def schema(self):
        try:
            url = self.app.config.get('rogue','url')
            arguments = self.app.pargs
            r = requests.get(f'{url}/projects/{arguments.name}/schema')

            if r.status_code == 200:
                self.app.render({'msg': r.text.replace(r'\n', '\n').replace('"','')},'msg.jinja2')
            else:
                self.app.render({'msg': colored(r.json(),'red')},'msg.jinja2')
        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')




     
        


    