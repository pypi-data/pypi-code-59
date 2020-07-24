from typing import *

import keras

# For type hints
from ..metrics.metrics import Metrics
from ..image.loader import ImageLoader

from .utils import logs_safe_update
from ..metrics.utils import get_function_name

class ValiderCallback(keras.callbacks.Callback):
  '''
  Deprecated: Use MetricsCallback instead.
  One pain point of Keras fit/fit_generator is that validation is done at
    the end of each epoch. This class is here to do validation at the same
    time as training. This enables us to monitor training more precisely.
  Fun fact: if validation_loader is also given to Keras fit_generator's
    validation_data, it nexts one batch before the first call ever to
    on_train_batch_begin, and it nexts one other batch before the first
    call ever to on_train_batch_end. It never does that again.
    <3 Keras

  Args:
    validation_loader: ImageLoader containing examples and labels for
      validation.
    sample_weight: Keras test_on_batch optional parameter.
    reset_metrics: Keras test_on_batch optional parameter.
  '''

  def __init__(
    self,
    validation_loader: ImageLoader,
    sample_weight: Optional[List[float]] = None,
    reset_metrics: bool = True,
  ) -> None:
    super().__init__()

    self.validation_loader = validation_loader
    self.sample_weight = sample_weight
    self.reset_metrics = reset_metrics

    self.prefix = 'vot_'

  def _compute_metrics(self, **kwargs) -> Dict[str, Any]:
    values = self.model.test_on_batch(
      *next(self.validation_loader),
      sample_weight=self.sample_weight,
      reset_metrics=self.reset_metrics,
    )

    ret = {
      self.prefix + get_function_name(metric): v
        for metric, v in zip(self.model._compile_metrics, values[1:])
    }
    ret[self.prefix + 'loss'] = values[0]

    return ret
    
  def on_epoch_begin(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.validation_loader.reset()
  
  def on_train_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    logs_safe_update(logs, self._compute_metrics())
    
  def on_test_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    '''
    Reset validation_loader in case it is also given to fit_generator as
       validation_data parameter.
    '''

    self.validation_loader.reset()