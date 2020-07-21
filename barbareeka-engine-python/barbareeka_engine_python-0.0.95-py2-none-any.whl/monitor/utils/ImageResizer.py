import base64
import io

from PIL import Image


class ImageResizer(object):
    image = Image

    def __init__(self, image):
        self.image = image

    def resize(self):
        with open(self.image, "rb") as imageFile:
            return base64.b64encode(imageFile.read())

    def resize3(self):
        pil_im = self.image.fromarray(self.image)
        b = io.BytesIO()
        pil_im.save(b, 'jpeg')
        im_bytes = b.getvalue()
        return im_bytes
        # image_to_open = Image.open(self.image)
        # image_to_open.thumbnail((550, 303), Image.ANTIALIAS)
        # image_to_open.transform((550, 303))

    def resize1(self):
        with open(self.image, "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)
            return b
