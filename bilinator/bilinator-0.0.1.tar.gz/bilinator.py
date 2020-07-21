import os
import sys
import gdal
import numpy as np
from PIL import Image
from astropy.io import fits
import multiprocessing as mp
from functools import partial

def foo(file,source_path,output_path,save_tiff,save_hdr):
	name,ext = os.path.splitext(file)	

	if ext == '.fits':
		#paths 
		filepath  = os.path.join(source_path,file)
		tiff_path = os.path.join(output_path,"tiff")
		bil_path  = os.path.join(output_path,name+'.bil')
		hdr_path  = os.path.join(output_path,name+'.hdr')
		tiff_file_path = os.path.join(tiff_path,name+".tif")

		print(f'converting {name} to tiff')

		#open fits and get data
		img = fits.open(filepath)
		img.verify('silentfix')

		data         = img[1].data
		width,height = data.shape
		outputArray  = np.array(data)

		outputArray = np.flip(outputArray) 
		outputArray = np.flip(outputArray,1)

		outputArray +=(np.nanmin(outputArray)*-1) if np.nanmin(outputArray) < 0 else np.nanmin(outputArray)
		outputArray = np.array(outputArray,dtype = np.uint16)

		output = Image.fromarray(outputArray.reshape((height, width)))
		if save_tiff: 
			if not os.path.exists(tiff_path): 
				os.makedirs(tiff_path)
			output.save(tiff_file_path)

		output  = np.array(output)
		print(np.shape(output))
		max_val = np.max(output) 

		for i in range(1,15):
		    if max_val > 2**i and max_val < 2**(i+1):
		        num_bits = i+1
		        # print('num_bits',num_bits)

		offset = 32 - num_bits
		# print('offset',offset)

		# create bil
		np.savetxt(bil_path,output,fmt=f'%0{offset}d')


		if save_hdr:
			# create hdr
			with open(hdr_path,'w+') as f:
				nROWS = np.shape(output)[0]
				nCOLS = np.shape(output)[1]
				f.write(f'BANDS:      1\nROWS:     {nROWS}\nCOLS:     {nCOLS}\nINTERLEAVING:   BIL\nDATATYPE: U16')
			print(f'{hdr_path} created!')
	else:
		print(f'skipped {file}')
                

def bilinate(source_path,output_path,save_tiff=True,save_hdr = True):
	if not os.path.exists(output_path):
		os.makedirs(output_path)

	input_data = os.listdir(source_path)
	foo_partial = partial(foo,source_path=source_path,output_path=output_path,save_tiff=True,save_hdr = True)

	no_of_cpus = mp.cpu_count()
	print(f"You have {no_of_cpus} cpu/s in you device")
	p = mp.Pool(no_of_cpus)
	p.map(foo_partial, input_data)

if __name__ == '__main__':
	bilinate('test/','output/')