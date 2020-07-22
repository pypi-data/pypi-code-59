import numpy as np
from scipy.stats import norm, poisson, binom

class Ranfdcl():
    '''
    The Ranfdcl object draws sets of random numbers according to the distributions parameters
            
    Attributes: 
        distro (str): The type of the distribution
        sample (numpy ndarray): an array of size n of values randomly chosen from the specified distribution
        
        - In case of normal distribution (distro == 'norm'): 
        loc (float): the mean of the normal distribution 
        sd (float): the standard distribution of the normal distribution
        
        - In case of poisson distribution (distro == 'poisson'): 
        mu (float): the mu shape parameter of the poisson distribution
        
        - In case of binomial distribution (distro == 'binom'): 
        nb (float): the n shape parameter of the binomial distribution 
        pb (float): the p shape parameter of the binomial distribution                    
        '''
        
    def __init__(self, distro='norm', **kwargs): 
        '''
        The constructor for RaNFD class 
        
        Parameters:
            distro (str): the type of the distribution from where the sample is drawn. Acceptable values include:
                'norm' (default): the sample is generated from a normal distribution
                'poisson': the sample is generated from a poisson distribution
                'binom': the sample is generated from a binomial distribution
            kwargs (dict): shape parameters of the distribution as keyword arguments 
                - For normal distribution pass as keyword arguments the following: 
                'mn' : the mean of the distribution 
                'sd' : the standard deviation of the distribution
                - For poisson distribution pass as keyword arguments the following: 
                'mu' : the mu of the poisson distribution 
                - For binomial distribution pass as keyword arguments the following: 
                'nb' : the n of the binomial distribution 
                'pb' : the p of the binomial distribution        
            
        '''
        
        self.distro = distro
        try: 
            if self.distro == 'norm':
                self.loc = kwargs['mn']
                self.scale = kwargs['sd']
                
            elif self.distro == 'poisson':
                self.mu = kwargs['mu']
                
            elif self.distro == 'binom':
                self.nb = kwargs['nb']
                self.pb = kwargs['pb']
                
        except:
            print('Exception in constructing object of RandSampleFromDistro \
                  Please check if shape parameters of distributions have been correclty initialized')
            
    
    def draw(self, n = 10):
        '''
        The draw method draws a fresh set of n random numbers from a specified distribution 
        
        Parameters: 
            n (int): the sample size (random numbers) to be returned by method draw, default = 10  
          
        Returns:
            None
        '''

        if self.distro == 'norm':
            self.sample = norm.rvs(loc = self.loc,
                                   scale = self.scale,
                                   size = n)
        elif self.distro == 'poisson':
            self.sample = poisson.rvs(mu = self.mu,
                                      size = n)          
        elif self.distro == 'binom':
            self.sample = binom.rvs(n = self.nb,
                                    p = self.pb,
                                    size = n)
            
    def summarize(self):
        '''
        The summarize method print the min, max, mean and standard deviation of the drawn sample
        
        Parameters: 
            None  
          
        Returns:
            None
        '''
        print('sample min = ', min(self.sample))
        print('sample max = ', max(self.sample))
        print('sample mn = ', np.mean(self.sample))
        print('sample sd = ', np.std(self.sample))
