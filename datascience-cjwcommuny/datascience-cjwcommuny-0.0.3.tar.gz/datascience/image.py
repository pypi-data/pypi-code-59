import base64
from io import BytesIO

from PIL.Image import Image


def image2base64(image: Image, color_format: str='RGB', store_format: str= 'JPEG', quality: int=100) -> str:
    image = image.convert(color_format)
    b64code = BytesIO()
    image.save(b64code, store_format, quality=quality)
    return base64.urlsafe_b64encode(b64code.getvalue())

