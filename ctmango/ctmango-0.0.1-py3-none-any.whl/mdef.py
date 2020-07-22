from scipy.stats import norm, poisson, binom 

def ranfd(n = 10, distro='norm', **kwargs):
    '''
    Description of the ranfd function (RAndom Numbers From Distribution)
    
    Parameters: n : int
                    sample size, default = 10 
                distro : str
                    'norm' (default): the sample is generated from a normal distribution
                    'poisson': the sample is generated from a poisson distribution
                    'binom': the sample is generated from a binomial distribution
                kwargs : dict, shape parameters of the distribution as keyword arguments 
                    - For normal distribution pass as keyword arguments the following: 
                    'mn' : the mean of the distribution 
                    'sd' : the standard deviation of the distribution
                    - For poisson distribution pass as keyword arguments the following: 
                    'mu' : the mu of the poisson distribution 
                    - For binomial distribution pass as keyword arguments the following: 
                    'nb' : the n of the binomial distribution 
                    'pb' : the p of the binomial distribution        
    
    Returns:
                numpy ndarray : an array of size n of values randomly chosen from the specified distribution. 
    
    '''
    

    try: 
        if distro == 'norm':
            sample = norm.rvs(loc = kwargs['mn'], 
                              scale = kwargs['sd'],
                              size = n)
            return sample
        
        elif distro == 'poisson':
            sample = poisson.rvs(mu = kwargs['mu'],
                                 size = n)
            return sample

        elif distro == 'binom':
            sample = binom.rvs(n = kwargs['nb'],
                               p = kwargs['pb'],
                               size = n)
            return sample
    
    except Exception as err:
        print(err)
        print('Exception in randf. Please check if shape parameters of distributions have been correclty initialized')




