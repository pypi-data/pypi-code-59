import unittest
from distributions.binomial import Binomial


class TestBinomial(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_pmf(self):
        b = Binomial(6, 0.3)
        output = b.pmf(4)
        assert output == 0.05953499999999999, "Incorrect PMF"

    def test_add(self):
        g1 = Binomial(1, 0.6)
        g2 = Binomial(2, 0.6)
        g3 = g1 + g2
        assert g1 + g2 == g3, "Unequal distributions"

    def test_estimate(self):
        data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        g = Binomial.estimate(data)

    def test_sample(self):
        expected = 600
        b = Binomial(1000, 0.6)
        outputs = sum(b.sample(1000))
        assert float(abs(outputs - expected)/expected) <= 0.05, "Sampling error"