#!/usr/bin/python

# vim: set expandtab ts=4 sw=4:

import numpy as np
from scipy import ndimage
from anamnesis import AbstractAnam, register_class

from . import util


class AbstractModelFit(AbstractAnam):
    """
    Class for performing a GLM fit and storing results
    """

    hdf5_outputs = ['betas', 'copes', 'varcopes', 'coapes', 'fstats',
                    'beta_dimlabels', 'cope_dimlabels',
                    'good_observations', 'dof_error', 'dof_model',
                    'ss_total', 'ss_model', 'ss_error', 'time_dim',
                    'regressor_names', 'contrast_names', 'ftest_names']

    def __init__(self, design=None, data_obj=None, standardise_data=False, tags=None, fit_args=None):
        """Computes a GLM fit on a defined model and a dataset.

        Parameters
        ----------

        design : GLMDesign instance
            Design object defined by GLMDesign

        data_obj : TrialGLMData or ContinuousGLMData instance
            Data object defined by TrialGLMData or ContinuousGLMData

        standardise_data : boolean (optional, default=False)
            Boolean flag indicating whether to z-transform input data prior to
            fitting.

        Returns
        -------
            GLMFit instance

        """
        AbstractAnam.__init__(self)

        # In case we're initialising in a classmethod (probably a better solution for this somewhere...)
        if design is None or data_obj is None:
            return

        design.sanity_check()

        # Collapse all dimensions apart from the observations
        # Parameters and COPEs are returned in the original data dimensions at the end
        data = data_obj.get_2d_data()

        if standardise_data:
            data = util.standardise_data(data)
            self.is_standardised = True
        else:
            self.is_standardised = False

        # Store a copy of the design matrix
        self.design_matrix = design.design_matrix

        # Compute number of valid observations (observations with NaNs are ignored)
        self.good_observations = np.isnan(data.sum(axis=1)) == False  # noqa: E712

        # Adjust degrees of freedom for bad samples
        n_bad_samples = design.num_observations - self.good_observations.sum()
        self.dof_error = design.dof_error - n_bad_samples
        self.dof_model = self.dof_error - np.linalg.matrix_rank(self.design_matrix)

        # Compute the paramter estimates
        self.compute_betas(design.design_matrix[self.good_observations, :],
                           data[self.good_observations, :],
                           fit_args=fit_args)

        # Compute contrasts
        self.copes = design.contrasts.dot(self.betas)
        self.coapes = design.contrasts.dot(np.abs(self.betas))

        # Compute varcopes
        self.varcopes = np.zeros((design.num_contrasts, data.shape[1]))

        # Compute sum squares for data and residuals
        self.ss_total = np.sum(np.power(data[self.good_observations, :], 2), axis=0)
        self.ss_model = np.sum(np.power(self.get_prediction(), 2), axis=0)
        self.ss_error = np.sum(np.power(self.get_residuals(data[self.good_observations, :]), 2), axis=0)

        # Compute varcopes
        residue_forming_matrix = np.linalg.pinv(
            design.design_matrix[self.good_observations, :].T.dot(design.design_matrix[self.good_observations, :]))
        var_forming_matrix = np.diag(np.linalg.multi_dot([design.contrasts,
                                                         residue_forming_matrix,
                                                         design.contrasts.T]))

        # This is equivalent to >> np.diag( resid.T.dot(resid) )
        resid = self.get_residuals(data[self.good_observations, :])
        self.resid_dots = np.einsum('ij,ji->i', resid.T, resid)
        del resid
        V = self.resid_dots / design.dof_error
        self.varcopes = var_forming_matrix[:, None] * V[None, :]

        # Compute F-tests if defined
        if design.ftests is None:
            self.fstats = None
        else:
            self.fstats = np.zeros((design.num_ftests, data.shape[1]))

            for jj in range(design.num_ftests):
                cont_ind = design.ftests[jj, :].astype(bool)
                C = design.contrasts[cont_ind, :]
                D = design.design_matrix

                a = np.linalg.pinv(D.T.dot(D))
                b = np.linalg.pinv(np.linalg.multi_dot([C, a, C.T]))

                for ii in range(data.shape[1]):

                    B = self.betas[:, ii]
                    c = np.linalg.multi_dot([B.T, C.T, b, C, B])

                    num = c / np.linalg.matrix_rank(C)
                    denom = self.resid_dots[ii] / self.dof_error

                    self.fstats[jj, ii] = num / denom

        # Restore original data shapes
        self.betas = data_obj.unsquash_array(self.betas)
        self.copes = data_obj.unsquash_array(self.copes)
        self.coapes = data_obj.unsquash_array(self.coapes)
        self.varcopes = data_obj.unsquash_array(self.varcopes)
        if self.fstats is not None:
            self.fstats = data_obj.unsquash_array(self.fstats)

        self.ss_total = data_obj.unsquash_array(self.ss_total[None, :])
        self.ss_error = data_obj.unsquash_array(self.ss_error[None, :])
        self.ss_model = data_obj.unsquash_array(self.ss_model[None, :])

        self.regressor_names = design.regressor_names
        self.contrast_names = design.contrast_names
        self.ftest_names = design.ftest_names
        if 'time_dim' in data_obj.info and data_obj.info['time_dim'] is not None:
            self.time_dim = data_obj.info['time_dim']
        else:
            self.time_dim = None
        self.tags = tags

        self.beta_dimlabels = list(('Regressors',
                                    *data_obj.info['dim_labels'][1:]))
        self.cope_dimlabels = list(('Contrasts',
                                    *data_obj.info['dim_labels'][1:]))
        self.tstat_dimlabels = list(('Contrasts',
                                     *data_obj.info['dim_labels'][1:]))

    def compute_betas(self, design_matrix, data, fit_args=None):

        raise NotImplementedError('This is an abstract class, please use OLSModel')

    def get_tstats(self, varcope_smoothing=None, smoothing_window=np.hanning, smooth_dims=None):
        """Computes t-statistics from COPEs in a fitted model, may add optional
        temporal varcope smoothing.

        Parameters
        ----------

        varcope_smoothing : {None, int} (optional, default=None)
            Optional window length for varcope smoothing of time dimension. The
            default is no smoothing as indicated by None.

        smoothing_window : {np.hanning,np.bartlett,np.blackman,np.hamming} default=np.hanning
            One of numpys window functions to apply during smoothing. Ignored
            if varcope_smoothing=None

        Returns
        -------

        ndarray
            Array containing t-statistic estimates

        """

        if varcope_smoothing == 'avg':

            dim_len = self.varcopes.shape[self.time_dim]
            varcopes = self.varcopes.mean(self.time_dim)
            varcopes = np.expand_dims(varcopes, self.time_dim)

            denom = np.repeat(np.sqrt(varcopes), dim_len, axis=self.time_dim)

        elif varcope_smoothing is not None and varcope_smoothing > 0 and isinstance(smooth_dims, int):
            # Create window normalised to have area of 1
            # TODO: probably redundant with newer method below
            w = smoothing_window(varcope_smoothing)
            w = w / w.sum()

            func = lambda m: np.convolve(m, w, mode='same')  # noqa E731
            varcope = np.apply_along_axis(func, smooth_dims, arr=self.varcopes)

            denom = np.sqrt(varcope)

        elif varcope_smoothing is not None and len(smooth_dims) > 1:
            sigma = np.zeros((self.varcopes.ndim,))
            sigma[np.array(smooth_dims)] = varcope_smoothing
            denom = np.sqrt(ndimage.gaussian_filter(self.varcopes, sigma))

        else:
            denom = np.sqrt(self.varcopes)

        # Compute t-values
        # run this in where to avoid RunTimeWarnings
        tstats = np.where(np.isnan(denom) == False, self.copes / denom, np.nan)  # noqa E712

        return tstats

    def get_prediction(self):

        return self.design_matrix[self.good_observations, :].dot(self.betas)

    def get_residuals(self, data):

        return data - self.get_prediction()

    @property
    def num_observations(self):

        return self.design_matrix.shape[0]

    @property
    def num_regressors(self):

        return self.betas.shape[0]

    @property
    def tstats(self):
        return self.get_tstats()

    @property
    def num_contrasts(self):

        return self.copes.shape[0]

    @property
    def num_tests(self):

        return self.betas.shape[1]

    @property
    def mse(self):

        return self.ss_error / self.dof_error

    @property
    def r_square(self):

        return 1 - (self.ss_error / self.ss_total)

    @property
    def log_likelihood(self):

        raise NotImplementedError('This is an abstract class')

    @property
    def aic(self):
        return self.log_likelihood() + 2*self.num_regressors

    @property
    def bic(self):
        return self.log_likelihood() + (self.num_regressors*np.log(self.num_observations))

    @classmethod
    def load_from_hdf5(cls, hdfpath):

        # This function will be removed soon but keeping it for reference atm.
        # Raise a warning if someone happens to use it
        raise DeprecationWarning('Please use Anamnesis API instead!')

        ret = cls()

        import h5py
        f = h5py.File(hdfpath)

        ret.betas = f['OLSModel/betas'][...]
        ret.copes = f['OLSModel/copes'][...]
        ret.coapes = f['OLSModel/coapes'][...]
        ret.varcopes = f['OLSModel/varcopes'][...]

        ret.ss_total = f['OLSModel/ss_total'][...]
        ret.ss_error = f['OLSModel/ss_error'][...]
        ret.ss_model = f['OLSModel/ss_model'][...]

        if 'fstats' in f['OLSModel'].keys():
            ret.fstats = f['OLSModel/fstats'][...]
            ret.ftest_names = list(f['OLSModel/ftest_names'][...])
        else:
            ret.fstats = None
            ret.ftest_names = None

        ret.regressor_names = list(f['OLSModel/regressor_names'][...])
        ret.contrast_names = list(f['OLSModel/contrast_names'][...])
        ret.beta_dimlabels = tuple(f['OLSModel/beta_dimlabels'][...])
        ret.cope_dimlabels = tuple(f['OLSModel/cope_dimlabels'][...])

        ret.good_observations = f['OLSModel/good_observations'][...]

        ret.dof_error = f['OLSModel'].attrs['dof_error']
        ret.dof_model = f['OLSModel'].attrs['dof_model']

        ret.time_dim = f['OLSModel'].attrs['time_dim']

        return ret


