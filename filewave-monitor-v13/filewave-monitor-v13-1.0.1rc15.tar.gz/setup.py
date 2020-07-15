import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filewave-monitor-v13",
    version="1.0.1rc15",
    author="John Clayton",
    author_email="johnc@filewave.com",
    description="An additional module that installs programs/config required to monitor v13 instances via Prometheus.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johncclayton/monitor-fw-13",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'monitor-v13-install=monitor.scripts:install_into_environment'
        ]
    },
    install_requires=[
        'click',
        'progressbar2'
    ],
    setup_requires=[
        'wheel'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
