from django.core.management import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model_path, fields in settings.MODELS_WITH_IMAGES_FOR_WEBP.items():
            print(f'Started processing instances of model {model_path}...')
            app_label, model_name = model_path.split('.')
            model = ContentType.objects.get(app_label=app_label, model=model_name.lower()).model_class()
            for instance in model.objects.all():
                for field in fields:
                    image = getattr(instance, field)
                    if image:
                        print(f'checking images of {instance}...')
                        instance.save()
                        break

        if 'filer' in settings.INSTALLED_APPS:
            print('Started processing instances of Filer Image model...')
            app_label, model_name = settings.FILER_IMAGE_MODEL.split('.')
            model = ContentType.objects.get(app_label=app_label, model=model_name.lower()).model_class()
            for instance in model.objects.filter(file__isnull=False):
                print(f'checking image {instance.file}')
                instance.save()
