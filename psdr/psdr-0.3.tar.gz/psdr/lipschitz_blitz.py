from functools import lru_cache
import numpy as np
import scipy.linalg
import cvxopt
from scipy.optimize import bisect, brentq

from .lipschitz_utils import *
from .lipschitz_utils import _quad_form, _vec_norm, _preprocess_data
from .lipschitz_solver import lipschitz_matrix_cvxopt, build_basis
from .iterprinter import IterationPrinter


def eval_step(Hf, Hi, X, fX, alpha_left = 0, alpha_right = 1):
	r""" Compute step length between Hi and Hf


	Here our goal is to compute a feasible point of the form

	..math::

		\mathbf{H} \leftarrow \alpha \mathbf{H}_i +  (1-\alpha) \mathbf{H}_f + \beta \mathbf{I}

	In standard BLITZ, we simply choose the largest :math:`\alpha` that yields
	a feasible :math:`\mathbf{H}` with res`pect to the evaluation constraints.
	Numerically there can be a problem if Hf is not strictly feasible in floating point;
	hence the perturbation :math:`\beta \mathbf{I}` is added to fix this. 


	Parameters
	----------
	Hf: np.array (m,m)
		Current feasible point
	Hi: np.array (m, m)
		Current infeasible iterate
	X: np.array (M, m)
		Location of function evaluations
	fX: np.array (M,)
		Function evaluation values


	Returns
	-------
	alpha: float
		Location along path between Hi and Hf

	beta: float
		Fudge factor to ensure feasibility

	"""
	M = len(X)
	if M == 0:
		return alpha_right, 0.

	I, J = np.triu_indices(M, k=1)
	P = (X[I] - X[J])
	pHfp = _quad_form(Hf, P)
	pHip = _quad_form(Hi, P)
	pp2 = _vec_norm(P)

	lhs = (fX[I] - fX[J])**2

	beta = max(0, -np.min((pHfp - lhs)/pp2))

	denom = pHfp - pHip 
	valid = denom > 0
	alphas = (pHfp[valid] + beta - lhs[valid])/denom[valid]
		
	return max(np.min(alphas),0), beta

# When we have access to rank-1 updates, it is faster to do all grads at once 
def grad_step(Hf, Hi, grads, alpha_right = 1):
	r""" Compute step length between Hi and Hf


	Here our goal is to compute a feasible point of the form

	..math::

		\mathbf{H} \leftarrow \alpha \mathbf{H}_i +  (1-\alpha) \mathbf{H}_f + \beta \mathbf{I}

	In standard BLITZ, we simply choose the largest :math:`\alpha` that yields
	a feasible :math:`\mathbf{H}` with res`pect to the evaluation constraints.
	Numerically there can be a problem if Hf is not strictly feasible in floating point;
	hence the perturbation :math:`\beta \mathbf{I}` is added to fix this. 


	Parameters
	----------
	Hf: np.array (m,m)
		Current feasible point
	Hi: np.array (m, m)
		Current infeasible iterate
	grads: np.array (M, m)
		Gradient evaluations

	Returns
	-------
	alpha: float
		Location along path between Hi and Hf

	beta: float
		Fudge factor to ensure feasibility
	"""
	if len(grads) == 0:
		return alpha_right, 0

	alpha_left = 0	
	m = Hf.shape[0]

	d0 = dist_grad_constraints(Hf, grads)

	# Correct possible infeasibility
	beta = max(0, -np.min(d0))
	d_left = d0 + beta

	dist = lambda a: dist_grad_constraints( (1-a)*Hf + a*Hi, grads) + beta

	d_right = dist_grad_constraints( (1-alpha_right)*Hf + alpha_right*Hi, grads) + (1-alpha_right)*beta
	
	# Right side is feasible
	if np.min(d_right) >= 0:
		return alpha_right, beta

	# Storage for corrected values at the middle
	d_mid = np.copy(d_right)
	d_mid_min = 1

	for it in range(16):
		active = d_right < 0
		# This hard codes the Illinois algorithm
		# Since smallest eigenvalue is convex as a function of alpha,
		# Regula Falsi always updates the left interval; hence we apply
		# the Illionis algorithm every other step (we have no need to check
		# the previous point is retained).
		if d_mid_min <= 0:
		#if it % 2 == 1:
			alpha_pred = (alpha_left*d_right[active] - alpha_right*d_left[active])/(d_right[active] - d_left[active])
		else:
			alpha_pred = (0.5*alpha_left*d_right[active] - alpha_right*d_left[active])/(0.5*d_right[active] - d_left[active])
		
		alpha_mid = np.nanmin(alpha_pred)
		if alpha_mid == alpha_right or alpha_mid == alpha_left:
			alpha_mid = (alpha_left + alpha_right)/2.
