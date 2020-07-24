from typing import *

import keras
import keras.backend as K
import tensorflow as tf

import numpy as np

from ..utils.utils import to_classes
from .utils import get_function_name

# TODO: thresholds

class Metrics:
  '''
  Args:
    metrics: Functions that require unmodified entries.
    metrics_1D: Functions that require (n_samples,) entries when data are
      (n_samples, n_classes). A call to to_classes is performed.
  '''

  def __init__(
    self,
    metrics: Iterable[Callable[[np.ndarray, np.ndarray], Any]],
    metrics_1D: Optional[Iterable[Callable[[np.ndarray, np.ndarray], Any]]] = None,
  ) -> None:
    self.metrics = metrics
    self.metrics_1D = metrics_1D

  def compute(
    self,
    y_true: np.ndarray,
    y_pred: np.ndarray,
  ) -> Dict[str, Any]:
    ret = {}

    for metric in self.metrics:
      ret[get_function_name(metric)] = metric(y_true, y_pred)

    if self.metrics_1D is not None:
      y_true_1D = to_classes(y_true)
      y_pred_1D = to_classes(y_pred)

      for metric in self.metrics_1D:
        ret[get_function_name(metric)] = metric(y_true_1D, y_pred_1D)

    return ret

  @staticmethod
  def matthews_2D(thresholds) -> Callable:
    def matthews_2D(y_true_2D, y_pred_2D):
      y_true_1D = to_classes(y_true_2D, thresholds)
      y_pred_1D = to_classes(y_pred_2D, thresholds)
      # TODO
      return 42
    return matthews_2D

  '''
  @staticmethod
  def my_true_positives_clip(y_true, y_pred):
    return K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
  @staticmethod
  def my_true_negatives_clip(y_true, y_pred):
    return K.sum(K.round(K.clip((1 - y_true) * (1 - y_pred), 0, 1)))
  @staticmethod
  def my_false_positives_clip(y_true, y_pred):
    return K.sum(K.round(K.clip((1 - y_true) * y_pred, 0, 1)))
  @staticmethod
  def my_false_negatives_clip(y_true, y_pred):
    return K.sum(K.round(K.clip(y_true * (1 - y_pred), 0, 1)))
  
  @staticmethod
  def my_true_positives(y_true, y_pred):
    return K.sum(K.round(y_true * y_pred))
  @staticmethod
  def my_true_negatives(y_true, y_pred):
    return K.sum(K.round((1 - y_true) * (1 - y_pred)))
  @staticmethod
  def my_false_positives(y_true, y_pred):
    return K.sum(K.round((1 - y_true) * y_pred))
  @staticmethod
  def my_false_negatives(y_true, y_pred):
    return K.sum(K.round(y_true * (1 - y_pred)))
    
  @staticmethod
  def my_accuracy(y_true, y_pred):
    true_positives = K.sum(K.round(y_true * y_pred))
    
    predicted_positives = K.sum(K.round(y_pred))
    
    return true_positives / (predicted_positives + K.epsilon())

  @staticmethod
  def my_recall(y_true, y_pred):    
    true_positives = K.sum(K.round(y_true * y_pred))
    
    possible_positives = K.sum(K.round(y_true))
    
    return true_positives / (possible_positives + K.epsilon())

  @staticmethod
  def my_f1_score(y_true, y_pred):
    a = Metrics.my_accuracy(y_true, y_pred)
    r = Metrics.my_recall(y_true, y_pred)
    return 2 * ((a * r) / (a + r + K.epsilon()))
  '''

  @staticmethod
  def categorical_true_negativesv2(y_true, y_pred):
    return K.sum(K.round(y_true * y_pred), axis=0)[0]
  @staticmethod
  def categorical_true_negatives(y_true, y_pred):
    return K.sum(K.round(y_true * y_pred), axis=0)[0]
  @staticmethod
  def categorical_true_positives(y_true, y_pred):
    return K.sum(K.round(y_true * y_pred), axis=0)[1]
  @staticmethod
  def categorical_false_positives(y_true, y_pred):
    return K.sum(K.round(y_true * (1 - y_pred)), axis=0)[0]
  @staticmethod
  def categorical_false_negatives(y_true, y_pred):
    return K.sum(K.round(y_true * (1 - y_pred)), axis=0)[1]