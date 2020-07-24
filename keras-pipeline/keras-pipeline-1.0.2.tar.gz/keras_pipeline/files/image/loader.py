from typing import *

import os
import matplotlib.pyplot as plt
import numpy as np

from keras.preprocessing.image import load_img, save_img, img_to_array

from .augmentation import ImageAugmentation
from .preprocess import ImagePreprocessing
from ...utils.batch import BatchLoopIterator
from ...utils.histogram import Histogram
from ..manager import FilesManager
   
class ImageLoader:
  '''
  Interface of ImageDataGenerator's flow* methods.
  Load images in memory with preprocessing, augmentation, ...

  Args:
    files_manager: Contains images' paths and labels.
    batch_size: Number of images simultaneously in memory.
    shuffle: Whether to shuffle paths and labels.
    seed: For replicability.
  '''

  def __init__(
    self,
    files_manager: FilesManager,
    batch_size: Optional[int] = None,
    shuffle: bool = True,
    seed: Optional[int] = None,
  ) -> None:
    self.batch_iterator = BatchLoopIterator(
      list(zip(*files_manager.get())),
      batch_size,
      shuffle,
      seed,
    )

    self.load_kwargs = {}
    self.preprocessing = None
    self.fit_kwargs = {}
    self.augmentation = None

  def set_augmentation(self, augmentation: ImageAugmentation) -> None:
    self.augmentation = augmentation

  def set_load_kwargs(self, **kwargs) -> None:
    # kwargs are defined here: keras.preprocessing.image.load_img
    self.load_kwargs = kwargs

  def set_preprocessing(self, preprocessing: ImagePreprocessing) -> None:
    self.preprocessing = preprocessing

  def set_fit_kwargs(self, **kwargs) -> None:
    # kwargs are defined here: keras.preprocessing.image.ImageDataGenerator.fit
    self.fit_kwargs = kwargs

  def reset(self) -> 'ImageLoader':
    self.batch_iterator.reset()
    return self

  def labels(self) -> np.ndarray:
    return np.array(list(zip(*self.batch_iterator.data))[1])

  def __len__(self) -> int:
    '''
    Returns:
      The number of batches in one epoch.
    '''

    return len(self.batch_iterator)

  def __iter__(self):
    return self

  def __next__(self) -> Tuple[np.ndarray, np.ndarray]:
    '''
    Load, preprocess, fit (if necessary) and augment images in a single batch.

    Returns:
      Loaded images as X_batch
      Labels as y_batch
    '''

    # Get paths and labels
    X_batch, y_batch = zip(*next(self.batch_iterator))

    # Load, preprocess, fit (if nacessary) and augment a batch of images.
    images = self.load_many(X_batch, **self.load_kwargs)
    images = self.preprocess_many(images, self.preprocessing)
    self.fit_many(images, self.augmentation, **self.fit_kwargs)
    images = self.augment_many(images, self.augmentation, seed=None)

    return images, np.array(y_batch)

    ''' TODO
    flow(
      sample_weight=None,
      save_to_dir=None,
      save_prefix='',
      save_format='png',
    )
    '''

  def plot_augmentation(
    self,
    filename_image: str,
    nb_rows: int = 4,
    nb_cols: int = 4,
    figsize: Tuple[int, int] = (18,18),
    seed: Optional[int] = None,
  ) -> None:
    '''
    Shows the preprocessing and augmentation that are performed on images
      during training/evaluation/testing in the form of a table.

    Args:
      filename_image: Test image.
      nb_rows: Number of rows in the table.
      nb_cols: Number of columns in the table.
        Resulting in (nb_rows * nb_cols) shown images.
      figsize: Dimensions of the images.
      seed: For replicability in augmentation.

    Raises:
      ValueError
        If filename_image doesn't exist.
    '''

    if not os.path.exists(filename_image):
      raise ValueError(f'File {filename_image} doesn\'t exists')

    # Load, preprocess, fit (if nacessary) and augment a single image.
    image = self.load_one(filename_image, **self.load_kwargs)
    image = self.preprocess_one(image, self.preprocessing)
    self.fit_many(np.array([image]), self.augmentation, **self.fit_kwargs)
    generator = (img for img in self.augment_many(
      [image for _ in range(nb_rows * nb_cols)],
      self.augmentation,
      seed=seed,
    ))
    
    fig, rows = plt.subplots(nrows=nb_rows, ncols=nb_cols, figsize=figsize)
    for col in rows:
      for row in col:
        row.imshow(next(generator))
        row.axis('off')
    plt.show()

  @staticmethod
  def load_one(filename: str, **kwargs) -> np.ndarray:
    '''
    Load one image using Keras' interface of Pillow's image loading.

    Args:
      filename: Path to the image.
      kwargs: keras.preprocessing.image.load_img.

    Returns:
      The image in the form of a Numpy array.
    '''

    # Load Pillow image from filename
    image_PIL = load_img(filename, **kwargs)

    # Convert Pillow image to 3D array (height, width, channels)
    image = img_to_array(image_PIL)

    # Close Pillow image
    image_PIL.close()

    return image

  @staticmethod
  def load_many(filenames: Iterable[str], **kwargs) -> np.ndarray:
    return np.array([ImageLoader.load_one(f, **kwargs) for f in filenames])

  @staticmethod
  def preprocess_one(
    image: np.ndarray,
    image_preprocessing: ImagePreprocessing,
  ) -> np.ndarray:
    return image_preprocessing.preprocess(image)

  @staticmethod
  def preprocess_many(
    images: Iterable[np.ndarray],
    image_preprocessing: ImagePreprocessing,
  ) -> np.ndarray:
    return np.array([
      ImageLoader.preprocess_one(image, image_preprocessing)
      for image in images
    ])

  @staticmethod
  def fit_many(
    images: np.ndarray,
    augmentation: ImageAugmentation,
    **kwargs
  ) -> None:
    augmentation.fit(images, **kwargs)

  @staticmethod
  def augment_one(
    image: np.ndarray,
    augmentation: ImageAugmentation,
    seed: Optional[int] = None,
  ) -> np.ndarray:
    return augmentation.transform(image, seed)

  @staticmethod
  def augment_many(
    images: Sequence[np.ndarray],
    augmentation: ImageAugmentation,
    seed: Optional[int] = None,
  ) -> np.ndarray:
    # Generate a list of seeds if a seed is given.
    seeds = np.random.RandomState(seed).random_integers(
      2**32,
      size=len(images),
    ) if seed else [None] * len(images)

    return np.array([
      ImageLoader.augment_one(image, augmentation, seed)
      for image, seed in zip(images, seeds)
    ])

  @staticmethod
  def save_one(
    image: np.ndarray,
    filename: str,
    **kwargs
  ) -> None:
    '''
    Save one image using Keras' interface of Pillow's image saving.

    Args:
      image: A loaded image.
      filename: Path to the image to create.
      kwargs: Pillow's PIL.Image.save one.
    '''

    # Force: 
    #   * Channels to be the last dimension ;
    #   * Format to be guessed from filename ;
    #   * Values to already be within [0, 255].
    save_img(
      filename,
      image,
      data_format='channels_last',
      file_format=None,
      scale=False,
      **kwargs,
    )

  @staticmethod
  def save_many(
    images: np.ndarray,
    filenames: Iterable[str],
    **kwargs
  ) -> None:
    for image, filename in zip(images, filenames):
      ImageLoader.save_one(image, filename, **kwargs)
