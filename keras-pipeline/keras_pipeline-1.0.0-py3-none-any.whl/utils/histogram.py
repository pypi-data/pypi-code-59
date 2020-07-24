from typing import *

class Histogram:
	'''
	Class counting elements and storing the counts in a dictionary where keys
		are elements.

	Args:
	  l: Elements to be counted.
	'''

	def __init__(self, l: Iterable[Any]) -> None:
		self.hist = {}

		for e in l:
			if e in self.hist:
				self.hist[e] += 1
			else:
				self.hist[e] = 1

		self.sum = sum(self.hist.values())

	def __getitem__(self, key: Any) -> int:
		'''
		Access a count.

		Args:
			key: Element of which we want the count.

		Returns:
			The count.

		Raises:
			ValueError
				If the specified key doesn't exist in the dictionary.
		'''

		if key not in self.hist:
			raise ValueError(f'Key {key} not found in the dictionary.')

		return self.hist[key]

	def get(self) -> Dict[Any, int]:
		return self.hist

	def keys(self) -> List[Any]:
		return list(self.hist.keys())