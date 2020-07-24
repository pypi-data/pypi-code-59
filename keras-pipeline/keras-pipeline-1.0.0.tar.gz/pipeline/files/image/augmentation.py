from typing import *

import numpy as np

from keras.preprocessing.image import ImageDataGenerator

from . import loader

class ImageAugmentation:
  '''
  Interface of ImageDataGenerator.

  Args:
    kwargs: Parameters to initialize the ImageDataGenerator object.
      More info: keras.preprocessing.image.ImageDataGenerator.__init__().
      It must not include validation_split.

  Raises:
    ValueError
      If validation_split is included.
  '''

  def __init__(self, **kwargs) -> None:
    if 'validation_split' in kwargs:
      raise ValueError('The parameter validation_split must not be included.')

    self.image_generator = ImageDataGenerator(**kwargs)

  def _must_fit(self) -> bool:
    '''
    Returns:
      A boolean to know whether it should fit images.
    '''

    return self.image_generator.featurewise_center\
      or self.image_generator.featurewise_std_normalization\
      or self.image_generator.zca_whitening

  def fit(self, images: np.ndarray, **kwargs) -> None:
    '''
    Interface of the fit function (which is not needed to be called everytime).
    If parameters that require us to fit the ImageDataGenerator are set,
      it fits given images.

    Args:
      images: 4D Numpy array of images of shape
        (batch, height, width, channels).
    '''

    if self._must_fit():
      self.image_generator.fit(images, **kwargs)

  def transform(
    self,
    image: np.ndarray,
    seed: Optional[int] = None,
  ) -> np.ndarray:
    '''
    Randomly augment the given image.

    Args:
      image: 3D Numpy array of shape (height, width, channels).
      seed: For replicability.

    Returns:
      The augmented image.
    '''

    image = self.image_generator.random_transform(image, seed)
    image = self.image_generator.standardize(image)
    
    return image