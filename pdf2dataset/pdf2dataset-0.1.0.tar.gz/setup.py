# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdf2dataset']

package_data = \
{'': ['*']}

install_requires = \
['fastparquet==0.4.0',
 'opencv-python==4.2.0.34',
 'packaging==20.4',
 'pdf2image==1.13.1',
 'pytesseract==0.3.4',
 'ray==0.8.6',
 'tqdm==4.47.0']

entry_points = \
{'console_scripts': ['pdf2dataset = pdf2dataset.__main__:main']}

setup_kwargs = {
    'name': 'pdf2dataset',
    'version': '0.1.0',
    'description': 'Easily convert a big folder with PDFs into a dataset, with extracted text using OCR',
    'long_description': '# pdf2dataset\n\n![pdf2dataset](https://github.com/icaropires/pdf2dataset/workflows/pdf2dataset/badge.svg)\n\nFor extracting text from PDFs and save to a dataset\n\n## Install\n\n### Install Dependencies\n\n#### Ubuntu (or debians)\n\n``` bash\n$ sudo apt update\n$ sudo apt install -y poppler-utils tesseract-ocr-por\n```\n\n### Install pdf2dataset\n\n#### For usage\n\n``` bash\n# first, clone repository\n\n$ pip3 install pdf2dataset --user # Please, isolate the environment\n```\n\n\n#### For development\n\n``` bash\n# first, clone repository\n\n$ poetry install\n```\n\n## Usage examples\n\n\n### Simple\n\n``` bash\n# Reads all PDFs from my_pdfs_folder and saves the resultant dataframe to my_df.parquet.gzip\n$ pdf2dataset my_pdfs_folder my_df.parquet.gzip\n```\n\n### Keeping progress\n\n``` bash\n# Keep progress in tmp folder, so can resume processing in case of any error or interruption\n# To resume, just use the same --tmp-dir folder\n$ pdf2dataset my_pdfs_folder my_df.parquet.gzip --tmp-dir tmp\n```\n\n### Help\n``` bash\n$ pdf2dataset -h\nusage: pdf2dataset [-h] [--tmp-dir TMP_DIR] [--lang LANG]\n                   [--num-cpus NUM_CPUS] [--address ADDRESS]\n                   [--webui-host WEBUI_HOST] [--redis-password REDIS_PASSWORD]\n                   input_dir results_file\n\nExtract text from all PDF files in a directory\n\npositional arguments:\n  input_dir             The folder to lookup for PDF files recursively\n  results_file          File to save the resultant dataframe\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --tmp-dir TMP_DIR     The folder to keep all the results, including log\n                        files and intermediate files\n  --lang LANG           Tesseract language\n  --num-cpus NUM_CPUS   Number of cpus to use\n  --address ADDRESS     Ray address to connect\n  --webui-host WEBUI_HOST\n                        Which port ray webui to listen\n  --redis-password REDIS_PASSWORD\n                        Redis password to use to connect with redis\n```\n\n### Sample output\n\n![output_sample](./images/output_sample.png)\n',
    'author': 'Ícaro Pires',
    'author_email': 'icaropsa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/icaropires/pdf2dataset',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
