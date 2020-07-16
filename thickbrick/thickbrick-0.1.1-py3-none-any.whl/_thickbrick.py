__all__ = ['Autocategorizer', 'Evaluator', 'FunctionalCategorizer', '_Categorizer']

import numpy as np
from . import _statisticaldistances as statdists

class Autocategorizer:
	def __init__(self, category_count, allow_rejection, statistical_distance, regression_method, default_regression_options={}):
		allowed_statistical_distances = ["Neyman_chisq", "Pearson_chisq", "Kullback_Leibler", "rev_Kullback_Leibler", "Jeffreys", "Bhattacharyya"]
		statistical_distance_dict = {"Neyman_chisq": statdists.Neyman_chisq, "Pearson_chisq": statdists.Pearson_chisq, \
								"Kullback_Leibler": statdists.Kullback_Leibler, "rev_Kullback_Leibler": statdists.rev_Kullback_Leibler, \
								"Jeffreys": statdists.Jeffreys, "Bhattacharyya": statdists.Bhattacharyya}
		
		assert statistical_distance in allowed_statistical_distances
		
		self.category_count = category_count
		self.allow_rejection = allow_rejection
		self.statistical_distance = statistical_distance_dict[statistical_distance]
		self.regression_method = regression_method
		self.default_regression_options = default_regression_options.copy()
		self.regression_options = default_regression_options.copy() #This is a shallow copy! Exercise caution if using mutable values in the default_regression_options.
	
	def set_data(self, x, p, weight=None, regression_options={}, point_wise_regression_options={}):
		self._data_x = x.copy()
		self._data_p = p.copy()
		
		if weight is None:
			self._data_weight = np.ones(p.shape)
		else:
			self._data_weight = weight.copy()
				
		self.regression_options = {**self.default_regression_options, **regression_options} #This is a shallow copy! Exercise caution if using mutable values in the regression_options.
		
		self._data_point_wise_regression_options = {}
		for _ in point_wise_regression_options:
			self._data_point_wise_regression_options[_] = point_wise_regression_options[_].copy() #point_wise_regression_options is copied at (only) one extra level of depth.
		
		regression_options = {**self.regression_options, **self._data_point_wise_regression_options}
		self.overall_means_oracle = self.regression_method(x = self._data_x, y = self._data_p, weight = self._data_weight, **regression_options)
		self.category_assignment = None
	
	def initialize_categorizer(self, mode='all_in_one_category'):
		def all_in_one_category(x, p):
			return np.zeros(x.shape)
		
		def random_assignment(x, p):
			np.random.randint(-1 if self.allow_rejection else 0, self.category_count, size=x.shape)
		
		mode_func_dict = {'all_in_one_category': all_in_one_category, 'random_assignment': random_assignment}
		
		assert mode in mode_func_dict
		self.current_categorizer = FunctionalCategorizer(mode_func_dict[mode])
		self.category_assignment = None
	
	def set_current_categorizer(self, categorizer):
		assert isinstance(categorizer, _CategorizerBase)
		self.current_categorizer = categorizer
		self.category_assignment = None
	
	def get_current_categorizer(self):
		try:
			return self.current_categorizer
		except AttributeError as err:
			raise AttributeError("`get_current_categorizer` method cannot be called before initializing the categorizer using `initialize_categorizer` or `set_current_categorizer`") from err
	
	def training_step(self, signal_scale=None):
		if self.category_assignment is None:
			self.category_assignment = self.current_categorizer.categorize(self._data_x, self._data_p)
		
		category_means_oracle = []
		for i in range(self.category_count):
			indices = ((self.category_assignment == i).nonzero())[0]
			
			if len(indices) == 0:
				category_means_oracle.append(self.overall_means_oracle)
				continue
			
			x = self._data_x[indices]
			p = self._data_p[indices]
			weight = self._data_weight[indices]
			
			point_wise_regression_options = {}
			for _ in self._data_point_wise_regression_options:
				point_wise_regression_options[_] = self._data_point_wise_regression_options[_][indices]
			
			regression_options = self.regression_options.copy()
			regression_options.update(point_wise_regression_options)
			
			category_means_oracle.append(self.regression_method(x = x, y = p, weight = weight, **regression_options))
		
		self.prev_category_assignment = self.category_assignment
		self.current_categorizer = _Categorizer(self.category_count, self.allow_rejection, self.statistical_distance, category_means_oracle, signal_scale)
		self.category_assignment = self.current_categorizer.categorize(self._data_x, self._data_p)
		
		to_return = {}
		to_return["category_reassignment_count"] = np.sum(self.category_assignment != self.prev_category_assignment)
		return to_return

