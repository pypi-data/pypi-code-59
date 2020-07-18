"""qtl.map: functions for mapping QTLs"""

__author__ = "Francois Aguet"
__copyright__ = "Copyright 2018-2019, The Broad Institute"
__license__ = "BSD3"

import numpy as np
import pandas as pd
import scipy.stats
from . import stats
from . import genotype as gt


def center_normalize(x, axis=0):
    """Center and normalize x"""
    if isinstance(x, pd.DataFrame):
        x0 = x - np.mean(x.values, axis=axis, keepdims=True)
        return x0 / np.sqrt(np.sum(x0.pow(2).values, axis=axis, keepdims=True))
    elif isinstance(x, pd.Series):
        x0 = x - x.mean()
        return x0 / np.sqrt(np.sum(x0*x0))
    elif isinstance(x, np.ndarray):
        x0 = x - np.mean(x, axis=axis, keepdims=True)
        return x0 / np.sqrt(np.sum(x0*x0, axis=axis))


def calculate_association(genotype, phenotype_s, covariates_df=None, impute=True):
    """Compute genotype-phenotype associations"""
    if isinstance(genotype, pd.Series):
        genotype_df = genotype.to_frame().T
    elif isinstance(genotype, pd.DataFrame):
        genotype_df = genotype
    else:
        raise ValueError('Input type not supported')

    assert np.all(genotype_df.columns==phenotype_s.index)
    if covariates_df is not None:
        assert np.all(covariates_df.index==genotype_df.columns)

    # impute missing genotypes
    if impute:
        gt.impute_mean(genotype_df, verbose=False)

    # residualize genotypes and phenotype
    if covariates_df is not None:
        r = stats.Residualizer(covariates_df)
        gt_res_df = r.transform(genotype_df)
        p_res_s = r.transform(phenotype_s)
        num_covar = covariates_df.shape[1]
    else:
        gt_res_df = genotype_df
        p_res_s = phenotype_s
        num_covar = 0

    n = p_res_s.std()/gt_res_df.std(axis=1)

    gt_res_df = center_normalize(gt_res_df, axis=1)
    p_res_s = center_normalize(p_res_s)

    r = gt_res_df.dot(p_res_s)
    dof = gt_res_df.shape[1] - 2 - num_covar

    tstat = r * np.sqrt(dof/(1-r*r))
    pval = 2*scipy.stats.t.cdf(-np.abs(tstat), dof)

    df = pd.DataFrame(pval, index=tstat.index, columns=['pval_nominal'])
    df['slope'] = r * n
    df['slope_se'] = df['slope'] / tstat
    df['r2'] = r*r
    df['tstat'] = tstat
    df['maf'] = genotype_df.sum(1) / (2*genotype_df.shape[1])
    df['maf'] = np.where(df['maf']<=0.5, df['maf'], 1-df['maf'])
    if isinstance(df.index[0], str) and '_' in df.index[0]:
        df['chr'] = df.index.map(lambda x: x.split('_')[0])
        df['position'] = df.index.map(lambda x: int(x.split('_')[1]))
    df.index.name = 'variant_id'
    if isinstance(genotype, pd.Series):
        df = df.iloc[0]
    return df


