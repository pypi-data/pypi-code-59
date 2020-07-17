from setuptools.command.install import install
from setuptools import setup
from os import path
from io import open
import sys
import os

VERSION = "1.1.1"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'


def run(self):
    tag = os.getenv('CIRCLE_TAG')
    if tag != VERSION:
        info = "Git tag: {0} does not match \
            the version of this app: {1}".format(
            tag, VERSION)

        sys.exit(info)

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.


setup(
    name='EasyWayAPI',
    version='1.0.1',
    description="EasyWayAPI allows creating and viewing of various resources",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/joseph-njogu/EasywayAPI',  # Optional

    # This should be your name or the name of the organization which owns the
    # project.
    author='Joseph',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='josephnjogu487@gmail.com',  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    # classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        # 'Development Status :: 1 - Alpha',
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Internet",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3 :: Only",
        ],
        
    keywords='api',
    install_requires=[
                    'requests==2.18.4',
                    'confusable-homoglyphs==3.2.0',
                    'Django==2.2.2',
                    'django-bootstrap3==9.1.0',
                    'django-cors-headers==3.4.0',
                    'django-google-maps==0.12.1',
                    'django-registration==2.4.1',
                    'djangorestframework==3.11.0',
                    'Pillow==5.0.0',
                    'pytz==2020.1',
                    'sqlparse==0.3.1',
                    'whitenoise==3.3.1',
                    ],

    python_requires='>=3',
    cmdclass={
            'verify': VerifyVersionCommand,
        }
)
