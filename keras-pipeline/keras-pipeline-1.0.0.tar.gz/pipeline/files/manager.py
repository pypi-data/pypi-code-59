from typing import *

import os
import imagesize

from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle as sk_shuffle

from keras.utils import to_categorical

from ..utils.histogram import Histogram

class FilesManager:
  '''
  Class managing files and data (labels) associated to these files.
  Store files and associated data/labels.
  Explores a directory and stores found files associated with name of
    subdirectories.

  Args:
    filenames: Paths to files.
    labels: Extra data associated to these files.
    directory: Path to a directory containing subdirectories as classes.
      Should have the following form:
        directory
        |
        |---- class_name_1
        |     |---- file_1
        |     |---- file_2
        |     |---- ...
        |     |---- file_k
        |
        |---- class_name_2
        |     |---- file_1
        |     |---- file_2
        |     |---- ...
        |     |---- file_n
        |
        |---- ...
        |
        |---- class_name_y
              |---- file_1
              |---- file_2
              |---- ...
              |---- file_z

  Raises:
    ValueError
      If filenames and labels have different lengths.
      If a path in filenames doesn't exist.
  '''

  def __init__(
    self,
    filenames: List[str] = [],
    labels: List = [],
    directory: Optional[str] = None,
  ) -> None:
    self.X = []
    self.y = []

    if filenames:
      self.add_files(filenames, labels)

    if directory is not None:
      self.add_directory(directory)

    self.label_encoder = None

  def __len__(self) -> int:
    return len(self.X)

  def get(self) -> Tuple[List[str], List[Any]]:
    return self.X, self.y

  def add_files(self, filenames: List[str], labels: List) -> None:
    '''
    Add filenames and extra data/labels to the current storage.

    Args:
      filenames: Paths to files.
      labels: Extra data associated to these files.

    Raises:
      ValueError
        If filenames and labels have different lengths.
        If a path in filenames doesn't exist.
    '''

    if len(filenames) != len(labels):
      raise ValueError(f'Expected filenames and labels to have the same\
        lengths but got: {len(filenames)} and {len(labels)}.')

    for e in filenames:
      if not os.path.exists(e):
        raise ValueError(f'{e} doesn\'t exist.')

    if len(self.X) == 0:
      self.X = filenames
      self.y = labels
    else:
      self.X += filenames
      self.y += labels

  def add_directory(self, directory: str) -> None:
    '''
    Explore a directory and stores found files associated with name of
      subdirectories.

    Args:
      directory: Path to a directory containing subdirectories as classes.
        Should have the following form:
          directory
          |
          |---- class_name_1
          |     |---- file_1
          |     |---- file_2
          |     |---- ...
          |     |---- file_k
          |
          |---- class_name_2
          |     |---- file_1
          |     |---- file_2
          |     |---- ...
          |     |---- file_n
          |
          |---- ...
          |
          |---- class_name_y
                |---- file_1
                |---- file_2
                |---- ...
                |---- file_z

    Raises:
      ValueError
        If directory doesn't exist.
        If filenames and labels have different lengths.
        If a path in filenames doesn't exist.
    '''

    if not os.path.exists(directory):
      raise ValueError(f'{directory} doesn\'t exist.')

    filenames = {}
    for e in os.listdir(directory):
      subdir = os.path.join(directory, e)
      if os.path.isdir(subdir):
        filenames[e] = [
          os.path.join(subdir, file) for file in os.listdir(subdir)
        ]

    # For each subdirectory k, stores found files and k.
    for k in filenames.keys():
      self.X += filenames[k]
      self.y += [k] * len(filenames[k])

  def add_manager(self, files_manager: 'FilesManager') -> None:
    self.add_files(*files_manager.get())

  def histogram(self) -> List[Tuple[Any, int, float]]:
    '''
    Count the number of files which have the same associated data/label.

    Returns:
      List of tuples of the following form:
        (label, number of files, ratio over the total).
    '''

    hist = Histogram(self.y)
    return [(k, hist[k], hist[k] / hist.sum * 100) for k in hist.keys()]\
      + [('Total', hist.sum, 100.)]

  def get_image_sizes(self) -> Dict[Any, Dict[Tuple[int, int], int]]:
    '''
    For image files exclusively.
    Get the histograms of image sizes.

    Returns:
      A dictionary of histogram of sizes for each different label.
    '''

    labels = set(self.y)

    # Store sizes for each different label.
    ret = {label: [] for label in labels}
    for image_filename, label in zip(self.X, self.y):
      ret[label].append(imagesize.get(image_filename))

    # Compute histograms for each label.
    for label in labels:
      ret[label] = Histogram(ret[label]).get()

    return ret

  def split(
    self,
    split_size, # TODO: Union[MyTypes.positive_int, MyTypes.positive_float]
    seed: Optional[int] = None,
  ) -> Tuple['FilesManager', 'FilesManager']:
    '''
    Split files and labels in two parts.

    Args:
      split_size: the number (if int) or the ratio (if float) of files and
        labels to include in the first returned FilesManager.
      seed: for replicability.

    Returns:
      Two splitted FilesManager.
    '''

    # Transform the ratio to an integer.
    if split_size < 1:
      split_size = round(split_size * len(self.X))

    # Get shuffled files and labels.
    X, y = sk_shuffle(self.X, self.y, random_state=seed)

    return (
      FilesManager(X[:split_size], y[:split_size]),
      FilesManager(X[split_size:], y[split_size:]),
    )

  def filter(
    self,
    predicate: Callable[[str, Any], bool],
  ) -> Tuple['FilesManager', 'FilesManager']:
    '''
    Use a predicate to split files and labels into one positive part and one
      negative according to the predicate.

    Args:
      predicate: A function returning a boolean that takes a path and a label.
    
    Returns:
      A FilesManager with filtered files and labels.
      A FilesManager with rejected files and labels.
    '''

    positives = [], []
    negatives = [], []

    for x, y in zip(self.X, self.y):
      if predicate(x, y):
        positives[0].append(x)
        positives[1].append(y)
      else:
        negatives[0].append(x)
        negatives[1].append(y)

    return FilesManager(*positives), FilesManager(*negatives)

  def encode_labels(
    self,
    y: Optional[List] = None,
    label_encoder: Optional[LabelEncoder] = None,
    b_categorical: bool = True,
  ) -> Tuple[LabelEncoder, List]:
    '''
    Encode labels with value between 0 and n_classes - 1 or between
      [0, O..O, 1] and [1, 0..0, 0].

    Args:
      y: Labels to encode. If None, it uses its own labels.
      label_encoder: LabelEncoder to use. If None, it creates its own
        LabelEncoder fitted on labels.
      b_categorical: Whether to use one-hot encoding or not.

    Returns:
      The label encoder used or created.
      The encoded labels.
    '''

    b_inplace = y is None

    if b_inplace:
      y = self.y

    if label_encoder:
      self.label_encoder = label_encoder

    if not self.label_encoder:
      self.label_encoder = LabelEncoder()
      self.label_encoder.fit(y)

    y = self.label_encoder.transform(y)

    if b_categorical:
      y = to_categorical(y, len(self.label_encoder.classes_))

    if b_inplace:
      self.y = y

    return self.label_encoder, y

  def decode_labels(
    self,
    y: Optional[List] = None,
    label_encoder: Optional[LabelEncoder] = None,
    b_categorical: bool = True,
  ) -> List:
    '''
    Decode labels either one-hot encoded or with values as class numbers.

    Args:
      y: Labels to decode. If None, it uses its own labels.
      label_encoder: LabelEncoder to use. If None, it uses its own
        LabelEncoder.
      b_categorical: Whether to use one-hot encoding or not.

    Raises:
      ValueError
        If label_encoder is None and self.label_encoder is undefined.
    '''

    b_inplace = y is None

    if b_inplace:
      y = self.y

    if label_encoder:
      self.label_encoder = label_encoder

    if not self.label_encoder:
      raise ValueError('label_encoder is None but it can\'t use\
        self.label_encoder because it\'s undefined')

    if b_categorical:
      y = np.argmax(y, axis=1)

    y = self.label_encoder.inverse_transform(y)

    if b_inplace:
      self.y = y

    return y
