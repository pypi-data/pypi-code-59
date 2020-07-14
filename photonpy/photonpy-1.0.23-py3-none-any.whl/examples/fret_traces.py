"""
Example of using the photonpy library to process 2D FRET image data. 
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_blinking(spots, numframes=2000, avg_on_time = 20, on_fraction=0.1):
    numspots = len(spots)

    p_off = 1-on_fraction
    k_off = 1/avg_on_time
    k_on =( k_off - p_off*k_off)/p_off 
    
    print(f"p_off={p_off}, k_on={k_on}, k_off={k_off}")
    
    blinkstate = np.random.binomial(1, on_fraction, size=numspots)

    xyI = np.zeros((numframes,numspots,3))
    oncounts = np.zeros(numframes, dtype=int)
    for f in range(numframes):
        turning_on = (1 - blinkstate) * np.random.binomial(1, k_on, size=numspots)
        remain_on = blinkstate * np.random.binomial(1, 1 - k_off, size=numspots)
        blinkstate = remain_on + turning_on

        c = np.sum(blinkstate)
        oncounts[f] = c

        xyI[f] = spots
        xyI[f,blinkstate == 0, 2] = 0
    return xyI

def generate_movie(xyI, imgsize, bg):
    numframes = len(xyI)
    frames = np.zeros((numframes, imgsize, imgsize), dtype=np.uint16)

    roisize = psf.sampleshape[0]
    roipos = np.clip((xyzI[:,[1,0]] - roisize/2).astype(int), 0, imgsize-roisize)
    theta = np.zeros((len(xyzI),5)) # assuming xyzIb
    theta[:,0:4] = xyzI
    theta[:,[1,0]] -= roipos
    on_spots = np.nonzero(on)[0]

    rois = psf.ExpectedValue(theta[on_spots])
    
    frames[f] = ctx.smlm.DrawROIs((imgsize,imgsize), rois, roipos[on_spots])
    frames[f] += bg

    