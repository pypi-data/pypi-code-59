from distutils.core import setup

setup(
    name='hello_world_library',
    packages=['hello_world_library'],
    version='0.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='testing a library',  # Give a short description about your library
    author='Shreyas S',  # Type in your name
    author_email='shreyas@infrrd.ai',  # Type in your E-Mail
    url='https://github.com/Shreyas7524',  # Provide either the link to your github or to your website
    download_url='https://github.com/Shreyas7524/hello_world_library/archive/0.1.tar.gz',
    keywords=['testing', 'hello world'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'validators',
        'beautifulsoup4',
        'Flask'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
