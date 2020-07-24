from setuptools import setup

# 需要将那些包导入
packages = ["itwalker"]

# 导入静态文件
# file_data = [
#     ("smart/static", ["smart/static/icon.svg", "smart/static/config.json"]),
# ]

# 第三方依赖
requires = [
    "PyMySQL>=0.10.0",
    "DBUtils>=1.3"
]

# 自动读取readme
with open("README.md", "r") as fh:
    long_description = fh.read()

#    data_files=file_data,  # 打包时需要打包的数据文件，如图片，配置文件等
#     include_package_data=True,  # 是否需要导入静态数据文件

setup(
    name='itwalker',  # 包名称
    version='1.0.0',  # 包版本
    description='',  # 包详细描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='itwalker',  # 作者名称
    author_email='2581870602@qq.com',  # 作者邮箱
    url='',  # 项目官网
    packages=packages,  # 项目需要的包
    python_requires=">=3.7",  # Python版本依赖
    install_requires=requires,  # 第三方库依赖
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    classifiers=[  # 程序的所属分类列表
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
