import setuptools

# readme.md = github readme.md, 這裡可接受markdown寫法
# 如果沒有的話，需要自己打出介紹此專案的檔案，再讓程式知道

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VerdictCut", # 
    version="0.0.4",
    author="seanbbear",
    author_email="k7489759@gmail.com",
    description="cut the verdict into different part",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)