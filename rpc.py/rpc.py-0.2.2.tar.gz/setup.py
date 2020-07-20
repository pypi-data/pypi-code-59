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
    'version': '0.2.2',
    'description': 'An easy-to-use and powerful RPC framework. Base WSGI & ASGI.',
    'long_description': '# rpc.py\n\nAn easy-to-use and powerful RPC framework. Base WSGI & ASGI.\n\nBased on WSGI/ASGI, you can deploy the rpc.py server to any server and use http2 to get better performance.\n\n## Install\n\nInstall from PyPi:\n\n```bash\npip install rpc.py\n```\n\nInstall from github:\n\n```bash\npip install git+https://github.com/abersheeran/rpc.py@setup.py\n```\n\n## Usage\n\n### Server side:\n\n```python\nimport uvicorn\nfrom rpcpy import RPC\n\napp = RPC(mode="ASGI")\n\n\n@app.register\nasync def none() -> None:\n    return\n\n\n@app.register\nasync def sayhi(name: str) -> str:\n    return f"hi {name}"\n\n\n@app.register\nasync def yield_data(max_num: int):\n    for i in range(max_num):\n        yield i\n\n\nif __name__ == "__main__":\n    uvicorn.run(app, interface="asgi3", port=65432)\n```\n\nOR\n\n```python\nimport uvicorn\nfrom rpcpy import RPC\n\napp = RPC()\n\n\n@app.register\ndef none() -> None:\n    return\n\n\n@app.register\ndef sayhi(name: str) -> str:\n    return f"hi {name}"\n\n\n@app.register\ndef yield_data(max_num: int):\n    for i in range(max_num):\n        yield i\n\n\nif __name__ == "__main__":\n    uvicorn.run(app, interface="wsgi", port=65432)\n```\n\n### Client side:\n\n```python\nimport httpx\nfrom rpcpy.client import Client\n\napp = Client(httpx.Client(), base_url="http://127.0.0.1:65432/")\n\n\n@app.remote_call\ndef none() -> None:\n    ...\n\n\n@app.remote_call\ndef sayhi(name: str) -> str:\n    ...\n\n\n@app.remote_call\ndef yield_data(max_num: int):\n    yield\n```\n\nOR\n\n```python\nimport httpx\nfrom rpcpy.client import Client\n\napp = Client(httpx.AsyncClient(), base_url="http://127.0.0.1:65432/")\n\n\n@app.remote_call\nasync def none() -> None:\n    ...\n\n\n@app.remote_call\nasync def sayhi(name: str) -> str:\n    ...\n\n\n@app.remote_call\nasync def yield_data(max_num: int):\n    yield\n```\n\n### Sub-route\n\nIf you need to deploy the rpc.py server under `example.com/sub-route/*`, you need to set `RPC(prefix="/sub-route/")` and modify the `Client(base_path=https://example.com/sub-route/)`.\n\n### Serialization of results\n\nCurrently supports two serializers, JSON and Pickle. JSON is used by default.\n\n```python\nfrom rpcpy.serializers import JSONSerializer, PickleSerializer\n\nRPC(serializer=JSONSerializer())\n# or\nRPC(serializer=PickleSerializer())\n```\n\n## Limitations\n\nCurrently, function parameters must be serializable by `json`.\n\nIn `v0.3`, a custom serializer will be introduced for function parameters.\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/rpc.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
