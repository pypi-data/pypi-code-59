import os
import sys
import cv2
import uuid
import argparse
from typing import Optional
from imdix.utils import Image
from imdix.utils import compare
from imdix.utils import image_resize
from imdix.utils import GENERIC_IMAGE

def search(image: Image, target_size: int, output: Optional[str] = None, ext: Optional[str] = None):
    """
    Function to perform search to find dimensions for target image file size
    parameters : <image>       : Image object containing source image
                 <target_size> : Target size for reducing image size to
    returns    : <boolean>     : Whether the task can be done
                 <image size>  : size of new image
                 <image name>  : name of new image file 
    """
    high = image
    low = GENERIC_IMAGE
    prev_image = None

    while compare(high, low):
        if prev_image:
            os.remove(prev_image)
        middle_h = (high.height + low.height)//2
        middle_w = (high.width + low.width)//2
        
        new_image = image_resize(image.image, height=middle_h)
        new_image_name = str(uuid.uuid4()) + '.jpeg'
        cv2.imwrite(new_image_name, new_image)
        del new_image

        size_of_new_image = os.stat(new_image_name).st_size // 1024
        
        if abs(size_of_new_image - target_size) <= 2:
            final_name = image.path.split('.')[0] + str(size_of_new_image)
            if output:
                final_name = output + '.' + image.path.split('.')[-1]
            elif ext:
                final_name = final_name + '.' + ext
            elif output and ext:
                final_name = output + '.' + ext
            else:
                final_name = final_name + f'_{size_of_new_image}.jpeg'
            os.rename(new_image_name, final_name)
            return True, size_of_new_image, final_name
        elif size_of_new_image < target_size:
            low = Image(new_image_name)
        elif size_of_new_image > target_size:
            high = Image(new_image_name)
        prev_image = new_image_name

def main():
    args = argparse.ArgumentParser(description="Dynamic image file resizer")
    args.add_argument('--image', '-i', help="Path to image file", required=True)
    args.add_argument('--size', '-s', help="Target output size", required=True)
    args.add_argument('--output', '-o', help="Output file name")
    args.add_argument('--ext', '-x', help="Extension of output file")
    res = args.parse_args()

    # create new image
    image = Image(res.image)
    target = res.size
    output = res.output
    ext = res.ext

    file_size = int(os.stat(image.path).st_size) // 1024
    if file_size >= int(target):
        done, size, name = search(image, int(target), output, ext)
        if done:
            print('[INFO] Resize complete...')
            print(f'[INFO] Filename: {name}, Size: {size}')
        else:
            print(f'[ERROR] Error resizing file')
    else:
        print(f"[ERROR] Target size({target} KB) greater than file size({file_size} KB)")