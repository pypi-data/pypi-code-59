from cement import Controller, ex
from cement import App
import requests
from termcolor import colored
from tabulate import tabulate
import unicodedata
import os
import yaml
from .utils import auth_error


class Project(Controller):
    class Meta:
        label = 'project'
        stacked_type = 'nested'
        stacked_on = 'base'
        description = 'Rogue Cli'
        epilog = 'Usage: rogue project command'
        help = 'Project'

        
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
            token = self.app.config.get('rogue','token')
            url = self.app.config.get('rogue','url')
            r = requests.get(f'{url}/projects',headers={'Authorization': f'token {token}'})

            if r.status_code == 200:
                json_s = r.json()

                projects = list(map(lambda x: [x['name']], json_s))

                headers = ['name']

                self.app.render({'table':tabulate(projects, headers)},'table.jinja2')
            
            elif r.status_code == 401:
                auth_error(self.app)
            else:
                error = {
                    'msg': colored(r.json(),'red')   
                }
                self.app.render(error ,'msg.jinja2')

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
        token = self.app.config.get('rogue','token')
        try:

            body = {
                "name": self.app.pargs.name,
                "template": self.app.pargs.template,
                "email": self.app.pargs.email
            }	

            r = requests.post(f'{url}/projects', json=body, headers={'Authorization': f'token {token}'})
            

            if r.status_code == 201:
                self.app.render(r.json(),'project.jinja2')
            elif r.status_code == 401:
                auth_error(self.app)
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
            token = self.app.config.get('rogue','token')
            if self.app.pargs.versions:
                r = requests.get(f'{url}/projects/{self.app.pargs.name}/version',headers={'Authorization': f'token {token}'})

                if r.status_code == 200:

                    headers = ['version', 'published']
                    data = []
                    for j in r.json():
                        published = 'YES' if j['published'] else 'NO'
                        data.append([j['version'],published])

            
                    self.app.render({'table':tabulate(data, headers)},'table.jinja2')
                elif r.status_code == 401:
                    auth_error(self.app)
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
            token = self.app.config.get('rogue','token')

            r = requests.post(f'{url}/projects/{self.app.pargs.name}/version',headers={'Authorization': f'token {token}'})

            if r.status_code == 202:
                msg = {
                        'msg': colored('A new versions is generating...')   
                }
                self.app.render(msg ,'msg.jinja2')
            elif r.status_code == 401:
                auth_error(self.app)
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
        token = self.app.config.get('rogue','token')
        try:

            # TODO: VALIDAR ANTES DE PUBLICAR
            arguments = self.app.pargs
            body = {
                        "extension": arguments.extension,
                        "override": arguments.force
                }

            r = requests.post(f'{url}/projects/{arguments.name}/{arguments.version}', json=body, headers={'Authorization': f'token {token}'})

            if r.status_code == 200:
                self.app.render({'msg': f'Version {arguments.version} published!'},'msg.jinja2')
            elif r.status_code == 401:
                auth_error(self.app)
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
            token = self.app.config.get('rogue','token')
            arguments = self.app.pargs
            body = {
                "validateAudios": arguments.audios
            }

            r = requests.post(f'{url}/projects/{arguments.name}/validate', json=body, headers={'Authorization': f'token {token}'})
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
                        cell = f'[{s["cell"]}]' if 'cell' in s else ''
                        if s['type'] == 'error':
                            errors += 1
                            state['status'] = colored('NOK', 'red')
                            pre_txt = colored(f'[Error]{cell} ','red')
                        else:
                            warnings += 1
                            pre_txt = colored(f'[Warning]{cell} ','yellow')

                        state['messages'].append(f"{pre_txt}{s['message']}")
                    
                    for p in result[r]['prompts']:
                        cell = f'[{p["cell"]}]' if 'cell' in p else ''
                        if p['type'] == 'error':
                            errors += 1
                            state['status'] = colored('NOK', 'red')
                            pre_txt = colored(f'[Error]{cell} ','red')
                        else:
                            warnings +=1
                            pre_txt = colored(f'[Warning]{cell} ','yellow')

                        state['messages'].append(f"{pre_txt}{p['message']}")

                    for t in result[r]['transitions']:
                        cell = f'[{t["cell"]}]' if 'cell' in t else ''
                        if t['type'] == 'error':
                            errors += 1
                            state['status'] = colored('NOK', 'red')
                            pre_txt = colored(f'[Error]{cell} ','red')
                        else:
                            warnings +=1
                            pre_txt = colored(f'[Warning]{cell} ','yellow')


                        state['messages'].append(f"{pre_txt}{t['message']}{cell}") 

                    obj['states'].append(state)

                obj['errors'] = errors
                obj['warnings'] = warnings
                
                self.app.render(obj,'validate.jinja2')           
            elif r.status_code == 401:
                auth_error(self.app)
            else:
                self.app.render({'msg': colored(r.json(),'red')},'msg.jinja2')
        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')
        except Exception as err:
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
            token = self.app.config.get('rogue','token')
            arguments = self.app.pargs
            r = requests.get(f'{url}/projects/{arguments.name}/schema',headers={'Authorization': f'token {token}'})

            if r.status_code == 200:
                self.app.render({'msg': r.text.replace(r'\n', '\n').replace('"','')},'msg.jinja2')
            elif r.status_code == 401:
                auth_error(self.app)
            else:
                self.app.render({'msg': colored(r.json(),'red')},'msg.jinja2')
        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')
    
    @ex(help='get prompts from project and save as yaml file',
    arguments=[
        (['name'],
        {'help': 'project name'}),
        (['output_path'],
        {'help': 'output path'})
    ]
    )
    def prompts(self):
        try:
            url = self.app.config.get('rogue','url')
            token = self.app.config.get('rogue','token')
            arguments = self.app.pargs
            r = requests.get(f'{url}/projects/{arguments.name}/prompts',headers={'Authorization': f'token {token}'})
           
            if r.status_code == 200:
                file_name = f'{arguments.output_path.rstrip("/")}/{arguments.name}-prompts.yml'

                data = r.json()

                for d in data:
                    data[d] = self.removeDiacritic(data[d])


                f = open(file_name, 'w')
                yaml.dump({'prompts': data}, f, default_flow_style=False)
                f.close()

                self.app.render({'msg': f'File {file_name} created'},'msg.jinja2')
            elif r.status_code == 401:
                auth_error(self.app)
            else:
                self.app.render({'msg': colored(r.json(),'red')},'msg.jinja2')

        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')
        except Exception as err:
            self.app.render({'msg': colored(err,'red')},'msg.jinja2')

    @ex(help='transfer Audios to Behavior-Bot',
    arguments=[
        (['name'],
        {'help': 'project name'})
    ]
    )
    def transfer_audios(self):
        try:
            url = self.app.config.get('rogue','url')
            token = self.app.config.get('rogue','token')
            arguments = self.app.pargs

            r = requests.post(f'{url}/projects/{arguments.name}/transfer',headers={'Authorization': f'token {token}'})
           
            if r.status_code == 200:
                self.app.render({'msg': f'Transfered'},'msg.jinja2')
            elif r.status_code == 401:
                auth_error(self.app)
            else:
                self.app.render({'msg': colored(r.json(),'red')},'msg.jinja2')

        except requests.exceptions.ConnectionError as err:
            self.app.render({'msg': colored('Erro api','red')},'msg.jinja2')
        except Exception as err:
            self.app.render({'msg': colored(err,'red')},'msg.jinja2')




    def removeDiacritic(self,text):
        return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode("utf-8")
     
        


    