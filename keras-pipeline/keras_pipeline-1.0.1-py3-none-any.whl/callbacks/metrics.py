from typing import *

import keras
import keras.backend as K
import tensorflow as tf

import numpy as np

# For type hints
from ..metrics.metrics import Metrics
from ..files.image.loader import ImageLoader

from .utils import logs_safe_update
from ..metrics.utils import get_function_name

class MetricsCallback(keras.callbacks.Callback):
  '''
  It collects model's outputs and labels. Then it computes metrics and adds
    them to logs. It repeats the operation for each batch during training,
    validation and testing.
  It avoids the cost of a second prediction.
  For this callback to work, a call to get_collecter_metric method must be
    added to the metrics parameter of model's compile method.
  Collecter stolen from https://stackoverflow.com/a/59697739.

  Args:
    model: The Keras model to which outputs and labels are associated.
    metrics: Metrics instance holding metrics to be computed for each batch.
    validation_loader: To perform validation on training (see ValiderCallback).
    sample_weight: Keras test_on_batch optional parameter.
    reset_metrics: Keras test_on_batch optional parameter.
  '''

  def __init__(
    self,
    model: keras.models.Model,
    metrics: Metrics,
    validation_loader: Optional[ImageLoader] = None,
    sample_weight: Optional[List[float]] = None,
    reset_metrics: bool = True,
  ) -> None:
    super().__init__()

    self.model = model
    self.metrics = metrics
    self.validation_loader = validation_loader
    self.sample_weight = sample_weight
    self.reset_metrics = reset_metrics

    # tf.Variable is better than K.Variable as it can handle different shapes.
    self.targets = tf.Variable(0.0, shape=tf.TensorShape(None))
    self.outputs = tf.Variable(0.0, shape=tf.TensorShape(None))

    self.in_epoch = False

  def get_collecter_metric(self) -> Callable[[Any, Any], float]:
    @tf.function
    def _collecter_metric(y_true, y_pred):
      self.targets.assign(self.model.targets[0])
      self.outputs.assign(self.model.outputs[0])
      return np.nan
    return _collecter_metric

  def get_ys(self) -> Tuple[np.ndarray, np.ndarray]:
    return K.eval(self.targets), K.eval(self.outputs)

  def _update_means(
    self,
    dict_metrics: Dict[str, Any],
    prefix: str,
    size: int,
  ) -> None:
    if prefix + list(dict_metrics.keys())[0] not in self.sum_means:
      for k in dict_metrics.keys():
        self.sum_means[prefix + k] = dict_metrics[k] * size
        self.div_means[prefix + k] = size
    else:
      for k, v in dict_metrics.items():
        self.sum_means[prefix + k] += v * size
        self.div_means[prefix + k] += size

  def _compute_log(
    self,
    logs: Dict,
    prefix: str = '',
    b_vot: bool = False,
  ) -> None:
    y_true, y_pred = self.get_ys()
    dict_metrics = self.metrics.compute(y_true, y_pred)
    logs_safe_update(logs, dict_metrics)
    self._update_means(dict_metrics, prefix, logs['size'])

    # Validation on training
    if b_vot and self.validation_loader:
      # Retrieve ys and metrics from before backprop
      y_true_val, y_pred_val = self.y_true_val, self.y_pred_val
      metric_values = self.metric_values

      dict_metrics_val = {}
      # Store already computed model metrics
      dict_metrics_val['vot_loss'] = metric_values[0]
      for metric, v in zip(self.model._compile_metrics, metric_values[1:]):
        k = get_function_name(metric)
        if k != '_collecter_metric':
          assert('vot_' + k not in dict_metrics_val)
          dict_metrics_val['vot_' + k] = v
      # Compute and store own metrics
      for k, v in self.metrics.compute(y_true_val, y_pred_val).items():
        assert('vot_' + k not in dict_metrics_val)
        dict_metrics_val['vot_' + k] = v

      logs_safe_update(logs, dict_metrics_val)
      self._update_means(dict_metrics_val, prefix, y_true_val.shape[0])

  def _reset_means(self) -> None:
    self.means = {}
    self.sum_means = {}
    self.div_means = {}

  def _compute_means(self) -> None:
    for k in self.sum_means:
      self.means[k] = self.sum_means[k] / self.div_means[k]

  def on_epoch_begin(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self._reset_means()
    self.in_epoch = True

    if self.validation_loader:
      self.validation_loader.reset()

  def on_train_batch_begin(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    # Saving values before backprop
    if self.validation_loader:
      X_val, self.y_true_val = next(self.validation_loader)
      self.metric_values = self.model.test_on_batch(
        X_val,
        self.y_true_val,
        sample_weight=self.sample_weight,
        reset_metrics=self.reset_metrics,
      )
      _, self.y_pred_val = self.get_ys()


  def on_train_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    del logs['_collecter_metric']
    self._compute_log(logs, b_vot=True)

  def on_test_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    if not self.in_epoch:
      self._reset_means()

    if self.validation_loader:
      self.validation_loader.reset()
    
  def on_test_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    del logs['_collecter_metric']
    if self.in_epoch:
      self._compute_log(logs, prefix='val_')
    else:
      self._compute_log(logs)

  def on_test_end(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    if not self.in_epoch:
      self._compute_means()

  def on_epoch_end(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    del logs['_collecter_metric']
    if 'val__collecter_metric' in logs:
      del logs['val__collecter_metric']
    # Don't log safely because Keras reuses last epoch logs for whatever reason
    # <3 Keras
    self._compute_means()
    logs.update(self.means)
    self.in_epoch = False