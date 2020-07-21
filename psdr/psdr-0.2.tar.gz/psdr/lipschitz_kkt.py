import numpy as np
import cvxopt, cvxopt.misc


		



def lipschitz_matrix_cvxopt(X, fX, grads, active_evals = None, active_grads = None, epsilon = 0, structure = 'full',
	verbose = True, abstol = None, reltol = None, feastol = None, refinement = None, kktsolver = None,
	H0 = None):
	r"""
	"""
	m = X.shape[1]
	# Build the basis for symmetric positive definite matrices
	Es = []
	I = np.eye(m)
	if structure == 'full':
		for i,j in zip(*np.triu_indices(m)): 
			if j == i:
				ei = I[:,i]
				Es.append(np.outer(ei,ei))
			else:
				ej = I[:,j]
				Es.append(0.5*np.outer(ei+ej,ei+ej))

	elif structure == 'diag':
		for i in range(m):
			ei = I[:,i]
			Es.append(np.outer(ei,ei))
	else:
		raise NotImplementedError	
	 
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
		active_grads = np.ones(len(grads), dtype = np.bool)

	for k in np.argwhere(active_grads):
		hsdp.append( -np.outer(grads[k], grads[k]).flatten('F'))
		dims['s'].append(m)

	##################################################################
	# Construct constraints corresponding to function evaluations
	##################################################################
	eval_idx = np.array(np.triu_indices(len(X), k = 1))
	if active_evals is None:
		active_evals = np.ones(eval_idx.shape[1], dtype = np.bool)

	Gineq = []
	hineq = []
	for k in np.argwhere(active_evals): 	
		i,j = eval_idx[:,k]
		p = (X[i] - X[j]).flatten()
		# Normalizing here seems to reduce the normalization once inside CVXOPT
		p_norm = np.linalg.norm(p)	
		# Vectorize to improve performance
		#G = [-p.dot(E.dot(p)) for E in Es]
		G = -np.tensordot(np.tensordot(Eten, p/p_norm, axes = (2,0)), p/p_norm, axes = (1,0))
		Gineq.append(G)
		hineq.append(-(np.abs(float(fX[i] - fX[j])) - epsilon)**2/p_norm**2)
		dims['l'] += 1

	Gineq = np.vstack(Gineq)
	

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
	c = cvxopt.matrix(np.array([ np.trace(E) for E in Es]))
	G = cvxopt.matrix(np.vstack([Gineq] + len(dims['s'])*[-Gsdp_basis] ))
	h = cvxopt.matrix(np.hstack(hineq + hsdp))
	Aeq = cvxopt.spmatrix([], [],[], (0, c.size[0]))

	def kktsolver(W):
		K = dims['l'] + m**2 * len(dims['s'])
		A = np.zeros((K,c.size[0]))
		b = np.zeros(K)

		di = np.array(W['di']).flatten()	
		A[:dims['l'],:] = np.diag(di) @ Gineq
		for k in range(len(dims['s'])):
			RTinv = np.array(W['rti'][k])
			for row in range(c.size[0]):
				U = -Gsdp_basis[:,k].reshape(m,m)
				A[dims['l']+k*m**2:dims['l']+(k+1)*m**2,row] = (RTinv.T @ U @ RTinv).flatten('F')

		Q, R = np.linalg.qr(A)
		
		RR = R.T @ R
		
		def f_new(bx, by, bz):
			rhs = np.array(bx)
				

		factor = cvxopt.misc.kkt_qr(G, dims, Aeq)
		f_qr = factor(W)
		def f(bx, by, bz):
			bx1 = cvxopt.matrix(bx)
			by1 = cvxopt.matrix(by)
			bz1 = cvxopt.matrix(bz)
			# Run the working version from cvxopt
			f_qr(bx, by, bz)

			# run my version
			f_new(bx1, by1, bz1)
			print(bx)
			print(bx1)
		return f
	
	sol = cvxopt.solvers.conelp(c, G, h, dims = dims, kktsolver = kktsolver)
	alpha = sol['x']
	H = np.sum([ alpha_i * Ei for alpha_i, Ei in zip(alpha, Es)], axis = 0)
	return H
