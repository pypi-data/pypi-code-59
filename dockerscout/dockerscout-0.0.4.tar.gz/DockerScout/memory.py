"""
Remember when we last saw each docker image
"""
import os
import json
import time
from .config import config_dir, HISTORY_FILE


def read_images():
    """
    Read the image history
    :return:
    """
    histfile = os.path.join(config_dir(), HISTORY_FILE)
    if os.path.exists(histfile):
        with open(histfile, "r") as cfg:
            return json.load(cfg)
    return {}


def save_images(images):
    """
    Save the image history
    :return:
    """
    if not os.path.exists(config_dir()):
        os.makedirs(config_dir())

    histfile = os.path.join(config_dir(), HISTORY_FILE)

    with open(histfile, "w") as cfg:
        json.dump(images, cfg, indent=2)


def notice(image):
    """
    Remember that we just saw an image
    :param image:
    :return:
    """
    now = time.time()

    images = read_images()
    images[image] = now
    save_images(images)


def forget(image):
    """
    Forget history of an image
    :param image:
    :return:
    """
    images = read_images()
    if image in images:
        del images[image]
    save_images(images)
