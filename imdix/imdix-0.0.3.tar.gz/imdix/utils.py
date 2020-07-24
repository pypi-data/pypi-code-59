import os
import cv2
from typing import Optional

class Image:
    """
    Class Image to combine all the properties required to perform image operations
    parameters : <path>      : path to file
                <is_generic> : used to represent NULL image
    returns    : None
    """
    def __init__(self, path: Optional[str] = None, is_generic: bool = False) -> None:
        if not path and not is_generic:
            return "Path required"
        else:
            self.path = path

        if not is_generic:    
            self.image = cv2.imread(self.path)
            self.height, self.width, _ = self.image.shape
            self.size = os.stat(self.path).st_size // 1024 # in KBs
        else:
            self.height = 0
            self.width = 0
            self.size = 0

GENERIC_IMAGE = Image(is_generic=True)

def compare(high: Image, low: Image):
    """
    Function to compare whether the images are equal
    
    parameters : high, low of type Image
    return     : boolean
    """
    if high.height >= low.height and high.width >= low.width:
        return True
    return False

def image_resize(image, width: Optional[int] = None, height: Optional[int] = None, inter = cv2.INTER_AREA):
    """
    Helper function to resize an image
    parameters : <image>  : image to be resized
                 <width>  : width to be resized to 
                 <height> : height to be resized to
                 <inter>  : type of interpolation
    returns    : <image>  : resized image 
    """
    dim = None
    h, w, _ = image.shape
    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized