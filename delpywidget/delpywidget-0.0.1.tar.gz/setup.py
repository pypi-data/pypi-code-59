from setuptools import setup


setup(
        name="delpywidget",
        version="0.0.1",
        packages=["delpy"],
        package_data={'delpy': ['*.xml', 'static/*']},
        url='https://github.com/Edwauline/DelpyWidget',
        license='MIT',
        author='Edwige Gros',
        author_email='edwige.gros@laposte.net',
        description='Blockly w/ Python on Jupyter Notebook',
        data_files=[
        # like `jupyter nbextension install --sys-prefix`
            ("share/jupyter/nbextensions/delpy", ["delpy/static/index.js","delpy/static/delpy_block.js","delpy/static/delpy_blockly.js","delpy/static/delpy_javascript.js","delpy/static/delpy_python.js","delpy/static/lang.js","delpy/static/run.js"])
        ],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
        ],
        install_requires=['jupyter']
)
