# encoding: utf-8
from distutils.core import setup
setup(
    name='covid_mx_data',
    packages=['covid_mx_data'],
    version='0.1',
    license='MIT',
    description='Descarga archivos de datos de Covid 19 de la Dirección General de Epidemiología (DGE) de la Secretaría de Salud del Gobierno de México.',
    author='Iván Fouilloux',
    author_email='contacto@ivanfouilloux.com',
    url='https://github.com/ivan-fouilloux/CovidMxData',
    # I explain this later on
    download_url='https://github.com/ivan-fouilloux/CovidMxData/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['COVID', 'MEXICO', 'DGE', 'SSA',
              'GOB', 'MX', 'COVID19', 'COVIDMX'],
    install_requires=[            # I get to this in a second
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
