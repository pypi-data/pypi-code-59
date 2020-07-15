from PIL import Image


class ImageResizer(object):
    image: Image

    def __init__(self, image):
        self.image = image

    def resize(self):
        image_to_open = Image.open(self.image)
        # image_to_open.thumbnail((550, 303), Image.ANTIALIAS)
        image_to_open.transform((550, 303))
