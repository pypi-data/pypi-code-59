import numpy as np
from scipy.spatial.distance import cdist, pdist, squareform
from iterprinter import IterationPrinter
from ..geometry import voronoi_vertex, cdist
from .maximin_coffeehouse import maximin_coffeehouse

def minimax_voronoi(domain, N, L = None, Xhat = None, maxiter = 10, verbose = True):
	r"""

	See [Pro17]_ section 3.2.2, using ideas from [CB05]_ and [CB09]_.

	"""
	
	if Xhat is None:
		Xhat = maximin_coffeehouse(domain, N, L)
		# Shrink slightly to pull points off the boundary
		Xhat = 0.8*(Xhat - np.outer(np.ones(N), domain.center)) + domain.center
		#Xhat = domain.sample(N)
	N0 = 100

	if verbose:
		printer = IterationPrinter(it = '4d', k = '4d', dist = '10.2e')
		printer.print_header(it = 'iter', k = 'k', dist = 'distance')

	P = np.zeros(Xhat.shape)
	for it in range(maxiter):
		# find the closest pairs of generators
		D = cdist(Xhat, Xhat, L = L) + np.diag(np.nan*np.ones(N))
		closest_dist = np.nanmin(D)
		radius = min(1e-10, closest_dist)
		
		for k in range(N):
			# Generate nearby points to Xhat[k]	inside the domain
			while True:
				X0 = np.outer(np.ones(N0), Xhat[k]) + radius*np.random.randn(N0, len(domain))
				X0 = X0[domain.isinside(X0)]
				if len(X0) > 0:
					break
				Xhat[k] = domain.sample()
					
			# push these to the boundary of the voronoi vertex
			X = voronoi_vertex(domain, Xhat, X0, L = L)
			# Restrict to those closest to Xhat
			D = cdist(Xhat, X, L = L)
			d = np.min(D, axis = 0)
			I = np.isclose(D[k], d)
			X = X[I]
			
			# find the furthest of these
			d = cdist(Xhat[k], X, L = L).flatten()
			j = np.argmax(d)
			# direction we want to go in
			P[k] = (X[j] - Xhat[k])/np.linalg.norm(X[j] - Xhat[k])
			
			alpha = domain.extent(Xhat[k], P[k])
			Xhat[k] += min(1e-2/(1+np.log(it+1)), 0.9*alpha)*P[k]
			if k == 0:
				print(Xhat[k], f'{np.max(d):7.2e} {np.min(d):7.2e}')	
#			if verbose:
#				printer.print_iter(it = it, k = k, dist = d[j])



	return Xhat
