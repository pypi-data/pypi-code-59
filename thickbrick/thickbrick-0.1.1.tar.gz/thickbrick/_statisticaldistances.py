__all__ = ['Neyman_chisq', 'Pearson_chisq', 'Kullback_Leibler', 'rev_Kullback_Leibler', 'Jeffreys', 'Bhattacharyya']

import numpy as _np

# Author's note to self: This is top-notch object-oriented programming. Well done!
class _genericdistancemeasure:
	@classmethod
	def eventwise_contrib_func(cls, p_c, p, signal_scale=None):
		p_c, p = _np.asarray(p_c), _np.asarray(p)
		if signal_scale is not None:
			p_c = signal_scale*p_c / (1. - p_c + signal_scale*p_c)
			p = signal_scale*p / (1. - p + signal_scale*p)
		
		return cls._eventwise_contrib_func(p_c, p)
	
	@classmethod
	def boundary_func(cls, p1, p2, signal_scale=None):
		p1, p2 = _np.asarray(p1), _np.asarray(p2)
		if signal_scale is not None:
			p1 = signal_scale*p1/(1. - p1 + signal_scale*p1)
			p2 = signal_scale*p2/(1. - p2 + signal_scale*p2)
			
			answer = cls._boundary_func(p1, p2)
			
			answer = answer / (signal_scale - signal_scale*answer + answer)
			return answer
		else:
			return cls._boundary_func(p1, p2)
	
	@classmethod
	def _boundary_func(cls, p1, p2): #Catch-all implementation to avoid explicit, numerically stable boundary function definitions
		bound1 = p1.copy()
		bound2 = p2.copy()
		for _ in range(54): #Error will be less than machine precision
			mid = 0.5*(bound1 + bound2)
			move_bound1 = (cls._eventwise_contrib_func(p1, mid) > cls._eventwise_contrib_func(p2, mid))
			bound1 = _np.where(move_bound1, mid, bound1)
			bound2 = _np.where(move_bound1, bound2, mid)
		return 0.5*(bound1 + bound2)

class Neyman_chisq(_genericdistancemeasure):
	@staticmethod
	def _eventwise_contrib_func(p_c, p):
		return -p_c**2. + 2.*p_c*p
	
	@staticmethod
	def _boundary_func(p1, p2):
		return 0.5*(p1+p2)

class Pearson_chisq(_genericdistancemeasure):
	@staticmethod
	def _eventwise_contrib_func(p_c, p):
		with _np.errstate(divide='ignore', invalid='ignore'):
			default = (-p_c**2. + 2.*p_c*p - p_c**2.*p)/(1.-p_c)**2.
			
			condlist = [(p_c == 1.) & (p == 1.), p_c == 1., p_c != 1.]
			choicelist = [_np.inf, -_np.inf, default]
			answer = _np.select(condlist, choicelist)
			
			if answer.ndim == 0:
				return answer.item()
			return answer

class Kullback_Leibler(_genericdistancemeasure):
	@staticmethod
	def _eventwise_contrib_func(p_c, p):
		with _np.errstate(divide='ignore', invalid='ignore'):
			default = -2.*_np.log1p(-p_c) - 2.*p_c*(1.-p)/(1.-p_c)
			small_p_c_lim = (2.*p_c*p - p_c**2. - p_c**3./3. - p_c**4./6. - p_c**5./10. - p_c**6./15.)/(1.-p_c)
			
			condlist = [(p_c == 1.) & (p == 1.), p_c == 1., p_c < 1e-3, p_c >= 1e-3]
			choicelist = [_np.inf, -_np.inf, small_p_c_lim, default]
			answer = _np.select(condlist, choicelist)
			
			if answer.ndim == 0:
				return answer.item()
			return answer

class rev_Kullback_Leibler(_genericdistancemeasure):
	@staticmethod
	def _eventwise_contrib_func(p_c, p):
		with _np.errstate(divide='ignore', invalid='ignore'):
			default = 2.*p_c + 2.*_np.log1p(-p_c)*(1.-p)
			small_p_c_lim = -p_c**2. - 2.*_np.log1p(-p_c)*p - 2.*(p_c**3./3. + p_c**4./4. + p_c**5./5. + p_c**6./6.)
			
			condlist = [(p_c == 1.) & (p == 1.), p_c == 1., p_c < 1e-3, p_c >= 1e-3]
			choicelist = [2., -_np.inf, small_p_c_lim, default]
			answer = _np.select(condlist, choicelist)
			
			if answer.ndim == 0:
				return answer.item()
			return answer

class Jeffreys(_genericdistancemeasure):
	@staticmethod
	def _eventwise_contrib_func(p_c, p):
		with _np.errstate(divide='ignore', invalid='ignore'):
			default = p_c*(p-p_c)/(1.-p_c) - _np.log1p(-p_c)*p
			
			condlist = [(p_c == 1.) & (p == 1.), p_c == 1., p_c != 1.]
			choicelist = [_np.inf, -_np.inf, default]
			answer = _np.select(condlist, choicelist)
			
			if answer.ndim == 0:
				return answer.item()
			return answer

class Bhattacharyya(_genericdistancemeasure):
	@staticmethod
	def _eventwise_contrib_func(p_c, p):
		with _np.errstate(divide='ignore', invalid='ignore'):
			default = 4.*(2.-p) - 4.*(2.-p_c-p)/_np.sqrt(1.-p_c)
			small_p_c_lim = (-p_c**2. - p_c**3. - (15./16.)*p_c**4. - (7./8.)*p_c**5. - (105./128.)*p_c**6.) + p*(2.*p_c + (3./2.)*p_c**2. + (5./4.)*p_c**3. + (35./32.)*p_c**4. + (63./64.)*p_c**5.)
			
			condlist = [(p_c == 1.) & (p == 1.), p_c == 1., p_c < 1e-3, p_c >= 1e-3]
			choicelist = [4., -_np.inf, small_p_c_lim, default]
			answer = _np.select(condlist, choicelist)
			
			if answer.ndim == 0:
				return answer.item()
			return answer
