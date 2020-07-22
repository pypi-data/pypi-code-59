# 实现一个深度学习神经网络框架，并发布到pip，别人就可以install使用
from sklearn.datasets import load_boston
from matplotlib import pyplot as plt
import random
import numpy as np
import networkx as nx
from collections import defaultdict
import random
from tqdm import tqdm_notebook


# region 框架的全部内容
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


# 排序
def based_on_feed_dict_create_graph(feed_dict):
    nodes = [n for n in feed_dict]  # know all the placeholder

    computing_graph = defaultdict(list)

    while nodes:
        n = nodes.pop(0)

        if isinstance(n, Placeholder):
            n.value = feed_dict[n]

        if n in computing_graph: continue

        for m in n.outputs:
            computing_graph[n].append(m)
            nodes.append(m)

    return computing_graph


def toplogic(graph):
    sorted_node = []

    while len(graph) > 0:

        all_inputs = []
        all_outputs = []

        for n in graph:
            all_inputs += graph[n]
            all_outputs.append(n)

        all_inputs = set(all_inputs)
        all_outputs = set(all_outputs)

        need_remove = all_outputs - all_inputs  # which in all_inputs but not in all_outputs

        if len(need_remove) > 0:
            node = random.choice(list(need_remove))

            need_to_visited = [node]

            if len(graph) == 1: need_to_visited += graph[node]

            graph.pop(node)
            sorted_node += need_to_visited

            for _, links in graph.items():
                if node in links: links.remove(node)
        else:  # have cycle
            break

    return sorted_node


# 排序
def node_compting_sort(feed_dict):
    graph = based_on_feed_dict_create_graph(feed_dict)

    return toplogic(graph)


def forward_and_backward(graph_order, monitor=False):
    # 整体的参数就更新了一次
    for node in graph_order:
        if monitor:
            print('forward computing node: {}'.format(node))
        node.forward()

    for node in graph_order[::-1]:
        if monitor:
            print('backward computing node: {}'.format(node))
        node.backward()


def optimizer(graph, learning_rate=1e-2):
    for t in graph:
        if t.is_trainable:
            t.value += -1 * t.gradients[t] * learning_rate
# endregion

# region 下面是应用测试
# # from xxxx import Linear, Sigmoid, L2_LOSS, Placeholder
# from sklearn.datasets import load_boston
#
# data = load_boston()
# X_, y_ = data['data'], data['target']
# X_rm = X_[:, 5]
#
# w1_, b1_ = np.random.normal(), np.random.normal()
# w2_, b2_ = np.random.normal(), np.random.normal()
# # w3_, b3_ = np.random.normal(), np.random.normal()
#
# X, y = Placeholder(name='X'), Placeholder(name='y')
# w1, b1 = Placeholder(name='w1', is_trainable=True), Placeholder(name='b1', is_trainable=True)
# w2, b2 = Placeholder(name='w2', is_trainable=True), Placeholder(name='b2', is_trainable=True)
# # w3, b3 = Placeholder(name='w3', is_trainable=True), Placeholder(name='b3', is_trainable=True)
# # build model
#
# output1 = Linear(X, w1, b1, name='linear_01')
# # output2 = Sigmoid(output1, name='sigmoid')
# output2 = Relu(output1, name='relu')
# y_hat = Linear(output2, w2, b2, name='linear_02')
# cost = L2_LOSS(y, y_hat, name='loss')
#
# feed_dict = {
#     X: X_rm,
#     y: y_,
#     w1: w1_,
#     w2: w2_,
#     b1: b1_,
#     b2: b2_,
# }
#
# graph_sort = node_compting_sort(feed_dict)
#
# epoch = 100
#
# learning_rate = 1e-2
# batch_num = 100
#
# losses = []
#
# for e in tqdm_notebook(range(epoch)):
#
#     batch_loss = 0
#
#     for b in range(batch_num):
#         index = np.random.choice(range(len(X_rm)))
#         X.value = X_rm[index]
#         y.value = y_[index]
#
#         forward_and_backward(graph_sort, monitor=False)
#
#         optimizer(graph_sort, learning_rate=learning_rate)
#         # sgd stocastic gradient descent
#
#         batch_loss += cost.value
#
#     losses.append(batch_loss / batch_num)
#
# plt.plot(losses)
# plt.show()
# endregion
