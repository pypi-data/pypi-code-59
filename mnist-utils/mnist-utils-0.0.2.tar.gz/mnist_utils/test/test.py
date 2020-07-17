from tensorflow import keras
import numpy as np
import os, os.path, shutil

import mnist_utils as mu

def test_ubytes_to_np():
    """
    Tests that reading the test data from the file and converting it to NP array yields the same
    array as the test data from fashion mnist
    """
    test_images_from_tf = load_test_data_from_tf()
    test_images_from_gz = mu.ubytes2np("assets/t10k-images-idx3-ubyte.gz", 10000, 28)

    assert test_images_from_tf[0].shape == test_images_from_gz[0].squeeze().shape
    assert test_images_from_tf.shape == test_images_from_gz.squeeze().shape
    assert test_images_from_tf.all() == test_images_from_gz.squeeze().all()


def test_ubytes_to_png():
    """
    Tests that 10 images are created - ww can verify the images to ensure the loading is being done correctly.
    """
    test_dir = "trial"
    create_test_dir(test_dir)

    num_files = 10
    mu.ubytes2png("assets/t10k-images-idx3-ubyte.gz", num_files, 28, test_dir)
    assert len(os.listdir(test_dir)) == num_files


def test_images_to_np():
    """
    Creates 100 images from the gz file -> Converts those images to np arrays -> Check whether the result is
    the same as the test data from the fashion mnist set from tensorflow
    """
    test_dir = "trial"
    create_test_dir(test_dir)
    mu.ubytes2png("assets/t10k-images-idx3-ubyte.gz", 100, 28, test_dir)
    
    test_images_from_tf = load_test_data_from_tf()[:100]
    test_data_from_images = mu.images2np(test_dir, 28)

    assert test_images_from_tf[0].shape == test_data_from_images[0].squeeze().shape
    assert test_images_from_tf.shape == test_data_from_images.squeeze().shape

    res = True
    for row in test_data_from_images:
        if not (test_data_from_images == row).all(1).any():
            res = False
            break
    assert res
    

def create_test_dir(test_dir):
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)



def load_test_data_from_tf():
    """
    Use the TF Keras data set and load the test data
    """
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    return test_images