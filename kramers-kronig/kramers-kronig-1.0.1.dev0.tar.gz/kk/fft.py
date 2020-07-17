"""Functions to compute Kramers-Kronig relations through Fourier transforms."""

import numpy
import numpy.fft

import kk.utils


def pure2kk(a, n=None, axis=-1):
    """Compute frequency response function of a complex-valued time response.

    Input should be its real or 1j*imaginary part. Input should be ordered
    like numpy.fft.ifft function.
    """
    padded = a if n is None else kk.utils.pad(a, n, axis=axis)

    sp = numpy.fft.ifft(padded, axis=axis)
    index = [slice(None, None)] * len(padded.shape)

    index[axis] = slice(padded.shape[axis] // 2 + 1, None)
    sp[tuple(index)] = 0

    index[axis] = slice(0, 1)
    sp[tuple(index)] /= 2

    if n is None:
        return 2 * numpy.fft.fft(sp, axis=axis)
    else:
        return 2 * kk.utils.pad(
            numpy.fft.fft(sp, axis=axis), a.shape[axis], axis=axis
        )


def pure2rkk(a, n=None, axis=-1):
    """Compute frequency response function of a real-valued time response.

    Input should be its real or 1j*imaginary part. Input should be ordered
    like numpy.fft.irfft function. Note that the frequency response function
    is hermitian symmetric.
    """
    padded = a if n is None else kk.utils.padr(a, n, axis=axis)

    sp = numpy.fft.irfft(padded, axis=axis)
    index = [slice(None, None)] * len(padded.shape)

    index[axis] = slice(padded.shape[axis], None)
    sp[tuple(index)] = 0

    index[axis] = slice(0, 1)
    sp[tuple(index)] /= 2

    if n is None:
        return 2 * numpy.fft.rfft(sp, axis=axis)
    else:
        return 2 * kk.utils.padr(
            numpy.fft.rfft(sp, axis=axis), a.shape[axis], axis=axis
        )
