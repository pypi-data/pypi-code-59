import math
from functools import reduce
import random
from distributions.base_distribution import Distribution, DistributionType


class Binomial(Distribution):
    """ Binomial distribution
    """

    def __init__(self, n, p):
        Distribution.__init__(self, DistributionType.BINOMIAL)
        self.n = n
        self.p = p

    def sample(self, n: int) -> list:
        upper_bound = max(1000, n)
        bar_num = int(upper_bound * self.p)
        samples = []
        for i in range(n):
            r = random.randint(0, upper_bound)
            samples.append(1 if r <= bar_num else 0)
        return samples

    @classmethod
    def estimate(cls, samples: list) -> Distribution:
        assert samples, "Empty samples"
        n = len(samples)
        p = float(sum(samples)) / n
        return Binomial(n, p)

    def pmf(self, k: int) -> int:
        smaller = min(k, self.n - k)
        num = [i for i in range(self.n - smaller+ 1, self.n + 1)]
        num = reduce(lambda a, b: a * b, num)
        denom = math.factorial(smaller)
        return (num / denom) * pow(self.p, k) * pow((1 - self.p), self.n-k)

    def __add__(self, other):
        assert isinstance(other, Binomial), f"Cannot add with Type {type(other)}"
        # if two Biomials do NOT have the same probability p,
        # then the variance of the sum will be smaller than the variance of a binomial variable
        # and we report NotImplemented here
        if other.p == self.p:
            return Binomial(self.n + other.n, self.p)
        else:
            raise NotImplemented

    def __sub__(self, other):
        assert isinstance(other, Binomial), f"Cannot sub with Type {type(other)}"
        if other.p == self.p:
            return Binomial(self.n - other.n, self.p)
        else:
            raise NotImplemented

    def __eq__(self, other):
        assert isinstance(other, Binomial), f"Cannot compare with Type {type(other)}"
        return True if self.n == other.n and self.p == other.p else False

    def __repr__(self):
        return f"Bionmial({self.n}, {self.p})"