from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="my_site",
    version="1.0.1",
    description="A Python package to make a poll.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com",
    author="Jesvin",
    author_email="Jesvin@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["my_site"],
    include_package_data=True,
    install_requires=["sys","os","django"],
    entry_points={
        "console_scripts": [
            "django-polls=my_site.polls.manage.py:main",
        ]
    },
)