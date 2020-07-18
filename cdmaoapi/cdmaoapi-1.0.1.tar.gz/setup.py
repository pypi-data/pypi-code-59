import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='cdmaoapi',
                 version='1.0.1',
                 description='获取/提交编程猫官方数据',
                long_description=long_description,
                long_description_content_type="text/markdown",
                 author='冷鱼花茶',
                 author_email='2991883280@qq.com',
                 url='http://doc.viyrs.com/cdmaoapi.html',
                 packages=setuptools.find_packages(),
                 install_requires = ['requests==2.23.0', 'lxml==4.5.1'],
                 classifiers=[
                     "Programming Language :: Python",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: Apache Software License",
                 ])