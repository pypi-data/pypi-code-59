from setuptools import setup

setup(
    name='build-server-client',
    version='0.1.1',
    description='Python client for a simple build server',
    url='https://github.com/GIT_USER/build-server-client',
    author='Matthew D. Scholefield',
    author_email='matthew331199@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='build server client',
    py_modules=['build_server_client'],
    install_requires=[
        'gitpython',
        'requests',
        'humanize',
        'tqdm',
        'bsdiff4'
    ],
    entry_points={
        'console_scripts': [
            'bsc=build_server_client:main'
        ],
    }
)