#			print("reverting to bisection")
		
		d_mid[active] =  dist_grad_constraints( (1-alpha_mid)*Hf + alpha_mid*Hi, grads[active]) + (1-alpha_mid)*beta
		d_mid_min = np.min(d_mid[active])
#		print(f'{alpha_left:18.10e} {alpha_mid:18.10e} {alpha_right:18.10e} {alpha_right - alpha_left: 10e} | {np.min(d_mid):10e} \t {np.sum(active)}')
		if d_mid_min >= 0:
			alpha_left = alpha_mid
			d_left[active] = d_mid[active]
		else:
			alpha_right = alpha_mid
			d_right[active] = d_mid[active]

		if alpha_right - alpha_left < 1e-12:
			break

	alpha = alpha_left
	return alpha, beta


def project_feasible(H, basis):
	r""" Project an initial H onto the avalible basis
	"""
	m = H.shape[0]
	Es = build_basis(m, basis)

	G = np.vstack([E.flatten('F') for E in Es]).T
	h = H.flatten('F') 
	c = np.array([np.trace(E) for E in Es])
	dims = {'l': 0, 'q': [], 's': [m]}
	G = cvxopt.matrix(-G)
	h = cvxopt.matrix(-h)
	c = cvxopt.matrix(c)
	cvxopt.solvers.options['show_progress'] = False
	sol = cvxopt.solvers.conelp(c, G, h, dims = dims)
	
	return  np.sum([ x_i * Ei for x_i, Ei in zip(sol['x'], Es)], axis = 0)
		


def active_eval_constraints(H, X, fX, tau, dof):
	M = len(X)
	if M == 0:
		return np.zeros(0, dtype = np.bool)

	m = H.shape[0]
	dist = dist_eval_constraints(H, X, fX)
	d = np.sort(dist)
	threshold = max(d[min(dof, len(d)-1)], 0) + tau
	#print(f"eval threshold {threshold:16.7e}", "d", d[0:50])
	return dist <= threshold

def active_grad_constraints(H, grads, tau, dof):
	N = len(grads)
	if N == 0:
		return np.zeros(0, dtype = np.bool)
	
	m = H.shape[0]
	dist = dist_grad_constraints(H, grads)
	d = np.sort(dist)
	k = max(int(np.floor(np.sqrt(2*dof) - 1)),0)	# Roughly number of grad required to fit dof
	threshold = max(d[min(k, len(d)-1)], 0) + tau
	#print(f"grad threshold {threshold:16.7e}", "d", d[0:50])
	
	return dist <= threshold


