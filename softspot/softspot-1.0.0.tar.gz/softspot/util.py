import numpy as np



def normalize_and_remove_translations(z, ndim, npart):
    remove_translations(z, ndim, npart)
    normalize(z)

def normalize(z):
    np.copyto( z, z/np.linalg.norm(z) )

def remove_translations(z, ndim, npart):
    for alpha in range(ndim):
        z[alpha::ndim] -= np.mean( z[alpha::ndim] )

def conjugate_gradient(b, apply_matrix_function, x0, options={'tol': 1e-10, 'max_iterations': 10000}):
    """
    does not normalize at the end
    """
    tol = options['tol']
    maxiter = options['max_iterations']
    n = b.size
    x = np.copy(x0)

    r  = np.ones(n)
    Ap = np.ones(n)
    r = apply_matrix_function(x)
    r = b - r
    p = np.copy(r)
    r_k_norm = np.dot(r.T, r)
    converged = False
    for k in range(1, maxiter+1):
        Ap = apply_matrix_function(p)
        alpha = r_k_norm / np.dot(p.T, Ap)
        x += alpha*p
        r -= alpha*Ap
        r_kplus1_norm = np.dot(r.T, r)
        beta     = r_kplus1_norm / r_k_norm
        r_k_norm = r_kplus1_norm
        if(np.sqrt(r_kplus1_norm) < tol):
            converged = True
            break
        p = r + beta*p

    return {'x': x, 'converged': converged, 'iterations': k}
