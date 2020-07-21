import dill 
dill.settings['recurse'] = True
import numpy as np
from borehole import borehole

def fun(x):
	return borehole(x)


funs = dill.dumps(fun)
print funs
x = np.random.randn(8)
del borehole

fun2 = dill.loads(funs)
print fun2(x)
