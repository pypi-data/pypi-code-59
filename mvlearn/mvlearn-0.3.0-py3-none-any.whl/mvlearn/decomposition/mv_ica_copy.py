# BSD 3-Clause License
# Copyright (c) 2020, Hugo RICHARD and Pierre ABLIN
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Modified from source package https://github.com/hugorichard/multiviewica

import numpy as np
import warnings
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment
from sklearn.decomposition import FastICA
from sklearn.utils.extmath import randomized_svd
from scipy import stats
from joblib import Parallel, delayed


def multiviewica(
    Xs,
    n_components=None,
    dimension_reduction="pca",
    noise=1.0,
    max_iter=1000,
    init="permica",
    random_state=None,
    tol=1e-3,
    verbose=False,
    n_jobs=30,
):
    """
    Multiview ICA for which views share a common source.

    Parameters
    ----------
    Xs : list of array-likes or numpy.ndarray
             - Xs length: n_views
             - Xs[i] shape: (n_samples, n_features_i)
        A group of data matrices from each view to transform based on the
            prior fit function.
    n_components : int, optional
        Number of components to extract.
        If None, no dimension reduction is performed
    dimension_reduction: str, optional
        if srm: use srm to reduce the data
        if pca: use group specific pca to reduce the data
    noise : float, optional
        Gaussian noise level
    max_iter : int, optional
        Maximum number of iterations to perform
    init : str or np array of shape (n_groups, n_components, n_components)
        If permica: initialize with perm ICA, if groupica, initialize with
        group ica. Else, use the provided array to initialize.
    random_state : int, RandomState instance or None, optional (default=None)
        Used to perform a random initialization. If int, random_state is
        the seed used by the random number generator; If RandomState
        instance, random_state is the random number generator; If
        None, the random number generator is the RandomState instance
        used by np.random.
    tol : float, optional
        A positive scalar giving the tolerance at which
        the un-mixing matrices are considered to have converged.
    verbose : bool, optional
        Print information

    Returns
    -------
    P : np array of shape (n_groups, n_components, n_features)
        K is the projection matrix that projects data in reduced space
    W : np array of shape (n_groups, n_components, n_components)
        Estimated un-mixing matrices
    S : np array of shape (n_components, n_samples)
        Estimated source

    Notes
    -----
    Given each view :math:`X_i` It optimizes:

        .. math::
            l(W) = mean_t [sum_k log(cosh(Y_avg(t)[k])) + sum_i l_i(X_i(t))]

    where

        .. math::
            l _i(X_i(t)) = - log(|W_i|) + 1/(2 noise) ||W_iX_i(t) -
            Y_avg(t)||^2,
    
    :math:`W_i` is the mixing matrix for view i and
    :math:`Y_avg = mean_i W_i X_i`.

    See also
    --------
    groupica
    permica
    """

    Xs = np.asarray([X.T for X in Xs])
    P, Xs = _reduce_data(
        Xs, n_components=n_components
    )
    # Initialization
    if type(init) is str:
        if init not in ["permica", "groupica"]:
            raise ValueError("init should either be permica or groupica")
        if init == "permica":
            _, W, S = permica(
                np.asarray([X.T for X in Xs]), max_iter=max_iter, random_state=random_state, tol=tol
            )
        else:
            _, W, S = groupica(
                np.asarray([X.T for X in Xs]), max_iter=max_iter, random_state=random_state, tol=tol
            )
    else:
        if type(init) is not np.ndarray:
            raise TypeError("init should be a numpy array")
        W = init
    # Performs multiview ica
    W, S = _multiview_ica_main(
        Xs, noise=noise, n_iter=max_iter, tol=tol, init=W, verbose=verbose
    )
    return P, W, S


