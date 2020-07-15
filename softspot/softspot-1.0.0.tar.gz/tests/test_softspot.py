import unittest
import numpy as np 
import scipy.sparse as sp
import pickle
from os.path import join

from softspot.softspot import SoftSpot


data_folder = "../data"

class Test(unittest.TestCase):
    def setUp(self):
        data_file = join(data_folder, "ipl_swap2D_N4096_T0.7.npz")
        data = np.load(data_file, allow_pickle=True)

        self.pos = data['pos']
        self.box = data['box']
        self.psi = data['psi']
        self.kappa_psi = data['kappa_psi']
        self.pi = data['pi']
        self.kappa_pi = data['kappa_pi']
        self.hessian = data['hessian'][()]
        self.ndim = data['ndim']
        self.npart = data['npart']

    def test_find_lowest_from_lowest_harmonic_cg(self):
        x_init = self.psi   # lowest harmonic mode
        soft_spot = SoftSpot(ndim=self.ndim, npart=self.npart, hessian=self.hessian)
        result = soft_spot.find(x_init, mode='cg')

        norm = np.linalg.norm(result['pi'])
        self.assertTrue( np.isclose(norm, 1.0) )
        self.assertTrue( np.isclose(self.kappa_pi, result['kappa']) )

    def test_find_lowest_from_lowest_harmonic_mapping(self):
        x_init = self.psi   # lowest harmonic mode
        soft_spot = SoftSpot(ndim=self.ndim, npart=self.npart, hessian=self.hessian)
        result = soft_spot.find(x_init, mode='mapping')

        norm = np.linalg.norm(result['pi'])
        self.assertTrue( np.isclose(norm, 1.0) )
        self.assertTrue( np.isclose(self.kappa_pi, result['kappa']) )

    def test_find_lowest_from_random(self):
        np.random.seed(1)
        z_init = np.random.rand((self.ndim*self.npart))
        soft_spot = SoftSpot(ndim=self.ndim, npart=self.npart, hessian=self.hessian)
        result = soft_spot.find(z_init, mode='cg')
        print(result)



if __name__ == '__main__':
    unittest.main()
