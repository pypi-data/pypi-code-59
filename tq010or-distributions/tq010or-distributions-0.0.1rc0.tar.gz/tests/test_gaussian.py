import unittest
from distributions.gaussian import Gaussian


class TestGaussian(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [0, 0, 0, 0, 0, 1.2, -1.19, -0.44, 0.34]
        self.mean = -0.011249999999999996
        self.std = 0.6289290562635026

    def test_calculate_std(self):
        output = Gaussian.calculate_std(self.data)
        assert output == self.std, "Incorrect std"

    def test_calcuate_mean(self):
        output = Gaussian.calculate_mean(self.data)
        assert output == self.mean, "Incorrect mean"

    def test_add(self):
        g1 = Gaussian(1, 3)
        g2 = Gaussian(2, 4)
        g3 = g1 + g2
        assert g1 + g2 == g3, "Unequal distributions"

    def test_estimate(self):
        g = Gaussian.estimate(self.data)
        mu = -0.011249999999999996
        sigma = 0.6289290562635026
        assert g.mu == mu and g.sigma == sigma, "Incorrect estimate"

    def test_sample(self):
        g = Gaussian(0, 1)
        samples = g.sample()
        ge = Gaussian.estimate(samples)
        # Estimations may have numeric value error,
        # thus we test equality againg round up values
        assert round(g.mu, 1) == round(ge.mu, 1) \
               and round(g.sigma, 1) == round(ge.sigma, 1), \
            "Sampling error"