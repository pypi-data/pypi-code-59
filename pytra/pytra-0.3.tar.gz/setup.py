import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()


setup(
    name='pytra',
    version='0.3',
    description='Simple command-line tool for translating',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/GeorgeStambulyants/pytra',
    author='George Stambulyants',
    author_email='george.stamb16@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['src', 'src.utils'],
    include_package_data=True,
    install_requires=[
        'click',
        'googletrans',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'pytra=src.pytra:pytra',
        ]
    },
)
