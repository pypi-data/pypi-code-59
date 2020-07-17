import numpy as np
from scipy.signal import periodogram, welch
import scipy.spatial.distance as dis


def joint_entropy(data, /, entropy='shannon', pds=False, base=2, **kwargs):  # P(X,Y)
    if pds:
        data = _pds2data(data)

    if entropy == 'shannon':
        pds = __shannon_pds(data, **kwargs)
    elif entropy == 'vq':
        pds = np.array([__vq_psd(d, **kwargs) for d in data])
    elif entropy == 'spectral':
        pds = np.array([__spectral_pds(d, **kwargs) for d in data])

    # jointProbs, edges = np.histogramdd(data, bins=bins, normed=True)
    # jointProbs /= jointProbs.sum()
    # non_zeros = jointProbs[jointProbs != 0]

    return np.sum(-pds * np.log(pds) / np.log(base))


def conditional_entropy(data, conditional_index=0, /, entropy='shannon', pds=False, base=2, **kwargs):  # P(X|Y)
    if pds:
        data = _pds2data(data)

    return joint_entropy(data, entropy=entropy, base=base, **kwargs) - joint_entropy(data[conditional_index], entropy=entropy, base=base, **kwargs)


def entropy(data, /, method='shannon', pds=False, base=2, **kwargs):
    if pds:
        data = _pds2data(data)

    return joint_entropy(data, entropy=method, base=base, **kwargs)


def vq_entropy(x, /, pds=False, r=None, tau=3):

    if pds:
        data = _pds2data(data)

    if r is None:
        r = 0.2 * x.std()

    psd = __vq_psd(x, r, tau)

    E = -np.sum(psd * np.log(psd)) / (x.shape[0] // tau)
    return E


def _pds2data(pds, N=1000):
    P = [p[p != 0] for p in pds if p[p != 0].shape[0]]
    data = np.array([[np.random.choice(p.shape[0], p=p / np.sum(p))
                      for i in range(N)] for p in P])
    return data


def __vq_psd(x, r=None, tau=3):

    if r is None:
        r = 0.2 * x.std()

    if m := x.shape[0] % tau:
        x = x[:-m]
    x = x.reshape(-1, tau)

    D = [x[0]]
    [D.append(sim) for sim in x if not np.sum(
        dis.cdist(np.asarray(D), [sim]) < r)]
    D = np.array(D)

    d = dis.cdist(D, x)
    sig = np.median(d)
    simil = np.exp(-((d)**2) / (2 * sig**2))

    Pd = simil.mean(axis=1)
    m = np.mean(np.asarray([x[:, i].reshape(
        x[:, i].shape[0], 1) * simil.T for i in range(x.shape[1])]), axis=1).T

    d2 = dis.cdist(x, m)
    var = np.mean(((dis.cdist(x, m).T)**2) * simil, axis=1)
    simil2 = np.exp(-((d2)**2) / (2 * var))

    psd = simil2.mean(axis=0)
    psd = psd * Pd

    return psd


def __shannon_pds(x, bins=16):
    """"""
    jointProbs, edges = np.histogramdd(x.T, bins=bins, normed=True)
    jointProbs /= jointProbs.sum()
    non_zeros = jointProbs[jointProbs != 0]
    return non_zeros


def __spectral_pds(x, sf=1, method='fft', nperseg=None):

    x = np.array(x)
    if method == 'fft':
        _, psd = periodogram(x, sf)
    elif method == 'welch':
        _, psd = welch(x, sf, nperseg=nperseg)
    psd_norm = np.divide(psd, psd.sum())

    psd_norm = np.abs(psd_norm)
    psd_norm = psd_norm[psd_norm > 0]

    return psd_norm

    # se = -np.multiply(psd_norm, np.log2(psd_norm.astype(float))).sum()
    # if normalize:
        # se /= np.log2(psd_norm.size)

    # return se


def __sliding_window(data, window, overlap):
    return np.array([data[start:start + window] for start in range(0, len(data) - (window - int(np.ceil(window * (1 - overlap)))), int(np.ceil(window * (1 - overlap))))], dtype=object)


def sliding(x, fn, window, overlap=0.9, **kwargs):
    sld_data = __sliding_window(x, window, overlap)
    return np.array([fn(d, **kwargs) for d in sld_data])

