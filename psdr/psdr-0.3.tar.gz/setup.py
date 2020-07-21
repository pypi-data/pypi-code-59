import os
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize, build_ext

#from Cython.Compiler.Options import directive_defaults

#directive_defaults['linetrace'] = True
#directive_defaults['binding'] = True

install_requires = [
	'numpy>=1.15', 
	'scipy>=1.1.0',
	'redis',
	'cvxpy',
	'cvxopt',
	'tqdm',
	'dask',
	'distributed',
	'sobol_seq',
	'satyrn>=0.3.2',
	'matplotlib',
	'iterprinter',
	]


# https://stackoverflow.com/a/54154022
os.environ["CC"] = "gcc"
os.environ["CXX"] = "g++"
exts = [Extension(name='psdr.lipschitz_fast',
		sources=['psdr/lipschitz_fast.pyx'],
#		extra_compile_args=['-fopenmp'],
#		extra_link_args=['-lomp', '-fopenmp', '-lgomp', '-Wl,-rpath,/opt/local/lib/gcc9/'],
		library_dirs = ["/opt/local/lib/libomp", '/opt/local/lib/gcc9'],
		libraries = ['omp'],
#		define_macros=[('CYTHON_TRACE', '1')],
        )
		]

setup(name='psdr',
	version = '0.3',
	description = 'Parameter Space Dimension Reduction Toolbox',
	author = 'Jeffrey M. Hokanson',
	packages = ['psdr', 'psdr.demos', 'psdr.domains', 'psdr.sample', 'psdr.geometry'],
	ext_modules = cythonize(exts, language_level = 3),
	cmdclass={'build_ext': build_ext},
	#cythonize(['psdr/dpr1.pyx', 'psdr/lipschitz_fast.pyx']),
	install_requires = install_requires,
	zip_safe = False,
	)
