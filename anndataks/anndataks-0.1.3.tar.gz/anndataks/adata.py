# vim: fdm=indent
# author:     Fabio Zanini
# date:       17/06/20
# content:    Kolmogorov Smirnov test on gene expression for AnnData objects
import numpy as np
import pandas as pd
import scipy.sparse
from warnings import warn
from .config import rc



def compare(adata1, adata2, log1p=False, alternative='two-sided', mode='auto'):
    '''Compare two AnnData gene expression by KS test

    Args:
        adata1 (AnnData): The first dataset
        adata2 (AnnData): The second dataset
        log1p (False or float): Whether the datasets are already pseudocounted
           and logged. If a float, it should specify the base of the log. If
           True, it will assume the data is in log2.
        alternative : {'two-sided', 'less', 'greater'}, optional
            Defines the alternative hypothesis.
            The following options are available (default is 'two-sided'):
              * 'two-sided'
              * 'less': one-sided, see explanation in Notes
              * 'greater': one-sided, see explanation in Notes
        mode : {'auto', 'exact', 'asymp'}, optional
            Defines the method used for calculating the p-value.
            The following options are available (default is 'auto'):
              * 'auto' : use 'exact' for small size arrays, 'asymp' for large
              * 'exact' : use exact distribution of test statistic
              * 'asymp' : use asymptotic distribution of test statistic

    Returns:
        pd.DataFrame: Rows are var_names, columns are the KS statistic (with
        sign > 0 if adata2 had a higher expression at the key spot), the
        expression level of the maximal KS statistic, the P value, the average
        of the expression in the first dataset, the average in the second
        dataset (both logged 2 with pseudocount of 1), and the log2 fold change
        of 2 over 1.

    '''
    if rc['use_experimental_ks_2samp']:
        from .stats import ks_2samp
    else:
        from scipy.stats import ks_2samp

    X1 = adata1.X
    X2 = adata2.X

    m1, m2 = X1.shape[1], X2.shape[1]
    if m1 != m2:
        raise ValueError('The AnnData matrices must have the same width')

    if scipy.sparse.issparse(X1) and (not scipy.sparse.isspmatrix_csc(X1)):
        X1 = X1.tocsc()

    if scipy.sparse.issparse(X2) and (not scipy.sparse.isspmatrix_csc(X2)):
        X2 = X2.tocsc()

    if rc['log_warn']:
        if log1p is False:
            if (X1.min() < 0) or (X2.min() < 0):
                warn('Negative counts found, is the data logged already?')
            if (X1.max() < 100) or (X2.max() < 100):
                warn('Maximal counts are small, is the data logged already?')
        else:
            if (X1.max() > 100) or (X2.max() > 100):
                warn('Maximal counts are large, are you sure the data is logged?')

    # Get the numbers out of the aux function
    if rc['use_experimental_ks_2samp']:
        ress = pd.DataFrame(
                np.zeros((m1, 3), np.float64),
                index=adata1.var_names,
                columns=['statistic', 'value', 'pvalue'],
                )
    else:
        ress = pd.DataFrame(
                np.zeros((m1, 2), np.float64),
                index=adata1.var_names,
                columns=['statistic', 'pvalue'],
                )
    for i in range(m1):
        data1 = X1[:, i]
        data2 = X2[:, i]
        # The comparison requires dense data ATM
        if scipy.sparse.issparse(data1):
            data1 = data1.toarray()[:, 0]
        if scipy.sparse.issparse(data2):
            data2 = data2.toarray()[:, 0]
        res = ks_2samp(data1, data2, alternative=alternative, mode=mode)
        ress.iloc[i] = res

    # Compute averages and log2 fold changes
    avg1 = X1.mean(axis=0)
    avg2 = X2.mean(axis=0)
    if scipy.sparse.issparse(X1):
        avg1 = np.asarray(avg1).reshape(-1)
    if scipy.sparse.issparse(X2):
        avg2 = np.asarray(avg2).reshape(-1)

    if log1p is False:
        avg1 = np.log2(avg1 + 1)
        avg2 = np.log2(avg2 + 1)
    elif log1p not in (True, 2):
        avg1 /= np.log2(log1p)
        avg2 /= np.log2(log1p)

    log2_fc = avg2 - avg1
    ress['avg1'] = avg1
    ress['avg2'] = avg2
    ress['log2_fold_change'] = log2_fc

    return ress
