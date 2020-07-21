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
 'pdftotext==2.1.4',
 'pytesseract==0.3.4',
 'ray==0.8.6',
 'tqdm==4.47.0']

entry_points = \
{'console_scripts': ['pdf2dataset = pdf2dataset.__main__:main']}

setup_kwargs = {
    'name': 'pdf2dataset',
    'version': '0.2.0',
    'description': 'Easily convert a big folder with PDFs into a dataset, with extracted text using OCR',
    'long_description': '# pdf2dataset\n\n![pdf2dataset](https://github.com/icaropires/pdf2dataset/workflows/pdf2dataset/badge.svg)\n\nConverts a whole subdirectory with big a volume of PDF documents to a dataset (pandas DataFrame) with the columns: path x page x text x error\n\n\n## Highlights\n\n* Conversion of a whole subdirectory with PDFs documents into a pandas DataFrame\n* Support for parallel and distributed computing through [ray](https://github.com/ray-project/ray)\n* Incremental writing of resulting DataFrame, to save memory\n* Ability to save processing progress and resume from it\n* Error tracking of faulty documents\n* Ability to extracting text through [pdftotext](https://github.com/jalan/pdftotext)\n* Ability to use OCR for extracting text through [pytesseract](https://github.com/madmaze/pytesseract) and [pdf2image](https://github.com/Belval/pdf2image)\n* Custom behavior through parameters (number of CPUs, text language, etc)\n\n\n## Installation\n\n### Install Dependencies\n\n#### Fedora\n\n``` bash\n# "-por" for portuguese, use the documents language\n$ sudo dnf install -y poppler-utils pkgconfig poppler-cpp-devel python3-devel tesseract-langpack-por\n```\n\n#### Ubuntu (or debians)\n\n``` bash\n$ sudo apt update\n\n# "-por" for portuguese, use the documents language\n$ sudo apt install -y poppler-utils build-essential libpoppler-cpp-dev pkg-config python3-dev tesseract-ocr-por\n```\n\n### Install pdf2dataset\n\n#### For usage\n\n``` bash\n$ pip3 install pdf2dataset --user  # Please, isolate the environment\n```\n\n#### For development\n\n``` bash\n# First, clone repository and cd into it\n$ poetry install\n```\n\n\n## Usage\n\n### Simple - CLI\n\n``` bash\n# Reads all PDFs from my_pdfs_folder and saves the resultant dataframe to my_df.parquet.gzip\n$ pdf2dataset my_pdfs_folder my_df.parquet.gzip\n```\n\n### Save Processing Progress - CLI\n\nIt\'s possible to save the progress to a temporary folder and resume from the saved state in case of\nany error or interruption. To resume the processing, just use the `--tmp-dir [directory]` flag:\n\n``` bash\n$ pdf2dataset my_pdfs_folder my_df.parquet.gzip --tmp-dir my_progress\n```\n\nThe indicated temporary directory can also be used for debugging purposes and **is not** deleted\nautomatically, so delete it when desired. \n\n\n### Using as a library\n\nThe `extract_text` function can be used analogously to the CLI:\n\n``` python\nfrom pdf2dataset import extract_text\n\nextract_text(\'my_pdfs_folder\', \'my_df.parquet.gzip\', tmp_dir=\'my_progress\')\n```\n\n#### Small\n\nOne feature not available to the CLI is the custom behavior for handling small volumes of data (small can\nbe understood as that the extraction won\'t run for hours or days and locally).\n\nThe complete list of differences are:\n\n* Don\'t save processing progress\n* Distributed processing not supported\n* Don\'t write dataframe to disk\n* Returns the dataframe\n\n##### Example:\n``` python\nfrom pdf2dataset import extract_text\n\ndf = extract_text(\'my_pdfs_folder\', small=True)\n# ...\n```\n### Results File\n\nThe resulting "file" is a parquet hive written with [fastparquet](https://github.com/dask/fastparquet), it can be\neasily read with pandas or dask:\n\n``` python\n>>> import pandas as pd\n>>> df = pd.read_parquet(\'my_df.parquet.gzip\')\n>>> df\n                             path  page                  text                                              error\nindex                                                                                                           \n0                single_page1.pdf     1  My beautiful sample!                                                   \n1       sub1/copy_multi_page1.pdf     2           Second page                                                   \n2      sub2/copy_single_page1.pdf     1  My beautiful sample!                                                   \n3       sub1/copy_multi_page1.pdf     3            Third page                                                   \n4                 multi_page1.pdf     1            First page                                                   \n5                 multi_page1.pdf     3            Third page                                                   \n6       sub1/copy_multi_page1.pdf     1            First page                                                   \n7                 multi_page1.pdf     2           Second page                                                   \n0                    invalid1.pdf    -1                        Traceback (most recent call last):\\n  File "/h...\n```\n\nThere is no guarantee about the uniqueness or sequence of the `index`, you might need to create a new index with\nthe whole data in memory.\n\nThe `-1` page number means that was not possible of even opening the document.\n\n### Run on a Cluster\n\n#### Setup the Cluster\n\nFollow ray documentation for [manual](https://docs.ray.io/en/latest/using-ray-on-a-cluster.html?setup#manual-cluster-setup) or [automatic](https://docs.ray.io/en/latest/autoscaling.html?setup#automatic-cluster-setup)\nsetup.\n\n#### Run it\n\nTo go distributed you can run it just like local, but using the `--address` and `--redis-password` flags to point to your cluster ([More information](https://docs.ray.io/en/latest/multiprocessing.html)).\n\nWith version >= 0.2.0, only the head node needs to have access to the documents in disk.\n\n### Help\n\n```\n$ pdf2dataset -h\nusage: pdf2dataset [-h] [--tmp-dir TMP_DIR] [--lang LANG] [--ocr OCR]\n                   [--num-cpus NUM_CPUS] [--address ADDRESS]\n                   [--webui-host WEBUI_HOST] [--redis-password REDIS_PASSWORD]\n                   input_dir results_file\n\nExtract text from all PDF files in a directory\n\npositional arguments:\n  input_dir             The folder to lookup for PDF files recursively\n  results_file          File to save the resultant dataframe\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --tmp-dir TMP_DIR     The folder to keep all the results, including log\n                        files and intermediate files\n  --lang LANG           Tesseract language\n  --ocr OCR             \'pytesseract\' if true, else \'pdftotext\'. default:\n                        false\n  --num-cpus NUM_CPUS   Number of cpus to use\n  --address ADDRESS     Ray address to connect\n  --webui-host WEBUI_HOST\n                        Which port ray webui to listen\n  --redis-password REDIS_PASSWORD\n                        Redis password to use to connect with redis\n```\n\n\n## Troubleshooting\n\n1. **Troubles with high memory usage**\n\nYou can try to decrease the number of CPUs in use, reducing the level of parallelism,\ntest it with `--num-cpus 1` flag and then increase according to your hardware.\n\n## How to Contribute\n\nJust open your [issues](https://github.com/icaropires/pdf2dataset/issues) and/or [pull requests](https://github.com/icaropires/pdf2dataset/pulls), all are welcome :smiley:!\n',
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
