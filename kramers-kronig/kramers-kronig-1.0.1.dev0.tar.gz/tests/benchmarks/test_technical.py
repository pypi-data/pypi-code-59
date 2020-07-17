import numpy.fft
import numpy.random


def ifft_fft(data, norm):
    numpy.fft.fft(numpy.fft.ifft(data, norm=norm), norm=norm)


def irfft_rfft(data, norm):
    numpy.fft.rfft(numpy.fft.irfft(data, norm=norm), norm=norm)


def test_None(benchmark):
    data = numpy.random.rand(1 << 16)
    benchmark(ifft_fft, data, None)


def test_ortho(benchmark):
    data = numpy.random.rand(1 << 16)
    benchmark(ifft_fft, data, "ortho")


def test_rNone(benchmark):
    data = numpy.random.rand(1 << 15)
    benchmark(irfft_rfft, data, None)


def test_rortho(benchmark):
    data = numpy.random.rand(1 << 15)
    benchmark(irfft_rfft, data, "ortho")


def pad_with_shift(data, n):
    numpy.fft.ifftshift(
        numpy.pad(
            numpy.fft.fftshift(data),
            ((n - len(data)) // 2, (n - len(data)) // 2),
            "constant",
            constant_values=0,
        )
    )


def test_pad_with_shift(benchmark):
    data = numpy.random.rand(1 << 14)
    benchmark(pad_with_shift, data, 1 << 16)


def pad_without_shift(data, n):
    result = numpy.empty(n)
    result[: len(data) // 2] = data[: len(data) // 2]
    result[len(data) // 2 : -len(data) // 2] = 0
    result[-len(data) // 2 :] = data[-len(data) // 2 :]


def test_pad_without_shift(benchmark):
    data = numpy.random.rand(1 << 14)
    benchmark(pad_without_shift, data, 1 << 16)
