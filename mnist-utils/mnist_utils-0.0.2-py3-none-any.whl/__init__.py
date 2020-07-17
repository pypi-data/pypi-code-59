# Useful methods for dealing with MNIST data or Image data
import mnist_utils.utils

def images2np(image_dir: str, image_size: int):
    """
    Given a directory of images (currently only accept PNGs), returns a
    numpy array of feature vectors.
    """
    return utils.images2np(image_dir, image_size)



def label2np(label_file: str, separator):
    """
    Assumes the labels provided are separated by the provided separator.
    Parses the labels_file and returns an numpy array of labels in the order
    they appear in the file.
    """
    return utils.label2np(label_file, separator)



def image2np(img_file: str, image_size: int):
    """
    Given a single image file, returns an MNIST representation of it (provided it's a PNG).
    
    (Converts each image to gray scale)
    """
    return utils.image2np(img_file, image_size)



def ubytes2np(img_folder, number_to_process, image_size):
    """
    Given an MNIST ubyte ".gz" file, the number of images to process (can be less than 
    the number ofimages in the file), and their size, returns a numpy array with features
    for each image.
    """
    return utils.ubytes2np(img_folder, number_to_process, image_size)



def ubytes2png(img_folder, number_to_process, image_size, dest_folder):
    """
    Given an MNIST ubyte ".gz" file, the number of images to process (can be less than 
    the number ofimages in the file), and their size, saves the image binaries as PNG files 
    in the destination folder.
    """
    return utils.ubytes2png(img_folder, number_to_process, image_size, dest_folder)