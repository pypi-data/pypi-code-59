from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='safexl',
    version='0.0.7',
    description='The Safe Way to Excel',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/ThePoetCoder/safexl',
    author='Eric Smith',
    author_email='ThePoetCoder@gmail.com',
    license='MIT',
    zip_safe=False,
    keywords='safexl Excel pywin32 win32 spreadsheet',
    test_suite='tests',
    python_requires='>=3.6',
    py_modules=[
        "safexl\\__init__",
        "safexl\\toolkit",
        "safexl\\colors",
        "safexl\\xl_constants",
        "safexl\\tests\\__init__",
        "safexl\\tests\\test_app",
        "safexl\\tests\\test_app_tools",
        "safexl\\tests\\test_psutil_wrappers"
    ],
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        "pywin32 >= 223",
        "psutil >= 5.6.2",
    ],
    include_package_data=True,
    # package_dir={'': 'safexl'},
)
