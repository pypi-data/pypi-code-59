import matplotlib.pyplot as plt
import numpy as np
from photonpy.cpp.lib import SMLM
from photonpy.cpp.context import Context
from photonpy.cpp.gaussian import Gaussian

import tqdm
from scipy.interpolate import InterpolatedUnivariateSpline
from photonpy.cpp.postprocess import PostProcessMethods


# https://aip.scitation.org/doi/full/10.1063/1.5005899
def phasor_localize(roi):
    fx = np.sum(np.sum(roi,0)*np.exp(-2j*np.pi*np.arange(roi.shape[1])/roi.shape[1]))
    fy = np.sum(np.sum(roi,1)*np.exp(-2j*np.pi*np.arange(roi.shape[0])/roi.shape[0]))
            
    #Get the size of the matrix
    WindowPixelSize = roi.shape[1]
    #Calculate the angle of the X-phasor from the first Fourier coefficient in X
    angX = np.angle(fx)
    if angX>0: angX=angX-2*np.pi
    #Normalize the angle by 2pi and the amount of pixels of the ROI
    PositionX = np.abs(angX)/(2*np.pi/WindowPixelSize)
    #Calculate the angle of the Y-phasor from the first Fourier coefficient in Y
    angY = np.angle(fy)
    #Correct the angle
    if angY>0: angY=angY-2*np.pi
    #Normalize the angle by 2pi and the amount of pixels of the ROI
    PositionY = np.abs(angY)/(2*np.pi/WindowPixelSize)
    
    return PositionX,PositionY


def crosscorrelation(A, B):
    A_fft = np.fft.fft2(A)
    B_fft = np.fft.fft2(B)
    return np.fft.ifft2(A_fft * np.conj(B_fft))

def crosscorrelation_cuda(A, B, smlm: SMLM):
    return smlm.IFFT2(np.conj(smlm.FFT2(A)) * smlm.FFT2(B))



