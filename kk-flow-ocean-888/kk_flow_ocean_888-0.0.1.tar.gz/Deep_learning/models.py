from sklearn.datasets import load_boston
from matplotlib import pyplot as plt
import random
import numpy as np
import networkx as nx
from collections import defaultdict
import random
from tqdm import tqdm_notebook


# 每个节点的抽象对象
class Node:
    def __init__(self, inputs=[], name=None, is_trainable=False):
        self.inputs = inputs
        self.outputs = []
        self.name = name
        self.is_trainable = is_trainable

        for n in self.inputs:
            n.outputs.append(self)

        self.value = None

        self.gradients = {}

    def forward(self):
        pass

    def backward(self):
        pass

    def __repr__(self):
        return '{}'.format(self.name)


# 节点实例对象
class Placeholder(Node):
    def __init__(self, name=None, is_trainable=False):
        Node.__init__(self, name=name, is_trainable=is_trainable)

    def forward(self, value=None):
        if value is not None: self.value = value

    def backward(self):
        self.gradients = {}
        for n in self.outputs:
            self.gradients[self] = n.gradients[self] * 1


# 节点实例对象
class Linear(Node):
    def __init__(self, x: None, weigth: None, bias: None, name=None, is_trainable=False):
        Node.__init__(self, [x, weigth, bias], name=name, is_trainable=False)

    def forward(self):
        k, x, b = self.inputs[1], self.inputs[0], self.inputs[2]
        self.value = k.value * x.value + b.value

    def backward(self):
        k, x, b = self.inputs[1], self.inputs[0], self.inputs[2]

        for n in self.outputs:
            grad_cost = n.gradients[self]

            self.gradients[k] = grad_cost * x.value

            self.gradients[x] = grad_cost * k.value

            self.gradients[b] = grad_cost * 1


# 节点实例对象
class Relu(Node):
    def __init__(self, x, name=None, is_trainable=False):
        Node.__init__(self, [x], name=name, is_trainable=is_trainable)
        self.x = x

    def forward(self):
        self.value = self.x.value * (self.x.value > 0)

    def backward(self):
        for n in self.outputs:
            grad_cost = n.gradients[self]
            self.gradients[self.x] = grad_cost * (self.x.value > 0)


# 节点实例对象
class Sigmoid(Node):
    def __init__(self, x, name=None, is_trainable=False):
        Node.__init__(self, [x], name=name, is_trainable=False)
        self.x = self.inputs[0]

    def _sigmoid(self, x):
        return 1. / (1 + np.exp(-1 * x))

    def forward(self):
        self.value = self._sigmoid(self.x.value)

    def partial(self):
        return self._sigmoid(self.x.value) * (1 - self._sigmoid(self.x.value))

    def backward(self):
        self.gradients[self.x] = 0

        for n in self.outputs:
            grad_cost = n.gradients[self]
            self.gradients[self.x] += grad_cost * self.partial()


# 节点实例对象
class L2_LOSS(Node):
    def __init__(self, y, y_hat, name=None, is_trainable=False):
        Node.__init__(self, [y, y_hat], name=name, is_trainable=False)
        self.y = y
        self.y_hat = y_hat

    def forward(self):
        y_v = np.array(self.y.value)
        yhat_v = np.array(self.y_hat.value)
        self.value = np.mean((y_v - yhat_v) ** 2)

    def backward(self):
        # 1/n sum (y- yhat)**2
        y_v = np.array(self.y.value)
        yhat_v = np.array(self.y_hat.value)
        self.gradients[self.y] = 2 * np.mean((y_v - yhat_v))
        self.gradients[self.y_hat] = -2 * np.mean((y_v - yhat_v))