def permica(
    Xs,
    n_components=None,
    dimension_reduction="pca",
    max_iter=1000,
    random_state=None,
    tol=1e-7,
):
    """
    Performs one ICA per view (ex: subject) and align sources
    using the hungarian algorithm.

    Parameters
    ----------
    Xs : np array of shape (n_views, n_features, n_samples)
        Training vector, where n_groups is the number of groups,
        n_samples is the number of samples and
        n_components is the number of components.
    n_components : int, optional
        Number of components to extract.
        If None, no dimension reduction is performed
    dimension_reduction: str, optional
        if srm: use srm to reduce the data
        if pca: use group specific pca to reduce the data
    max_iter : int, optional
        Maximum number of iterations to perform
    random_state : int, RandomState instance or None, optional (default=None)
        Used to perform a random initialization. If int, random_state is
        the seed used by the random number generator; If RandomState
        instance, random_state is the random number generator; If
        None, the random number generator is the RandomState instance
        used by np.random.
    tol : float, optional
        A positive scalar giving the tolerance at which
        the un-mixing matrices are considered to have converged.

    Returns
    -------
    P : np array of shape (n_groups, n_components, n_features)
        K is the projection matrix that projects data in reduced space
    W : np array of shape (n_groups, n_components, n_components)
        Estimated un-mixing matrices
    S : np array of shape (n_components, n_samples)
        Estimated source

    See also
    --------
    groupica
    multiviewica
    """
    Xs = np.asarray([X.T for X in Xs])
    P, Xs = _reduce_data(
        Xs, n_components=n_components
    )
    n_pb, p, n = Xs.shape
    W = np.zeros((n_pb, p, p))
    S = np.zeros((n_pb, p, n))
    for i, X in enumerate(Xs):
        fica = FastICA(max_iter=max_iter, tol=tol, random_state=random_state)
        Si = fica.fit_transform(X.T)
        Si = Si.T
        scale = np.linalg.norm(Si, axis=1)
        S[i] = Si / scale[:, None]
        W[i] = fica.components_ / scale[:, None]
        # Ki, Wi, Si = picard(
        #     x,
        #     ortho=False,
        #     extended=False,
        #     centering=False,
        #     max_iter=max_iter,
        #     tol=tol,
        #     random_state=random_state,
        # )
    orders, signs, S = _find_ordering(S)
    for i, (order, sign) in enumerate(zip(orders, signs)):
        W[i] = sign[:, None] * W[i][order, :]
    return P, W, S

def groupica(
    Xs,
    n_components=None,
    dimension_reduction="pca",
    max_iter=1000,
    random_state=None,
    tol=1e-7,
):
    """
    Performs PCA on concatenated data across groups (ex: subjects)
    and apply ICA on reduced data.

    Parameters
    ----------
    X : np array of shape (n_groups, n_features, n_samples)
        Training vector, where n_groups is the number of groups,
        n_samples is the number of samples and
        n_components is the number of components.
    n_components : int, optional
        Number of components to extract.
        If None, no dimension reduction is performed
    dimension_reduction: str, optional
        if srm: use srm to reduce the data
        if pca: use group specific pca to reduce the data
    max_iter : int, optional
        Maximum number of iterations to perform
    random_state : int, RandomState instance or None, optional (default=None)
        Used to perform a random initialization. If int, random_state is
        the seed used by the random number generator; If RandomState
        instance, random_state is the random number generator; If
        None, the random number generator is the RandomState instance
        used by np.random.
    tol : float, optional
        A positive scalar giving the tolerance at which
        the un-mixing matrices are considered to have converged.

    Returns
    -------
    P : np array of shape (n_groups, n_components, n_features)
        P is the projection matrix that projects data in reduced space
    W : np array of shape (n_groups, n_components, n_components)
        Estimated un-mixing matrices
    S : np array of shape (n_components, n_samples)
        Estimated source


    See also
    --------
    permica
    multiviewica
    """
    Xs = np.asarray([X.T for X in Xs])
    P, Xs = _reduce_data(
        Xs, n_components=n_components
    )
    n_pb, p, n = Xs.shape
    Xs_concat = np.vstack(Xs)
    U, S, V = np.linalg.svd(Xs_concat, full_matrices=False)
    U = U[:, :p]
    S = S[:p]
    V = V[:p]
    Xs_reduced = np.diag(S).dot(V)
    U = np.split(U, n_pb, axis=0)
    fica = FastICA(max_iter=max_iter, tol=tol, random_state=random_state)
    S = fica.fit_transform(Xs_concat.T)
    S = S.T
    scale = np.linalg.norm(S, axis=1)
    S = S / scale[:, None]
    W = np.array([S.dot(np.linalg.pinv(X)) for X in Xs])
    #W = np.array([np.linalg.pinv(X).T.dot(S.T).T for X in Xs])
    # K, W, S = picard(
    #     X_reduced,
    #     ortho=False,
    #     extended=False,
    #     centering=False,
    #     max_iter=max_iter,
    #     tol=tol,
    #     random_state=random_state,
    # )
    # scale = np.linalg.norm(S, axis=1)
    # S = S / scale[:, None]
    # W = np.array([S.dot(np.linalg.pinv(x)) for x in X])
    return P, W, S


