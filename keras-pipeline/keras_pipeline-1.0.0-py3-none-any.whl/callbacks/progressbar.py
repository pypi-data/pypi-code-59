from typing import *

import keras

import reprint

print('▏▎▍▌▋▊▉█')
print('▁▂▃▄▅▆▇█')

class ProgressbarCallback(keras.callbacks.Callback):
  def __init__(
    self,
    total_epoch: int,
    total_batch: int,
  ) -> None:
    super().__init__()

    self.total_epoch = total_epoch
    self.total_batch = total_batch

  def _print_on_end(self, logs: Dict, prefix: str = '') -> None:
    d = {
      'batch': logs['batch'],
      'size': logs['size'],
    }
    print(f"logs={d}")
    print(f'+')
    for k, v in logs.items():
      if k in ['batch', 'size']:
        continue
      print(f'{prefix}\'{k}\': {v}')
  
  def on_train_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_train_begin')
    print(f'logs={logs}')
    
  def on_epoch_begin(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    self.current_epoch = epoch
  
  def on_train_batch_begin(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_train_batch_begin batch #{batch}')
    print(f'logs={logs}')
  
  def on_train_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_train_batch_end batch #{batch}')
    self._print_on_end(logs)
    
  def on_test_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_test_begin')
    print(f'logs={logs}')
    
  def on_test_batch_begin(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_test_batch_begin batch #{batch}')
    print(f'logs={logs}')
    
  def on_test_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_test_batch_end batch #{batch}')
    self._print_on_end(logs, prefix='val_')
    
  def on_test_end(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_test_end')
    print(f'logs={logs}')
    
  def on_epoch_end(
    self,
    epoch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_epoch_end epoch #{epoch}')
    keys = []
    val_keys = []
    for k in logs.keys():
      if k[:4] == 'val_':
        val_keys.append(k)
      else:
        keys.append(k)
    print(f'logs={{}}')
    print(f'+')
    for k in keys:
      print(f'mean_\'{k}\': {logs[k]}')
    print(f'+')
    for k in val_keys:
      print(f'mean_\'{k}\': {logs[k]}')
      
  def on_train_end(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_train_end')
    print(f'logs={logs}')

  def on_predict_begin(
    self,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_predict_begin')
    print(f'logs={logs}')

  def on_predict_batch_begin(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_predict_batch_begin batch={batch}')
    print(f'logs={logs}')
  
  def on_predict_batch_end(
    self,
    batch: int,
    logs: Optional[Dict] = None,
  ) -> None:
    if 'outputs' in logs:
      del logs['outputs']
    print(f'\n### on_predict_batch_end batch={batch}')
    self._print_on_end(logs)

  def on_predict_end(
    self, 
    logs: Optional[Dict] = None,
  ) -> None:
    print(f'\n### on_predict_end')
    print(f'logs={logs}')