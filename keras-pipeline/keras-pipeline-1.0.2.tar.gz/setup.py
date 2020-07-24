import setuptools

with open('README.md', 'r') as f:
  long_description = f.read()

setuptools.setup(
  name='keras-pipeline',
  version='1.0.2',
  author='Amaury Moulin',
  author_email='egipcy@gmail.com',
  description='Keras/Tensorflow Pipeline',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/egipcy/Pipeline',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6.10',
)
