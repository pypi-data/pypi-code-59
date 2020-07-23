'''
utils.py

Utility functions used by simpledots.py

by Lincoln Ombelets, 2019-2020
Distributed under the MIT license

'''
import numpy as np
import pandas as pd
import os
import os.path as osp
import skimage
import scipy


def fetch_image(data_dir, cycle, position, hyb_pattern='HybCycle_(\d+)$', im_pattern='^MMStack_Pos(\d+)(.*)'):
    '''
    fetch_image(data_dir, cycle, position, prefix, postfix, reshape):
    Fetches an image file from a specified hyb cycle and position, as produced by an automation experiment in MicroManager.
    Assumes images are located in files named 'HybCycle_#postfix' where # is the cycle and postfix is an optional string.
    Within these folders are one or more TIF stacks corresponding to each position, which are generally named as prefix_Pos#.ome.tif,
    where # is the position index. Raw MicroManager output uses 'MMStack' as the prefix, but after swapping channels and slices I change the name,
    so `prefix` allows specifying which specific set of images in the hyb cycle folder to fetch.
    
    If `reshape` is true, which it is by default, then the image will be returned in channel-first indexing shape.
    
    Returns:
    raw: Scikit image MultiImage (equivalent to a Numpy ndarray) containing the raw image data.
    '''
    
    image = None
    
    for f in os.scandir(data_dir):
        cycle_search = re.search(hyb_pattern, f.name)
        
        if not cycle_search:
            continue
            
        if int(cycle_search[1]) == cycle:
            
            if not osp.isdir(f.path):
                print('error: that isnt a directory!')

                return None
            
            break # break out of the folder/cycle loop
        
        else:
            
            continue # jump to the next folder if this one doesn't match
            
    for g in os.scandir(f.path):
        pos_search = re.search(im_pattern, g.name)
            
        if not pos_search:
            continue
                
        if int(pos_search[1]) == position:

            image = g.path

            break # we have found the image, exit position loop
        
    if not image:
        print('Could not find image for cycle {}, position {}'.format(cycle, position))
        return None
    
    raw = skimage.io.MultiImage(image)[0]
        
    return raw
        
def _shift_image(im, dx=0, dy=0):
    '''
    shift_image(im, dx, dy):
    Quick and dirty pixelwise translation of an image, throwing away pixels that spill over. 'New' pixels are set to the mode of the original image, usually a background-ish value...
    This could be done better, perhaps by Gaussian blurring the original and using the local blurred values, but this way is very fast, and we are only losing <5 pixels generally.
    Note that indexing is from the top left, so positive dx shifts down and positive dy shifts right.
    
    
    Returns:
    im_final: Image of the same shape as `im` but shifted dx rows and dy columns. 
    '''
    dims = im.shape
    
    expansion = 100
    margin = expansion//2
    
    bg = scipy.stats.mode(np.ravel(im))[0]
    
    im_expanded = np.full((dims[0]+expansion, dims[1]+expansion), bg)
    
    im_expanded[(margin+dy):(margin+dy+dims[0]), (margin+dx):(margin+dx+dims[1])] = im
    
    im_final = im_expanded[margin:-margin, margin:-margin]
    
    return im_final

def shift_image(im, dx=0, dy=0):
    '''
    shift_image(im, dx, dy):
    Calls _shift_image on a multi-channel image to shift each channel. If only a single channel (i.e. shape is 2 dimensional), just shifts that image.
    
    Returns:
    result: (multi-channel) image shifted dx and dy.
    '''
    result = np.empty_like(im)
    
    if len(result.shape) == 2:
        result = _shift_image(im, dx, dy)
    else:
        for i, c in enumerate(im):
            if len(result.shape) == 4:
                for j, z in enumerate(c):
                    result[i, j] = _shift_image(z, dx, dy)
            else:
                result[i] = _shift_image(c, dx, dy)

    return result

def pixelwise_dapi_align(im1, im2, dapi_channel=3, dapi_channel2=None):
    '''
    pixelwise_dapi_align(im1, im2, dapi_channel):
    Take two multichannel images and perform correlation-based pixelwise alignment on the DAPI image using `skimage.feature.register_translation`.
    Returns:
    shift: 2-tuple with the integer row and column offset that best moves im2 to im1. 
    error: float that specifies translation-invariant error between the two images. Can be thought of as an estimate as alignment precision.
    '''
    if not dapi_channel2:
        dapi_channel2 = dapi_channel
        
    shift, error, _ = skimage.feature.register_translation(im1[dapi_channel], im2[dapi_channel2])
    
    return shift.astype(int), error


def subtract_background_fft(input_im, radius=50):
    image_fft = np.fft.rfft2(input_im)
    bg_fft = scipy.ndimage.fourier.fourier_gaussian(image_fft, radius, n=input_im.shape[0])
    return np.maximum(0, np.fft.irfft2(image_fft - bg_fft)), np.maximum(0, np.fft.irfft2(bg_fft))

    
def local_max_image_2(image,
                    bg_std,
                    thresh_coeff=3,
                    thresh_abs=0,
                    min_distance=1, 
                    exclude_border=2,
                    intensity_image=None,
                    mask=None,
                    verbose=False):
    '''
    local_max_image_2: Performs the same thing as local_max_image, but uses scikit-image 0.16.0's `label` and `regionprops_table` to more elegantly create a DataFrame
    while keeping the intensity image associated. Does NOT perform max filtering; returns
    single-pixel maxima image, from which 'expanded' images can be generated.
    
    Returns:
    local_maxes: binary image of same shape as `image` where 1/True indicates local maximum and 0/False everything else
    props_df: DataFrame containing numerical label, area, coordinates and intensity for each dot. Note coordinates are arrays in a single column and intensity is a 2D array with a single value for the one-pixel local maxima.
    '''
    # we use the absolute threshold if it is specified.
    if thresh_abs > 0:
        thresh = thresh_abs
    else:
        thresh = thresh_coeff * bg_std
        
    if verbose:
        print('local_max_image: finding local maxes above threshold of {}'.format(int(thresh)))
    
    local_maxes = skimage.feature.peak_local_max(image, 
                                                 min_distance=min_distance, 
                                                 threshold_abs=thresh, 
                                                 exclude_border=exclude_border,
                                                 footprint=mask,
                                                 indices=False)
    
    labeled  = skimage.measure.label(local_maxes)
    
    if type(intensity_image) == type(None):
        intensity_image = image
    
    try:
        props_df = pd.DataFrame(skimage.measure.regionprops_table(labeled, intensity_image, 
                                                 properties=('label', 'area', 'coords', 'max_intensity')))
    except:
        props_df = pd.DataFrame(columns=['label', 'area', 'coords', 'max_intensity']) # empty DF if no regions are found
    
    if verbose:
        print('local_max_image: found {} local max pixels'.format(len(props_df)))
    
    return local_maxes.astype(bool), props_df