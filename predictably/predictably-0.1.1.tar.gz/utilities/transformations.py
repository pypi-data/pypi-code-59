import numpy as np
from math import floor


def _guerrero_cv(box_cox_lambda, x, frequency):
    """ Computes Coefficient of Variation to implement Guerroro's (1994) method
    of determining the optimal lambda value for a Box-Cox transformation.

    Parameters
    ----------
    box_cox_lambda : float
        Value corresponding to lambda in Box-Cox transformation.
    x : array-like, shape (n_samples,) or (n_samples, 1)
        Input vector, where n_samples is the number of samples.
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
