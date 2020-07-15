import numpy as np

'''
Make a fake template and target.
'''


def make_template(mean=(0, 1), covariance=np.array([[4,0],[0,1]]), shape=(100, 100)):
    return np.random.normal(loc=mean, scale=covariance, size=shape)