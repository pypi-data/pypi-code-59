from setuptools import setup, find_packages

setup(
    name='robot_webcam',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'imutils'
    ],
    entry_points={
        'console_scripts': [
            'robot_webcam=robot_webcam.main:run'
        ]
    }
)