"""wal_g810 - setup.py"""
import setuptools

try:
    import wal_g810
except (ImportError):
    print("error: wal_g810 requires Python 3.5 or greater.")
    quit(1)

VERSION = wal_g810.VERSION
DOWNLOAD = "https://github.com/MKJM2/wal_g810/archive/%s.tar.gz" % VERSION


setuptools.setup(
    name="wal_g810",
    version=VERSION,
    author="Michał Kurek",
    author_email="mailformmk@gmail.com",
    description=" Automate g810 profile creation from generated pywal colors",
    license="MIT",
    url="https://github.com/MKJM2/wal_g810",
    download_url=DOWNLOAD,
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires="pywal >= 0.6.7",
    scripts=['wal_g810.py'],
    entry_points={
        "console_scripts": ["wal-g810=wal_g810:main"]
    },
    python_requires=">=3.5",
    include_package_data=True
)
