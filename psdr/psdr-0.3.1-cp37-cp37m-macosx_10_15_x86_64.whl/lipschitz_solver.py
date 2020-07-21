r""" Function versions of different Lipschitz matrix estimation frunctions

"""
import numpy as np
import scipy.linalg
import cvxopt

from .lipschitz_utils import *

# TODO: switch to enumerated input to then vectorize P = X[I] - X[J], and the conquent rows of inner product

def build_basis(m, basis):
	# Build the basis for symmetric positive definite matrices
	Es = []
	I = np.eye(m)
	if not isinstance(basis, str):
		try:
			U = np.array(basis)
			# Ensure basis is orthonormal
			Q, _ = np.linalg.qr(U)
			r = U.shape[1]
			# First the components in the range of U
			for i,j in zip(*np.triu_indices(r)):
				if j == i:
					Es.append(np.outer(Q[:,i], Q[:,i]))
				else:
					Es.append(0.5*np.outer(Q[:,i] + Q[:,j], Q[:,i] + Q[:,j]))
			# now the remainder
			if r < m:
				Es.append( I -  Q @ Q.T)
		except:
			raise NotImplementedError

	elif basis == 'full':
		for i,j in zip(*np.triu_indices(m)): 
			if j == i:
				Es.append(np.outer(I[:,i],I[:,i]))
			else:
				Es.append(0.5*np.outer(I[:,i] + I[:,j], I[:,i] + I[:,j]))

	elif basis == 'diag':
		for i in range(m):
			Es.append(np.outer(I[:,i],I[:,i]))

	return Es

def lipschitz_matrix_cvxopt(X, fX, grads, active_evals = None, active_grads = None, epsilon = 0, basis = 'full',
	H0 = None, verbose = False, abstol = 1e-9, reltol = 1e-9, feastol = 1e-9, refinement = 2,  kktsolver = 'robust'):
	r""" Estimate the Lipschitz matrix using CVXOPT through its native interface 


	Parameters
	----------
	X: np.array (M,m)
		Sample coordinates
	fX: np.array (M,)
		Value of function at corresponding points in X, i.e., f(X[j]) = fX[j]
	grads: np.array (N,m)
		Gradients of the function
	
	"""
	m = X.shape[1]
	
	Es = build_basis(m, basis)

	Eten = np.array(Es)
		
	# LHS of every sdp constraint is the same
	Gsdp_basis = np.vstack([E.flatten('F') for E in Es]).T

	hsdp = []

	dims = {'l': 0, 'q': [], 's': []}

	##################################################################
	# Positive definite constraint
	##################################################################
	hsdp.append(np.zeros((m,m)).flatten('F'))
	dims['s'].append(m)
	
	##################################################################
	# Construct constraints corresponding to gradients
	##################################################################
	if active_grads is None:
		active_grads = range(len(grads))

	for k in active_grads:
		hsdp.append( -np.outer(grads[k], grads[k]).flatten('F'))
		dims['s'].append(m)

	##################################################################
	# Construct constraints corresponding to function evaluations
	##################################################################
	if active_evals is None:
		active_evals = np.array(np.triu_indices(len(X), k = 1))

	Gineq = []
	hineq = []
	for i,j in zip(*active_evals): 	
		#i,j = eval_idx[:,k]
		p = (X[i] - X[j]).flatten()
		# Normalizing here seems to reduce the normalization once inside CVXOPT
		#p_norm = np.linalg.norm(p)	
		p_norm2 = p.T @ p
		# Vectorize to improve performance
		#G = [-p.dot(E.dot(p)) for E in Es]
		#G = -np.tensordot(np.tensordot(Eten, p/p_norm, axes = (2,0)), p/p_norm, axes = (1,0))
		G = -np.einsum('ijk,j,k->i', Eten, p, p)/p_norm2
		Gineq.append(G)
		hineq.append(-(np.abs(float(fX[i] - fX[j])) - epsilon)**2/p_norm2)
		dims['l'] += 1

	

	if verbose:
		cvxopt.solvers.options['show_progress'] = True
	else:
		cvxopt.solvers.options['show_progress'] = False
	
	if abstol is not None:
		cvxopt.solvers.options['abstol'] = abstol
	if reltol is not None:
		cvxopt.solvers.options['reltol'] = reltol
	if feastol is not None:
		cvxopt.solvers.options['feastol'] = feastol
	if refinement is not None:
		cvxopt.solvers.options['refinement'] = refinement
	if kktsolver is not None:
		cvxopt.solvers.options['kktsolver'] = kktsolver
	

	# Setup objective
	c = np.array([ np.trace(E) for E in Es])
	G = np.vstack(Gineq + len(dims['s'])*[-Gsdp_basis] )
	h = np.hstack(hineq + hsdp)
	
	primalstart = None
	dualstart = None

	if H0 is not None:
		x, _, _, _ = scipy.linalg.lstsq(Gsdp_basis, H0.flatten('F'))
		assert np.linalg.norm( H0 - (Gsdp_basis @ x).reshape(m,m), 'fro') < 1e-10
		s = h - G @ x
		#z = np.copy(-h)
		# add a small perturbation to the slack variable to ensure numerically satisfying constraints
		for k in range(len(dims['s'])):
			s[dims['l'] +k*m**2: dims['l'] + (k+1)*m**2: m+1] += 1e-07	
		#	z[dims['l'] +k*m**2: dims['l'] + (k+1)*m**2: m+1] += 1e-07	
		primalstart = {'x': cvxopt.matrix(x), 's': cvxopt.matrix(s)}
		#dualstart = {'z': cvxopt.matrix(-h), 'y': cvxopt.matrix([], (0,1))}
		#dualstart = {'z': cvxopt.matrix(z)}
	
	c = cvxopt.matrix(c)
	G = cvxopt.matrix(G)
	h = cvxopt.matrix(h)

	# Note CVXOPT solves
	# min_x  c.T @ x
	# st.    G @ x + s = h
	#        A @ x = b
	#        s >= 0

	# We seek to solve
	# min Tr(H) s.t.  H - g @ g.T >=0  
	# => min Tr(H) s.t. H + S = - g @ g.T, S >= 0

	sol = cvxopt.solvers.conelp(c, G, h, dims = dims, primalstart = primalstart, dualstart = dualstart)

	H = np.sum([ x_i * Ei for x_i, Ei in zip(sol['x'], Es)], axis = 0)

	return H

