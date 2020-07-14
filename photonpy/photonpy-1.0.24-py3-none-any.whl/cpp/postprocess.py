# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import ctypes
from .lib import SMLM
import numpy as np
import numpy.ctypeslib as ctl


class PostProcessMethods:
    def __init__(self, ctx):
        self.lib = ctx.smlm.lib

        #CDLL_EXPORT void LinkLocalizations(int numspots, int* frames, Vector2f* xyI, float maxDist, int frameskip, int *linkedSpots)

        self._LinkLocalizations = self.lib.LinkLocalizations
        self._LinkLocalizations.argtypes = [
            ctypes.c_int32,  # numspots
            ctl.ndpointer(np.int32, flags="aligned, c_contiguous"),  # framenum
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # xyI
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # crlbXYI
            ctypes.c_float,  # maxdist (in crlbs)
            ctypes.c_float, # max intensity distance (in crlb's)
            ctypes.c_int32,  # frameskip
            ctl.ndpointer(np.int32, flags="aligned, c_contiguous"),  # linkedspots
            ctl.ndpointer(np.int32, flags="aligned, c_contiguous"), # startframes
            ctl.ndpointer(np.int32, flags="aligned, c_contiguous"),  # framecounts
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # linkedXYI
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # linkedCRLBXYI
        ]
        self._LinkLocalizations.restype = ctypes.c_int32
        

        #(const Vector2f* xy, const int* spotFramenum, int numspots,
        #float sigma, int maxiterations, Vector2f* driftXY,  float gradientStep, float maxdrift, float* scores, int flags)

        self.ProgressCallback = ctypes.CFUNCTYPE(
            ctypes.c_int32,  # continue
            ctypes.c_int32,  # iteration
            ctypes.c_char_p
        )
        
        

        self._GaussianOverlapDriftEstimate = self.lib.GaussianOverlapDriftEstimate
        self._GaussianOverlapDriftEstimate.argtypes = [
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # xy Vector2f
            ctl.ndpointer(np.int32, flags="aligned, c_contiguous"),  # framenum
            ctypes.c_int32,  # numspots
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # sigma [dims]
            ctypes.c_int32, #maxit
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # drift XY
            ctypes.c_int32, # framesperbin
            ctypes.c_float, # gradientstep
            ctypes.c_float, # maxdrift
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # scores
            ctypes.c_int32,
            self.ProgressCallback] # flags
        self._GaussianOverlapDriftEstimate.restype = ctypes.c_int32
        
    
        #void ComputeContinuousFRC(const float* data, int dims, int numspots, const float* rho, int nrho, float* frc, float maxDistance, bool useCuda)
        self._ComputeContinuousFRC = self.lib.ComputeContinuousFRC
        self._ComputeContinuousFRC.argtypes = [
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # data (xy or xyz)
            ctypes.c_int32,  # number of dimensions
            ctypes.c_int32,  # numspots
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # rho
            ctypes.c_int32,  # nrho
            ctl.ndpointer(np.float32, flags="aligned, c_contiguous"),  # output frc
            ctypes.c_float, # maxdistance
            ctypes.c_bool, # usecuda
            ctypes.c_float, # cutoffDist
            ctypes.c_float # cutoffSigma
        ]
        
                
    
    def LinkLocalizations(self, xyI, crlbXYI, framenum, maxdist, maxIntensityDist, frameskip):
        """
        linked: int [numspots], all spots that are linked will have the same index in linked array.
        """
        xyI = np.ascontiguousarray(xyI,dtype=np.float32)
        crlbXYI = np.ascontiguousarray(crlbXYI,dtype=np.float32)
        framenum = np.ascontiguousarray(framenum, dtype=np.int32)
        linked = np.zeros(len(xyI),dtype=np.int32)
        framecounts = np.zeros(len(xyI),dtype=np.int32)
        startframes = np.zeros(len(xyI),dtype=np.int32)
        resultXYI = np.zeros(xyI.shape,dtype=np.float32)
        resultCRLBXYI = np.zeros(crlbXYI.shape,dtype=np.float32)
        
        assert crlbXYI.shape[1] == 3
        assert xyI.shape[1] == 3
        assert len(xyI) == len(crlbXYI)
        
        nlinked = self._LinkLocalizations(len(xyI), framenum, xyI, crlbXYI, maxdist, maxIntensityDist, 
                                          frameskip, linked, startframes, framecounts, resultXYI, resultCRLBXYI)
        startframes = startframes[:nlinked]
        framecounts = framecounts[:nlinked]
        resultXYI = resultXYI[:nlinked]
        resultCRLBXYI = resultCRLBXYI[:nlinked]
        return linked, framecounts,startframes, resultXYI, resultCRLBXYI
    
    def GaussianOverlapDriftEstimate(self, xy, framenum, drift, sigma, iterations, stepsize, maxdrift, framesPerBin=1, cuda=False, progcb=None):
        xy = np.ascontiguousarray(xy,dtype=np.float32)
        framenum = np.ascontiguousarray(framenum,dtype=np.int32)
        drift = np.ascontiguousarray(drift,dtype=np.float32)
        
        nframes = np.max(framenum)+1
        
        assert len(drift)>=nframes and drift.shape[1]==2

        if len(drift)>nframes:
            drift = drift[:nframes]
            drift = np.ascontiguousarray(drift,dtype=np.float32)

        flags = 1 if cuda else 0
        
        scores = np.zeros(iterations,dtype=np.float32)
        
        if xy.shape[1] == 3:
            flags |= 2 # 3D
            
        sigma = np.array([sigma,sigma],dtype=np.float32)

        if progcb is None:
            progcb = lambda i,txt: 1

        nIterations = self._GaussianOverlapDriftEstimate(
            xy, framenum, len(xy), sigma, iterations, drift, framesPerBin,
            stepsize, maxdrift, scores, flags, self.ProgressCallback(progcb))

        return drift, scores[:nIterations]
    
    def ContinuousFRC(self, points, maxdistance, freq, cutoffDist, cutoffSigma, useCuda=True):
        points = np.ascontiguousarray(points,dtype=np.float32)
        
        npts = len(points)
        if not np.array_equal(points.shape, [npts,2]) and not np.array_equal(points.shape,[npts,3]):
            raise ValueError(f'Expected points to have shape [numpoints, dimensions] where dimensions is either 2 or 3. Given:{points.shape}')
            
        rho = np.ascontiguousarray(freq * 2*np.pi,dtype=np.float32)
        frc = np.zeros(len(rho),dtype=np.float32)
        self._ComputeContinuousFRC(points, points.shape[1], npts, rho, len(rho), frc, maxdistance, useCuda, cutoffDist, cutoffSigma)
        
        return frc
        

        