def map_pairs(genotype_df, phenotype_df, covariates_df=None, impute=True):
    """Calculates association statistics for arbitrary phenotype-variant pairs"""
    assert genotype_df.shape[0] == phenotype_df.shape[0]
    assert genotype_df.columns.equals(phenotype_df.columns)
    assert genotype_df.columns.equals(covariates_df.index)
    if impute:
        impute_mean(genotype_df)

    # residualize genotypes and phenotype
    if covariates_df is not None:
        r = stats.Residualizer(covariates_df)
        gt_res_df = r.transform(genotype_df)
        p_res_df = r.transform(phenotype_df)
        num_covar = covariates_df.shape[1]
    else:
        gt_res_df = genotype_df
        p_res_df = phenotype_df
        num_covar = 0

    n = p_res_df.std(axis=1).values / gt_res_df.std(axis=1).values

    gt_res_df = center_normalize(gt_res_df, axis=1)
    p_res_df = center_normalize(p_res_df, axis=1)

    r = np.sum(gt_res_df.values * p_res_df.values, axis=1)
    dof = gt_res_df.shape[1] - 2 - num_covar

    tstat2 = dof*r*r / (1-r*r)
    pval = scipy.stats.f.sf(tstat2, 1, dof)

    df = pd.DataFrame({'phenotype_id':phenotype_df.index, 'variant_id':genotype_df.index, 'pval_nominal':pval})
    df['slope'] = r * n
    df['slope_se'] = df['slope'].abs() / np.sqrt(tstat2)
    df['maf'] = genotype_df.sum(1).values / (2*genotype_df.shape[1])
    df['maf'] = np.where(df['maf']<=0.5, df['maf'], 1-df['maf'])
    return df


def calculate_interaction(genotype_s, phenotype_s, interaction_s, covariates_df=None, impute=True):

    assert np.all(genotype_s.index==interaction_s.index)

    # impute missing genotypes
    if impute:
        impute_mean(genotype_s)

    # interaction term
    gi = genotype_s * interaction_s

    # center
    g0 = genotype_s - genotype_s.mean()
    gi0 = gi - gi.mean()
    i0 = interaction_s - interaction_s.mean()
    p0 = phenotype_s - phenotype_s.mean()

    dof = phenotype_s.shape[0] - 4
    # residualize
    if covariates_df is not None:
        r = stats.Residualizer(covariates_df)
        g0 =  r.transform(g0.values.reshape(1,-1), center=False)
        gi0 = r.transform(gi0.values.reshape(1,-1), center=False)
        p0 =  r.transform(p0.values.reshape(1,-1), center=False)
        i0 =  r.transform(i0.values.reshape(1,-1), center=False)
        dof -= covariates_df.shape[1]
    else:
        g0 = g0.values.reshape(1,-1)
        gi0 = gi0.values.reshape(1,-1)
        p0 = p0.values.reshape(1,-1)
        i0 = i0.values.reshape(1,-1)

    # regression
    X = np.r_[g0, i0, gi0].T
    Xinv = np.linalg.inv(np.dot(X.T, X))
    b = np.dot(np.dot(Xinv, X.T), p0.reshape(-1,1))
    r = np.squeeze(np.dot(X, b)) - p0
    rss = np.sum(r*r)
    b_se = np.sqrt(np.diag(Xinv) * rss / dof)
    b = np.squeeze(b)
    tstat = b / b_se
    pval = 2*scipy.stats.t.cdf(-np.abs(tstat), dof)

    return pd.Series({
        'b_g':b[0], 'b_g_se':b_se[0], 'pval_g':pval[0],
        'b_i':b[1], 'b_i_se':b_se[1], 'pval_i':pval[1],
        'b_gi':b[2],'b_gi_se':b_se[2],'pval_gi':pval[2],
    })#, r[0]