def lipschitz_matrix_blitz(X = None, fX = None, grads = None, maxiter = 100, verbose = False, 
	xtol = 1e-7, tau = None, warmstart = False, H0 = None, basis = 'full', r = None,
	initial = 'identity'):
	r""" Estimate the Lipschitz matrix using the Blitz working set approach
	""" 

	if tau is None and r is None:
		r = 0.85

	# Ensure data is in a reasonable format	
	X, fX, grads = _preprocess_data(X, fX, grads)

	# Dimension of ambient space
	m = X.shape[1]
	M = len(fX)

	# Construct a solution to the unconstrained problem;
	# this is called x in the JG15.
	# For the Lipschitz matrix, this is simply the zero matrix
	H_infeasible = np.zeros((m,m))

	# We now find a feasible (but suboptimal) point
	# based on projecting onto the feasible cone for each constraint
	# This is called y in JG15
	
	if H0 is None:
		# If we haven't been provided an initial H0, 
		# simply start with zeros
		H_feasible = np.zeros((m,m))
		if initial == 'identity':
			dist_eval = dist_eval_constraints(H_feasible, X, fX)
			dist_grad = dist_grad_constraints(H_feasible, grads)
			H_feasible = np.eye(m)*np.max(-np.hstack([dist_eval, dist_grad]))
			dist_grad = dist_grad_constraints(H_feasible, grads)
		elif initial == 'projection':
			# Now project the initial feasible point onto the 
			# feasible cones for the evaluations and gradients
			# irrespective of the basis for H
			H_feasible = project_evals(H_feasible, X, fX)
			H_feasible = project_grads(H_feasible, grads)
		else:
			raise ValueError("Invalid value of 'initial' provided")
	else:
		# Otherwise, make sure this is a matrix
		H_feasible = np.array(H0)
		assert H_feasible.shape == (m,m)
	
	
	
	if not isinstance(basis, str):
		# If we have been provided a basis, ensure the initial
		# feasible H satisfies this construction
		H_feasible = project_feasible(H_feasible, basis)
	
		U = basis
		r = U.shape[1]
		# The additional degree of freedom seems necessary 
		dof = (r*(r+1))//2 + 1
		dof_eval = dof 
		dof_grad = r
	elif basis == 'full':
		U = None
		dof = m*(m+1)//2
		dof_eval = dof 
		dof_grad = m
	elif basis == 'diag':
		U = None
		dof = m 
		dof_eval = dof 

	# Determine which constraints are currently active	
	active_eval_Hi = np.zeros(M*(M-1)//2, dtype = np.bool)
	active_grad_Hi = np.zeros(len(grads), dtype = np.bool)

	# Ordering used for evaluation constraints
	eval_idx = np.array(np.triu_indices(len(X), k = 1))

	# Data for warmstarting H
	Hi_dist_eval = None
	Hi_dist_grad = None

	if verbose:
		printer = IterationPrinter(it = '4d', obj = '22.15e', gap = '10.4e', alpha = '10.4e',
			beta = '10.4e', tau = '10.4e', eval_con = '5d', eval_act = '5d', grad_con = '5d', grad_act = '5d',  work_feas = '10.3e', 
			all_feas = '10.3e')
		printer.print_header(it = 'iter', obj = 'Trace(Hf)', gap = 'gap', alpha = 'alpha', eval_con = 'eval con',
				eval_act = 'eval act', grad_con = 'grad con', grad_act = 'grad act',  work_feas = 'Hi feas.', beta = 'beta', all_feas = 'Hf feas.',
				tau = 'tau')


	dof_bonus = 0

	# Main loop in Blitz
	for it in range(maxiter):

		# STEP 1
		# Compute alpha such that H(alpha) is feasible where 
		# H(alpha) = (1-alpha)*H_feasible + alpha*H_infeasible
	
		if it == 0:
			# Due to the construction of H_feasible, one of the constraints will be binding
			# and the line search will terminate with zero length
			alpha = 0	
			beta = 0
		else:
			alpha, beta_eval = eval_step(H_feasible, H_infeasible, X, fX)
			alpha, beta_grad = grad_step(H_feasible, H_infeasible, grads, alpha_right = alpha) 
			beta = max(beta_grad, beta_eval)

		# STEP 2: Update the feasible point
		H_feasible = (1-alpha)*(H_feasible + beta*np.eye(m)) + alpha*H_infeasible 


		# STEP 3: Compute active constraints

		# We want at least one additional constraint so that we generate 
		# a new set of active constraints at the next iteration
		# however, if we fail to produce a substantial step, increase the number
		# of constraints that will be active 
		# NB: this is rarely ever called and so I cannot be sure it actually helps
		if alpha < 1e-8:
			dof_bonus += 1
		else:
			dof_bonus = 1

		tau = 0

		if False:
			dist_eval = dist_eval_constraints(H_feasible, X, fX)
			dist_grad = dist_grad_constraints(H_feasible, grads)
			# Determine threshold
			d = np.sort(np.hstack([dist_eval, dist_grad]))
			k = min(dof + dof_bonus, len(d)-1)
			tau = max(d[k], 0) + 1e-8
			active_evals = ((dist_eval) <= tau) | active_eval_Hi
			active_eval_new = active_evals ^ active_eval_Hi
			active_grads = (dist_grad <= tau) | active_grad_Hi
			active_grad_new = active_grads ^ active_grad_Hi

		if len(X) > 0:
			dist_eval = dist_eval_constraints(H_feasible, X, fX)
			d = np.sort(dist_eval)
			k = min(dof_eval + dof_bonus, len(d)-1)
			threshold = max(d[k], 0) + 1e-9
			active_evals = ((dist_eval) <= threshold) | active_eval_Hi
			active_eval_new = active_evals ^ active_eval_Hi

			tau = max(tau, threshold)
		else:
			active_evals = np.ones(0, dtype = np.bool)
			active_eval_new = np.zeros(0, dtype = np.bool)	

		if len(grads)> 0:	
			dist_grad = dist_grad_constraints(H_feasible, grads)
			d = np.sort(dist_grad)
			k = min(dof_grad + dof_bonus, len(d)-1)
			threshold = max(d[k], 0) + 1e-9
			active_grads = (dist_grad <= threshold) | active_grad_Hi
			active_grad_new = active_grads ^ active_grad_Hi
			
			tau = max(tau, threshold)
		else:	
			active_grads = np.ones(0, dtype = np.bool)
			active_grad_new = np.zeros(0, dtype = np.bool)	
	
		# STEP 4: Solve convex program with reduced list of constraints
		
		# STEP 4.1.2 Make old infeasible solution feasible with respect to the current active constraints
		# the new gradient constraints that weren't active on the previous iteration
		# project the old infeasible point
		if warmstart:
			if it  == 0:
				#H0 = np.copy(H_feasible) + 1e-10*np.eye(m)
				H0 = None	 # This seems to do better
			else:
				# As there are new active constraints, we need to update Hi
				# to incorporate this information
				beta = 0
				if Hi_dist_eval is not None:
					beta = max(beta, -np.min(Hi_dist_eval[active_evals]))
				if Hi_dist_grad is not None:
					beta = max(beta, -np.min(Hi_dist_grad[active_grads]))
				H0 = H_infeasible + (beta+1e-10)*np.eye(m)
		else:
			H0 = None

		
		# Solve semidefinite program with respect to active constraints
		H_infeasible = lipschitz_matrix_cvxopt(X, fX, grads,
			active_evals = (eval_idx[0, active_evals], eval_idx[1, active_evals]),
			active_grads = np.argwhere(active_grads), 
			verbose = (verbose - 1) and verbose, 
			H0 = H0, 
			basis = basis)

		#print(tau, np.linalg.norm(H_feasible - H_infeasible, 'fro'))

		# Due to finite precision, H_infeasible may not exactly satisfy the active constraints
		# hence we nudge this matrix slightly to be feasible 

		beta = 0	# The amount we will nudge Hi by

		if len(X) > 0:
			Hi_dist_eval = dist_eval_constraints(H_infeasible, X, fX)
			beta_eval = max(0, -np.min(Hi_dist_eval[active_evals]))
			beta = max(beta, beta_eval)
			# Compute which evaluation constraints were active for the next iteration
			active_eval_Hi = ( Hi_dist_eval < 1e-7) & active_evals
		else:
			active_eval_Hi = np.zeros(0, dtype = np.bool)

		if len(grads) > 0:
			Hi_dist_grad = dist_grad_constraints(H_infeasible, grads)
			beta_grad = max(0, -np.min(Hi_dist_grad[active_grads]))
			beta = max(beta, beta_grad)
			# Compute which gradient constraints were active for the next iteration
			active_grad_Hi = ( Hi_dist_grad < 1e-7) & active_grads
		else:
			active_eval_Hi = np.zeros(0, dtype = np.bool)

	
		H_infeasible += beta * np.eye(m)	

		# Compute how feasible H_infeasible is with respect to all the constraints
		work_feas = 0
		if len(X) > 0:	
			work_feas = np.min(Hi_dist_eval + beta)
		if len(grads) > 0:
			work_feas = min(work_feas, np.min(Hi_dist_grad + beta))

		
		H_delta = np.linalg.norm(H_feasible - H_infeasible, 'fro')

		if verbose:
			all_feas = np.inf
			if len(X) > 0:
				all_feas = np.min(dist_eval_constraints(H_feasible, X, fX))
			if len(grads) > 0:
				all_feas = min(all_feas, np.min(dist_grad_constraints(H_feasible, grads)) )
			printer.print_iter(it = it, obj = np.trace(H_feasible), gap = H_delta, 
				alpha = alpha, eval_con = np.sum(active_evals), grad_con = np.sum(active_grads),
				eval_act = np.sum(active_eval_Hi), grad_act = np.sum(active_grad_Hi),
				work_feas = work_feas, beta = beta, all_feas = all_feas, tau = tau) 

		if H_delta < xtol*np.linalg.norm(H_infeasible, 'fro'):
			if verbose: print("Small mismatch between feasible and infeasible iterates\n")
			return H_feasible

		if np.all(active_evals) and np.all(active_grads):
			if verbose: print("All constraints active at current iterate\n")
			return H_infeasible

		if work_feas >= 0:
			if verbose: 
				printer.print_iter(it = it, obj = np.trace(H_infeasible), 
				)
			if verbose: print("Working set solution satisfies all constraints\n")
			return H_infeasible



	if verbose:
		print('Reached iteration limit\n')
	return H_feasible

  
