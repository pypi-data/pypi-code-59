from __future__ import annotations
from enum import Enum
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class DistributionType(Enum):
    GAUSSIAN = 1
    BINOMIAL = 2


class Distribution(ABC):

    def __init__(self, dist_type: DistributionType):
        """Generic distribution class for calculating and visualizing a probability distribution.

        :param dist_type: A distribution type defined in DistributionType
        """
        assert isinstance(dist_type, DistributionType), f"Unknown type of {type(dist_type)}"
        self.dist_type = dist_type

    @abstractmethod
    def sample(self, n: int) -> list:
        """Get one ore more samples for this probability distribution

        :param n: number of samples to return for this distribution
        :return: A list containing samples containing n samples from this distribution
        """
        pass

    @classmethod
    @abstractmethod
    def estimate(cls, samples: list) -> Distribution:
        """Estimate the parameters for this distribution with the given samples

        :param samples: a list of samples to estimate from
        :return: an estimated distribution
        """
        pass

    def plot(self, plt_data: list = None):
        """Plot histogram of the data

        :param plt_data: None or a list of data points
        :return: None
        """
        if not plt_data:
            plt_data = self.sample(20)
        plt.hist(plt_data)
        plt.title(f'Histogram of {self.dist_type.name}')
        plt.xlabel('data')
        plt.ylabel('count')

    def __and__(self, other: Distribution) -> Distribution:
        """Addition of two distributions

        :param other: another distribution of the same type to be added
        :return: A new distribution
        """
        return NotImplemented

    def __sub__(self, other):
        """Subtraction of two distributions

        :param other: another distribution of the same type to substract
        :return: A new distribution
        """
        return NotImplemented

    def __eq__(self, other):
        """Comparison of distributions

        :param other: another distribution of the same type
        :return: boolean to indicate the equality
        """
        return NotImplemented

    def __repr__(self):
        return f"Distribution({self.dist_type.name})"
