from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='johnpackagetest',
      version='0.3.1',
      description='hello world test package',
      long_description=long_description,
      long_description_content_type="text/markdown",
      keywords='test package learning education',
      url='http://github.com/jritsema/johnpackagetest',
      author='John Ritsema',
      author_email='john_ritsema@yahoo.com',
      license='MIT',
      packages=['johnpackagetest'],
      include_package_data=True,
      zip_safe=False)
