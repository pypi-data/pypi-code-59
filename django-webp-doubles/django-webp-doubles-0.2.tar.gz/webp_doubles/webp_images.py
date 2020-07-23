from django.db.models.signals import post_save
from django.core.files.storage import default_storage
from django.conf import settings
from django.db.models import Model

from PIL import Image
from io import BytesIO


FILER_IS_ENABLED = 'filer' in settings.INSTALLED_APPS


def get_double_filename(filename):
    if filename.endswith('webp'):
        return filename[:-4] + 'jpg', 'JPEG'
    if filename.endswith('jpg') or filename.endswith('png'):
        return filename[:-3] + 'webp', 'WEBP'
    return None, None


def create_double(image):
    try:
        file = image.file
        filename = file.name
        double_filename, goal_extension = get_double_filename(filename)
        if double_filename and goal_extension and not default_storage.exists(double_filename):
            pillow_image = Image.open(file)
            if goal_extension == 'JPEG' and pillow_image.mode == 'RGBA':
                goal_extension = 'PNG'
            new_image = BytesIO()
            pillow_image.save(new_image, goal_extension)
            path = default_storage.save(double_filename, new_image)
            print(f'created file {path}...')
    except FileNotFoundError:
        print('FileNotFoundError')


def convert_images(*args, **kwargs):
    instance = kwargs.get('instance')
    sender = kwargs.get('sender')
    if sender and instance:
        model_name = f'{sender._meta.app_label}.{sender._meta.object_name}'
        fields = settings.MODELS_WITH_IMAGES_FOR_WEBP.get(model_name)
        for field in fields:
            image = getattr(instance, field, None)
            if image:
                if FILER_IS_ENABLED and isinstance(image, Model):
                    image.save()
                else:
                    create_double(image)


def convert_filer_images(*args, **kwargs):
    instance = kwargs.get('instance')
    if instance and instance.file:
        create_double(instance.file)


def connect_signals():
    # connect local models
    for model_name, fields in settings.MODELS_WITH_IMAGES_FOR_WEBP.items():
        post_save.connect(convert_images, sender=model_name)

    # connect filer model
    if FILER_IS_ENABLED:
        post_save.connect(convert_filer_images, sender=settings.FILER_IMAGE_MODEL)
