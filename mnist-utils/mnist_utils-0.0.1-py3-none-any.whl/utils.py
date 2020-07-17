# Useful methods for dealing with MNIST data or Image data
import numpy as np
import os, os.path, gzip
from PIL import Image
import matplotlib.pyplot as plt


def images2np(image_dir: str, image_size: int) -> np.array:
    """
    Given a directory of images (currently only accept PNGs), returns a
    numpy array of feature vectors.
    """
    features_data = np.empty((0, image_size, image_size, 1))

    list_of_files = os.listdir(image_dir)
    for image_file in list_of_files:
        full_img_path = os.path.join(image_dir, image_file)
        image_vector = image2np(full_img_path, image_size)
        if image_vector is not None:
            features_data = np.append(features_data, image_vector, axis=0)
        else:
            exit(1)

    return features_data



def label2np(label_file: str, separator) -> np.array:
    """
    Assumes the labels provided are separated by the provided separator.
    Parses the labels_file and returns an numpy array of labels in the order
    they appear in the file.
    """
    with open(label_file, "r") as lf:
        lines = lf.read()
        lines = lines.split(sep=separator)
        label_data = np.array(lines)

        return label_data

    return np.array()



def image2np(img_file: str, image_size: int) -> np.array:
    """
    Given a single image file, returns an MNIST representation of it (provided it's a PNG).
    
    (Converts each image to gray scale)
    """
    if img_file.endswith(".png"):
        image = Image.open(img_file).convert("L")
        image = np.resize(image, (image_size, image_size, 1))

        image = np.array(image)
        image = image.reshape(1, image_size, image_size, 1)
        return image

    return None



def ubytes2np(img_folder, number_to_process, image_size) -> np.array:
    """
    Given an MNIST ubyte ".gz" file, the number of images to process (can be less than 
    the number ofimages in the file), and their size, returns a numpy array with features
    for each image.
    """
    images = np.empty((image_size, image_size, 1))

    f = gzip.open(img_folder,'r')

    f.read(16)
    buf = f.read(image_size * image_size * number_to_process)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    data = data.reshape(number_to_process, image_size, image_size, 1)

    return data



def ubytes2png(img_folder, number_to_process, image_size, dest_folder) -> np.array:
    """
    Given an MNIST ubyte ".gz" file, the number of images to process (can be less than 
    the number ofimages in the file), and their size, saves the image binaries as PNG files 
    in the destination folder.
    """
    data = ubytes2np(img_folder, number_to_process, image_size)

    for i, image in enumerate(data):
        image = image.squeeze()
        plt.imshow(image)
        plt.savefig(os.path.join(dest_folder, str(i) + ".png"))