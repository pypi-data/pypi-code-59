import numpy as np
from math import floor
from scipy.stats import boxcox, boxcox_normmax
from scipy.special import inv_boxcox
from scipy.optimize import brentq
from utilities.validations import is_tuple_list_like

def guerrero_cv(box_cox_lambda, x, frequency):
    """ Computes Coefficient of Variation to implement Guerroro's (1994) method
    of determining the optimal lambda value for a Box-Cox transformation.

    Parameters
    ----------
    box_cox_lambda : float
        Value corresponding to lambda in Box-Cox transformation.
    x : array-like, shape (n_samples,) or (n_samples, 1)
        Input vector, where n_samples in the number of samples.
    frequency : int
        The seasonal frequency of the input data x (1 for non-seasonal).

    Returns
    -------
    cv : float
    """
   
    nonseasonal_length = 2 
    period = max(nonseasonal_length, frequency)
    x_obs = x.shape[0]
    colz = floor(x_obs / period)
    obs_to_use = colz*period
    x_matrix = x[(x_obs - obs_to_use):x_obs].reshape(period, colz)
    x_mean = x_matrix.mean(axis = 0)
    x_std = x_matrix.std(axis = 0)
    x_ratio = x_std / np.power(x_mean, 1-box_cox_lambda)
    cv = x_ratio.std() /x_ratio.mean()

    return cv

class  BoxCoxTransformer(object):
    """ NEED TO FILL IN
    """
    def __init__(self, method="guerrero"):
        self.method = method
        self.lambda_ = None
        super(BoxCoxTransformer, self).__init__()

    def fit(self, y_train, **fit_params):
        self.lambda_ = self._boxcox_lambda_seek(y_train, method=self.method)
        self._is_fitted = True
        return self

    def transform(self, y, **transform_params):
        self.check_is_fitted()
        check_y(y)
        yt = boxcox(y.values, self.lambda_)
        return pd.Series(yt, index=y.index)

    def inverse_transform(self, y, **transform_params):
        self.check_is_fitted()
        check_y(y)
        yt = inv_boxcox(y.values, self.lambda_)
        return pd.Series(yt, index=y.index)

    def update(self, y_new, update_params=False):
        raise NotImplementedError()

    def _boxcox_lambda_seek(self, x, method = 'guerrero'):
        """ Seeks out optimal Lambda for Box-Cox transformation.
            Uses Guerroro's (1994) method to determine the optimal lambda 
            value for a Box-Cox transformation or by maximizing log-likelihood
            via maximum likelihood estimation.

            Parameters
            ----------
            x : array-like, shape (n_samples,) or (n_samples, 1)
            Input vector, where n_samples in the number of samples.
            method : string, default = guerrero
                Method to use to find optimal lambda for Box-Cox transformation.
                Must be one of 'guerrero', 'mle' or 'pearsonr'

            Returns
            -------
            float
                Lambda value that minimizes Guerrero's CV ratio.
        """
        if method == 'guerrero':
            return self._guerrero(x)
        elif method in ['mle', 'pearsonr']:
            return boxcox_normmax(x, method = method)
        else:
            raise ValueError("Must supply method as one of guerrero or loglik.")

    def _guerrero(self, x, interval = (-1,2)):
        """ Uses Guerroro's (1994) method to determine the optimal lambda 
            value for a Box-Cox transformation.
        Parameters
        ----------
        x : array-like, shape (n_samples,) or (n_samples, 1)
            Input vector, where n_samples in the number of samples.
        interval : tuple or list
            A tuple or list with two elements.

        Returns
        -------
        lambda_opt : float
            Lambda value that minimizes Guerrero's CV ratio.

        References
        ----------
        .. [1] Guerrero, V.M. (1993) Time-series analysis supported by 
               power transformations. Journal of Forecasting, 12, 37–48.
        """
        if not is_tuple_list_like(interval):
            raise TypeError("interval must be tuple or list like.")
        elif len(interval) != 2:
            raise ValueError(
                f"interval length should be 2, but length is {len(interval)}.")

        frequency = 1
        lambda_opt = brentq(guerrero_cv, interval[0], interval[1], 
                            args = (x,frequency))
        return lambda_opt