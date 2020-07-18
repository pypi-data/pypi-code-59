# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpcpy']

package_data = \
{'': ['*']}

install_requires = \
['python-multipart>=0.0.5,<0.0.6']

extras_require = \
{'client': ['httpx>=0.13.3,<0.14.0'], 'full': ['httpx>=0.13.3,<0.14.0']}

setup_kwargs = {
    'name': 'rpc.py',
    'version': '0.2.1',
    'description': '',
    'long_description': '# rpc.py\n\nAn easy-to-use and powerful RPC framework. Base WSGI & ASGI.\n\nBased on WSGI/ASGI, you can deploy the rpc.py server to any server and use http2 to get better performance.\n\n## Install\n\nInstall from PyPi:\n\n```bash\npip install rpc.py\n```\n\nInstall from github:\n\n```bash\npip install git+https://github.com/abersheeran/rpc.py@setup.py\n```\n\n## Usage\n\n### Server side:\n\n```python\nimport uvicorn\nfrom rpcpy import RPC\n\napp = RPC(mode="ASGI")\n\n\n@app.register\nasync def none() -> None:\n    return\n\n\n@app.register\nasync def sayhi(name: str) -> str:\n    return f"hi {name}"\n\n\n@app.register\nasync def yield_data(max_num: int):\n    for i in range(max_num):\n        yield i\n\n\nif __name__ == "__main__":\n    uvicorn.run(app, interface="asgi3", port=65432)\n```\n\nOR\n\n```python\nimport uvicorn\nfrom rpcpy import RPC\n\napp = RPC()\n\n\n@app.register\ndef none() -> None:\n    return\n\n\n@app.register\ndef sayhi(name: str) -> str:\n    return f"hi {name}"\n\n\n@app.register\ndef yield_data(max_num: int):\n    for i in range(max_num):\n        yield i\n\n\nif __name__ == "__main__":\n    uvicorn.run(app, interface="wsgi", port=65432)\n```\n\n### Client side:\n\n```python\nimport httpx\nfrom rpcpy.client import Client\n\napp = Client(httpx.Client(), base_url="http://127.0.0.1:65432/")\n\n\n@app.remote_call\ndef none() -> None:\n    ...\n\n\n@app.remote_call\ndef sayhi(name: str) -> str:\n    ...\n\n\n@app.remote_call\ndef yield_data(max_num: int):\n    yield\n```\n\nOR\n\n```python\nimport httpx\nfrom rpcpy.client import Client\n\napp = Client(httpx.AsyncClient(), base_url="http://127.0.0.1:65432/")\n\n\n@app.remote_call\nasync def none() -> None:\n    ...\n\n\n@app.remote_call\nasync def sayhi(name: str) -> str:\n    ...\n\n\n@app.remote_call\nasync def yield_data(max_num: int):\n    yield\n```\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/setup.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