def _reduce_data(Xs, n_components, n_jobs=None):
    """
    Reduce the number of features in X via group specific PCA

    Parameters
    ----------
    X : np array of shape (n_groups, n_features, n_samples)
        Training vector, where n_groups is the number of groups,
        n_samples is the number of samples and
        n_components is the number of components.
    n_components : int, optional
        Number of components to extract.
        If None, no dimension reduction is performed
    Returns
    -------
    projection: np array of shape (n_groups, n_components, n_features)
        the projection matrix that projects data in reduced space
    reduced: np array of shape (n_groups, n_components, n_samples)
        Reduced data
    """
    if n_components is None:
        return None, Xs
    n_groups = len(Xs)
    reduced = []
    basis = []
    def temp(X):
        U_i, S_i, V_i = randomized_svd(X, n_components=n_components)
        return U_i.T, S_i.reshape(-1, 1) * V_i

    parallelized_pca = Parallel(n_jobs=n_jobs)(
        delayed(temp)(X) for X in Xs
    )
    # for i in range(n_groups):
    #     U_i, S_i, V_i = randomized_svd(X[i], n_components=n_components)
    #     reduced.append(S_i.reshape(-1, 1) * V_i)
    #     #basis.append(U_i.T)
    #     #print(f'Group {i}: {reduced[-1].shape}, {basis[-1].shape}')
    projections, reduced = zip(*parallelized_pca)
    return np.asarray(projections), np.asarray(reduced)


def _multiview_ica_main(
    Xs,
    noise=1.0,
    n_iter=1000,
    tol=1e-6,
    verbose=False,
    init=None,
    ortho=False,
    return_gradients=False,
):
    # Turn list into an array to make it compatible with the rest of the code
    if type(Xs) == list:
        Xs = np.array(Xs)

    # Init
    n_pb, p, n = Xs.shape
    basis_list = init.copy()
    Y_avg = np.mean([np.dot(W, X) for W, X in zip(basis_list, Xs)], axis=0)
    # Start scaling
    g_norms = 0
    g_list = []
    for i in range(n_iter):
        g_norms = 0
        # Start inner loop: decrease the loss w.r.t to each W_j
        for j in range(n_pb):
            X = Xs[j]
            W_old = basis_list[j].copy()
            # Y_denoise is the estimate of the sources without Y_j
            Y_denoise = Y_avg - W_old.dot(X) / n_pb
            # Perform one ICA quasi-Newton step
            basis_list[j], g_norm = _noisy_ica_step(
                W_old, X, Y_denoise, noise, n_pb, ortho, scale=True
            )
            # Update the average vector (estimate of the sources)
            Y_avg += np.dot(basis_list[j] - W_old, X) / n_pb
            g_norms = max(g_norm, g_norms)
        if verbose:
            print(
                "it %d, loss = %.4e, g=%.4e"
                % (
                    i + 1,
                    _loss_total(basis_list, Xs, Y_avg, noise),
                    g_norms,
                )
            )
        if g_norms < tol:
            break
    # Start outer loop
    g_norms = 0
    for i in range(n_iter):
        g_norms = 0
        # Start inner loop: decrease the loss w.r.t to each W_j
        for j in range(n_pb):
            X = Xs[j]
            W_old = basis_list[j].copy()
            # Y_denoise is the estimate of the sources without Y_j
            Y_denoise = Y_avg - W_old.dot(X) / n_pb
            # Perform one ICA quasi-Newton step
            basis_list[j], g_norm = _noisy_ica_step(
                W_old, X, Y_denoise, noise, n_pb, ortho
            )
            # Update the average vector (estimate of the sources)
            Y_avg += np.dot(basis_list[j] - W_old, X) / n_pb
            g_norms = max(g_norm, g_norms)
        g_list.append(g_norms)
        if verbose:
            print(
                "it %d, loss = %.4e, g=%.4e"
                % (
                    i + 1,
                    _loss_total(basis_list, Xs, Y_avg, noise),
                    g_norms,
                )
            )
        if g_norms < tol:
            break

    else:
        warnings.warn(
            "Multiview ICA has not converged - gradient norm: %e " % g_norms
        )
    if return_gradients:
        return basis_list, Y_avg, g_list
    return basis_list, Y_avg


