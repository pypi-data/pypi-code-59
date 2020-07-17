import numpy
import numpy.fft
import numpy.testing

import kk


def test_kk_real():
    w = (
        numpy.fft.ifftshift(numpy.arange(-(1 << 14), 1 << 14))
        * 100
        / (1 << 14)
    )
    X = (1 + 1j) / (1 + 1j * 10 * (w - 50)) + (1 + 1j) / (
        1 + 1j * 10 * (w + 50)
    )
    Xkk = kk.pure2kk(X.real)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5


def test_kk_imag():
    w = (
        numpy.fft.ifftshift(numpy.arange(-(1 << 14), 1 << 14))
        * 100
        / (1 << 14)
    )
    X = (1 + 1j) / (1 + 1j * 10 * (w - 50)) + (1 + 1j) / (
        1 + 1j * 10 * (w + 50)
    )
    Xkk = kk.pure2kk(1j * X.imag)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5


def test_kkr_real():
    w = numpy.linspace(0, 100, 1 << 14)
    X = 1 / (1 + 1j * 10 * (w - 50))
    Xkk = kk.pure2rkk(X.real)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5


def test_kkr_imag():
    w = numpy.linspace(0, 100, 1 << 14)
    X = 1 / (1 + 1j * 10 * (w - 50))
    Xkk = kk.pure2rkk(1j * X.imag)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5


def test_kk_real_N():
    w = (
        numpy.fft.ifftshift(numpy.arange(-(1 << 14), 1 << 14))
        * 100
        / (1 << 14)
    )
    X = (1 + 1j) / (1 + 1j * 10 * (w - 50)) + (1 + 1j) / (
        1 + 1j * 10 * (w + 50)
    )
    Xkk = kk.pure2kk(X.real, 1 << 16)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5


def test_kk_imag_N():
    w = (
        numpy.fft.ifftshift(numpy.arange(-(1 << 14), 1 << 14))
        * 100
        / (1 << 14)
    )
    X = (1 + 1j) / (1 + 1j * 10 * (w - 50)) + (1 + 1j) / (
        1 + 1j * 10 * (w + 50)
    )
    Xkk = kk.pure2kk(1j * X.imag, 1 << 16)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5


def test_kkr_real_N():
    w = numpy.linspace(0, 100, 1 << 14)
    X = 1 / (1 + 1j * 10 * (w - 50))
    Xkk = kk.pure2rkk(X.real, 1 << 16)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5


def test_kkr_imag_N():
    w = numpy.linspace(0, 100, 1 << 14)
    X = 1 / (1 + 1j * 10 * (w - 50))
    Xkk = kk.pure2rkk(1j * X.imag, 1 << 16)
    assert numpy.mean(numpy.abs(Xkk.real - X.real) ** 2) < 2e-5
    assert numpy.mean(numpy.abs(Xkk.imag - X.imag) ** 2) < 2e-5
