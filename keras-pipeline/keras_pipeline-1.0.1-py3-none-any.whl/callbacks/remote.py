from typing import *

import keras
import keras.backend as K
import tensorflow as tf

import numpy as np

import requests
import json

# For type hints
from ..files.image.loader import ImageLoader

class MyJSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, np.float32):
      return str(obj)
    if isinstance(obj, np.ndarray):
      return obj.tolist()
    return json.JSONEncoder.default(self, obj)

class RemoteCallback(keras.callbacks.Callback):
  '''
  It collects and share model's outputs and labels for each batch during
    training, validation and testing.
  It avoids the cost of a second prediction.
  For this callback to work, a call to get_collecter_metric method must be
    added to the metrics parameter of model's compile method.
  Collecter stolen from https://stackoverflow.com/a/59697739.

  Args:
    server_addr: Address to HTTP server for remote monitoring.
    model: The Keras model to which outputs and labels are associated.
    validation_loader: To perform validation on training (see ValiderCallback).
  '''

  def __init__(
    self,
    server_addr: str,
    model: keras.models.Model,
    validation_loader: Optional[ImageLoader] = None,
  ) -> None:
    super().__init__()

    self.server_addr = server_addr
    self.model = model
    self.validation_loader = validation_loader

    self.in_training = False

    # tf.Variable is better than K.Variable as it can handle different shapes.
    self.targets = tf.Variable(0.0, shape=tf.TensorShape(None))
    self.outputs = tf.Variable(0.0, shape=tf.TensorShape(None))

  def get_collecter_metric(self) -> Callable[[Any, Any], float]:
    @tf.function
    def _collecter_metric(y_true, y_pred):
      self.targets.assign(self.model.targets[0])
      self.outputs.assign(self.model.outputs[0])
      return np.nan
    return _collecter_metric

  def get_ys(self) -> Tuple[np.ndarray, np.ndarray]:
    return K.eval(self.targets), K.eval(self.outputs)

  def _send(
    self,
    batch: int,
    b_vot: bool = False,
  ) -> None:
    y_true, y_pred = self.get_ys()

    dict_json = {
      'epoch': self.current_epoch if self.in_training else -1,
      'batch': batch,
      'y_true': y_true.tolist(),
      'y_pred': y_pred.tolist(),
    }

    # Validation on training
    if b_vot and self.validation_loader:
      dict_json['y_true_vot'] = self.y_true_vot.tolist()
      dict_json['y_pred_vot'] = self.y_pred_vot.tolist()

    requests.post(self.server_addr, json=dict_json)

  def _send_message(self, message: str) -> None:
    requests.post(self.server_addr, json={'message': message})

  def on_train_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self._send_message('on_train_begin')
    self.in_training = True

  def on_epoch_begin(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.current_epoch = epoch
    if self.validation_loader:
      self.validation_loader.reset()

  def on_train_batch_begin(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    # Saving values before backprop
    if self.validation_loader:
      X_val, self.y_true_vot = next(self.validation_loader)
      self.y_pred_vot = self.model.predict_on_batch(X_val)

  def on_train_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    del logs['_collecter_metric']
    self._send(batch, b_vot=True)

  def on_test_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self.send('on_valid_begin' if self.in_training else 'on_eval_begin')
    if self.validation_loader:
      self.validation_loader.reset()
    
  def on_test_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    del logs['_collecter_metric']
    self._send(batch)

  def on_test_end(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self.send('on_valid_end' if self.in_training else 'on_eval_end')

  def on_epoch_end(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    del logs['_collecter_metric']
    if 'val__collecter_metric' in logs:
      del logs['val__collecter_metric']

  def on_train_end(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self._send_message('on_train_end')
    self.in_training = False