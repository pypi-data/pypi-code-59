# 拓扑图绘制，流程演算
from sklearn.datasets import load_boston
from matplotlib import pyplot as plt
import random
import numpy as np
import networkx as nx


# region 初始化数据
# 加载波士顿房价数据
data = load_boston()
# 传给X,y
X, y = load_boston(return_X_y=True)
# 打印测试数据获取
# X[1]=[2.7310e-02 0.0000e+00 7.0700e+00 0.0000e+00 4.6900e-01 6.4210e+00 7.8900e+01 4.9671e+00 2.0000e+00 2.4200e+02 1.7800e+01 3.9690e+02 9.1400e+00]
# y[1]=21.6
# X.shape=(506, 13)
# print(X[1], y[1], X.shape)
# 获取波士顿房价和卧室面积（x的第五个数据）的图样
# plt.scatter(X[:, 5], y)
# # 显示图样
# plt.show()

# # 不知道拟合直线的数据时候，取随机数尝试
# k, b = random.randint(-100, 100), random.randint(-100, 100)


# # 创建一个函数，利用常规公式，输入一个卧室面积，返回一个价格
# def price_jiu(x):
#     # 公式：y=k*x+b
#     return k*x+b


# 把卧室面积（x的第五个数据）进行赋值
X_rm = X[:, 5]
# y_hat = [price(x) for x in X_rm]
# # 把随机的数据写到图样里
# plt.plot(X_rm, y_hat)
# # 显示图样
# plt.show()
# endregion


def price_(x, k, b):
    # Operation : CNN, RNN, LSTM, Attention 比KX+B更复杂的对应关系
    return k * x + b


def linear_(x, k1, b1):
    return k1 * x + b1


def sigmoid_(x):
    return 1 / (1 + np.exp(-x))


def y_(x, k1, k2, b1, b2):
    output1 = linear(x, k1, b1)
    output2 = sigmoid(x)
    output3 = linear(x, k2, b2)
    return output3


trying_times = 50000

min_cost = float('inf')

losses = []

scala = 0.3

# k, b = random.random() * 100 - 200, random.random() * 100 - 200
# 参数初始化问题！ Weight Initizalition 问题！

k1, b1 = np.random.normal(), np.random.normal()
k2, b2 = np.random.normal(), np.random.normal()

learning_rate = 1e-3  # Optimizer Rate


def loss(y, y_hat):
    sum_ = sum([(y_i - y_hat_i) ** 2 for y_i, y_hat_i in zip(y, y_hat)])
    return sum_ / len(y)

def loss_partial(y, y_hat):
    return 2/len(y) * sum(y_i - y_hat_i for y_i, y_hat_i in zip(y, y_hat)) * -1


def partial_k(x, y, y_hat):
    gradient = 0

    for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)):
        gradient += (y_i - y_hat_i) * x_i

    return -2 / len(y) * gradient


def partial_b(y, y_hat):
    gradient = 0

    for y_i, y_hat_i in zip(list(y), list(y_hat)):
        gradient += (y_i - y_hat_i)

    return -2 / len(y) * gradient


# for i in range(trying_times):
#     price_by_random_k_and_b = [y(r, k1, k2, b1, b2) for r in X_rm]
#
#     cost = loss(list(y), price_by_random_k_and_b)
#
#     k_gradient = partial_k(X_rm, y, price_by_random_k_and_b)  # 变化的方向
#     b_gradient = partial_b(y, price_by_random_k_and_b)
#
#     k1 += -1 * (partial_of_k1) * learning_rate
#     k2 += -1 * (partial_of_k2) * learning_rate
#     b1 += -1 * (partial_of_b1) * learning_rate
#     b2 += -1 * (partial_of_b2) * learning_rate






def linear(k, b, x):
    return k * x + b


def linear_partial(k, b, x):
    return k

# def y_hat = linear() which x is sigmoid(x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_partial(x):
    return sigmoid(x) (1 - sigmoid(x))

# partials = [
#     loss_partial(y, y_hat),
#     linear_partial(k2, b2, sigmoid(x)),
#     sigmoid_partial(linear(k1, b1, x)),
#     linear_partial(k1, b1, x)
# ]

loss_partial_of_k1 = 1
#
# for p in partials:
#     loss_partial_k1 *= p



computing_graph = {
    'x1': ['linear'],
    'k1': ['linear'],
    'b1': ['linear'],
    'linear': ['sigmoid'],
    'sigmoid': ['linear_2'],
    'k2': ['linear_2'],
    'b2': ['linear_2'],
    'linear_2': ['loss']
}
graph = nx.DiGraph(computing_graph)

layout = nx.layout.spring_layout(graph)
nx.draw(nx.DiGraph(computing_graph), layout, with_labels=True)
plt.show()


def visited_procedure(graph, postion, visited_order, step, sub_plot_index=None, colors=('red', 'green')):
    changed = visited_order[:step] if step is not None else visited_order

    before, after = colors

    color_map = [after if c in changed else before for c in graph]

    nx.draw(graph, postion, node_color=color_map, with_labels=True, ax=sub_plot_index)


visited_order = ['x1', 'b1', 'k1', 'linear', 'sigmoid', 'b2', 'k2','linear_2', 'loss']


dimension = int(len(visited_order)**0.5)

fig, ax = plt.subplots(dimension, dimension+1, figsize=(15,15))

# 正向
for i in range(len(visited_order)+1):
    ix = np.unravel_index(i, ax.shape)
    plt.sca(ax[ix])
    ax[ix].title.set_text('Feed Forward Step: {}'.format(i))
    visited_procedure(graph, layout, visited_order, step=i, sub_plot_index=ax[ix])
plt.show()


# # 反向 正向和反向不能一起画
# for i in range(len(visited_order)+1):
#     ix = np.unravel_index(i, ax.shape)
#     plt.sca(ax[ix])
#     ax[ix].title.set_text('Feed Forward Step: {}'.format(i))
#     visited_procedure(graph, layout, visited_order[::-1], step=i, sub_plot_index=ax[ix],
#                      colors=('green', 'black'))
# plt.show()


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
            graph.pop(node)
            sorted_node.append(node)

            for _, links in graph.items():
                if node in links: links.remove(node)
        else:
            break

    return sorted_node


class Node:
    def __init__(self, inputs=[]):
        self.inputs = inputs
        self.outputs = []

        for n in self.inputs:
            n.outputs.append(self)
            # set 'self' node as inbound_nodes's outbound_nodes

        self.value = None

        self.gradients = {}
        # keys are the inputs to this node, and their
        # values are the partials of this node with
        # respect to that input.
        # \partial{node}{input_i}

    def forward(self):
        '''
        Forward propagation.
        Compute the output value vased on 'inbound_nodes' and store the
        result in self.value
        '''

        raise NotImplemented

    def backward(self):
        raise NotImplemented
