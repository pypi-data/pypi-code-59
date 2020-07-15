import urwid
import os
from os.path import join
import operator
import shutil
import yaml
import git
import threading
import datetime
import re

from .components import TextButton, EditDisplay, LineWalker, SimpleForm
from .config import CONFIG_PATH, HOME
from .messages import backup_sucess, doing_backup, welcome_url, welcome, git_explication

class GitModel:
    def __init__(self, docs_path):
        self.docs_path = docs_path

    def exists(self):
        git_path = os.path.join(self.docs_path, '.git')
        return os.path.exists(git_path)

    def init_and_pull(self, git_repo_url):
        repo = git.Repo.init(self.docs_path)
        origin = repo.create_remote('origin', git_repo_url)
        origin.fetch()
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout()

    def bkp(self):
        x = datetime.datetime.now()
        COMMIT_MESSAGE = 'BKP: %s' % x.strftime("%x %X")
        repo = git.Repo(self.docs_path)
        repo.git.add('.')
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()


class FileModel:
    opened = False

    def __init__(self, name, base_path):
        self.base_path = base_path
        self.name = name

    @property
    def path(self):
        return os.path.join(self.base_path, self.name)

    def icon(self, open=False):
        if self.is_file():
            return ''
        return u'\u25BC ' if open else u'\u25B6 '

    def is_file(self):
        return os.path.isfile(self.path)


class BrowserModel:
    label = 'Browse'
    regex_ignored_names = '.git'

    def get_options(self, docs_path, opened_folders=[], file_selected=None, *args, **kwargs):
        def _get_options(root_path, depth=0):
            options = []
            spaces =  depth * '  '
            try:
                files_names = os.listdir(root_path)
            except FileNotFoundError:
                os.makedirs(root_path)
                files_names = []
            for name in files_names:
                if re.search(self.regex_ignored_names, name):
                    continue

                f = FileModel(name, root_path)
                is_file = f.is_file()
                action = ('open_folder', f) if not is_file else ('open', f.path)

                options.append({
                    'name': f.name,
                    'action': action,
                    'icon': spaces + f.icon(f.path in opened_folders),
                    'is_file': is_file,
                    'childs': _get_options(f.path + '/', depth + 1) if f.path in opened_folders else [],
                    'path': f.path
                })
            options.sort(key=operator.itemgetter('is_file', 'name'))

            # Flat options
            flattened_options = []
            for idx, o in enumerate(options):
                if not o['is_file'] and file_selected == o['path']:
                    on = [
                        (o, 3.5),
                        ({
                            'name': u'- \N{wastebasket}',
                            'action': ('remove_folder', o['path']),
                            'icon': '',
                        }, 1),
                        ({
                            'name': u'+ \U0001F5C1',
                            'action': ('create_folder', o['path']),
                            'icon': '',
                        }, 1),
                        ({
                            'name': u' + \U0001F5CE',
                            'action': ('create', o['path']),
                            'icon': '',
                        }, 1),
                    ]
                else:
                    on = o

                flattened_options.append(on)
                if o.get('childs'):
                    flattened_options.extend(o['childs'])

            # Add actions
            if root_path == docs_path:
                actions = [
                    ({
                        'name': u'\U0001F5C1  Add Folder +',
                        'action': ('create_folder', root_path),
                        'icon': '',
                    }, 1),
                    ({
                        'name': u'\U0001F5CE Add File +',
                        'action': ('create', root_path),
                        'icon': '',
                    }, 1)
                ]
                flattened_options.append(actions)

            return flattened_options

        return _get_options(docs_path)


class ConfigModel:
    PATH = CONFIG_PATH
    label = 'Config'
    _data = {}

    def __init__(self):
        if not os.path.exists(self.PATH):
            with open(self.PATH, 'w'): pass

    def get_options(self, *args, **kwargs):
        return [
            # {
            #     'name': 'Set configs',
            #     'action': ('set_config', None),
            #     'icon': ' 1. '
            # },
            {
                'name': 'Backup',
                'action': ('backup', None),
                'icon': ' 1. '
            },
        ]

    @property
    def data(self):
        if not self._data:
            with open(self.PATH) as f:
                self._data = yaml.load(f, Loader=yaml.FullLoader) or {}
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        with open(self.PATH, 'w') as f:
            yaml.dump(self.data, f)

    def set_key(self, key, value):
        self._data[key] = value
        self.data = self.data


class MenuModel:
    BROWSE = 'browse'
    CONFIG = 'config'

    MODELS = {
        BROWSE: BrowserModel(),
        CONFIG: ConfigModel()
    }

    choice_selected = BROWSE

    def get_choices(self):
        return  [(model.label, choice) for choice, model in self.MODELS.items()]

    def set_choice(self, choice):
        self.choice_selected = choice

    def get_menu_body_choices(self, *args, **kwargs):
        return self.MODELS[self.choice_selected].get_options(*args, **kwargs)

    def body_menu_choice_selected(self, selected):
        return selected[0](selected[1])


