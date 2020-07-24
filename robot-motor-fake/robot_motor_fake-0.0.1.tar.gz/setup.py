from setuptools import setup, find_packages

setup(
    name='robot_motor_fake',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'imutils',
        'numpy',
        'opencv-python'
    ]
)
