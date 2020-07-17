"""Utility functions."""

import numpy
import numpy.fft


def pad(a, n, axis=-1):
    """Pad a frequency response with zeros at lowest and highest frequencies.

    Input should be ordered like numpy.fft.ifft function.
    """
    shape = list(a.shape)
    shape[axis] = n
    padded = numpy.empty(shape, a.dtype)

    index = [slice(None, None)] * len(a.shape)

    n_padded = a.shape[axis] if n > a.shape[axis] else n

    index[axis] = slice(None, (n_padded + 1) // 2)
    padded[tuple(index)] = a[tuple(index)]

    index[axis] = slice((-n_padded + 1) // 2, None)
    padded[tuple(index)] = a[tuple(index)]

    if n > a.shape[axis]:
        index[axis] = slice((n_padded + 1) // 2, (-n_padded + 1) // 2)
        padded[tuple(index)] = 0

    return padded


def padr(a, n, axis=-1):
    """Pad a frequency response with zeros at highest frequencies.

    Input should be ordered like numpy.fft.irfft function.
    """
    shape = list(a.shape)
    shape[axis] = n
    padded = numpy.empty(shape, a.dtype)

    index = [slice(None, None)] * len(a.shape)

    n_padded = a.shape[axis] if n > a.shape[axis] else n

    index[axis] = slice(None, n_padded)
    padded[tuple(index)] = a[tuple(index)]

    if n > a.shape[axis]:
        index[axis] = slice(n_padded, None)
        padded[tuple(index)] = 0

    return padded
