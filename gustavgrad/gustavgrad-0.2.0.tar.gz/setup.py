# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gustavgrad']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'gustavgrad',
    'version': '0.2.0',
    'description': '',
    'long_description': "# gustavgrad\n[![Tests](https://github.com/gustavgransbo/gustavgrad/workflows/Tests/badge.svg)](https://github.com/gustavgransbo/gustavgrad/actions?workflow=Tests)\n[![codecov](https://codecov.io/gh/gustavgransbo/gustavgrad/branch/master/graph/badge.svg)](https://codecov.io/gh/gustavgransbo/gustavgrad)\n[![PyPI](https://img.shields.io/pypi/v/gustavgrad.svg)](https://pypi.org/project/gustavgrad)\n[![Python Version](https://img.shields.io/pypi/pyversions/gustavgrad.svg)](https://github.com/gustavgransbo/gustavgrad)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nAn autograd library built on NumPy, inspired by [Joel Grus's livecoding](https://github.com/joelgrus/autograd/tree/master).\n\n## Installation\n### With pip\n```bash\npip install gustavgrad\n```\n\n## How to use the library\n### `Tensor` operations\nThe `Tensor` class is the cornerstone of `gustavgrad`.\nIt behaves much like an ordinary `numpy.ndarray`.\n\n`Tensors` can be added together,\n```python\n>>> from gustavgrad import Tensor\n>>> x = Tensor([1, 2, 3])\n>>> x + x\nTensor(data=[2 4 6], requires_grad=False)\n```\n... subracted from each other,\n```python\n>>> x - x\nTensor(data=[0 0 0], requires_grad=False)\n```\n... their dot-product can calculated,\n```python\n>>> x * x\nTensor(data=[1 4 9], requires_grad=False)\n```\n... and they can be multiplied with each other.\n```python\n>>> y = Tensor([[1], [2], [3]])\n>>> x @ y\nTensor(data=[14], requires_grad=False)\n```\n`Tensor` operations also support broadcasting:\n```python\n>>> x * 3\nTensor(data=[3 6 9], requires_grad=False)\n>>> z = Tensor([[1, 2, 3], [4, 5, 6]])\n>>> x * z\nTensor(data=\n[[ 1  4  9]\n [ 4 10 18]], requires_grad=False)\n```\n### Automatic backpropagation\nBut a `Tensor` is not just an `ndarray`, they also keep track of their own gradient.\n```python\n>>> speed = Tensor(1, requires_grad=True)\n>>> time = Tensor(10, requires_grad=True)\n>>> distance = speed * time\n>>> distance\nTensor(data=10, requires_grad=True)\n```\nIf a `Tensor` is created as the result of a `Tensor` operation involving a `Tensor` with `requires_grad=True`,\nthe resulting `Tensor` will be able to backpropagate it's own gradient to it's ancestor.\n```python\n>>> distance.backward()\n>>> speed.grad\narray(10.)\n>>> time.grad\narray(1.)\n```\nBy calling the `backward` method on `distance` the gradient of `speed` and `time` is automatically updated.\nWe can see that increasing `speed` by 1 would result in an increase in `distance` by 10, while an increase\nin `time` by 1 would only increase `distance` by 1.\n\nThe `Tensor` class supports backpropagation over arbitrary compositions of `Tensor` operations.\n```python\n>>> t1 = Tensor([[1, 2, 3], [4, 5, 6]], requires_grad=True)\n>>> t2 = Tensor([[1], [2], [3]])\n>>> t3 = t1 @ t2 + 1\n>>> t4 = t3 * 7\n>>> t5 = t4.sum()\n>>> t5.backward()\n>>> t1.grad\narray([[ 7., 14., 21.],\n       [ 7., 14., 21.]])\n```\n### The `Module` API\n`gustavgrad` provides some tools to simplify setting up and training machine learning models.\nThe `Module` API makes it easier to manage multiple related `Tensors` by registering them as\n`Parameters`.\nA `Parameter` is just a randomly initialized `Tensor`.\n```python\nfrom gustavgrad.module import Module, Parameter\nfrom gustavgrad.function import tanh\nclass MultilayerPerceptron(Module):\n    def __init__(self, input_size: int, output_size: int, hidden_size: int = 100) -> None:\n        self.layer1 = Parameter(input_size, hidden_size)\n        self.bias1 = Parameter(hidden_size)\n        self.layer2 = Parameter(hidden_size, output_size)\n        self.bias2 = Parameter(output_size)\n        \n    def predict(self, x: Tensor) -> Tensor:\n        x = x @ self.layer1 + self.bias1\n        x = tanh(x)\n        x = x @ self.layer2 + self.bias2\n        return x\n```\nBy subclassing `Module` our `MultilayerPerceptron` class automatically gets some helper methods\nfor managing its `Parameters`.\nLet's create a `MultilayerPerceptron` that tries to learn the XOR function.\n```python\nxor_input = Tensor([[0, 0], [0, 1], [1, 0], [1, 1]])\nxor_targets = Tensor([[0], [1], [1], [0]])\nxor_mlp = MultilayerPerceptron(input_size=2, output_size=1, hidden_size=4)\n```\nWe can use the model to make predictions on the `xor_input` `Tensor`.\n```python\n>>> predictions = xor_mlp.predict(xor_input)\n>>> predictions\nTensor(data=\n[[-1.79888385]\n [-1.07965756]\n [ 0.34373135]\n [ 1.63366069]], requires_grad=True)\n```\nThe predictions of the randomly initialized model aren't right, but we can improve the model by\ncalculating the gradient of it's `Parameters` in respect to a loss function.\n```python\nfrom gustavgrad.loss import SquaredErrorLoss\nse_loss = SquaredErrorLoss()\nloss = se_loss.loss(xor_targets, predictions)\nloss.backward()\n```\n`loss` is a `Tensor`, so we can call its `backward` method to do backpropagation through our `xor_mlp`.\nWe can then adjust the weights of all `Parameters` in `xor_mlp` using gradient descent:\n```python\nfrom gustavgrad.optim import SGD\noptim = SGD(lr=0.01)\noptim.step(xor_mlp)\n```\nAfter updating the weights we can reset the gradients of all parameters and make new predictions:\n```python\n>>> xor_mlp.zero_grad()\n>>> predictions = xor_mlp.predict(xor_input)\n>>> predictions\nTensor(data=\n[[-1.51682686]\n [-0.78583272]\n [ 0.55994602]\n [ 1.67962174]], requires_grad=True)\n```\nSee [examples/xor.py](examples/xor.py) for a full example of how `gustavgrad` can be used to learn the XOR function.\nThe [examples](examples/) directory also contains some other basic examples of how the library can be used.\n",
    'author': 'Gustav Gränsbo',
    'author_email': 'gustav.gransbo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gustavgransbo/gustavgrad',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
