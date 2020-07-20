import math
import warnings
import random
from distributions.base_distribution import Distribution, DistributionType


class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and visualizing a Gaussian distribution.
    """

    def __init__(self, mu, sigma):
        Distribution.__init__(self, DistributionType.GAUSSIAN)
        self.mu = mu
        self.sigma = sigma

    @classmethod
    def load_data_from_iterables(cls, iterables) -> Distribution:
        data = []
        for dp in iterables:
            data.append(float(dp))
        return Gaussian.estimate(data)

    @classmethod
    def estimate(cls, samples: list) -> Distribution:
        mu = Gaussian.calculate_mean(samples, sample_flag=True)
        sigma = Gaussian.calculate_std(samples, sample_flag=True)
        return Gaussian(mu, sigma)

    def sample(self, n: int = 10000) -> list:
        return [random.gauss(self.mu, self.sigma) for _ in range(n)]

    @staticmethod
    def calculate_mean(data: list, sample_flag=True) -> float:
        """Calculate the sample/population mean

        :param data: data for mean calculation
        :param sample_flag: True to indicate this is sample mean, False for population mean
        :return: the sample/distribution mean
        """
        # In case there is only one data point
        if sample_flag and data and len(data) == 1:
            warnings.warn("There is only one data point provided")
            return data[0]
        num = 1.0 * sum(data)
        denom = len(data) - 1 if sample_flag else len(data)
        assert denom > 0, f"denominator should be positive integers"
        return num / denom

    @staticmethod
    def calculate_std(data: list, sample_flag=True) -> float:
        """Calculate Gaussian standard deviation (std)

        :param data: data for std calculation
        :param sample_flag: True to indicate this is sample mean, False for population mean
        :return: the sample/distribution std
        """
        n = len(data) - 1 if sample_flag else len(data)
        mean = Gaussian.calculate_mean(data, sample_flag)
        sigma = math.sqrt(sum((d - mean) ** 2 for d in data) / n)
        return sigma

    def pdf(self, x: float) -> float:
        """Calculate the probability density function (PDF) given the input point x

        :param x: point for calculating PDF
        :return: the PDF result
        """
        return (1.0 / (self.sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.mu) / self.sigma) ** 2)

    def __add__(self, other):
        assert isinstance(other, Gaussian), f"Cannot add with Type {type(other)}"
        mu = self.mu + other.mu
        sigma = math.sqrt(self.sigma ** 2 + other.sigma ** 2)
        return Gaussian(mu, sigma)

    def __sub__(self, other):
        assert isinstance(other, Gaussian), f"Cannot subtract with Type {type(other)}"
        mu = self.mu - other.mu
        sigma = math.sqrt(self.sigma ** 2 - other.sigma ** 2)
        return Gaussian(mu, sigma)

    def __eq__(self, other):
        assert isinstance(other, Gaussian), f"Cannot compare with Type {type(other)}"
        return True if self.mu == other.mu and self.sigma == other.sigma else False

    def __repr__(self):
        return f"Gaussian({self.mu}, {self.sigma})"


