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
    'version': '0.1.1',
    'description': 'Easily convert a big folder with PDFs into a dataset, with extracted text using OCR',
    'long_description': '# pdf2dataset\n\n![pdf2dataset](https://github.com/icaropires/pdf2dataset/workflows/pdf2dataset/badge.svg)\n\nConverts a whole subdirectory with big volume of PDF documents to a dataset (pandas DataFrame) with the columns: path x page x text x error\n\n\n## Highlights\n\n* Conversion of a whole subdirectory with PDFs documents into a pandas DataFrame\n* Support for parallel and distributed computing through [ray](https://github.com/ray-project/ray)\n* Incremental writing of resulting DataFrame, to save memory\n* Ability to save processing progress and resume from it\n* Error tracking of faulty documents\n* Use OCR for extracting text through [pytesseract](https://github.com/madmaze/pytesseract) and [pdf2image](https://github.com/Belval/pdf2image)\n* Custom behaviour through parameters (number of CPUs, text language, etc)\n\n\n## Install\n\n### Install Dependencies\n\n#### Ubuntu (or debians)\n\n``` bash\n$ sudo apt update\n$ sudo apt install -y poppler-utils tesseract-ocr-por  # "-por" for portuguese, use your language\n```\n\n### Install pdf2dataset\n\n#### For usage\n\n``` bash\n$ pip3 install pdf2dataset --user # Please, isolate the environment\n```\n\n\n#### For development\n\n``` bash\n# First, clone repository and cd into it\n$ poetry install\n```\n\n\n## Usage\n\n### Simple\n\n``` bash\n# Reads all PDFs from my_pdfs_folder and saves the resultant dataframe to my_df.parquet.gzip\n$ pdf2dataset my_pdfs_folder my_df.parquet.gzip\n```\n\n### Save Processing Progress\n\nIt\'s possible to save the progress to a temporary folder and resume from the saved state in case of\nany error or interruption. To resume the processing, just use the `--tmp-dir [directory]` flag:\n\n``` bash\n$ pdf2dataset my_pdfs_folder my_df.parquet.gzip --tmp-dir my_progress\n```\n\nThe indicated temporary directory can also be used for debugging pourposes and **is not** deleted\nautomatically, so delete it when desired. \n\n### Results File\n\nThe resulting "file" is a parquet hive written with [fastparquet](https://github.com/dask/fastparquet), it can be\neasily read with pandas or dask:\n\n``` python\n>>> import pandas as pd\n>>> df = pd.read_parquet(\'my_df.parquet.gzip\')\n>>> df\n                             path  page                  text                                              error\nindex                                                                                                           \n0                single_page1.pdf     1  My beautiful sample!                                                   \n1       sub1/copy_multi_page1.pdf     2           Second page                                                   \n2      sub2/copy_single_page1.pdf     1  My beautiful sample!                                                   \n3       sub1/copy_multi_page1.pdf     3            Third page                                                   \n4                 multi_page1.pdf     1            First page                                                   \n5                 multi_page1.pdf     3            Third page                                                   \n6       sub1/copy_multi_page1.pdf     1            First page                                                   \n7                 multi_page1.pdf     2           Second page                                                   \n0                    invalid1.pdf    -1                        Traceback (most recent call last):\\n  File "/h...\n```\n\nThere is no guarantee about the uniqueness or sequence of the `index`, you might need to create a new index with\nthe whole data in memory.\n\nThe `-1` page number means that was not possible of even openning the document.\n\n### Help\n\n``` bash\n$ pdf2dataset -h\nusage: pdf2dataset [-h] [--tmp-dir TMP_DIR] [--lang LANG]\n                   [--num-cpus NUM_CPUS] [--address ADDRESS]\n                   [--webui-host WEBUI_HOST] [--redis-password REDIS_PASSWORD]\n                   input_dir results_file\n\nExtract text from all PDF files in a directory\n\npositional arguments:\n  input_dir             The folder to lookup for PDF files recursively\n  results_file          File to save the resultant dataframe\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --tmp-dir TMP_DIR     The folder to keep all the results, including log\n                        files and intermediate files\n  --lang LANG           Tesseract language\n  --num-cpus NUM_CPUS   Number of cpus to use\n  --address ADDRESS     Ray address to connect\n  --webui-host WEBUI_HOST\n                        Which port ray webui to listen\n  --redis-password REDIS_PASSWORD\n                        Redis password to use to connect with redis\n```\n\n\n## Troubleshooting\n\n1. **Troubles with high memory usage**\n\nYou can try to decrease the number of CPUs in use, reducing the level of\nparallelism, test with `--num-cpus 1` flag and then increasy according to your hardware.\n',
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
