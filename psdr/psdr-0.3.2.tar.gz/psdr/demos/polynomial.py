r""" Synthetic demo functions based on polynomials 

""" 

import numpy as np
from scipy.linalg import orth

from psdr import Function, BoxDomain

class AffineFunction(Function):
	r""" Constructs an affine function

	Parameters
	"""
	def __init__(self, linear = None, constant = None, domain = None):
		if linear is None:
			if domain is not None:
				self.linear = np.random.randn(len(domain))
			else:
				self.linear = np.random.randn(5)
		else:
			self.linear = np.array(linear).flatten()

		if constant is None:
			self.constant = 0
		else:
			self.constant = float(constant)


		if domain is None:
			domain = BoxDomain(-np.ones(len(self.linear)), np.ones(len(self.linear)))
		

		Function.__init__(self, self._func, domain, grads = self._func_grad, vectorized = True)

	def _func(self, X):
		return self.linear.dot(X.T) + self.constant 

	def _func_grad(self, X):
		return np.tile(self.linear, (len(X),1))



class QuadraticFunction(Function):
	r""" A simple quadratic function in arbitrary dimensions

	This construct a quadratic function 

	..math::
	
		f(\mathbf x) = \frac12 \mathbf x^\top \mathbf A \mathbf x + \mathbf x^\top \mathbf b + \gamma

	where math:`\mathbf A` is a symmetric matrix.

	Parameters
	----------
	dim: int
	
	"""
	def __init__(self, dim = None, A = None, b = None, gamma = None, domain = None, eigs = None, dask_client = None):
		assert not (dim is None and A is None and domain is None and eigs is None), "One of dim, A, eigs, or domain must be specified"

		self.A = None
		self.b = None
		self.gamma = None
		self.domain = None

		# Process input options
		if dim is not None:
			dim = int(dim)

		if A is not None:
			self.A = np.array(A)
			assert len(self.A.shape) == 2 and self.A.shape[0] == self.A.shape[1], "A must be a square matrix"
			if dim is not None:
				assert dim == self.A.shape[0]
			else:
				dim = self.A.shape[0]

		if eigs is not None:
			assert self.A is None, "Cannot specify both A and eigs"
			eigs = np.array(eigs)
			if dim is not None:
				assert dim == len(eigs)
			else:
				dim = len(eigs)
			
		if domain is not None:
			if dim is not None:
				assert dim == len(domain), "input dimension does not match the dimension of the domain"
			dim = len(domain)

		if b is not None:
			b = np.array(b).flatten()
			if dim is not None:
				assert dim == b.shape[0]
			else:
				dim = b.shape[0]

		assert dim is not None, "Could not infer dimension"
		
		if A is None:
			if eigs is None:
				eigs = np.ones(dim)
			# Random rotation matrix
			U = orth(np.random.randn(dim, dim))
			self.A = U @ np.diag(eigs) @ U.T

		if b is not None:
			self.b = np.array(b).flatten()
		else:
			self.b = np.zeros(dim)

		
		if gamma is None:
			self.gamma = 0
		else:
			self.gamma = float(gamma)

		if domain is None:
			domain = BoxDomain(-np.ones(dim), np.ones(dim))

		Function.__init__(self, self._func, domain, grads = self._func_grad, vectorized = True)

	def _func(self, X):
		# Fast quadratic form computation
		# https://stackoverflow.com/a/18542236
		X = np.atleast_2d(X)
		return 	(X.dot(self.A)*X).sum(axis = 1) + self.b.dot(X.T) + self.gamma

	def _func_grad(self, X):
		 return 2*X.dot(self.A) + np.tile(self.b, (len(X),1))