class MainView(urwid.WidgetWrap):
    palette = [
            ('bg', 'dark red', 'dark red', 'dark red', 'light gray', 'g11'),
            ('selected', 'dark red', 'dark red', 'dark red', 'light gray', 'g11'),
        ]

    def __init__(self, controller):
        self.controller = controller
        self.vline = urwid.AttrWrap( urwid.SolidFill(u'\u2502'), 'line')
        self.editor = EditDisplay(welcome_url)
        self.editor_view = self.editor.view
        urwid.WidgetWrap.__init__(self, self.main_window())

    def get_menu(self):
        choices = self.controller.get_menu_choices()

        cells = []
        for choice in choices:
            item = TextButton(self.controller.on_selected_menu_choice, *choice)
            if not choice == choices[0]:
                item = urwid.LineBox(item, tline=None, lline='│', rline=None, bline=None)
            cells.append(item)

        return  urwid.Columns(cells)

    def get_body_menu_items(self):
        choices = self.controller.get_body_menu()
        menu_items = []
        for choice in choices:
            if isinstance(choice, list):
                cells = [
                    ('weight', weight, TextButton(
                        self.controller.on_selected_body_menu_choice,
                        caption=sub_choice['name'],
                        user_data=sub_choice['action'],
                        icon=sub_choice['icon']
                    )) for sub_choice, weight in choice
                ]
                menu_items.append(urwid.Columns(cells))
            else:
                menu_items.append(
                    TextButton(
                        self.controller.on_selected_body_menu_choice,
                        caption=choice['name'],
                        user_data=choice['action'],
                        icon=choice['icon']
                    )
                )
        return menu_items

    def get_body_menu(self):
        return urwid.Pile(self.get_body_menu_items())

    def update_menu(self):
        choices = self.get_body_menu_items()
        self.body_menu.contents = [(item, (urwid.widget.WEIGHT, 1) ) for item in choices]

    def get_aside(self):
        menu = self.get_menu()
        self.body_menu = self.get_body_menu()

        aside = urwid.ListBox(urwid.SimpleListWalker([
            urwid.Divider(div_char=' '),
            menu,
            urwid.Divider(div_char='_'),
            urwid.Divider(div_char=' '),
            self.body_menu
        ]))
        aside = urwid.Padding(aside, left=2, right=1)
        return aside

    def get_body(self):
        self.main_view = urwid.Frame(self.overlay(urwid.Text(welcome, align='center')))
        return self.main_view

    def main_window(self):
        self.body = self.get_body()
        vline = urwid.AttrWrap( urwid.SolidFill(u'\u2502'), 'line')
        aside = self.get_aside()

        main = urwid.Columns([
            ('weight',4,self.body),
            ('fixed',1,self.vline),
            aside
        ])
        w = urwid.AttrMap(main, 'bg')
        w = urwid.AttrWrap(w,'body')
        return w

    def get_create_pop_up(self, response):
        return SimpleForm(u"ingrese el nombre el archivo:\n", response=response)

    def get_create_folder_pop_up(self, response):
        return SimpleForm(u"ingrese el nombre de la carpeta:\n", response=response)

    def get_remove_folder_pop_up(self, response, folder_name):
        return SimpleForm('Para eliminar la carpeta escriba **{}**:\n'.format(folder_name), response=response)

    def get_git_origin_url(self, response):
        return SimpleForm(git_explication, response=response)

    def simple_message(self, message):
        self.show_pop_up(urwid.Text(message, align='center'))

    def overlay(self, widget):
        return urwid.Overlay(urwid.LineBox(urwid.Filler(widget)), urwid.SolidFill(' '),
            align='center', width=('relative', 60),
            valign='middle', height=('relative', 60),
            min_width=20, min_height=9)

    def show_pop_up(self, widget):
        top = self.overlay(widget)
        self.main_view.set_body(top)