def _hungarian(M):
    u, order = linear_sum_assignment(-abs(M))
    vals = M[u, order]
    return order, np.sign(vals)


def _find_ordering(S_list, n_iter=10):
    n_pb, p, _ = S_list.shape
    for s in S_list:
        s /= np.linalg.norm(s, axis=1, keepdims=1)
    S = S_list[0].copy()
    order = np.arange(p)[None, :] * np.ones(n_pb, dtype=int)[:, None]
    signs = np.ones_like(order)
    for _ in range(n_iter):
        for i, s in enumerate(S_list[1:]):
            M = np.dot(S, s.T)
            order[i + 1], signs[i + 1] = _hungarian(M)
        S = np.zeros_like(S)
        for i, s in enumerate(S_list):
            S += signs[i][:, None] * s[order[i]]
        S /= n_pb
    return order, signs, S


def _logcosh(X):
    Y = np.abs(X)
    return Y + np.log1p(np.exp(-2 * Y))


def _loss_total(basis_list, X_list, Y_avg, noise):
    n_pb, p, _ = basis_list.shape
    loss = np.mean(_logcosh(Y_avg)) * p
    for i, (W, X) in enumerate(zip(basis_list, X_list)):
        Y = W.dot(X)
        loss -= np.linalg.slogdet(W)[1]
        loss += 1 / (2 * noise) * np.mean((Y - Y_avg) ** 2) * p
    return loss


def _loss_partial(W, X, Y_denoise, noise, n_pb):
    p, _ = W.shape
    Y = np.dot(W, X)
    loss = -np.linalg.slogdet(W)[1]
    loss += np.mean(_logcosh(Y / n_pb + Y_denoise)) * p
    fact = (1 - 1 / n_pb) / (2 * noise)
    loss += fact * np.mean((Y - n_pb * Y_denoise / (n_pb - 1)) ** 2) * p
    return loss


def _noisy_ica_step(
    W,
    X,
    Y_denoise,
    noise,
    n_pb,
    ortho,
    lambda_min=0.001,
    n_ls_tries=50,
    scale=False,
):
    """
    ICA minimization using quasi Newton method. Used in the inner loop.
    """
    p, n = X.shape
    loss0 = _loss_partial(W, X, Y_denoise, noise, n_pb)
    Y = W.dot(X)
    Y_avg = Y / n_pb + Y_denoise

    # Compute relative gradient and Hessian
    thM = np.tanh(Y_avg)
    G = np.dot(thM, Y.T) / n / n_pb
    # print(G)
    const = 1 - 1 / n_pb
    res = Y - Y_denoise / const
    G += np.dot(res, Y.T) * const / noise / n
    G -= np.eye(p)
    if scale:
        G = np.diag(np.diag(G))
    # print(G)
    if ortho:
        G = 0.5 * (G - G.T)
    g_norm = np.max(np.abs(G))

    # These are the terms H_{ijij} of the approximated hessian
    # (approximation H2 in Pierre's thesis)
    h = np.dot((1 - thM ** 2) / n_pb ** 2 + const / noise, (Y ** 2).T,) / n

    # Regularize
    discr = np.sqrt((h - h.T) ** 2 + 4.0)
    eigenvalues = 0.5 * (h + h.T - discr)
    problematic_locs = eigenvalues < lambda_min
    np.fill_diagonal(problematic_locs, False)
    i_pb, j_pb = np.where(problematic_locs)
    h[i_pb, j_pb] += lambda_min - eigenvalues[i_pb, j_pb]
    # Compute Newton's direction
    det = h * h.T - 1
    direction = (h.T * G - G.T) / det
    if ortho:
        direction = 0.5 * (direction - direction.T)
    # print(direction)
    # Line search
    step = 1
    for j in range(n_ls_tries):
        if ortho:
            new_W = expm(-step * direction).dot(W)
        else:
            new_W = W - step * direction.dot(W)
        new_loss = _loss_partial(new_W, X, Y_denoise, noise, n_pb)
        if new_loss < loss0:
            break
        else:
            step /= 2.0
    return new_W, g_norm