register_class(AbstractModelFit)


class OLSModel(AbstractModelFit):

    def compute_betas(self, design_matrix, data, fit_args=None):

        # Invert design matrix
        design_matrix_inv = np.linalg.pinv(design_matrix)

        # Estimate betas
        self.betas = design_matrix_inv.dot(data)

    def log_likelihood(self):

        ll = - self.num_observations / 2.
        ll = ll * np.log(self.ss_error)
        return ll + (1 + np.log(2*np.pi)/self.num_observations)


register_class(OLSModel)


class SKLModel(AbstractModelFit):

    def compute_betas(self, design_matrix, data, fit_args=None):
        from sklearn import linear_model

        if fit_args is None:
            fit_args = {'lm': 'LinearRegression'}

        # Always assume that the design matrix has this right
        if 'fit_intercept' not in fit_args:
            fit_args['fit_intercept'] = False

        self.fit_args = fit_args.copy()

        # Actual model fit
        rtype = fit_args.pop('lm')
        batch = fit_args.pop('batch', 'sklearn')
        njobs = fit_args.pop('njobs', 1)
        reg = getattr(linear_model, rtype)

        if rtype == 'RANSACRegressor':
            # We need to pass in a base estimator
            base_estimator = linear_model.LinearRegression(**fit_args)
            reg = reg(base_estimator=base_estimator)
        else:
            reg = reg(**fit_args)

        if batch == 'sklearn':
            # Use sklearns internal batching - this considers all features
            # together. For instance, outliers will be detected across the
            # whole dataset

            self.betas, self.skm = _fit_sk(reg, design_matrix, data)

        else:
            # Use an external batching loop - this will consider each
            # regression as a separate entity. For instance, outliers are
            # detected independantly in each 'feature'

            args = [(reg, design_matrix, data[:, ii]) for ii in range(data.shape[1])]

            import multiprocessing as mp
            p = mp.Pool(processes=njobs)

            res = p.starmap(_fit_sk, args)

            self.betas = np.concatenate(([r[0] for r in res]), axis=1)
            self.skm = [r[1] for r in res]


register_class(SKLModel)


def _fit_sk(reg, design_matrix, data):

    skm = reg.fit(X=design_matrix, y=data)
    if hasattr(skm, 'coef_'):
        betas = skm.coef_.T
    elif hasattr(skm, 'estimator_') and hasattr(skm.estimator_, 'coef_'):
        betas = skm.estimator_.coef_.T

    if betas.ndim == 1:
        betas = betas[:, None]

    return betas, skm
