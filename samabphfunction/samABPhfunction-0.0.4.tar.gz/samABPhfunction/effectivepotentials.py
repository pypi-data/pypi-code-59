import numpy as np

import scipy.special as spec

from .wfuncsoft import wFuncSoft

class W2potential(wFuncSoft):

    def __init__(self,Omega=None,Pe=1,epsilon=1,Pi=1):

        super().__init__(Omega=Omega,Pe=Pe,epsilon=epsilon,Pi=Pi)
        
        return


    def evaluate(self,r):
        
        return (self.V_WCA(r)
                -0.5*self.Pe**2*self.w(r)**2*r**2)    


    def prime(self,r):

        w = self.w(r)

        return (self.V_WCA_prime(r)-self.Pe**2*r*w**2
                -self.Pe**2*r**2*w*self.w_prime(r))

class W3potential(wFuncSoft):

    def __init__(self,Omega=None,Pe=1,epsilon=1,Pi=1):

        super().__init__(Omega=Omega,Pe=Pe,epsilon=epsilon,Pi=Pi)
        
        return

    
    def evaluate(self,u,v,theta):
        
        return (-3./2.*self.Pe**2*self.w(u)*self.w(v)
               *u*v*np.cos(theta))

    def prime_u(self,u,v,theta):

        return (-3./2.*self.Pe**2*self.w_prime(u)*self.w(v)
                *u*v*np.cos(theta)
                -3./2.*self.Pe**2*self.w(u)*self.w(v)
                *v*np.cos(theta))

    def prime_v(self,u,v,theta):

        return self.prime_u(v,u,theta)
        

class Chi2potential(wFuncSoft):

    def __init__(self,Omega=None,Pe=1,epsilon=1,Pi=1):
            
        super().__init__(Omega=Omega,Pe=Pe,epsilon=epsilon,Pi=Pi)
        
        return

    def evaluate(self,r):

        w = self.w(r)

        return self.V_WCA(r)-2*np.log(spec.i0(self.Pe*w*r))
    

    def prime(self,r):

        w = self.w(r)

        return (self.V_WCA_prime(r)
                -2*self.Pe*spec.ivp(0,self.Pe*w*r)/spec.i0(self.Pe*w*r)
                *(w+r*self.w_prime(r)))    
