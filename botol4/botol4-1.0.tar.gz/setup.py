import setuptools



with open("README.md", "r") as fh:

    long_description = fh.read()



setuptools.setup(

    name="botol4", 

    version="1.0",

    author="BotolMehedi",

    author_email="Botol@email.com",

    description="Bangladeshi Account Cracker",

    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),

    url="https://github.com/botolmehedi/botol",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 2",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=2.7',

)
