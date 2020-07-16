__all__ = ['NW_kerreg_1d']

import numpy as np
from ._onedim import _kernelregression_1d_base

def NW_kerreg_1d(x, y, bandwidth, kernel="rectangular", weight=None, delay_input_processing=False):
	allowed_kernels = ["rectangular", "exponential"]
	NW_1d_dict = {"rectangular": _NW_1d_rectangular, "exponential": _NW_1d_exponential}
	
	if len(allowed_kernels) == 2:
		allowed_kernels_string = f'''"{allowed_kernels[0]}" and "{allowed_kernels[1]}"'''
	elif len(allowed_kernels) > 2:
		allowed_kernels_string = f'''"{'", "'.join(allowed_kernels[:-1])}", and "{allowed_kernels[-1]}"'''
	
	if kernel not in allowed_kernels:
		raise(ValueError(f"Invalid option for 'kernel' parameter. Possible options are {allowed_kernels_string}."))
	
	#TODO: input sanitation
	
	to_return = NW_1d_dict[kernel](x, y, bandwidth, weight, delay_input_processing)
	to_return.kernel_name = kernel
	return to_return

class _NW_1d_rectangular(_kernelregression_1d_base):
	_variable_bandwidth_allowed = True
	
	def process_input(self):
		self.breakpoints = np.concatenate((self.x - self.bandwidth, self.x + self.bandwidth))
		
		Nr_terms = 0.5*self.weight*self.y/self.bandwidth
		Nr_terms = np.concatenate((Nr_terms, -Nr_terms))
		Dr_terms = 0.5*self.weight/self.bandwidth
		Dr_terms = np.concatenate((Dr_terms, -Dr_terms))
		
		del self.x, self.y, self.weight, self.bandwidth
		
		sort_indices = np.argsort(self.breakpoints)
		self.breakpoints = self.breakpoints[sort_indices]
		Nr_terms = Nr_terms[sort_indices]
		Dr_terms = Dr_terms[sort_indices]
		
		self.Nr_atbreakpoints = np.cumsum(Nr_terms)
		self.Dr_atbreakpoints = np.cumsum(Dr_terms)
	
	def evaluate(self, q, return_Nr_Dr = False):
		index = np.searchsorted(self.breakpoints, q, side='right') #right => [)
		Nr = np.where(index > 0, self.Nr_atbreakpoints[index-1], 0.)
		Dr = np.where(index > 0, self.Dr_atbreakpoints[index-1], 0.)
		
		if return_Nr_Dr:
			return Nr, Dr
		else:
			return Nr/Dr

class _NW_1d_exponential(_kernelregression_1d_base):
	_variable_bandwidth_allowed = False
	
	def process_input(self):
		self.Nr_aux_cumsum_left = self.weight*self.y
		self.Dr_aux_cumsum_left = self.weight
		del self.y, self.weight
		
		sort_indices = np.argsort(self.x)
		self.x = self.x[sort_indices]
		self.Nr_aux_cumsum_left = self.Nr_aux_cumsum_left[sort_indices]
		self.Dr_aux_cumsum_left = self.Dr_aux_cumsum_left[sort_indices]
		
		self.Nr_aux_cumsum_right = np.copy(self.Nr_aux_cumsum_left)
		self.Dr_aux_cumsum_right = np.copy(self.Dr_aux_cumsum_left)
		
		kernel_dropfactor = np.exp(-np.diff(self.x)/self.bandwidth)
		
		for i in range(self.x.size-1):
			self.Nr_aux_cumsum_left[i+1] += self.Nr_aux_cumsum_left[i]*kernel_dropfactor[i]
			self.Dr_aux_cumsum_left[i+1] += self.Dr_aux_cumsum_left[i]*kernel_dropfactor[i]
			
			self.Nr_aux_cumsum_right[-2-i] += self.Nr_aux_cumsum_right[-1-i]*kernel_dropfactor[-1-i]
			self.Dr_aux_cumsum_right[-2-i] += self.Dr_aux_cumsum_right[-1-i]*kernel_dropfactor[-1-i]
	
	def evaluate(self, q, return_Nr_Dr = False):
		index = np.searchsorted(self.x, q, side='right') #side doesn't matter
		
		tmp1 = np.where(index == 0, -np.inf, self.x[index-1] - q)
		tmp2 = np.where(index == self.x.size, -np.inf, q - self.x[index-self.x.size])
		
		Nr = self.Nr_aux_cumsum_left[index-1]*np.exp(tmp1) + self.Nr_aux_cumsum_right[index-self.x.size]*np.exp(tmp2)
		Dr = self.Dr_aux_cumsum_left[index-1]*np.exp(tmp1) + self.Dr_aux_cumsum_right[index-self.x.size]*np.exp(tmp2)
		
		if return_Nr_Dr:
			return Nr, Dr
		else:
			return Nr/Dr
