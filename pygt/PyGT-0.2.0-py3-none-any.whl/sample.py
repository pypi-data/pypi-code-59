# -*- coding: utf-8 -*-
r"""
Calculate sensitivity to additional computational discovery
------------------------------------------------------
Tools to calculate the sensitivity to the branching probability
between macrostates :math:`\mathcal{A}` and :math:`\mathcal{B}`
when expanding the underlying transition network
through additional computational discovery.
Details can be found in [Swinburne20a]_.

"""

import numpy as np
from io import StringIO
import time,os, importlib
#from tqdm import tqdm
np.set_printoptions(linewidth=160)
from . import io as kio
from . import GT
from scipy.sparse import save_npz,load_npz, diags, eye, csr_matrix,bmat
from scipy.sparse.linalg import eigs,inv,spsolve
import scipy as sp
import scipy.linalg as spla

def sensitivity(Q,npairs=20,nfilter=10000,rho=None):
		Nr = np.arange(self.sys.N)
		if self.sparse:
			rK = self.sys.rK.copy()# - sp.diags(self.sys.rK.diagonal(),format='csr')
		else:
			rK = self.sys.rK.copy() - np.diagflat(self.sys.rK.diagonal())

		kt = np.ravel(rK.sum(axis=0))
		selA,selI,selB=self.sys.selA*(kt>0.0),self.sys.selI*(kt>0.0),self.sys.selB*(kt>0.0)
		nA,nI,nB = selA.sum(),selI.sum(),selB.sum()
		mapA,mapI,mapB = Nr[selA], Nr[selI], Nr[selB]
		if rho is None:
			rho = np.ones(self.sys.N)
		rhoB = rho[selB].copy() / rho[selB].sum()

		if self.sparse:
			iDI = sp.diags(1.0 / kt[selI], format='csr')
			iDB = sp.diags(1.0 / kt[selB], format='csr')
			rK = rK.tocsr()
			BIB = rK[selI,:][:,selB]@iDB
			BAB = rK[selA,:][:,selB]@iDB
			BAI = rK[selA,:][:,selI]@iDI
			BII = rK[selI,:][:,selI]@iDI
			BBI = rK[selB,:][:,selI]@iDI
		else:
			iDI = np.diagflat(1.0/kt[selI])
			iDB = np.diagflat(1.0/kt[selB])
			BIB = rK[selI,:][:,selB].dot(iDB)
			BAB = rK[selA,:][:,selB].dot(iDB)
			BAI = rK[selA,:][:,selI].dot(iDI)
			BII = rK[selI,:][:,selI].dot(iDI)
			BBI = rK[selB,:][:,selI].dot(iDI)

		pi = np.exp(-self.sys.beta*self.sys.f)
		piA,piI,piB = pi[selA],pi[selI],pi[selB]
		oneA = np.ones(nA)
		Nt = float(nA+nI+nB) * float(nA+nI+nB)
		Na = float(self.probed.sum() // 2)
		if self.sparse:
			ed = float(self.sys.rK.nnz) / Nt
		else:
			ed = 1.0/Nt * (self.sys.rK>0.0).sum()
		"""
		linear solves:
		(1-BII).x = iGI.x = BIB.piB
		y.(1-BII) = y.iGI = 1.BAI
		"""
		# inverse Green function
		if self.sparse:
			iGI = sp.diags(np.ones(nI), format='csr') - BII
			x = spsolve(iGI,BIB@rhoB)
			y = spsolve(iGI.transpose(),oneA@BAI)
		else:
			iGI = np.identity(nI) - BII
			try:
				x = np.linalg.solve(iGI,np.ravel(BIB@rhoB))
			except np.linalg.LinAlgError as err:
				x,resid,rank,s = np.linalg.lstsq(iGI,np.ravel(BIB@rhoB),rcond=None)
			try:
				y = np.linalg.solve(iGI.transpose(),np.ravel(oneA@BAI))
			except np.linalg.LinAlgError as err:
				y = np.linalg.lstsq(iGI.transpose(),np.ravel(oneA@BAI),rcond=None)[0]

		iDx = iDI@x
		bab = (BAI@x).sum()+(BAB@rhoB).sum()
		yBIB = np.ravel(y@BIB)

		# i.e. take largest ij rate to ~ remove state Boltzmann factor
		if self.sparse:
			mM = (rK+rK.transpose())/2.0
			lM = -np.log(mM.data)
		else:
			mM = np.vstack((rK.flatten(),rK.transpose().flatten())).max(axis=0)
			lM = -np.log(mM[mM>0.0])

		mix = min(1.0,np.exp(-lM.std()/lM.mean()))
		ko = 1.0*np.exp(-3.0)
		mink = ko*(1.0-mix) + mix*np.exp(-lM.mean())

		fmapI = mapI
		iDBs = np.ravel(iDB@rhoB)
		yvB = np.ravel(yBIB) * np.ravel(iDBs)

		yvI = np.ravel(y) * np.ravel(iDx)

		cII = np.outer(y,iDx)-np.outer(np.ones(nI),yvI)
		cAI = np.outer(np.ones(nA),iDx-yvI)
		cIB = np.outer(y,iDBs)-np.outer(np.ones(nI),yvB)-np.outer(yvI,np.ones(nB)) # need phi.....


		"""
		b = k/kt -> (k+dk) / (kt+dk) -> 1.0 as dk->infty
		=> db < 1-b....
		dp/dt = -G^{-1}Dp => p = exp(-G^{-1}Dt)p = sum vlexp(-llt)pl
		G^{-1}
		p(t) = int_0^t dp/dt = sum (pl/ll)(1-exp(-llt))vl
		p(t) ~ p0/l0 qsd, [p0/l0] = (1/T)/(1/T) = 1
		iGDp -> sum vl ll pl
		=> D^{-1}G p = sum (1/ll) vl pl ~ p0/l0 qsd
		=> GP ~ p0/l0 D.qsd ->  D/rate . pi
		=> cab . Dpi/rate = 1 doesn't tell me anything..
		=> cab = rate/Dpi
		"""

		kf = np.outer(piA,1.0/piI)
		kf[kf>1.0] = 1.0
		cAI *= kf * mink

		kf = np.outer(piI,1.0/piI)
		kf[kf>1.0] = 1.0
		cII *= kf * mink

		kf = np.outer(piI,1.0/piB)
		kf[kf>1.0] = 1.0
		cIB *= kf * mink

		if self.sparse:
			cAI[self.probed[selA,:][:,selI].A] = 0.0
			cII[self.probed[selI,:][:,selI].A] = 0.0
			cIB[self.probed[selI,:][:,selB].A] = 0.0
		else:
			cAI[self.probed[selA,:][:,selI].A] = 0.0
			cII[self.probed[selI,:][:,selI].A] = 0.0
			cIB[self.probed[selI,:][:,selB].A] = 0.0

		#print("\n----\n",cAI.max(),cAI.min(),cII.max(),cII.min(),cIB.max(),cIB.min(),"\n----")
		c_tot = np.hstack(((np.triu(cII+cII.T)).flatten(),cAI.flatten(),cIB.flatten()))

		#print("c_tot:",c_tot.max(),c_tot.min(),c_tot.mean(),cmp,cmn,cm)

		res = {}

		# sparsity
		res['Sparsity'] = 0.5*np.exp(-0.001*Na) + (1.0 - np.exp(-0.001*Na))*ed
		em = res['Sparsity'] / (1.0-res['Sparsity'])

		res['SingleMaxMin'] = [c_tot.max(),c_tot.min()]
		res['ExpectMaxMin'] = [c_tot[c_tot>0.0].mean() * em ,c_tot[c_tot<0.0].mean() * em]
		res['TotalMaxMin'] = [c_tot[c_tot>0.0].sum(),c_tot[c_tot<0.0].sum()]
		res['TotalSparseMaxMin'] = [c_tot[c_tot>0.0].sum()*res['Sparsity'],c_tot[c_tot<0.0].sum()*res['Sparsity']]
		res['ExpectMaxMaxMin'] = [c_tot[c_tot>0.0].max() * em ,c_tot[c_tot<0.0].min() * em]



		res['ebab'] = bab
		res['mink'] = mink
		res['MaxInRegion'] = np.r_[[np.abs(cAI).max()/bab,np.abs(cII).max()/bab,np.abs(cIB).max()/bab]]
		"""
		pp = np.abs(c_tot).argsort()[-npairs:]#[::-1][:npairs]
		fp_in = np.zeros((npairs,2),int)
		nII = (pp<nI*nI).sum()
		if nII>0:
			fp = pp[pp<nI*nI]
			fp_in[:nII] = np.vstack((fmapI[fp//nI],fmapI[fp%nI])).T
		nAI = (pp<nI*nI+nA*nI).sum()
		if nAI>nII:
			fp = pp[(pp>nI*nI)*(pp<nI*nI+nA*nI)]-nI*nI
			fp_in[nII:nAI] = np.vstack((fmapI[fp//nI],fmapI[fp%nI])).T
		nIB = (pp>=nI*(nI+nA)).sum()
		if nIB>nAI:
			fp = pp[pp>=nI*(nI+nA)]-nI*(nI+nA)
			fp_in[-nIB:] = np.vstack((fmapI[fp//nB],fmapI[fp%nB])).T
		"""
		fp_in = []
		for fp in np.abs(c_tot).argsort()[::-1]:
			if np.abs(c_tot[fp])>1.0e-9*bab:
				fff = np.abs(c_tot[fp])
				if fp<nI*nI:
					p = [fmapI[fp//nI],fmapI[fp%nI]]
				elif fp<nI*nI+nA*nI:
					fp -= nI*nI
					p = [mapA[fp//nI],mapI[fp%nI]]
				else:
					fp -= nI*nI+nA*nI
					p = [mapI[fp//nB],mapB[fp%nB]]
				if not self.probed[p[0],p[1]]:
					fp_in.append(p)
				else:
					print("PROB")

			if len(fp_in) >= npairs:
				break
		return fp_in,res
