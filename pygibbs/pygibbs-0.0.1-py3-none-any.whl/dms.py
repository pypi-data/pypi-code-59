import  numpy as np
from scipy.sparse import spdiags
DTYPE   = np.float



def class FD:
    ''' 
    Finite Differenc (central) NxN  differentiation matrix (DM)
    '''

    
    def __init__(self, N, s, h):
        '''
        N, s, h = grid, #stencil points (odd), grid spacing
        '''
        self.N  = N
        self.s  = s
        self.h  = h
        self.st = int(s/2.0-1.0/2.0)               

        self.data0   = np.ones((s, N), dtype=DTYPE)        
        self.data    = np.zeros((s, N), dtype=DTYPE)        
        self.stp     = np.arange(-self.st, self.st + 1, dtype=DTYPE)    # stencil points 
        self.beta    = np.ones((self.s), dtype=DTYPE) 
        self.weights = np.zeros((self.s), dtype=DTYPE) 

        self.diagsL  = np.arange(-(N-1), -(N-1)+self.st, 1)       # lower circulant for PBC
        self.diagsU  = np.arange(N-self.st, N, 1)                 # upper circulant


    def diffmat(self, m):
        '''
        m-th order differentiation matrix using central differences.
        '''
        N=self.N; s=self.N; st=self.st

        self.diffweight(m)           
        D = spdiags(self.data, self.stp, N, N)
        
        #ensure PBC  
        D += spdiags(self.data[st+1:s,:],self.diagsL,N,N) + spdiags(self.data[0:st,:],self.diagsU,N,N)
        
        # scale by grid resolution
        D = D/(self.h**m)

        return D
            
        
    def diffweight(self, m):        
        '''
        *weights of the m-th order derivative using central Difference 
        *this can be read from the table if the code needs to be made fast
        *first generate the table using the code!
        '''
        wts=np.zeros((m+1, self.s), dtype=DTYPE)
        b0=1, bb, ihm=1.0/pow(self.h, m)
        for i in range(1, self.s):
            self.beta[i] = np.prod(self.stp[i]-self.stp[0:i])
        bt = self.beta  
        ww  = wts
        d0  = self.data0
        d1  = self.data 
        stp = self.stp

        ww[0,0] = 1.
        for i in range(1, self.s):
            jj = min(i, m)+1;   bb=b0/bt[i]
            for k in range(jj):
                ww[k, i] = bb*(k*ww[k-1,i-1]-(stp[i-1])*ww[k,i-1])
            b0 = bt[i]

            for j in range(i):
                for k in range(min(i,m),-1,-1):
                    ww[k,j] = ((stp[i])*ww[k,j]-k*ww[k-1,j])/(stp[i]-stp[j])
        
        for i in range(self.s):
            for j in range(self.N):
                d1[i,j] = d0[i,j] * ww[m, i] * ihm
        self.weights = wts[m, :] 
        return




def class FourierSpectral:
    ''' 
    Spectral method using Fourier tranform to compute the differentiation matrix (DM)
    '''
    def __init__(self, grid):
        '''
        grid is the argument
        '''
        self.dim = grid.get('dim')
        

        if self.dim == 1: 
            self.Nx = grid.get('Nx')
            self.kx  = 2*np.pi*np.fft.fftfreq(self.Nx)
            self.ksq = self.kx*self.kx

        elif self.dim == 2:
            self.Nx, self.Ny = grid.get('Nx'), grid.get('Ny')
            kxx = 2*np.pi*np.fft.fftfreq(self.Nx)
            kyy = 2*np.pi*np.fft.fftfreq(self.Ny)
            self.kx, self.ky = np.meshgrid(kxx, kyy)
            self.ksq = self.kx*self.kx + self.ky*self.ky


    def diffmat(self, m):
        '''
        m-th order differentiation matrix using FourierSpectral
        '''
        if self.dim==1:
            if m==1:
                D = 1j*self.kx
            elif m==2:
                D = -self.kx*self.kx
            else:
                print ('construct using combination of 1 and 2!')

        elif self.dim==2:
            if m==1:
                D = (1j*self.kx, 1j*self.ky)
            elif m==2:
                D = -(self.kx*self.kx + self.ky*self.ky)
            else:
                print ('construct using combination of 1 and 2!')
        
        else:
            print ('to implement 3D soon!')
        return D
            
        
    def dealias(self, double kDA):        
        '''
        dealias operator
        kDA: how much to dealias
        '''
        kxx = 2*np.pi*np.fft.fftfreq(self.Nx)
        kyy = 2*np.pi*np.fft.fftfreq(self.Ny)
        kx, ky = np.meshgrid(kxx, kyy)
        
        kmax = kDA*np.max(np.abs(kx))
        
        filtr1 = np.ones_like(kx)
        filtr2 = np.ones_like(ky)
        
        filtr1[np.where(np.abs(kx)>kmax)] = 0.
        filtr2[np.where(np.abs(ky)>kmax)] = 0.
        
        return filtr1*filtr2
