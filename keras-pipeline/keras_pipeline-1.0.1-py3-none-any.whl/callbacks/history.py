from typing import *

import keras

import numpy as np

import functools
import requests
import json

class MyJSONEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, np.float32):
      return str(obj)
    if isinstance(obj, np.ndarray):
      return obj.tolist()
    return json.JSONEncoder.default(self, obj)

class SynchronizedHistory:
  '''
  Store everything (usually metrics) that is written in logs.
  Store it over epochs (in history_epoch) and batches (in history_batch).

  Args:
    server_addr: Address to HTTP server for remote monitoring.
  '''

  def __init__(
    self,
    server_addr: Optional[str] = None,
  ) -> None:
    self.server_addr = server_addr

    self.history_batch = {
      'train_epoch_batch': [],
      'train_total_batch': [],
      'val_epoch_batch': [],
      'val_total_batch': [],
      'eval_epoch_batch': [],
      'eval_total_batch': [],
      'test_epoch_batch': [],
      'test_total_batch': [],
    }
    self.history_epoch = {
      'epoch': [],
    }

  def _synchronize(func):
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):
      if self.server_addr is not None:
        name_json = json.dumps(func.__name__)
        args_json = json.dumps(args, cls=MyJSONEncoder)
        kwargs_json = json.dumps(kwargs, cls=MyJSONEncoder)
        
        requests.post(self.server_addr, json={
          'name': name_json,
          'args': args_json,
          'kwargs': kwargs_json,
        })
      return func(self, *args, **kwargs)
    return wrap

  @_synchronize
  def reset_prefix(self, prefix: str) -> None:
    keys = list(self.history_batch.keys()) # Copy
    for k in keys:
      if k[:len(prefix)] == prefix:
        if k[len(prefix):] in ['epoch_batch', 'total_batch']:
          self.history_batch[k] = []
        else:
          del self.history_batch[k]

  @_synchronize
  def reset_epoch(self) -> None:
    self.history_epoch = {
      'epoch': [],
    }

  @_synchronize
  def store_batch(
    self,
    epoch: int,
    batch: int,
    logs: Dict,
    prefix: str,
  ) -> None:
    self.history_batch[prefix + 'epoch_batch'].append((epoch, batch))

    current_batch = 0
    if len(self.history_batch[prefix + 'total_batch']) > 0:
      current_batch = self.history_batch[prefix + 'total_batch'][-1] + 1
    self.history_batch[prefix + 'total_batch'].append(current_batch)

    for k, v in logs.items():
      self.history_batch.setdefault(prefix + k, []).append(v)

  @_synchronize
  def store_epoch(
    self,
    epoch: int,
    logs: Dict,
  ) -> None:
    self.history_epoch['epoch'].append(epoch)
    for k, v in logs.items():
      self.history_epoch.setdefault(k, []).append(v)


class HistoryCallback(keras.callbacks.Callback):
  '''
  Store everything (usually metrics) that is written in logs into history.
  Should be placed in the list of callbacks after those who write things in
    logs.

  Args:
    b_reset: Whether to reset part of the history each time we run the
      associated part of whole process (training, validation, evaluation or
      testing).
    server_addr: Address to HTTP server for remote monitoring.
  '''

  def __init__(
    self,
    b_reset: bool = True,
    server_addr: Optional[str] = None,
  ) -> None:
    super().__init__()

    self.b_reset = b_reset

    self.history = SynchronizedHistory(server_addr)
    self.current_epoch = 0

    self.in_training = False

  def _reset_part(self, part: str) -> None:
    if not self.b_reset:
      return
    # else:
    # Reset all if 'train': it doesn't make sense to keep old model values
    if part == 'train':
      self.history.reset_prefix('train_')
      self.history.reset_prefix('val_')
      self.history.reset_epoch()
      self.current_epoch = 0
    if part in ['train', 'eval']:
      self.history.reset_prefix('eval_')
    if part in ['train', 'test']:
      self.history.reset_prefix('test_')
  
  def on_train_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self._reset_part('train')
    self.in_training = True
    
  def on_epoch_begin(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.current_epoch = epoch
  
  def on_train_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.history.store_batch(self.current_epoch, batch, logs, 'train_')
    
  def on_test_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    if not self.in_training:
      self._reset_part('eval')

  def on_test_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.history.store_batch(
      self.current_epoch,
      batch,
      logs,
      'val_' if self.in_training else 'eval_',
    )
    
  def on_epoch_end(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.history.store_epoch(self.current_epoch, logs)

  def on_train_end(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self.in_training = False

  def on_predict_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self._reset_part('test')

  def on_predict_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    if 'outputs' in logs:
      del logs['outputs']
    self.history.store_batch(self.current_epoch, batch, logs, 'test_')