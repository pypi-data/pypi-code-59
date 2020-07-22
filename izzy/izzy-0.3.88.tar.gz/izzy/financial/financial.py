
import numpy as np
import numpy_financial as npf


def cumipmt(coupon, exposure, n_statements):
    return np.sum(npf.ipmt(rate=coupon / 12., per=np.arange(n_statements) + 1, nper=n_statements, pv=exposure))
