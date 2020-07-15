import numpy as np
from macopt import Macopt

from softspot.softspot_wrap import softspot_module
from softspot.util import normalize_and_remove_translations, conjugate_gradient



class SoftSpot:
    """
    Parameters
    ----------

    ndim : int
        The dimensionality of the system under consideration.
    npart : int
        The number of particles.
    hessian : scipy.sparse.csr_matrix
        Hessian matrix in scipy's `Compressed Sparse Row representation <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html>`_.
    pair_lookup : array_like
        Numpy array of shape ``(num_contacts, 2)`` with ``dtype=int`` containing particle pairs for calculating ``sum_zij_squared`` (and its gradient) — the denominator of Eq. 2 of the paper. For example, ``pair_lookup[0] == [4, 5]`` indicates that particles 4 and 5 will contribute to ``sum_zij_squared``. Default is ``None``: in most use cases — *i.e.*, short-range potentials — the relevant particle pairs can be automatically derived from the Hessian matrix, and will coincide with the interacting pairs. In this case, the user does not have to specify this field. In the case of long-range interactions, the user might want to manually specify only nearby pairs to calculate ``sum_zij_squared``, in order to effectively penalize modulating (phonon) fields in the cost function (see discussion below Eq. 3 in the paper). 


    Example
    -------
    .. code-block:: python

        import numpy as np

        # Example for a high-parent-temperature 2D SWAP system
        # consisting of 4096 particles.
        # See iPython tutorial for more details.
        np.random.seed(1)
        ndim = 2
        npart = 4096
        z_init = np.random.rand((ndim*npart))
        soft_spot = SoftSpot(ndim=ndim, npart=npart, hessian=hessian)
        result = soft_spot.find(z_init, mode='cg')
        # => {
        #    'pi': array([-0.00445838,  0.00169628, -0.00328873, ...,  0.00055183, -0.00468846,  0.00158765]),
        #    'kappa': 3.7748011979346128,
        #    'cost_function': 36.194330960051445
        #    'converged': True,
        #    'tol': 9.87820288575708e-11,
        #    'iterations': 1085,
        # }
    """
    default_options_cg = {'tol': 1e-10, 'max_iterations': 100000}
    default_options_mapping = {'tol': 1e-10, 'tol_cg': 1e-10, 'max_iterations': 20000, 'max_iterations_cg': 10000}

    def __init__(self, ndim, npart, hessian, pair_lookup=None):
        self.ndim    = ndim
        self.npart   = npart
        self.hessian = hessian

        if pair_lookup is not None: # contact map provided by the user
            self.pair_count  = len(pair_lookup)
            self.pair_lookup = np.array(pair_lookup).astype(int)
        else: # contact map constructed from the Hessian
            self.build_contact_map()

    def find(self, z_init, mode='cg', options={}):
        """
        Finds a pseudo-harmonic mode of the system. This is the main interface for regular users. 

        Parameters
        ----------

        z_init : array_like
            Initial direction on the energy landscape from which to start the optimization. Must be a 1-D numpy array of size ``npart * ndim``.
            Before the optimization starts, ``z_init`` will be made translation-free (since by assumption the potential energy is translationally invariant)
            and will be normalized.
        mode : str
            Either ``'cg'`` (default) or ``'mapping'``. If ``'cg'``, will minimize the cost function with a `conjugate gradient minimizer <https://macopt.readthedocs.io/en/latest/>`_. If ``'mapping'``, will repeatedly apply the mapping (Eq. 4 of the paper) until convergence.
        options : dict, optional
            Dictionary of solver options.

            When mode is ``'cg'``, the most pertinent options are:

                tol : float
                    Tolerance criterion for the dimensionless norm of the gradient. Default: ``1e-10``.
                max_iterations : int
                    Maximum number of iterations. Default: ``100000``.

            In general, all possible options of the `Macopt <https://macopt.readthedocs.io/en/latest/>`_ conjugate gradient minimizer may be supplied,
            except for the ``normalize_function``, which is overridden.

            When mode is ``'mapping'``, the possible options are

                tol : float
                    Tolerance criterion for the convergence of the mapping. Default: ``1e-10``.
                tol_cg: float
                    Tolerance criterion for the conjugate gradient iterative linear solver of the equation ``H x = zeta`` (see Eqs. 4 and 5 of the paper). Default: ``1e-10``.
                max_iterations : int
                    Maximum times to iteratively apply the mapping. Default: ``20000``.
                max_iterations_cg : int
                    Maximum iterations for the conjugate gradient iterative linear solver of the equation ``H x = zeta`` (see Eqs. 4 and 5 of the paper). Default: ``10000``.

        Returns
        -------

        result : dict

            Dictionary with the result of the optimization.

                pi : array_like
                    Pseudo-harmonic mode resulting from the optimization.
                kappa : float
                    Stiffness of ``pi``.
                cost_function : float
                    Value of the cost function at the minimum ``pi``.
                iterations : int
                    Number of iterations.
                tol : float
                    Final tolerance.
                converged : bool
                    ``False`` if the optimization did not converge, ``True`` otherwise.
        """
        self._normalize_and_remove_translations(z_init)

        if mode == 'cg':
            options = {**self.default_options_cg, **options}
            options['normalize_function'] = self._normalize_and_remove_translations
            result = Macopt(self.gradient_cost_function, z_init, options).minimize()
            result['pi'] = result.pop('x')  # rename the general name 'x' to the more specific 'pi'.
        elif mode == 'mapping':
            options = {**self.default_options_mapping, **options}
            result = self._iterate_mapping(z_init, options)
        else:
            raise RuntimeError("The only possible modes are 'cg' and 'mapping'.")

        result['kappa'] = np.dot( self.hessian.dot(result['pi']), result['pi'])
        result['cost_function'] = self.cost_function(result['pi'])
        return result

    def build_contact_map(self):
        rows, cols = self.hessian.nonzero()
        rows_ij = (rows[:]/self.ndim).astype(int)
        cols_ij = (cols[:]/self.ndim).astype(int)

        pair_lookup = []
        for i in range(self.npart):
            idj = cols_ij[ np.where(rows_ij == i)[0] ]
            idj = idj[ :int(len(idj) / self.ndim):self.ndim ]
            for jj in idj[ np.logical_and(idj != i, idj > i) ]:
                pair_lookup.append([i, jj])
        
        self.pair_count  = len(pair_lookup)
        self.pair_lookup = np.array(pair_lookup).astype(int)

    def cost_function(self, z):
        """
        Returns the value of the cost function ``C(z) = (H:zz)^2 / sum_zij_squared`` (see Eq. 2 of the paper).
        This function is not called by the user in the regular use case of this class, but may be used by to those who wish to implement their own optimization schemes.

        Parameters
        ----------

        z : array_like
            Direction on the energy landscape. Must be a 1-D numpy array of size ``npart * ndim``.

        """
        sum_zij_squared = softspot_module.sum_zij_squared(self.pair_lookup, z, self.ndim, self.npart, self.pair_count)
        kappa = np.dot( self.hessian.dot(z), z)

        return kappa*kappa / sum_zij_squared

    def gradient_cost_function(self, z):
        """
        Returns the gradient of the cost function ``C(z) = (H:zz)^2 / sum_zij_squared`` (Eq. 2 of the paper).
        This function is not called by the user in the regular use case of this class, but may be used by to those who wish to implement their own optimization schemes.

        Parameters
        ----------

        z : array_like
            Direction on the energy landscape. Must be a 1-D numpy array of size ``npart * ndim``.

        Returns
        -------

        gradient : array_like
            Gradient of the cost function.
        convergence : float
            Convergence criterion; this is the dimensionless norm of the gradient:

            ``np.sqrt( np.dot(gradient, gradient)  / np.dot(hesOnZ, hesOnZ)) / kappa``, where ``hesOnZ`` is the Hessian applied to ``z``, and ``kappa`` is the stiffness of ``z``.
        """

        normalize_and_remove_translations(z, self.ndim, self.npart)

        hesOnZ  = self.hessian.dot(z)
        kappa = np.dot(hesOnZ, z)
        sum_zij_squared      = softspot_module.sum_zij_squared(self.pair_lookup, z, self.ndim, self.npart, self.pair_count)
        sum_zij_squared_grad = softspot_module.sum_zij_squared_grad(self.pair_lookup, z, self.ndim, self.npart, self.pair_count)

        gradient = 4.*kappa*hesOnZ/sum_zij_squared - ( kappa*kappa/(sum_zij_squared*sum_zij_squared) )*sum_zij_squared_grad

        typical_grad_barrier = np.sqrt( np.dot(gradient, gradient) / z.shape[0] )
        typical_grad_scale = kappa*np.sqrt( np.dot(hesOnZ, hesOnZ) / z.shape[0] )
        convergence = typical_grad_barrier / typical_grad_scale

        return gradient, convergence

    def _iterate_mapping(self, z_init, options):
        cg_options = {'max_iterations': options['max_iterations_cg'], 'tol': options['tol_cg']}
        z0_cg = np.zeros_like(z_init)
        tol = options['tol']
        max_iterations = options['max_iterations']
        z = np.copy(z_init)

        converged = False
        for it in range(1, max_iterations + 1):
            z, convergence = self.mapping(z, z0_cg, cg_options)
            if convergence < tol:
                converged = True
                break

        result = {'pi': z, 'iterations': it, 'tol': convergence, 'converged': converged}
        return result

    def mapping(self, z, z0_cg, options):
        """
        Returns the result of applying the mapping once to the vector ``z`` (see Eq. 4 of the paper).
        This function is not called by the user in the regular use case of this class, but may be used by to those who wish to implement their own optimization schemes.

        Parameters
        ----------

        z : array_like
            Direction on the energy landscape. Must be a 1-D numpy array of size ``npart * ndim``.
        z0_cg : array_like
            Initial vector for the conjugate gradient iterative linear solver of the equation ``H x = zeta`` (See Eqs. 4 and 5 of the paper).
        options : dict
            Options for the conjugate gradient iterative linear solver of the equation ``H x = zeta`` (See Eqs. 4 and 5 of the paper).
            Must contain the options ``tol_cg`` and ``max_iterations_cg`` described in the ``find`` method.

        Returns
        -------

        mapped_z : array_like
            Result of applying the mapping to ``z``.
        convergence : float
            Convergence criterion ``np.linalg.norm(mapped_z - z) / npart``.

        """
        zeta = softspot_module.sum_zij_squared_grad(self.pair_lookup, z, self.ndim, self.npart, self.pair_count)
        result = conjugate_gradient(zeta, self._apply_hessian, z0_cg, options=options)
        hess_inv_zeta, converged = result['x'], result['converged']

        if not converged:
            raise RuntimeError("Conjugate gradient iterative solver for H x = zeta did not converge.")
        
        mapped_z = hess_inv_zeta / np.linalg.norm(hess_inv_zeta)
        convergence = np.linalg.norm(mapped_z - z) / np.sqrt(z.shape[0])

        return mapped_z, convergence

    def _normalize_and_remove_translations(self, x):
        normalize_and_remove_translations(x, self.ndim, self.npart)

    def _apply_hessian(self, z):
        return self.hessian.dot(z)
