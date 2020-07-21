import numpy as np
import cvxopt
from itertools import product
from scipy.optimize import brentq

from .lipschitz_utils import *
from .lipschitz_solver import *
from .lipschitz_blitz import *
from .iterprinter import IterationPrinter

def descent_direction_cvxpy(X, fX, grads, U0, J0, alpha0, epsilon = 0, active_evals = None, active_grads = None):
	import cvxpy as cp

	m, r = U0.shape
	Gamma = cp.Variable((r, r), symmetric = True)
	Delta = cp.Variable((m, r))
	delta = cp.Variable(1)
	
	I = np.eye(m)

	# Setup bulk variables for convience

	H0 = U0 @ J0 @ U0.T + alpha0*(I - U0 @ U0.T)
	H1 = U0 @ Gamma @ U0.T + U0 @ J0 @ Delta.T + Delta @ J0 @ U0.T
	H1 += delta*(I - U0 @ U0.T) - alpha0*(U0 @ Delta.T + Delta @ U0.T)


	obj = cp.trace(H1)
	constraints = []

	# Orthogonality constraint
	constraints.append( U0.T @ Delta == np.zeros((r,r)) )

	#####################################################################
	# Setup evaluation constraints
	#####################################################################
	
	M = fX.shape[0]
	if active_evals is None:
		active_evals = np.triu_indices(M, k = 1)

	for i, j in zip(*active_evals):
		p = X[i] - X[j]
		constraints.append( (fX[i] - fX[j])**2 - epsilon <= p.T @ H0 @ p + p.T @ H1 @ p)
	
	#####################################################################
	# Setup gradient constraints
	#####################################################################
	N = len(grads)
	if active_grads is None:
		active_grads = range(N)

	for k in active_grads:
		constraints.append( np.outer(grads[k], grads[k]) << H0 + H1)

	constraints.append(np.zeros((m,m)) << H0 + H1)
	
	prob = cp.Problem(cp.Minimize(obj), constraints)

	prob.solve(verbose = False, solver = 'CVXOPT', abstol = 5e-8, reltol = 5e-8, feastol = 5e-8, refinement = 3)
	return Delta.value, Gamma.value, delta.value

def descent_direction(X, fX, grads, U0, J0, alpha0, epsilon = 0, active_evals = None, active_grads = None, 
	verbose = False, abstol = 1e-9, reltol = 1e-9, feastol = 1e-9, refinement = 2):

	m, r = U0.shape
	I = np.eye(m)

	# The zero-th order perturbation	
	H0 = U0 @ J0 @ U0.T + alpha0*( I - U0 @ U0.T)

	# The first order pertubation is for CVXOPT
	# sum_j E_j * x_j

	# The basis for Gamma and delta are built using 
	# the same approach as for J and alpha  
	Es = build_basis(m, U0)
	
	# For the remaining terms of Delta,
	# constructing such that orthogonality follows immediately
	DeltaBasis = []
	Q, _ = np.linalg.qr(U0, mode = 'complete')
	for i, j in product(range(m-r), range(r)):
		DeltaBasis.append(np.zeros((m,r)))
		DeltaBasis[-1][:,j] = Q[:,i+r]
	
	for Delta in DeltaBasis:
		Es.append( U0 @ J0 @ Delta.T + Delta @ J0 @U0.T - alpha0*(U0 @ Delta.T + Delta @ U0.T))

	Eten = np.array(Es)

	dims = {'l': 0, 'q': [], 's': []}

	##################################################################
	# Construct constraints corresponding to gradients
	##################################################################
	if active_grads is None:
		active_grads = range(len(grads))

	hsdp = []
	# try to ensure found point is positive semidefinite
	hsdp.append( -( - H0).flatten('F'))
	dims['s'].append(m)

	for k in active_grads:
		# H0 + H1 >> g g^T 
		hsdp.append( -(np.outer(grads[k], grads[k]) - H0).flatten('F'))
		dims['s'].append(m)
	
	##################################################################
	# Construct constraints corresponding to function evaluations
	##################################################################
	if active_evals is None:
		active_evals = np.array(np.triu_indices(len(X), k = 1))

	Gineq = []
	hineq = []
	for i, j in zip(*active_evals): 	
		p = (X[i] - X[j]).flatten()
		# Normalizing here seems to reduce the normalization once inside CVXOPT
		p_norm2 = p.T @ p
		# Vectorize to improve performance
		#G = [-p.dot(E.dot(p)) for E in Es]
		#G = -np.tensordot(np.tensordot(Eten, p/p_norm, axes = (2,0)), p/p_norm, axes = (1,0))
		G = -np.einsum('ijk,j,k->i', Eten, p, p)/p_norm2
		Gineq.append(G)
		lhs = (np.abs(float(fX[i] - fX[j])) - epsilon)**2 - float(p.T @ H0 @ p)
		hineq.append(-lhs/p_norm2)
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


	Gsdp_basis = np.vstack([E.flatten('F') for E in Es]).T

	# Setup objective
	c = np.array([ np.trace(E) for E in Es])
	G = np.vstack(Gineq + len(dims['s'])*[-Gsdp_basis] )
	h = np.hstack(hineq + hsdp)
	
	# Convert to CVXOPT format
	c = cvxopt.matrix(c)
	G = cvxopt.matrix(G)
	h = cvxopt.matrix(h)
	sol = cvxopt.solvers.conelp(c, G, h, dims = dims)

	# Convert back into matrix format
	x = sol['x']
	GammaBasis = build_basis(r, 'full')
	Gamma = np.sum([G*xi for G, xi in zip(GammaBasis, x[:len(GammaBasis)])], axis = 0)
	delta = float(x[len(GammaBasis)])
	Delta = np.sum([Delta*xi for Delta, xi in zip(DeltaBasis,x[len(GammaBasis)+1:])], axis = 0)
	return Delta, Gamma, delta


