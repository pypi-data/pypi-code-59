import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vphack",
    packages=['vphack'],
    package_dir={'vphack':'vphack/src'},
    version='0.0.1',
    license='License.txt',
    scripts=['bin/vphackez-a',
             'bin/vphackez'],
    author='Viper Hacker',
    author_email='viperhackerth@gmail.com',
    description='A Tools Viper Hacker @onehack',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/NRTnarathip/vphackez.git",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'License :: OSI Approved :: MIT License',
    ],
)