class Evaluator:
	def __init__(self, statistical_distance, regression_method, default_regression_options={}):
		allowed_statistical_distances = ["Neyman_chisq", "Pearson_chisq", "Kullback_Leibler", "rev_Kullback_Leibler", "Jeffreys", "Bhattacharyya"]
		statistical_distance_dict = {"Neyman_chisq": statdists.Neyman_chisq, "Pearson_chisq": statdists.Pearson_chisq, \
								"Kullback_Leibler": statdists.Kullback_Leibler, "rev_Kullback_Leibler": statdists.rev_Kullback_Leibler, \
								"Jeffreys": statdists.Jeffreys, "Bhattacharyya": statdists.Bhattacharyya}
		
		self.statistical_distance = statistical_distance_dict[statistical_distance]
		self.regression_method = regression_method
		self.default_regression_options = default_regression_options.copy()
		self.regression_options = default_regression_options.copy() #This is a shallow copy! Exercise caution if using mutable values in the default_regression_options.
	
	def set_data(self, x, p, weight=None, regression_options={}, point_wise_regression_options={}):
		self._data_x = x.copy()
		self._data_p = p.copy()
		
		if weight is None:
			self._data_weight = np.ones(p.shape)
		else:
			self._data_weight = weight.copy()
				
		self.regression_options = {**self.default_regression_options, **regression_options} #This is a shallow copy! Exercise caution if using mutable values in the regression_options.
		
		self._data_point_wise_regression_options = {}
		for _ in point_wise_regression_options:
			self._data_point_wise_regression_options[_] = point_wise_regression_options[_].copy() #point_wise_regression_options is copied at (only) one extra level of depth.
	
	def upper_limit(self, signal_scale=None):
		if signal_scale is None:
			_data_scaled_weight = self._data_weight
		else:
			_data_scaled_weight = (1. - self._data_p + signal_scale*self._data_p)*self._data_weight
		
		Nr = np.sum(_data_scaled_weight*self.statistical_distance.eventwise_contrib_func(self._data_p, self._data_p, signal_scale))
		Dr = np.sum(_data_scaled_weight)
		
		return Nr/Dr
	
	def evaluate(self, cat, category_count, signal_scale=None):
		self.category_assignment = cat.categorize(self._data_x, self._data_p)
		
		if signal_scale is None:
			_data_scaled_weight = self._data_weight
		else:
			_data_scaled_weight = (1. - self._data_p + signal_scale*self._data_p)*self._data_weight
		
		Dr = np.sum(_data_scaled_weight)
		
		####################################################
		Nr = 0.
		for i in range(category_count):
			indices = ((self.category_assignment == i).nonzero())[0]
			
			if len(indices) == 0:
				continue
			
			x = self._data_x[indices]
			p = self._data_p[indices]
			weight = self._data_weight[indices]
			scaled_weight = _data_scaled_weight[indices]
			
			point_wise_regression_options = {}
			for _ in self._data_point_wise_regression_options:
				point_wise_regression_options[_] = self._data_point_wise_regression_options[_][indices]
			
			regression_options = self.regression_options.copy()
			regression_options.update(point_wise_regression_options)
			
			category_mean_oracle = self.regression_method(x = x, y = p, weight = weight, **regression_options)
			category_mean = category_mean_oracle(x)
			
			Nr += np.sum(scaled_weight*self.statistical_distance.eventwise_contrib_func(category_mean, category_mean, signal_scale))
		####################################################
		
		return Nr/Dr

class _CategorizerBase:
	def __call__(self, *args, **kwargs):
		return self.categorize(*args, **kwargs)

class FunctionalCategorizer(_CategorizerBase):
	def __init__(self, func):
		self.categorize = func

class _Categorizer(_CategorizerBase):
	def __init__(self, category_count, allow_rejection, statistical_distance, prev_category_means_oracle, signal_scale):
		self.category_count = category_count
		self.allow_rejection = allow_rejection
		self.statistical_distance = statistical_distance
		self.prev_category_means_oracle = prev_category_means_oracle
		self.signal_scale = signal_scale
	
	def categorize(self, x, p):
		#prev_category_means = np.zeros((self.category_count+1, ) + x.shape) #[cat_index][x_index]
		#for i in range(self.category_count):
		#	prev_category_means[i+1] = self.prev_category_means_oracle[i](x)
		
		prev_category_means = [None]*(self.category_count+1)
		for i in range(self.category_count):
			prev_category_means[i+1] = self.prev_category_means_oracle[i](x)
		prev_category_means[0] = np.zeros(prev_category_means[-1].shape)
		prev_category_means = np.asarray(prev_category_means)
		
		# Sorting to ensure that categories don't interweave #########
		prev_category_means[1:].sort(axis=0)
		##############################################################
		
		# Use np.expand_dims(p, axis=0) or np.reshape(p, (1, -1)) instead of p in the next line?
		eventwise_contrib = self.statistical_distance.eventwise_contrib_func(prev_category_means, p, self.signal_scale)
		if self.allow_rejection == True:
			argmax_low = np.argmax(eventwise_contrib, axis=0) - 1 #-1 => rejected
			argmax_high = self.category_count - np.argmax(eventwise_contrib[::-1], axis=0) - 1
		else:
			argmax_low = np.argmax(eventwise_contrib[1:], axis=0)
			argmax_high = self.category_count - 1 - np.argmax(eventwise_contrib[:0:-1], axis=0)
		
		tie_breaker = (p < np.choose(argmax_low+1, prev_category_means)) # Equivalently: tie_breaker = (p < prev_category_means[argmax_low + 1, np.arange(len(x))])
		answer = np.where(tie_breaker, argmax_low, argmax_high) # Unless p[i] < prev_category_means[argmax_low[i]+1][i], prefer argmax_high[i]
		
		if answer.ndim == 0:
			return answer.item()
		return answer
	
	def boundaries(self, x):
		#prev_category_means = np.zeros((self.category_count+1, ) + x.shape) #[cat_index][x_index]
		#for i in range(self.category_count):
		#	prev_category_means[i+1] = self.prev_category_means_oracle[i](x)
		
		prev_category_means = [None]*(self.category_count+1)
		for i in range(self.category_count):
			prev_category_means[i+1] = self.prev_category_means_oracle[i](x)
		prev_category_means[0] = np.zeros(prev_category_means[-1].shape)
		prev_category_means = np.asarray(prev_category_means)
		
		# Sorting to ensure that categories don't interweave #########
		prev_category_means[1:].sort(axis=0)
		##############################################################
		
		boundaries = []
		for i in range(0 if self.allow_rejection else 1, self.category_count):
			boundaries.append( self.statistical_distance.boundary_func(prev_category_means[i], prev_category_means[i+1], self.signal_scale) )
		
		return np.asarray(boundaries)