class ConfigView(urwid.WidgetWrap):
    palette = [
        ('bg', 'dark red', 'dark red', 'dark red', 'light gray', 'g11'),
    ]

    def __init__(self, controller, response):
        self.controller = controller
        self.response = response
        urwid.WidgetWrap.__init__(self, self.main_window())

    def main_window(self):
        self.body = self.get_body()
        vline = urwid.AttrWrap( urwid.SolidFill(u'\u2502'), 'line')

        main = urwid.Columns([
            ('weight',4,self.body),
        ])
        w = urwid.AttrMap(main, 'bg')
        w = urwid.AttrWrap(w,'body')
        return w

    def get_body(self):
        r = self.response
        class Form(urwid.Edit):
            def __init__(self, *args, **kw):
                super(Form, self).__init__(*args, **kw)
                self.edit_text = os.path.join(HOME, 'ayuda-docs')

            def keypress(self, size, key):
                if key != 'enter':
                    return super(Form, self).keypress(size, key)
                r(self.edit_text)

        return self.overlay(Form('Ingrese la carpeta raiz **default**:\n', align='center'))

    def overlay(self, widget):
        return urwid.Overlay(urwid.LineBox(urwid.Filler(widget)), urwid.SolidFill(' '),
            align='center', width=('relative', 60),
            valign='middle', height=('relative', 60),
            min_width=20, min_height=9)

    def show_pop_up(self, widget):
        top = self.overlay(widget)
        self.view.main_view.set_body(top)


class MainController:
    """
    A class responsible for setting up the model and view and running
    the application.
    """
    handle_editor_keys = False
    opened_folders = []
    file_selected = None

    def __init__(self):
        self.menu_model = MenuModel()
        self.config_model = self.menu_model.MODELS[MenuModel.CONFIG]
        self.init_app()

    def init_app(self):
        if not self.config_model.data:
            self.view = ConfigView(self, self.set_docs_path)
            return
        self.handle_editor_keys = True
        self.view = MainView(self)

    def get_menu_choices(self):
        return self.menu_model.get_choices()

    def get_body_menu(self):
        return self.menu_model.get_menu_body_choices(
            docs_path=self.config_model.data['docs_path'],
            opened_folders=self.opened_folders,
            file_selected=self.file_selected
        )

    def on_selected_menu_choice(self, button, choice):
        self.menu_model.set_choice(choice)
        self.view.update_menu()

    def on_selected_body_menu_choice(self, button, choice):
        action_name, data = choice
        getattr(self, action_name)(data)

    def open(self, path):
        self.file_selected = None
        self.handle_editor_keys = True
        self.view.main_view.set_body(self.view.editor_view)
        self.view.editor.open(path, on_delete=self.on_delete)

    def open_folder(self, file_model):
        self.file_selected = file_model.path
        if file_model.path in self.opened_folders:
            self.opened_folders.remove(file_model.path)
        else:
            self.opened_folders.append(file_model.path)
        self.view.update_menu()

    def create(self, initial_path):
        self.handle_editor_keys = False

        def response(name):
            if name:
                self.open(os.path.join(initial_path, name))
                self.view.update_menu()

        self.view.show_pop_up(self.view.get_create_pop_up(response))

    def create_folder(self, initial_path):
        self.handle_editor_keys = False

        def response(name):
            if name:
                os.mkdir(os.path.join(initial_path, name))
                self.view.simple_message('created')
                self.view.update_menu()

        self.view.show_pop_up(self.view.get_create_folder_pop_up(response))

    def remove_folder(self, initial_path):
        self.handle_editor_keys = False
        if initial_path.endswith(os.path.sep):
            initial_path = initial_path[:-1]

        folder_name = os.path.basename(initial_path)
        def response(name):
            if name == folder_name:
                shutil.rmtree(initial_path)
                self.view.simple_message('deleted')
                self.view.update_menu()
            else:
                self.view.simple_message('Response incorrect')

        self.view.show_pop_up(self.view.get_remove_folder_pop_up(response, folder_name))

    def on_delete(self, *args, **kw):
        self.view.update_menu()

    def set_config(self, data):
        print('TODOOO')

    def backup(self, data):
        docs_path = self.config_model.data['docs_path']
        git_model = GitModel(docs_path)

        def call_bkp(message):
            git_model.bkp()
            self.view.simple_message(message)

        def response(name):
            self.config_model.set_key('git_repo_url', name)
            self.view.simple_message('Trayendo repositorio')

            git_model.init_and_pull(name)
            threading.Thread(target=call_bkp, args=['Repositorio traido y backup realizado!']).start()

        if not git_model.exists() :
            self.view.show_pop_up(self.view.get_git_origin_url(response))
        else:
            self.view.simple_message(doing_backup)
            threading.Thread(target=call_bkp, args=[backup_sucess]).start()

    def set_docs_path(self, name):
        self.config_model.set_key('docs_path', name)
        self.init_app()
        self.main()

    def main(self):
        self.loop = urwid.MainLoop(self.view, self.view.palette, unhandled_input=self.exit_on_q)
        self.loop.screen.set_terminal_properties(colors=256)
        self.loop.run()

    def exit_on_q(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

        if self.handle_editor_keys:
            self.view.editor.unhandled_keypress(key, self.loop)


def main():
    MainController().main()

if __name__== "__main__":
    main()