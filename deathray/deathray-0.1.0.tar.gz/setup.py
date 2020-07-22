from setuptools import setup, find_packages


setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest>=3', ]
requirements = ['argh',]


COMMANDS = [
    'greet = deathray.cli:greet',
]


setup(
    author="Drew Schmidt and Todd Young",
    author_email='youngmt1@ornl.gov',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Anomaly Detection in an Astrophysics Simulation",
    entry_points={'console_scripts': COMMANDS},
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='deathray',
    name='deathray',
    packages=find_packages(include=['deathray', 'deathray.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/yngtodd/deathray',
    version='0.1.0',
    zip_safe=False,
)
