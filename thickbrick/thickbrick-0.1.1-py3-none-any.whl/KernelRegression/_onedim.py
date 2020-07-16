import numpy as np

class _kernelregression_1d_base:
	def __init__(self, x, y, bandwidth, weight, delay_input_processing):
		#ndim = max((numpy.ndim(x), numpy.ndim(y), numpy.ndim(bandwidth), numpy.ndim(weight)
		#
		#if ndim > 2:
		#	return ValueError("Unsupported operation. Check the shapes of input arrays.")
		
		#TODO: input sanitation
		
		self.x = np.copy(x)
		self.y = np.copy(y)
		
		if weight is None:
			self.weight = np.ones(self.x.shape)
		else:
			self.weight = np.copy(weight)
		
		if self._variable_bandwidth_allowed:
			#TODO: Input sanitation, check that bandwidth is positive
			if callable(bandwidth):
				self.bandwidth = bandwidth(self.x)
			elif np.issubdtype(type(bandwidth), np.number):
				self.bandwidth = bandwidth
			else:
				self.bandwidth = np.copy(bandwidth)
		else:
			#TODO: Input sanitation, check that bandwidth is positive
			self.bandwidth = bandwidth
		
		if not delay_input_processing:
			self.process_input()
	
	def process_input(self):
		#To be overridden by derived classes
		pass
	
	def evaluate(self, q):
		#To be overridden by derived classes
		return None
	
	def __call__(self, *args, **kwargs):
		return self.evaluate(*args, **kwargs)
