import numpy as np
from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "hxlxalgos/external/nms",
        ["hxlxalgos/external/nms.pyx"],
        extra_compile_args=["-Wno-cpp", "-Wno-unused-function"]
    )
]
setup(
    name='hxlxalgotrt',
    packages=['hxlxalgos', "hxlxalgos.algos", "hxlxalgos.core", "hxlxalgos.utils", "hxlxalgos.external"],
    version='0.0.3',
    license='MIT',
    description='Algorithms apis by hxlx.',
    author='hxlx',
    author_email='wenlong.hu@ai-baby.com',
    keywords=['computer vision', 'deep learning', 'person detection', 'face recognition'],
    classifiers=[],
    package_data={"hxlxalgos.external": ["*.pyx"]},
    ext_modules=cythonize(extensions),
    include_dirs=[np.get_include()],
    install_requires=["cython",
                      "matplotlib>=3.0.3",
                      "numpy>=1.18.5",
                      "opencv-python>=4.3.0.36",
                      "pandas>=0.24.2",
                      "Pillow>=7.2.0",
                      "pycocotools>=2.0.1",
                      "pycuda>=2019.1.2",
                      "scikit-image>=0.15.0",
                      "scikit-learn>=0.22.2.post1",
                      "scipy==1.4.1",
                      "tqdm>=4.48.0"])
