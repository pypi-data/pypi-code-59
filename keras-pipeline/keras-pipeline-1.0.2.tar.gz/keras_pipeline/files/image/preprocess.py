from typing import *

import numpy as np

import tensorflow as tf

# For inspiration: https://www.tensorflow.org/api_docs/python/tf/image

class ImagePreprocessing:
  '''
  Transform images.
  Define a pipeline of transformations to apply to images.

  Args:
    functions: List of transformations in sequence. 
  '''

  def __init__(
    self,
    functions: Iterable[Callable[[np.ndarray], np.ndarray]] = [],
  ) -> None:
    self.functions = functions

  def preprocess(self, image: np.ndarray) -> np.ndarray:
    '''
    Apply defined pipeline of transformations to the given image.

    Args:
      image: Numpy array of shape (height, width, channels).
    '''

    for function in self.functions:
      image = function(image)

    return image

  @staticmethod
  def scale_pixels(
    from_range: Union[Tuple[int, int], Tuple[float, float]] = (0, 255),
    to_range: Union[Tuple[int, int], Tuple[float, float]] = (0, 1),
  ) -> Callable[[np.ndarray], np.ndarray]:
    '''
    Create a rescaler of the pixels of the image.

    Args:
      from_range: The original range of pixel values.
      to_range: The targeted range of pixel values.

    Returns:
      The rescaler.
    '''

    # from_range[0] <= image[x] <= from_range[1]
    # => to_range[0] <= scaled_image[x] <= to_range[1]
    return lambda image: to_range[0] + \
      (image - from_range[0]) * \
      (to_range[1] - to_range[0]) / \
      (from_range[1] - from_range[0])

  @staticmethod
  def crop_rect(
    rect: Tuple[int, int, int, int] = (0, 0, 100, 100)
  ) -> Callable[[np.ndarray], np.ndarray]:
    '''
    Create a cropper of image.

    Args:
      rect: Coordinates a the rectangle to retrieve.

    Returns:
      The cropper.
    '''

    return lambda image: image[rect[0]:rect[1], rect[2]:rect[3]]

  @staticmethod
  def crop(
    box: Tuple[int, int] = (100, 100),
    location: Tuple[int, int] = (0, 0),
  ) -> Callable[[np.ndarray], np.ndarray]:
    '''
    Create a cropper of image.

    Args:
      box: Height and width of the rectangle to retrieve.
      location: Top-left corner of the rectangle.

    Returns:
      The cropper.
    '''

    return ImagePreprocessing.crop_rect([
      location[0],
      location[0] + box[0],
      location[1],
      location[1] + box[1],
    ])

  @staticmethod
  def resize_many(
    height: int,
    width: int,
    **kwargs
  ) -> Callable[[np.ndarray], np.ndarray]:
    '''
    Create a resizer.

    Args:
      height: Target height.
      width: Target width,
      kwargs: More info here: tf.image.resize.

    Returns:
      The resizer.
    '''

    return lambda images: tf.image.resize(
      images,
      size=(height, width),
      **kwargs
    ).numpy()

  @staticmethod
  def resize_one(
    height: int,
    width: int,
    **kwargs
  ) -> Callable[[np.ndarray], np.ndarray]:
    return lambda image: ImagePreprocessing.resize_many(
      height,
      width,
      **kwargs
    )(np.array([image]))

  @staticmethod
  def pad_n(
    padding_value: Union[np.ndarray, str],
    n: int,
    location: str,
  ) -> Callable[[np.ndarray], np.ndarray]:
    '''
    Create a padder.

    Args:
      padding_value:
        Numpy array: Pads the zone with this color (ABC -> vv[ABC]vv).
        'last': Copy the first/last row/column (ABC -> AA[ABC]CC).
        'same': Copy the first/last rows/columns (ABCD -> BCD[ABCD]ABC).
        'reverse': Like 'same' but flip rows/columns (ABCD -> CBA[ABCD]DCB).
      n: Number of rows/columns to add.
      location: 'left', 'right', 'top', 'bottom'.

    Returns:
      The padder.
    '''

    def my_padding(image: np.ndarray):
      '''
      Pad the given image.

      Args:
        image: A loaded image as Numpy array.

      Returns:
        The padded image.

      Raises:
        ValueError:
          If, in 'same' or 'reverse' mode, n is higher than the image.
      '''

      if n == 0:
        return image

      # Define the axis to modify.
      # 0 -> height ; 1 -> width.
      axis = 0 if location in ['top', 'bottom'] else 1

      if isinstance(padding_value, np.ndarray):
        # Modify the shape.
        padding_shape = list(image.shape)
        padding_shape[axis] = n

        # Fill with the given value.
        padding = np.full(padding_shape, padding_value)

      else:
        # Number of rows/columns to copy.
        k = 1 if padding_value == 'last' else n

        # TODO: repeat if shape < k.
        if image.shape[axis] < k:
          raise(f'The number of rows/columns to copy can\'t be higher than \
            image.shape[{axis}]. Expected <= {image.shape[axis]}. Got {k}.')

        # Retrieve the rows/columns to copy.
        padding = {
          'left': image[:, :k],
          'right': image[:, -k:],
          'top': image[:k],
          'bottom': image[-k:],
        }[location]

        if padding_value == 'last':
          padding = np.repeat(padding, n, axis=axis)

        elif padding_value == 'reverse':
          padding = np.flip(padding, axis=axis)

      # Define the applying order.
      t = (padding, image) if location in ['left', 'top'] else (image, padding)

      return np.concatenate(t, axis=axis)

    return my_padding

  @staticmethod
  def pad_to_target(
    padding_value: Union[np.ndarray, str],
    target_size: Tuple[int, int],
    horizontal_padding: str,
    vertical_padding: str,
  ) -> Callable[[np.ndarray], np.ndarray]:
    '''
    Create a padder.

    Args:
      padding_value:
        Numpy array: Pads the zone with this color (ABC -> vv[ABC]vv).
        'last': Copy the first/last row/column (ABC -> AA[ABC]CC).
        'same': Copy the first/last rows/columns (ABCD -> BCD[ABCD]ABC).
        'reverse': Like 'same' but flip rows/columns (ABCD -> CBA[ABCD]DCB).
      target_size: (height, width). Must be higher than image shape.
      horizontal_padding: define the horizontal coordinates of the zone to pad.
        'left': ABC -> vvABC.
        'right': ABC -> ABCvv.
        'center': ABC -> vABCv.
      vertical_padding: define the vertical coordinates of the zone to pad.
        'top', 'bottom' or 'center'.

    Returns:
      The padder.
    '''

    def my_padding(image):
      '''
      Pad the given image.

      Args:
        image: A loaded image as Numpy array.

      Returns:
        The padded image.

      Raises:
        ValueError:
          If, in 'same' or 'reverse' mode, n is higher than the image.
          If the given image is bigger than the target size.
      '''

      # Compute the number of rows/columns to add.
      horiz_nb = target_size[1] - image.shape[1]
      vert_nb = target_size[0] - image.shape[0]

      if horiz_nb < 0:
        raise ValueError(f'Expected image.shape[1] < target_size[1].\
          Got {image.shape[1]} >= {target_size[1]}.')
      if vert_nb < 0:
        raise ValueError(f'Expected image.shape[0] < target_size[0].\
          Got {image.shape[0]} >= {target_size[0]}.')

      # Compute the number of left/right columns to add.
      left_nb = horiz_nb if horizontal_padding == 'left' else 0
      right_nb = horiz_nb if horizontal_padding == 'right' else 0
      if horizontal_padding == 'center':
        left_nb, mod = divmod(horiz_nb, 2)
        right_nb = left_nb + mod

      # Compute the number of top/bottom raws to add.
      top_nb = vert_nb if vertical_padding == 'top' else 0
      bottom_nb = vert_nb if vertical_padding == 'bottom' else 0
      if vertical_padding == 'center':
        top_nb, mod = divmod(vert_nb, 2)
        bottom_nb = top_nb + mod

      image = ImagePreprocessing.pad_n(padding_value, left_nb, 'left')(image)
      image = ImagePreprocessing.pad_n(padding_value, right_nb, 'right')(image)
      image = ImagePreprocessing.pad_n(padding_value, top_nb, 'top')(image)
      image = ImagePreprocessing.pad_n(padding_value, bottom_nb, 'bottom')(image)

      return image

    return my_padding