def findshift(cc, smlm:SMLM, plot=False):
    # look for the peak in a small subsection
    r = 6
    hw = 20
    cc_middle = cc[cc.shape[0] // 2 - hw : cc.shape[0] // 2 + hw, cc.shape[1] // 2 - hw : cc.shape[1] // 2 + hw]
    peak = np.array(np.unravel_index(np.argmax(cc_middle), cc_middle.shape))
    peak += [cc.shape[0] // 2 - hw, cc.shape[1] // 2 - hw]
    
    peak = np.clip(peak, r, np.array(cc.shape) - r)
    roi = cc[peak[0] - r + 1 : peak[0] + r, peak[1] - r + 1 : peak[1] + r]
    if plot:
        plt.figure()
        plt.imshow(cc_middle)
        plt.figure()
        plt.imshow(roi)

    px,py = phasor_localize(roi)
#    roi_top = fit_sigma_2d(roi, initial_sigma=2)[[0, 1]]
    #            roi_top = lsqfit.lsqfitmax(roi)
    return peak[1] + px - r + 1 - cc.shape[1] / 2, peak[0] + py - r + 1 - cc.shape[0] / 2


def findshift_pairs(images, pairs, smlm:SMLM, useCuda=True):
    fft2 = smlm.FFT2 if useCuda else np.fft.fft2
    ifft2 = smlm.IFFT2 if useCuda else np.fft.ifft2
    
    print("FFT'ing")
    w = images.shape[-1]
    fft_images = fft2(images)
    fft_conv = np.zeros((len(pairs), w, w),dtype=np.complex64)
    for i, (a,b) in enumerate(pairs):
        fft_conv[i] = np.conj(fft_images[a]) * fft_images[b]
        
    print("IFFT'ing")
    cc =  ifft2(fft_conv)
    cc = np.abs(np.fft.fftshift(cc, (-2, -1)))

    print("Finding cc peaks..")
    shift = np.zeros((len(pairs),2))
    for i in tqdm.trange(len(pairs)):
        shift[i] = findshift(cc[i], smlm)
    
    return shift

def rcc(xyI, framenum, timebins, rendersize, maxdrift=3, wrapfov=1, zoom=1, sigma=1, maxpairs=1000,RCC=True,smlm:SMLM=None):
#    area = np.ceil(np.max(xyI[:,[0,1]],0)).astype(int)
 #   area = np.array([area[0],area[0]])
    
    area = np.array([rendersize,rendersize])
    
    nframes = np.max(framenum)+1
    framesperbin = nframes//timebins
        
    with Context(smlm) as ctx:
        g = Gaussian(ctx)
        
        imgshape = area*zoom//wrapfov
        images = np.zeros((timebins, *imgshape))
            
        for k in range(timebins):
            img = np.zeros(imgshape,dtype=np.float32)
            
            indices = np.nonzero(framenum//framesperbin==k)[0]

            spots = np.zeros((len(indices), 5), dtype=np.float32)
            spots[:, 0] = (xyI[indices,0] * zoom) % imgshape[1]
            spots[:, 1] = (xyI[indices,1] * zoom) % imgshape[0]
            spots[:, 2] = sigma
            spots[:, 3] = sigma
            spots[:, 4] = xyI[indices,2]

            images[k] = g.Draw(img, spots)
            
        print(f"RCC pairs: {timebins*(timebins-1)//2}. Bins={timebins}")
            
        if RCC:
            pairs = np.array(np.triu_indices(timebins,1)).T
            if len(pairs)>maxpairs:
                pairs = pairs[np.random.choice(len(pairs),maxpairs)]
            pair_shifts = findshift_pairs(images, pairs, smlm, useCuda=False)
            
            A = np.zeros((len(pairs),timebins))
            A[np.arange(len(pairs)),pairs[:,0]] = 1
            A[np.arange(len(pairs)),pairs[:,1]] = -1
            
            inv = np.linalg.pinv(A)
            shift_x = inv @ pair_shifts[:,0]
            shift_y = inv @ pair_shifts[:,1]
            shift_y -= shift_y[0]
            shift_x -= shift_x[0]
            shift = -np.vstack((shift_x,shift_y)).T / zoom
        else:
            pairs = np.vstack((np.arange(timebins-1)*0,np.arange(timebins-1)+1)).T
            shift = np.zeros((timebins,2))
            shift[1:] = findshift_pairs(images, pairs, smlm)
            shift /= zoom
            #shift = np.cumsum(shift,0)
            
        t = (0.5+np.arange(timebins))*framesperbin
        spl_x = InterpolatedUnivariateSpline(t, shift[:,0], k=2)
        spl_y = InterpolatedUnivariateSpline(t, shift[:,1], k=2)
        
        shift_interp = np.zeros((nframes,2))
        shift_interp[:,0] = spl_x(np.arange(nframes))
        shift_interp[:,1] = spl_y(np.arange(nframes))
        
        shift_estim = np.zeros((len(shift),3))
        shift_estim[:,[0,1]] = shift
        shift_estim[:,2] = t
        
            
    return shift_interp,shift_estim, images
        

def interp_shift_xy(shift,framesperbin,nframes):

    t = (np.arange(len(shift))+0.5)*framesperbin,
    spl_x = InterpolatedUnivariateSpline(t, shift[:,0], k=2)
    spl_y = InterpolatedUnivariateSpline(t, shift[:,1], k=2)
    
    shift_interp = np.zeros((nframes,2))
    shift_interp[:,0] = spl_x(np.arange(nframes))
    shift_interp[:,1] = spl_y(np.arange(nframes))
    
    return shift_interp

def maxlc(xyz, framenum, crlb, framesperbin, pixelsize, imgshape, sigmaMultiplier=1, dataname=None, outputfn=None,debugMode=False):
    """
    Maximize localization correlation
    """
    numframes = np.max(framenum)+1
    
    xyI=xyz*1
    xyI[:,2]=1    

    useCuda=True
    
    with Context(debugMode=debugMode) as ctx:
        xy = xyz[:,:2]
        sigma = np.mean(crlb[:,:2]) * sigmaMultiplier
        
        numIterations = 10000
        step = 0.000001

        set1 = xy[:,0]>xy[:,1]
        #set1 = np.arange(len(xy)) % 2 == 0
        set2 = np.logical_not(set1)
        
        ppm = PostProcessMethods(ctx)
        
        # Coarse drift
        
        print("Computing initial coarse drift estimate...",flush=True)
        with tqdm.tqdm() as pbar:
            def update_pbar(i,info): 
                pbar.set_description(info.decode("utf-8")); pbar.update(1)
                return 1
            
            coarse_drift,score = ppm.GaussianOverlapDriftEstimate(
                xy, framenum, np.zeros((numframes,2)), sigma*5, numIterations, step, 5, framesPerBin=framesperbin*5, cuda=useCuda,progcb=update_pbar)

        print("\nComputing precise drift estimate...",flush=True)
        with tqdm.tqdm() as pbar:
            def update_pbar(i,info): 
                pbar.set_description(info.decode("utf-8"));pbar.update(1)
                return 1
            ndrift,score = ppm.GaussianOverlapDriftEstimate(
                xy, framenum, coarse_drift*1, sigma, numIterations, step, 5, framesPerBin=framesperbin, cuda=useCuda, progcb=update_pbar)
                
        print("\nComputing drift estimation precision...",flush=True)
        with tqdm.tqdm() as pbar:
            def update_pbar(i,info): 
                pbar.set_description(info.decode("utf-8"));pbar.update(1)
                return 1
            ndrift_set1,score_set1 = ppm.GaussianOverlapDriftEstimate(
                xy[set1], framenum[set1], coarse_drift*1, sigma, numIterations, step, 5, framesPerBin=framesperbin,cuda=useCuda, progcb=update_pbar)

            ndrift_set2,score_set2 = ppm.GaussianOverlapDriftEstimate(
                xy[set2], framenum[set2], coarse_drift*1, sigma, numIterations, step, 5, framesPerBin=framesperbin,cuda=useCuda,progcb=update_pbar)

        n = f" for {dataname}" if dataname is not None else ""
        plt.figure()
        plt.plot(score,label='Score (full set)')
        plt.plot(score_set1,label='Score (subset 1)')
        plt.plot(score_set2,label='Score (subset 2)')
        plt.title(f'Optimization score progress{n}')
        plt.xlabel('Iteration')
        plt.legend()

        ndrift_set1 -= ndrift_set1[0]
        ndrift_set2 -= ndrift_set2[0]
        ndrift -= ndrift[0]
        drift = ndrift

        # both of these use half the data (so assuming precision scales with sqrt(N)), 2x variance
        # subtracting two 2x variance signals gives a 4x variance estimation of precision
        L = min(len(ndrift_set1),len(ndrift_set2))
        diff = ndrift_set1[:L] - ndrift_set2[:L]
        est_precision = np.std(diff,0)/2
        print(f"Estimated precision: {est_precision}")

        #hf = drift-drift_smoothed
        #vibration_std = np.sqrt(np.var(hf,0) - est_precision**2)
        #print(f'Vibration estimate: X={vibration_std[0]*pixelsize:.1f} nm, Y={vibration_std[1]*pixelsize:.1f} nm')
        
        fig,ax=plt.subplots(2,1,sharex=True)
        ax[0].plot(ndrift_set1[:,0], label='Drift X (MGO) - set1')
        ax[0].plot(ndrift_set2[:,0], label='Drift X (MGO) - set2')
        ax[1].plot(ndrift_set1[:,1], label='Drift Y (MGO) - set1')
        ax[1].plot(ndrift_set2[:,1], label='Drift Y (MGO) - set2')
        ax[0].plot(coarse_drift[:,0], label='Drift X (Initial coarse)')
        ax[1].plot(coarse_drift[:,1], label='Drift Y (Initial coarse)')
        ax[0].legend()
        ax[1].legend()
        
        plt.suptitle(f'Drift trace{n}. Est. Precision: X/Y={est_precision[0]*pixelsize:.1f}/{est_precision[1]*pixelsize:.1f} nm ({est_precision[1]:.3f}/{est_precision[1]:.3f} pixels), ')
        if outputfn is not None:
            plt.savefig(outputfn)
            
        r = np.zeros((len(drift),8))
        r[:,:2] = drift
        r[:,2:4] = ndrift_set1
        r[:,4:6] = ndrift_set2
        r[:,6:8] = coarse_drift
        
        return r

