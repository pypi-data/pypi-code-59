
try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(
    name = 'xxl',
    version = '0.0.1',
    description = 'this is a only test file',
    classifiers = [],
    keywords = 'test python',
    author = 'hanfei321',
    author_email = '1154104163@qq.com',
    url = 'https://pypi.org/manage/project/xxl/',
    packages = ['xxl',],
    include_package_data=True,
    zip_safe=True,
)