# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['azulejo']

package_data = \
{'': ['*'], 'azulejo': ['bin/*']}

install_requires = \
['attrs>=19.3.0,<20.0.0',
 'biopython>=1.76,<2.0',
 'click>=7.1.2,<8.0.0',
 'click_loguru>=0.3.3,<0.4.0',
 'click_plugins>=1.1.1,<2.0.0',
 'dask[bag]>=2.15.0,<3.0.0',
 'gffpandas>=1.2.0,<2.0.0',
 'matplotlib>=3.2.1,<4.0.0',
 'networkx>=2.4,<3.0',
 'numpy>=1.18.3,<2.0.0',
 'pandas>=1.0.3,<2.0.0',
 'paramiko>=2.7.1,<3.0.0',
 'pathvalidate>=2.3.0,<3.0.0',
 'poetry-dynamic-versioning>=0.8.1,<0.9.0',
 'seaborn>=0.10.1,<0.11.0',
 'sh>=1.13.1,<2.0.0',
 'smart-open>=2.0.0,<3.0.0',
 'toml>=0.10.1,<0.11.0',
 'uri>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['azulejo = azulejo:cli']}

setup_kwargs = {
    'name': 'azulejo',
    'version': '0.8.1',
    'description': 'tile phylogenetic space with subtrees',
    'long_description': '.. epigraph:: azulejo\n              noun INFORMAL\n              a glazed tile, usually blue, found on the inside of churches and palaces in Spain and Portugal.\n\nazulejo\n=======\n``azulejo`` azulejo tiles phylogenetic space with subtrees\nnormalizes and validates genomic data files prior to further processing\nor inclusion in a data store such as that of the\n`Legume Federation <https://www.legumefederation.org/en/data-store/>`_.\n\nPrerequisites\n-------------\nPython 3.6 or greater is required. This package is tested under Linux using Python 3.8.  ``azulejo``\nrelies on `usearch <https://www.drive5.com/usearch/download.html>`_ for clustering, which you must\ndownload and install manually due to licensing restrictions (free download, no registration required at\nthe link).  ``azulejo`` also uses `MUSCLE <https://www.drive5.com/muscle/downloads.htm>`_ and requires\nversion 3.8.1551 or greater.  ``MUSCLE`` is in the public domain and can be downloaded and\nbuilt from source `here <https://www.drive5.com/muscle/muscle_src_3.8.1551.tar.gz>`_.\n\nInstallation for Users\n----------------------\nInstall via pip or (better yet) `pipx <https://pipxproject.github.io/pipx/>`_: ::\n\n     pipx install azulejo\n\n``azulejo`` contains some long commands and many options.  To enable command-line\ncompletion for ``azulejo`` commands, execute the following command if you are using\n``bash`` as your shell: ::\n\n    eval "$(_AZULEJO_COMPLETE=source_bash azulejo)"\n\nFor Developers\n--------------\nIf you plan to develop ``azulejo``, you\'ll need to install\nthe `poetry <https://python-poetry.org>`_ dependency manager.\nIf you haven\'t previously installed ``poetry``, execute the command: ::\n\n    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n\nNext, get the master branch from GitHub ::\n\n\tgit clone https://github.com/legumeinfo/azulejo.git\n\nChange to the ``azulejo/`` directory and install with poetry: ::\n\n\tpoetry install -v\n\nRun ``azulejo`` with ``poetry``: ::\n\n    poetry run azulejo\n\nUsage\n-----\nInstallation puts a single script called ``azulejo`` in your path.  The usage format is::\n\n    azulejo [GLOBALOPTIONS] COMMAND [COMMANDOPTIONS][ARGS]\n\nMaster Input File\n-----------------\n``azulejo`` uses a configuration file in `TOML  <https://github.com/toml-lang/toml>`_\nformat as the master input that associates files with phylogeny.  The format of this file\nis the familiar headings in square brackets followed by configuration values::\n\n    [glycines]\n    rank = "genus"\n    name = "Glycine"\n\n    [glycines.glyso]\n    rank = "species"\n    name = "Glycine soja"\n\n    [glycines.glyso.PI483463]\n    rank = "strain"\n    gff = "glyso.PI483463.gnm1.ann1.3Q3Q.gene_models_main.gff3.gz"\n    fasta = "glyso.PI483463.gnm1.ann1.3Q3Q.protein_primaryTranscript.faa.gz"\n    uri = "https://v1.legumefederation.org/data/index/public/Glycine_soja/PI483463.gnm1.ann1.3Q3Q/"\n    comments = """\n    Glycine soja accession PI 483463 has been identified as being unusually\n    salt-tolerant (Lee et al., 2009)."""\n\n\n* [headings]\n    There can be only one top-level heading, and that will be the name of the\n    resulting output set.  This name will be the name of an output directory that will be\n    created in the current working directory, so this heading (and all subheadings) must\n    obey UNIX filesystem naming rules or an error will result.  Each heading level\n    (indicated by a ".") will result in another taxonomic level and another directory level\n    in the output directory.  Depths do not need to be consistent.\n\n* rank\n    Each level defined must have a ``rank`` defined, and that rank must match one of the\n    taxonomic ranks defined by ``azulejo``, which you can view and test using the\n    ``check-taxonomic-rank`` command.   There are 24 major taxonomic ranks, each of which\n    may be modified by 16 different prefixes for a total of 174 taxonomic levels (some of\n    which are synonoymous).\n\n* name\n    Each level may (and usually should) have a ``name`` defined.  This name is intended\n    to be human-readable with no restrictions on the characters used, but it goes into\n    plot legends in places, so it\'s best to not make it too long. If the name is not specified,\n    it will be taken from the level name enclosed in single quotes (e.g., \'PI483463\' for the\n    example above).\n\n* fasta\n    If the level specifies a genome, it must have a ``fasta`` entry corresponding\n    to the name of the *protein* FASTA file.  In eukaryotes, the FASTA file should be a\n    file of primary (generally longest) protein transcripts, if available, rather than all protein\n    transcripts (i.e., not including splice variants). Sequences will be cleaned of dashes, stops,\n    and other out-of-alphabet characters.  Ambiguous residues at the beginnings and ends of\n    sequences will be trimmed. Zero-length sequences will be discarded, which can result in a\n    smaller number of sequences out.  These files may be compressed, with extensions ``.gz`` or\n    ``.bz2``.\n\n* gff\n    If the level specifies a genome, it must have a ``gff`` entry corresponding\n    to a version 3 Genome Feature File (GFF3) containing ``CDS`` entries with ID values\n    matching those IDs in the FASTA file.  The same compression extensions as for\n    ``fasta`` entries apply.  If the ``SOURCE`` fields in those CDS entries\n    (which contain the names of the DNA fragments such as scaffolds that the CDS came from)\n    contain dot-separated components, those components that are identical across the entire\n    file will be discarded by default.  There is an opportunity later in the process to\n    remap DNA source names to a common dictionary for comparison among chromosomes and\n    plastids.\n\n* uri\n    This optional field may contain a a uniform resource identifier such as\n    ``https://sitename/dir/``.  ``azulejo`` uses `smart-open <https://www.pypi.org/project/smart-open/>`_\n    for doing transparent on-the-fly decompression from a variety of file systems\n    including HTTPS, HDFS, SSH, and SFTP (but not FTP).\n    If this field is not supplied, local file access is assumed with paths relative to\n    the current working directory. The URI will be prepended to ``fasta``\n    and ``gff`` paths, allowing for convenient downloading on-the-fly from sites such as\n    LegumeInfo or GenBank.   Downloads are not cached, so if you intend to run ``azulejo``\n    multiple times on the same input data, you will save time by downloading and uncompressing\n    files to local storage.\n\n* preference\n    This optional field may be used to override the genome preference heuristic\n    that is the fall-thru preference after proxy-gene heuristics have been applied.  This is an integer\n    value, with lower integers getting the highest priority.  Set this value to zero if you\n    know in advance that one of the input genomes is considered the reference genome and,\n    all things being equal, you would prefer to select proxy genes from this genome.  You\n    may also set these preference values later, after the default genome preference (genomes\n    will be preferred in order of the most genes in a single DNA fragment) has already been\n    applied, but before proxy gene selection.\n\n* other info\n    A design goal for ``azulejo`` was to not lose metadata, even if it\n    was not used by ``azulejo`` itself, while keeping metadata out of file names.\n    As an aid in that goal, for each (sub)heading level/output directory, ``azulejo``\n    creates a JSON file named ``node_properties.json`` at each node in the output\n    hierarchy that containing all information from this file as well as other information\n    calculated at ingestion time by ``azulejo``.  You may specify any additional data you would\n    like to pass along (e.g., for later use in a web page) and it will be translated from TOML\n    to JSON and passed along, such as the multi-line ``comments`` field in the example.\n    Examples of useful metadata that may be easier to enter at ingestion time than to\n    garner later include taxon IDs of the level and its parent, common names, URLs of\n    papers describing the genome, and geographic origin of the sample.\n\nA copy of the input file will be saved in the output directory under the name ``input.toml``.\nSee the examples in the ``tests/testdata`` repository directory for examples of input data.\n\nGlobal Options\n--------------\nThe following options are global in scope and, if used must be placed before\n``COMMAND``:\n\n============================= ===========================================\n   -v, --verbose              Log debugging info to stderr.\n   -q, --quiet                Suppress logging to stderr.\n   --no-logfile               Suppress logging to file.\n   -e, --warnings_as_errors   Treat warnings as fatal (for testing).\n============================= ===========================================\n\nCommands\n--------\nA listing of commands is available via ``azulejo --help``.\nThe currently implemented commands are:\n\n========================= ==================================================\n  analyze-clusters        Statistics of clustering as function of identity.\n  annotate-homology       Cluster, align, and calculate tree info.\n  cluster-in-steps        Cluster in steps from low to 100% identity.\n  clusters-to-histograms  Compute histograms from cluster file.\n  combine-clusters        Combine synteny and homology clusters,\n  compare-clusters        compare one cluster file with another\n  dagchainer-synteny      Read DAGchainer synteny into homology frames.\n  ingest-data             Marshal protein and genome sequence information.\n  length-std-dist         Plot length distribution of singletons in clusters\n  outlier-length-dist     Plot length distribution of outliers in clusters.\n  prepare-protein-files   Sanitize and combine protein FASTA files.\n  proxy-genes             Calculate a set of proxy genes from synteny files.\n  synteny-anchors         Calculate synteny anchors.\n  usearch-cluster         Cluster at a global sequence identity threshold.\n========================= ==================================================\n\nEach command has its ``COMMANDOPTIONS``, which may be listed with: ::\n\n    azulejo COMMAND --help\n\nProject Status\n--------------\n+-------------------+------------+------------+\n| Latest Release    | |pypi|     | |azulejo|  |\n+-------------------+------------+            +\n| Activity          | |repo|     |            |\n+-------------------+------------+            +\n| Downloads         ||downloads| |            |\n+-------------------+------------+            +\n| Download Rate     ||dlrate|    |            |\n+-------------------+------------+            +\n| License           | |license|  |            |\n+-------------------+------------+            +\n| Code Grade        | |codacy|   |            |\n+-------------------+------------+            +\n| Coverage          | |coverage| |            |\n+-------------------+------------+            +\n| Travis Build      | |travis|   |            |\n+-------------------+------------+            +\n| Dependencies      | |depend|   |            |\n+-------------------+------------+            +\n| Issues            | |issues|   |            |\n+-------------------+------------+            +\n| Code Style        | |black|    |            |\n+-------------------+------------+------------+\n\n\n.. |azulejo| image:: docs/azulejo.jpg\n     :target: https://en.wikipedia.org/wiki/Azulejo\n     :alt: azulejo Definition\n\n.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square\n    :target: https://github.com/psf/black\n    :alt: Black is the uncompromising Python code formatter\n\n.. |pypi| image:: https://img.shields.io/pypi/v/azulejo.svg\n    :target: https://pypi.python.org/pypi/azulejo\n    :alt: Python package\n\n.. |repo| image:: https://img.shields.io/github/last-commit/legumeinfo/azulejo\n    :target: https://github.com/legumeinfo/azulejo\n    :alt: GitHub repository\n\n.. |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg\n    :target: https://github.com/legumeinfo/azulejo/blob/master/LICENSE\n    :alt: License terms\n\n.. |rtd| image:: https://readthedocs.org/projects/azulejo/badge/?version=latest\n    :target: http://azulejo.readthedocs.io/en/latest/?badge=latest\n    :alt: Documentation Server\n\n.. |travis| image:: https://img.shields.io/travis/legumeinfo/azulejo.svg\n    :target:  https://travis-ci.org/legumeinfo/azulejo\n    :alt: Travis CI\n\n.. |codacy| image:: https://api.codacy.com/project/badge/Grade/99549f0ed4e6409e9f5e80a2c4bd806b\n    :target: https://www.codacy.com/app/joelb123/azulejo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=legumeinfo/azulejo&amp;utm_campaign=Badge_Grade\n    :alt: Codacy.io grade\n\n.. |coverage| image:: https://codecov.io/gh/legumeinfo/azulejo/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/legumeinfo/azulejo\n    :alt: Codecov.io test coverage\n\n.. |issues| image:: https://img.shields.io/github/issues/LegumeFederation/lorax.svg\n    :target:  https://github.com/legumeinfo/azulejo/issues\n    :alt: Issues reported\n\n.. |requires| image:: https://requires.io/github/legumeinfo/azulejo/requirements.svg?branch=master\n     :target: https://requires.io/github/legumeinfo/azulejo/requirements/?branch=master\n     :alt: Requirements Status\n\n.. |depend| image:: https://api.dependabot.com/badges/status?host=github&repo=legumeinfo/azulejo\n     :target: https://app.dependabot.com/accounts/legumeinfo/repos/203668510\n     :alt: dependabot dependencies\n\n.. |dlrate| image:: https://img.shields.io/pypi/dm/azulejo\n    :target: https://pypistats.org/packages/azulejo\n    :alt: Download stats\n\n.. |downloads| image:: https://pepy.tech/badge/azulejo\n    :target: https://pepy.tech/project/azulejo\n    :alt: Download stats',
    'author': 'Joel Berendzen',
    'author_email': 'joelb@ncgr.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/legumeinfo/azulejo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
