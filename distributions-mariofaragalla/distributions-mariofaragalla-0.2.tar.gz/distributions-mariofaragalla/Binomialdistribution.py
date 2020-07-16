import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
            
    """
    
    def __init__(self, prob=.5, size=20):          
        
        self.p = prob
        self.n = size
        
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        
    def calculate_mean(self):
        
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """       
        p = self.p 
        n = self.n
        self.mean = 1.0* p * n  
        return self.mean


    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        p = self.p 
        n = self.n
        self.stdev = (n * p * (1 - p))**0.5
        return self.stdev
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
        pass
        
        self.n = len(self.data)
        self.p = 1.0 * self.data.count(1) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n # you must return n and p in this order to pass the unit test
    
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        
        # helpful link: https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm
        
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        xaxis = ['0', '1']
        tails = self.data.count(0)
        heads = self.data.count(1)
        yaxis = [tails, heads]
        ax.set_xlabel('x axis')
        ax.set_ylabel('y axis')
        ax.set_title('No. of occurences')
        ax.bar(xaxis, yaxis)
        
        plt.show()
        
        
    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """

        n = self.n
        p = self.p
        n_fac = math.factorial(n)
        k_fac = math.factorial(k)
        diff_n_k_fac = math.factorial(n-k)
        f = 1.0 * (n_fac/(k_fac*diff_n_k_fac))* (p**k)*(1-p)**(n-k)
        return f
    
    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        k_list = [range(0, self.n, 1)] 
        xaxis = [k_list]
        ax.set_xlabel('k')
        ax.set_ylabel('pdf')
        ax.set_title('k vs probability density function')
        ax.bar(xaxis, yaxis)
        

        for k in range(0,self.n):
            pdf_list= self.pdf(k)
        
        yaxis = [pdf_list]
        plt.show()
        
        
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
        result.p = self.p
        result.n = self.n + other.n
        
        return result
    
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
    
        return "mean {}, standard deviation {}, p {} , n {}".format(self.mean, self.stdev, self.p, self.n)
