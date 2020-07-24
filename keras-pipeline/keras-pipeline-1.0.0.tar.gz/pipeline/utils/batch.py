from typing import *

import random
import math

class BatchLoopIterator:
  '''
  Iterator returning batches of defined length and looping indefinitely.

  Args:
    data: The data we want to loop over.
    batch_size: The number of element in regular batch. If None, set the
      size to then entire data, resulting in one unique batch.
    shuffle: Whether to shuffle the data.
    seed: Seed for the shuffling.
  '''

  def __init__(
    self,
    data: Sequence[Any],
    batch_size: Optional[int] = 32, # TODO: Optional[MyTypes.positive_int]
    shuffle: bool = True,
    seed: int = None,
  ) -> None:
    self.data = data

    if shuffle:
      random.Random(seed).shuffle(self.data)

    self.batch_size = batch_size if batch_size else len(self.data)

    # Compute the number of steps for one epoch.
    self.length = math.ceil(len(self.data) / self.batch_size)

    self.reset()

  def __len__(self) -> int:
    '''
    Returns:
      The number of steps for one epoch.
    '''

    return self.length

  def __next__(self) -> Sequence[Any]:
    '''
    Store previous batch.
    Compute next batch.

    Returns:
      A batch of at most batch_size elements. The last batch can be smaller.
    '''

    self.previous_batch = self.next_batch

    self.i = (self.i + 1) % self.length

    self.next_batch = self._compute_next_batch()

    return self.previous_batch

  def _compute_next_batch(self):
    low = self.i * self.batch_size
    high = low + self.batch_size
    return self.data[low:high]


  def reset(self) -> 'BatchLoopIterator':
    self.i = 0
    self.previous_batch = None
    self.next_batch = self._compute_next_batch()
    return self