def lipschitz_matrix_partial(X, fX, grads, r, U0 = None, maxiter = 100, epsilon = 0, 
	verbose = True, ftol = 1e-7, blitz = True):

	m = X.shape[1]
	I = np.eye(m)
	M = len(X)
	N = len(grads)

	if blitz:
		lipschitz_matrix = lipschitz_matrix_blitz
	else:
		# Since H0 in cvxopt is a warm start, we disable it
		def lipschitz_matrix(*args, H0 = None, **kwargs):
			return lipschitz_matrix_cvxopt(*args, **kwargs)

	if U0 is None:
		H0 = np.zeros((m,m))
		H0 = project_evals(H0, X, fX)
		H0 = project_grads(H0, grads)

		# Eigenvalues are in increasing order
		ew, V = np.linalg.eigh(H0)
		U0 = V[:,-r:]
		U0 = U0[:,::-1]
	else:
		H0 = None
	
	U = np.copy(U0)

	# Find initial J, alpha
	H = lipschitz_matrix(X, fX, grads, basis = U, H0 = H0, verbose = verbose - 1)

	H_trace = np.trace(H)

	if verbose:
		printer = IterationPrinter(it = '4d', obj = '20.14e', decrease = '14.7e', step = '10.4e', eval_con = '7d', grad_con = '7d')
		printer.print_header(it = 'iter', obj = 'trace(H)', decrease = 'decrease', step =  'step length',
			 eval_con = 'eval. con.', grad_con = 'grad. con.')	
		printer.print_iter(obj = H_trace)
	
	for it in range(maxiter):
		# Convert back into low-rank representation
		J = U.T @ H @ U
		ew = np.linalg.eigvalsh(H)
		alpha = ew[-r-1]
	
		# Compute descent direction
		if blitz:
			tau = 1e-5
			dof = m*r + r*(r+1)//2
			eval_constraints = active_eval_constraints(H, X, fX, tau, dof)
			grad_constraints = active_grad_constraints(H, grads, tau, dof)

			II, JJ = np.triu_indices(len(X),k=1)
			active_evals = (II[eval_constraints], JJ[eval_constraints])
			active_grads = np.argwhere(grad_constraints).flatten()

			Delta, Gamma, delta = descent_direction(X, fX, grads, U, J, alpha, epsilon = epsilon,
				active_evals = active_evals, active_grads = active_grads, verbose = False)
				
		else:
			Delta, Gamma, delta = descent_direction(X, fX, grads, U, J, alpha, epsilon = epsilon)
							

		# Precompute the SVD for use with computing the geodesic step
		Y, Sigma, ZT = np.linalg.svd(Delta, full_matrices = False)

		# Prediced decrease
		pred = np.trace(Gamma) + np.trace( U @ J @ Delta.T + Delta @ J @ U.T)
		pred += delta*(m-r) - alpha*np.trace(U @ Delta.T + Delta @ U.T) 
		

		for bt in range(20):
			# Here we use the 1 suffix to denote the new values

			t = 0.5**bt		# Step length

			# Geodesic step
			U1 = U @ ZT.T @ np.diag(np.cos(Sigma * t)) @ ZT + Y @ np.diag(np.sin(Sigma*t)) @ ZT
			
			# H0 is the estimate from the search direction of what H we should have
			# at the next step
			# This helps accelerate Blitz to construct a near-optimal feasible point
			H0 = H + t* U @ Gamma @ U.T + t*(U @ J @ Delta.T + Delta @ J @ U.T)
			H0 += t*delta*(I - U @ U.T) - t*alpha*(U @ Delta.T + Delta @ U.T)

			# Compute the Lipschitz matrix using the H0 warm start
			H1 = lipschitz_matrix(X, fX, grads, basis = U1, H0 = H0, verbose = verbose - 1)

			# Objective function value
			H1_trace = np.trace(H1)

			#print("eig H1", np.linalg.eigvalsh(H1))
			# Armijo step acceptance criteria
			if H1_trace - H_trace < 0.001*pred*t:
				break
 
			# Terminate if predicted improvement is small
			if (np.abs(H1_trace - H_trace) < ftol and pred < ftol):	
				break

		# Update
		dec = H1_trace - H_trace
		
		# Print convergence data
		if verbose:
			printer.print_iter(it = it, obj = H1_trace, decrease = -dec, step = t, 
				eval_con = np.sum(eval_constraints), grad_con = np.sum(grad_constraints))
		
		if dec > 0:

			if verbose:
				print("Increased objective value; returned previous step")
			break
		else:
			H = H1
			U = U1
			H_trace = H1_trace
			
	
		if -dec < ftol*H_trace:
			if verbose:
				print("Decrease less than ftol")
			break

	return H
