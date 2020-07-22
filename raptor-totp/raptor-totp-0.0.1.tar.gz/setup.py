import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="raptor-totp",
    version="0.0.1",
    author_email="zhoujianwen@aliyun.com",
    description="Raptor, reeve time-based one time password ahead rapidly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bgi-tumour.oss-cn-hangzhou.aliyuncs.com/code/skip_totp/raptor.py",
    include_package_data=False,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
