from distutils.core import setup

# Get the long description from the info_file
with open('DESCRIPTION.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vmx_editor',
    packages=['vmx_editor'],
    version='0.3.1',
    license='MIT',
    description='Read and edit .vmx configurations file programmatically',
    long_description=long_description,
    author='lennisthemenace',
    author_email='',
    url='https://github.com/lennisthemenace/vmx_editor',
    download_url='https://github.com/lennisthemenace/vmx_editor/archive/0.3.1.tar.gz',
    keywords=['VMX', 'EDITOR', 'VMWARE'],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
