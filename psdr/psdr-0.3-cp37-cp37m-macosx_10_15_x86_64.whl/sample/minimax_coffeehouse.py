import numpy as np
from ..geometry import voronoi_vertex, cdist, miniball
from .minimax_fp import _update_voronoi_sample, _update_voronoi_full


def _circumcenter(domain, V, L):
	x = cp.Variable(len(domain))
	ones = np.ones((1, len(V)))
	obj = cp.mixed_norm( (L @ ( cp.reshape(x,(len(domain),1)) @ ones - V.T)).T, 2, np.inf)
	prob = cp.Problem(cp.Minimize(obj), constraints)
	prob.solve()
	return x.value

def minimax_coffeehouse(domain, M, L = None, M0 = None):
	r"""
	
	"""

	if L is None:
		L = np.eye(len(domain))
	if M0 is None:
		M0 = 5*M*len(domain)

	update_voronoi = _update_voronoi_full

	Xhat = [domain.center]
	
	X0 = domain.sample(M0)

	for it in range(1, M):
		print(np.vstack(Xhat))
		V = update_voronoi(domain, np.vstack(Xhat), X0, L, M0)

		x_best = None
		score_best = np.inf

		X1 = domain.sample(10*it)
		for x in X1:
			# Compute nearest neighbors to x when added to Xhat
			Xt = np.vstack(Xhat + [x])
			D = cdist(Xt,V, L) 
			d = np.min(D, axis = 0)
			I = np.isclose(D[-1],d) 
			
			# Compute circumcenter		
			# Note: we do not need to include constraints because convexity of the domain	
			# ensures that the resulting point is inside 	
			x, _ = miniball(V[I], L = L) 

			Xt = np.vstack(Xhat + [x])
			score = np.max(np.min(cdist(Xt,V, L), axis = 0))
			if score < score_best:
				x_best = x
				score_best = score

		Xhat += [x_best]		 
						
	return np.vstack(Xhat)

