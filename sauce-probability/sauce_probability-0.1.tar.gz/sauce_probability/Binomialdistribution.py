import matplotlib.pyplot as plt
from .Generaldistribution import Distribution
import math


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    def __init__(self, prob=.5, n=20):
        self.p = prob
        self.n = n

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())



    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """

        mean = self.n * self.p
        return mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args:
            None

        Returns:
            float: standard deviation of the data set

        """
        stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return stdev


    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """

        self.n = len(self.data)
        self.p = sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n

    def plot_bar(self):

        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(x=['0', '1'], height=[(1 - self.p) * self.n, self.p * self.n])
        plt.xlabel('Outcome')
        plt.ylabel('Count')
        plt.title('Count of Outcomes in Data')
        plt.show()

    def pdf(self, k):

        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        exp = math.factorial(self.n) / (math.factorial(self.n - k) * math.factorial(k))
        x = exp * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return x


    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """
        x = []
        y = []
        for i in range(0, len(self.data)):
            x.append(i)
            y.append(round(self.pdf(k=i), 2))

        plt.bar(x, y)
        plt.xlabel('Outcome')
        plt.ylabel('Probability of Outcome')
        plt.title('PDF of Binomial Distribution for all Possible Outcomes')
        plt.show()

        return x, y

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        return result


    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """

        return "Mean: {}, Standard Deviation: {}, p: {}, n: {}.".format(self.mean, self.stdev, self.p, self.n)
