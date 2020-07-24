from typing import *

import numpy as np

import keras

class StopperCallback(keras.callbacks.Callback):
  '''
  Stop training when a monitored quantity has stopped improving over batches.
  Like EarlyStopping but granularity is batch instead of epoch.

  Args:
    monitor: Quantity to be monitored. Anything that is inside logs in
      on_batch_end method.
    mode: 'min' or 'max'. Training will stop when the quantity monitored has
      stopped increasing or decreasing (whether mode is 'max' or 'min').
    min_delta: Minimum change in the monitored quantity to qualify as an
      improvement, i.e. an absolute change of less than min_delta, will
      count as no improvement.
    patience: Number of batches with no improvement after which training
      will be stopped.
    verbose: Verbosity mode. 1 or 0.
    baseline: Baseline value for the monitored quantity to reach.
      Training will stop if the model doesn't show improvement over the
      baseline.
    restore_best_weights: Whether to restore model weights from the batch
      with the best value of the monitored quantity or to keep the weights
      of the last step of training.
  '''

  def __init__(
    self,
    monitor: str,
    mode: str,
    min_delta: Union[float, int] = 0,
    patience: Union[float, int] = 0,
    verbose: bool = True,
    baseline: Union[None, float, int] = None,
    restore_best_weights: bool = True,
  ) -> None:
    super().__init__()

    self.monitor = monitor
    self.mode = mode
    self.min_delta = min_delta * (1 if self.mode == 'min' else -1)
    self.patience = patience
    self.verbose = verbose
    self.baseline = baseline
    self.restore_best_weights = restore_best_weights

    self.best_weights = None
    self.monitor_op = np.less if self.mode == 'min' else np.greater
    self.stop_training = False

  def on_train_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    self.wait = 0
    self.stopped_epoch_batch = (0, 0)
    
    self.best = self.baseline
    if self.baseline is None:
      self.best = np.inf * (1 if self.mode == 'min' else -1)

  def on_epoch_begin(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.epoch = epoch

  def on_train_batch_begin(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    # Store weights before backprop because metrics are computed before it
    self.weights = self.model.get_weights()

  def on_train_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    current = logs[self.monitor]

    if self.monitor_op(current - self.min_delta, self.best):
      self.best = current
      self.wait = 0
      if self.restore_best_weights:
        self.best_weights = self.weights
        self.best_epoch_batch = (self.epoch, batch)
    else:
      self.wait += 1
      if self.wait >= self.patience:
        self.stopped_epoch_batch = (self.epoch, batch)
        self.model.stop_training = True
        self.stop_training = True
        if self.restore_best_weights and self.best_weights is not None:
          self.model.set_weights(self.best_weights)
          if self.verbose:
            print(
              f'Model weights restored from the best batch at '
              f'{{Epoch: {self.best_epoch_batch[0]}, '
              f'Batch: {self.best_epoch_batch[1]}}}'
            )
        else:
          # Restore weigths before backprop
          self.model.set_weights(self.weights)

  def on_epoch_end(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    # Repeat stop_training because Keras forget it
    # <3 Keras
    if self.stop_training:
      self.model.stop_training = True

  def on_train_end(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    if self.wait >= self.patience:
      if self.verbose:
        print(
          f'EarlyStopping at '
          f'{{Epoch: {self.stopped_epoch_batch[0]}, '
          f'Batch: {self.stopped_epoch_batch[1]}}}'
        )
