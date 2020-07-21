import math
import numpy as np
import matplotlib.pyplot as plt
import scipy

def TR(n):
	tr=n*(n-1)
	return tr
def tn(n, t1, d):
	tn=t1+d*(n-1)
	return tn

pi=3.14159265358979323846264338327950
e=2.7182818284590452353602874713527

def sqrt(n):
	sqrty=math.sqrt(n)
	return sqrty

def square(n):
	n=n**2
	return n

def pow(x, y):
	n=x**y
	return n

def absgraph(x):
        pass

def dectofrac(dec):
    frac=str(dec)+'/1'
    return frac

