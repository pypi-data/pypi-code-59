from typing import *

import numpy as np

def to_classes(
  y: np.ndarray,
  threshold: Union[None, float, Sequence[float]] = None,
  b_multiclass: bool = False,
) -> np.ndarray:
  '''
  Inverse function of to_categorical.
  Convert categorical labels to integers corresponding to class indexes.

  Args:
    y: Labels of any dimension where the last axis holds categorical values.
    threshold: Zero, one or more values.
      If None, get class index(es) of the best value.
        In case of equality:
          If b_multiclass is False, get the lower index.
          Else, get every indexes.
      If float, it's the minimum for a value to be positive to a class.
        In case of multiple positives:
          If b_multiclass is False, get the index of the higher value.
          Else, get every positive indexes.
        In case of no positive, return -1.
      If multiple thresholds, apply the same rules than for one threshold for
        each class and threshold.
    b_multiclass: Whether to keep multiple values when possible or only one.

  Returns:
    An array of class indexes whose inital values are validated by the
      threshold(s). In case of multiclass, multiples indexes can be returned
      for each example.

  Raises:
    ValueError
      If multiple thresholds but not as many values as there are classes.
  '''

  nb_classes = y.shape[-1]

  if threshold is None:
    if not b_multiclass:
      return np.argmax(y, axis=-1)
      
    # else:
    m = np.max(y, axis=-1)
    y = np.concatenate([
      np.where(y[..., i] == m, i, -1)[..., np.newaxis]
        for i in range(nb_classes)
    ], axis=-1)
    # TODO: some cleaning can be done here.
    return y

  # else:
  # Keep values higher than the threshold(s)
  if hasattr(threshold, '__iter__'):
    if len(threshold) != nb_classes:
      raise ValueError(f'Wrong number of thresholds. ' + \
        f'Expected: {nb_classes}. ' + \
        f'Got: {len(threshold)}.')
    y = np.concatenate([
      np.where(y[..., i] >= th, y[..., i], -np.inf)[..., np.newaxis]
        for i, th in enumerate(threshold)
    ], axis=-1)
    threshold = np.min(threshold)
  else:
    y = np.where(y >= threshold, y, -np.inf)

  # Append a column of threshold to the end
  ret = np.insert(y, nb_classes, threshold, axis=-1)

  # Get column indices of the higher value
  ret = np.argmax(ret, axis=-1)

  # Set to -1 if the last column is the higher
  ret[ret==nb_classes] = -1

  return ret