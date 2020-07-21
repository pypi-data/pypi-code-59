from __future__ import print_function, division
import numpy as np
import cvxpy as cp

def _obj_step(Hc, rho):
	#H = cp.Variable(Hc.shape, PSD = True)
	#obj = cp.trace(H) + rho/2*cp.norm(H - Hc, 'fro')**2
	#prob = cp.Problem(cp.Minimize(obj))
	#prob.solve()
	#return H.value
	ew, ev = np.linalg.eigh(Hc)
	#H = ev.dot(np.diag(np.maximum(ew - np.min(ew)*2, 0))).dot(ev.T)
	H = ev.dot(np.diag(np.maximum(ew - 1., 0))).dot(ev.T)
	
	#lam = np.linalg.eigvalsh(Hc)
	#H = Hc - np.eye(*Hc.shape)*np.min(lam)
	return H 

def _constraint_grad_cvxpy(grads, Hc):
	r""" Find closest point obeying constraint
	"""
	H = cp.Variable(Hc.shape, PSD = True)
	obj = cp.norm(H - Hc, 'fro')**2
	con = [ np.outer(grad, grad) << H for grad in grads]
	prob = cp.Problem(cp.Minimize(obj), con)
	prob.solve()
	return H.value

def _constraint_grad(grad, Hc):
	r""" Find closest point obeying constraint
	"""
	# TODO: Use DLAED9 instead for DSR1 problem
	ew, ev = np.linalg.eigh(Hc - np.outer(grad, grad))
	H = ev.dot(np.diag(np.maximum(ew, 0))).dot(ev.T) + np.outer(grad, grad)
	return H

def lipschitz_matrix_consensus_admm_v1(X = None, fX = None, grads = None, rho = 1e-2, maxiter = 100):
	r""" Estimate the Lipschitz matrix using a consensus ADMM approach
	"""
	m = grads.shape[1]
	
	Hx = np.zeros((m,m))
	#Hz = _constraint_grad_cvxpy(grads, Hx)

	Hz = np.copy(Hx)
	Hu = np.zeros((m,m))

	for it in range(maxiter):
		Hx_old = Hx
		Hx = _obj_step(Hz - Hu, rho)
		print(np.linalg.norm(Hx - Hx_old, 'fro'))
		Hz = _constraint_grad_cvxpy(grads, Hx + Hu)
		Hu = Hu + Hx - Hz

	return Hx

def lipschitz_matrix_consensus_admm(X = None, fX = None, grads = None, rho = 100, maxiter = 1000):
	r""" Estimate the Lipschitz matrix using a consensus ADMM approach
	"""
	m = grads.shape[1]

	H0 = sum([np.outer(g,g) for g in grads]) 

	Hs = [np.copy(H0) for k in range(len(grads))]
	Hm = np.copy(H0)
	Ys = [np.zeros((m,m)) for k in range(len(grads))]	
	
	for it in range(maxiter):

		for k in range(len(grads)):
			Hhat = Hs[k] - 1./rho*(np.eye(m) + Ys[k])
			g = grads[k]
			ew, ev = np.linalg.eigh(Hhat - np.outer(g,g)) 
			Hs[k] = np.outer(g,g) + ev.dot(np.diag(np.maximum(0, ew))).dot(ev.T)
		
		# Update the mean solution
		Hm = sum(Hs)/len(Hs)

		# Update Lagrange multipliers
		for k in range(len(grads)):
			Ys[k] += rho*( Hs[k] - Hm)
			if k == 0:
				print(np.linalg.svd(Ys[k])[1])

			#lam = np.trace(Hm)/np.linalg.norm(grads[k])**4
			#Ys[k] = -0*np.eye(m) + lam*np.outer(grads[k], grads[k])
			#ew, ev = np.linalg.eig(Hs[k])
			#u = ev[-1]
			#lam =  -np.trace(Hs[k] - Hm)/np.trace(np.outer(u,u).dot(Hs[k]-Hm))
			#Ys[k] = np.eye(m) + lam*np.outer(u,u)

		# Evaluate lack of satisfaction of constraints
		err = 0
		move = 0
		for k in range(len(grads)):
			err_k = np.min(np.linalg.eigvalsh(Hm - np.outer(grads[k], grads[k])))
			err -= np.minimum(err_k, 0)
			move += np.linalg.norm(Hm - Hs[k],'fro')
		print('%4d | %8.4e | %8.4e | %8.4e' % (it, err, move, np.trace(Hm)))

	return Hm
