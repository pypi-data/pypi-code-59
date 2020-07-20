from pprint import pprint
from pathlib import Path
import os
import sys
from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Automatically builds DRF APIs for every locally installed model'

    def handle(self, *args, **kwargs):
        settings = sys.modules[os.environ['DJANGO_SETTINGS_MODULE']]
        urls = sys.modules[settings.ROOT_URLCONF]

        print('running autogenapis')
        app_list = list(apps.get_app_configs())
        for app in app_list:
            if app.path.startswith(settings.BASE_DIR):
                models = app.__dict__.get('models', None)
                views = os.path.join(app.path, 'views.py')
                Path(views).touch()
                insert_string = """from rest_framework import serializers, viewsets\n"""
                insert_string += """from rest_framework.permissions import IsAuthenticated\n"""
                for model in models:
                    short_name = model
                    module_path = models[model].__dict__['__module__']
                    model_name, model_attributes = models[model].__dict__['__doc__'][:-1].split('(')
                    model_attributes = model_attributes.split(', ')  # use this later
                    insert_string += f"from {module_path} import {model_name}\n\n"
                    insert_string += f"""
class {model_name}Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = {model_name}
        fields = {str(model_attributes)}
\n"""
                    insert_string += f"""
class {model_name}ViewSet(viewsets.ModelViewSet):
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}Serializer
\n\n"""
                    with open(views, 'w') as fn:
                        fn.write(insert_string)
                assert False, "UNDER CONSTRUCTION; need to add routers"
