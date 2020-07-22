import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spotify-flask-downloader",
    version="0.0.2",
    author="Hitesh Kumar Saini",
    author_email="saini123hitesh@gmail.com",
    description="A Flask based backend to search & download music from Spotify",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexmercerind/react-python-spotify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'youtube-search-python',
          'flask',
          'youtube-dl',
          'flask-cors'
    ],
    python_requires='>=3.6',
)