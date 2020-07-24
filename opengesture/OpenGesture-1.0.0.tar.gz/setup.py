import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OpenGesture", # Replace with your own username
    version="1.0.0",
    author="Gatlen Culp, Eshan Ramesh",
    description="Customizable numerical hand recognition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/esrh/cvgesture-functions",
    packages=setuptools.find_packages(),
    install_requires = ['numpy','opencv-python','imutils','sklearn','pyyaml','keyboard','mouse'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={'console_scripts':['opengesture=opengesture.numberrecog:main']},
    python_requires='>=3.6',
)
