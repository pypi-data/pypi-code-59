#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:56:37 2020

@author: jraidal
"""


from datetime import datetime
import itertools
import numpy
from numpy import arange
from numpy import vstack
from numpy import argmax
from numpy import asarray
from numpy.random import normal
from numpy.random import uniform
from scipy.stats import norm
from sklearn.gaussian_process import GaussianProcessRegressor
from warnings import catch_warnings
from warnings import simplefilter
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.gaussian_process.kernels import Matern, ConstantKernel, RBF, ExpSineSquared, RationalQuadratic, WhiteKernel
import sys


# Define objective function

def Bayesian2D_opt(x_bounds, y_bounds, starting_n, iterations, max_min, exploration, function = 'Rosenbrock' ):
    startTime = datetime.now()
    numpy.random.seed()
      
    e=exploration
    
    model = GaussianProcessRegressor(kernel= Matern(), alpha = 1e-10)
    
    x1, x2 = x_bounds
    y1, y2 = y_bounds
    
    def objective(x, y, function):
        if function == 'Beale':
          #Beale
            return (1.5-x+x*y)**2+(2.25-x+x*y**2)**2+(2.625-x+x*y**3)**2
        if function == 'Goldstein-Price':
          #Goldstein-Price
            return (1+(x+y+1)**2 * (19-14*x+3*x**2-14*y+6*x*y+3*y**2))*(30+(2*x-3*y)**2 * (18-32*x+12*x**2+48*y-36*x*y+27*y**2))
        if function == 'Rosenbrock':
          #Rosenbrock
            return ((1 - x)**2 + 100*(y - x**2)**2)
        if function == 'Ackley':
          #Ackley
            return -20*numpy.exp(-0.2*numpy.sqrt(0.5*(x**2 + y**2)))-numpy.exp(0.5*(numpy.cos(2*numpy.pi*x) + numpy.cos(2*numpy.pi*y)))+numpy.exp(1)+20
        else:
            return eval(function)
    
    # surrogate model
    def surrogate(model, XY): 
        return model.predict(XY, return_std=True)
    
    # Maximum probability of improvement acquisition function
    def acquisition(XY, XYsamples, e, model):
        # calculate the best surrogate score found so far
        zhat, _ = surrogate(model, XY)
        # zhat = preprocessing.scale(zhat)
        if max_min == 'maximum':
            best = numpy.max(zhat)
        if max_min == 'minimum':
            best = numpy.min(zhat)
        # calculate mean and covariance via surrogate function
        mu, std = surrogate(model, XYsamples)
        # calculate the probability of improvement
        r=(mu-best)
        c=(r)/(std+1e-9)
        with catch_warnings():
            # ignore generated warnings
            simplefilter("ignore")
            c= preprocessing.scale(c)  
        probs=norm.cdf(c - e)
        return probs
    
    # optimize the acquisition function
    def opt_acquisition(XY):
      Xsamples = ([])
      Ysamples = ([])
      for i in range(100):
          a = uniform(x1,x2)
          Xsamples.append(a)
          b = uniform(y1,y2)
          Ysamples.append(b)
      Xsamples = numpy.array(Xsamples)
      Ysamples = numpy.array(Ysamples)
      XYsamples=numpy.vstack((Xsamples, Ysamples)).T
      # calculate the acquisition function for each sample
      # locate the index of the largest scores
      scores = acquisition(XY, XYsamples, e, model)
      
      if max_min == 'maximum':
            index_max = (numpy.argwhere(scores == numpy.max(scores)))
      if max_min == 'minimum':
            index_max = (numpy.argwhere(scores == numpy.min(scores)))
      
      ix_max = index_max[0,0]
      X_max, Y_max = XYsamples[ix_max]
      Xsamples = float(X_max)
      Ysamples = float(Y_max)
      return Xsamples, Ysamples
    
    # plot real observations
    def plot():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # surface plot of objective function
        Xsamples = numpy.linspace(x1, x2, 500)
        Ysamples = numpy.linspace(y1, y2, 500)
        X, Y = numpy.meshgrid(Xsamples, Ysamples)
        Z = objective(X, Y, function)
        ax.plot_surface(X,Y,Z, cmap = 'jet' )
        # show the plot
        ax.view_init(45, 45)
        plt.show()
    
    
    # Set domain and evaluations per cycle
    def initial_points():
        X = ([])
        for i in range(0, starting_n):
            a = uniform(x1, x2)
            X.append(a)
        Y = ([])
        for i in range(0, starting_n):
            b = uniform(y1, y2)
            Y.append(b)
        X=numpy.array(X)
        Y=numpy.array(Y)
        XY=numpy.vstack((X, Y)).T
        z= objective(X, Y, function)
        return XY, z

        
    def fit_model(model, data_input, data_output):
        # fit the model
        model.fit(data_input, data_output)
        # plot before hand

        """Editisid "/home/jraidal/anaconda3/lib/python3.7/site-packages/sklearn/gaussian_process/_gpr.py", line 312"""
        
    def optimize():
        plot()
        XY, z = initial_points()
        # perform the optimization process
        for i in range(iterations):
            # select the next point to sample
            x, y = opt_acquisition(XY)
            XYmingi = numpy.array(([x, y]))
            XYmingi = XYmingi.reshape(1, -1)
            # sample the point
            actual = objective(x, y, function)
            # summarize the finding
            print(f'{i+1}/{iterations} completed')
            print(f'Currently evaluating x=%.3f y=%.3f with value of z=%.4f' % (x, y, actual))
            # add the data to the dataset
            XYnew_element = numpy.array(([x, y]))
            XY=numpy.vstack((XY, XYnew_element))
            z = list(z)
            z.append(actual)
            z = numpy.array(z)
            if max_min == 'maximum':
                z_best = numpy.max(z)
            if max_min == 'minimum':
                z_best = numpy.min(z)
            print(f'Current {max_min} found is z = {z_best}')
            # update the model
            model.fit(XY, z)
        return XY, z
        
    def results(): 
        
        XY, z = optimize()
        # best result
        if max_min == 'maximum':
            index = (numpy.argwhere(z == numpy.max(z)))
            z_best = numpy.max(z)
            ix = index[0, 0]
        if max_min == 'minimum':
            index = (numpy.argwhere(z == numpy.min(z)))
            z_best = numpy.min(z)
            ix = index[0,0]
        
        x, y = XY[ix]
        Xfinal=([])
        Yfinal=([])
        for x, y in XY:
            Xfinal.append(x)
            Yfinal.append(y)
        Xfinal=numpy.array(Xfinal)
        Yfinal=numpy.array(Yfinal)
        Z = z
                
        ax = plt.axes(projection='3d')
        ax.scatter(Xfinal, Yfinal, Z, linewidth=0.5)
        ax.view_init(45, 45)
        plt.show()
        
        
        print('')
        print('The %s is at x=%f, y=%f with a value of z=%f' % (max_min, x, y, z_best))
        print('Time elapsed', datetime.now() - startTime)
        print('Time per cycle', (datetime.now() - startTime)/iterations)
        return x, y, z_best


    return results()



# xy = ([])
# res = ([])
# for i in range(10):  
#     x, y , z = Bayesian2D_opt(([-100, 100]), ([-100, 100]), 10, 200, 'minimum', 0.1, 'Rosenbrock')
#     xy.append(([x, y]))
#     res.append(z)
# print(xy)
# print(res)
# iasd=numpy.argmin(res)
# print(xy[iasd], res[iasd])