# def calculate_interaction_nominal(genotypes_df, phenotype_s, interaction_s, covariates_df=None):
#     """
#     genotypes_t:   [num_genotypes x num_samples]
#     phenotypes_t:   [num_phenotypes x num_samples]
#     interaction_t: [1 x num_samples]
#     """
#     ng, ns = genotypes_df.shape
#
#     # centered inputs
#     g0 = genotypes_df - np.mean(genotypes_df.values, 1, keepdims=True)
#     gi = genotypes_df * interaction_s
#     gi0 = gi - np.mean(gi.values, 1, keepdims=True)
#     i0 = interaction_s - interaction_s.mean()
#     # p0 = phenotype_s - phenotype_s.mean()
#     p0 = phenotype_s.values.reshape(1,-1) - phenotype_s.mean()
#
#     # residualize rows
#     if covariates_df is not None:
#         residualizer = stats.Residualizer(covariates_df)
#         g0 = residualizer.transform(g0, center=False)
#         gi0 = residualizer.transform(gi0, center=False)
#         p0 = residualizer.transform(p0, center=False)
#         i0 = residualizer.transform(i0, center=False)
#     i0 = np.repeat(i0.values.reshape(1,-1), ng, 0)
#
#
#     X = np.stack([g0, i0, gi0], 2)  # ng x ns x 3
#     Xinv = torch.matmul(torch.transpose(X_t, 1, 2), X_t).inverse() # ng x 3 x 3
#     p0_tile_t = p0_t.unsqueeze(0).expand([ng, *p0_t.shape])  # ng x np x ns
#
#     # calculate b, b_se
#     # [(ng x 3 x 3) x (ng x 3 x ns)] x (ng x ns x np) = (ng x 3 x np)
#     b_t = torch.matmul(torch.matmul(Xinv, torch.transpose(X_t, 1, 2)), torch.transpose(p0_tile_t, 1, 2))
#     dof = residualizer.dof - 2
#     r_t = torch.matmul(X_t, b_t).squeeze() - p0_t
#     rss_t = (r_t*r_t).sum(1)
#     b_se_t = torch.sqrt(Xinv[:, torch.eye(3, dtype=torch.uint8).bool()] * rss_t.unsqueeze(1) / dof)
#     b_t = b_t.squeeze(2)
#
#     tstat_t = (b_t.double() / b_se_t.double()).float()  # (ng x 3 x np)
#
#     # calculate MAF
#     # n2 = 2*ns
#     # af_t = genotypes_t.sum(1) / n2
#     # ix_t = af_t <= 0.5
#     # maf_t = torch.where(ix_t, af_t, 1 - af_t)
#
#     # calculate MA samples and counts
#     # m = genotypes_t > 0.5
#     # a = m.sum(1).int()
#     # b = (genotypes_t < 1.5).sum(1).int()
#     # ma_samples_t = torch.where(ix_t, a, b)
#     # a = (genotypes_t * m.float()).sum(1).round().int()  # round for missing/imputed genotypes
#     # ma_count_t = torch.where(ix_t, a, n2-a)
#     # return tstat_t, b_t, b_se_t, maf_t, ma_samples_t, ma_count_t


def get_conditional_pvalues(group_df, genotypes, phenotype_df, covariates_df, phenotype_id=None, window=200000):
    """"""
    assert np.all(phenotype_df.columns==covariates_df.index)
    variant_id = group_df['variant_id'].iloc[0]
    chrom, pos = variant_id.split('_')[:2]
    pos = int(pos)

    if isinstance(genotypes, gt.GenotypeIndexer):
        gt_df = genotypes.get_genotype_window(variant_id, window=window)
    elif isinstance(genotypes, pd.DataFrame):
        gt_df = genotypes
    else:
        raise ValueError('Unsupported input format')

    maf = gt_df.sum(1) / (2*gt_df.shape[1])
    maf = np.where(maf<=0.5, maf, 1-maf)

    gt_df = gt_df[maf>0]

    res = []
    if phenotype_id is not None:
        pval_df = calculate_association(gt_df, phenotype_df.loc[phenotype_id], covariates_df=covariates_df)
        pval_df['r2'] = gt_df.corrwith(gt_df.loc[variant_id], axis=1, method='pearson')**2
        res.append(pval_df)

    for k,(variant_id, phenotype_id) in enumerate(zip(group_df['variant_id'], group_df['phenotype_id']), 1):
        print('\rProcessing {}/{}'.format(k, group_df.shape[0]), end='')
        covariates = pd.concat([covariates_df, gt_df.loc[np.setdiff1d(group_df['variant_id'], variant_id)].T], axis=1)
        pval_df = calculate_association(gt_df, phenotype_df.loc[phenotype_id], covariates_df=covariates)
        pval_df['r2'] = gt_df.corrwith(gt_df.loc[variant_id], axis=1, method='pearson')**2

        res.append(pval_df)
    return res
