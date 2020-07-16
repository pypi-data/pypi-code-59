import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="PyEmotion",
  version="0.0.1",
  author="Karthick Nagarajan",
  author_email="karthick965938@gmail.com",
  description="A Python package to for facial emotion.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords='image data datascience emotion PyEmotion expression ML ml machinelearning AI ai',
  license='MIT',
  url="https://github.com/karthick965938/PyEmotion",
  packages=setuptools.find_packages(),
  install_requires=[
    'opencv-python',
    'Pillow',
    'art',
    'termcolor',
    'progress',
    'pytest',
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.8',
)