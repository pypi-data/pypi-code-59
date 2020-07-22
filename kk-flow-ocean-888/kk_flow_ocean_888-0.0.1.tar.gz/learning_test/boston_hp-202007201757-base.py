# 深度学习理论基础-波士顿房价
'''
目的：找到一条“最佳”的直线，拟合卧室和房价的关系
过程：
'''
from sklearn.datasets import load_boston
from matplotlib import pyplot as plt
import random
import numpy as np


# region matplotlib测试代码
# x = range(2,26,2)
# y = [15,13,14,17,20,25,26,26,24,22,18,15]
# plt.plot(x,y)
# plt.show()
# endregion


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


# region 三种计算loss的方法
def draw_room_and_price():
    plt.scatter(X[:, 5], y)


# 创建一个函数，利用常规公式，输入卧室面积,k,b，返回一个价格
def price(x, k, b):
    # todo 这里就是比较重要的，核心模型 Operation:cnn/rnn/lstm/attention 本质就是：比kx+b更复杂的对应关系
    return k*x+b


# 目的：想找到最合适的k和b
# 我们就需要一个标准去衡量这个值合适不合适
# 统计学里的y是y_true,预测(估值)的y是y_hat
# y_true和y_hat之间缺失情况，损失了多少，叫做 todo 损失函数（loss）
# todo 损失函数第一种：y_true 减 y_hat 的绝对值表示为损失函数，损失函数越小，这个数越合适
# 比如实际y是3，预估值为4、3.5、2，则损失函数得到的绝对值为1,0.5,1，也就是说3.5更合适做预估值
# todo 损失函数第二种：多组y_true 减 多组y_hat 的差值 的绝对值 的和表示为损失函数，损失函数越小，这个数越合适
# todo 由于不同的多组y_ture和y_hat的损失函数结果可能相同，所以定义生成一个损失函数2（loss2），把y_true 减 y_hat 的绝对值给一个惩罚值，放大他的差值，可以过滤出波动更小的更合适的损失函数


# loss2函数,带惩罚值
def loss(y, y_hat):
    # 把y_true 减 y_hat 的绝对值给一个惩罚值，放大他的差值，可以过滤出波动更小的更合适的损失函数
    sum_ = sum([(y_i-y_hat_i) ** 2 for y_i, y_hat_i in zip(y, y_hat)])
    return sum_/len(y)


# # 测试：计算损失函数1（loss1）差值相同，但是加入惩罚值后计算损失函数2（loss2）即可区分波动情况，选择比较小的
# y = [3, 4, 4]
# y_h1 = [1, 1, 4]  # 差值2+3+0=5
# y_h2 = [3, 4, 0]  # 差值1+0+4=5
# print(loss(y, y_h1))  # 4.333333333333333
# print(loss(y, y_h2))  # 5.333333333333333


# 根据上面的最优解，画出相应图样
def plot_by_k_and_b(k, b, price_by_random_k_and_b):
    # 画出原始卧室面积数据
    draw_room_and_price()
    # 把求导的数据输入图样
    plt.scatter(X_rm, price_by_random_k_and_b)

    # 显示图样，对比查看，结果是完全不符合的
    plt.show()


# 方法1
def nd_1():
    # 循环生成若干组y_hat，找到最小损失函数的那组
    trying_times = 1000  # 循环多少次
    best_k, best_b, price_by_random_k_and_b = None, None, None  # 初始化最优k和b
    min_cost = float('inf')  # 初始化最小的损失函数

    losses = []  # 记录损失函数的下降情况
    for i in range(trying_times):
        # 不知道拟合直线的数据时候，取随机数尝试
        k = random.random()*100 - 200  # random.randint(-100, 100)
        b = random.random()*100 - 200  # random.randint(-100, 100)
        # 循环计算卧室面积对应的价格
        price_by_random_k_and_b = [price(r, k, b) for r in X_rm]
        # # 打印查看随机生成的值
        # print('the random k:{}, b:{}'.format(k, b))
        # 计算损失函数
        cost = loss(list(y), price_by_random_k_and_b)
        # print('the loss of k:{}, b:{} is {}'.format(k, b, cost))
        # 例：the loss of k:67, b:22 is 178547.15172407706   cost的值越小越合适
        # todo loss：一件事情你只要知道如何评价它好与坏，基本上就完成了一半的工作了

        if cost < min_cost:
            min_cost = cost
            print('在第{}次，k和b更新了'.format(i))
            best_k, best_b = k, b
            losses.append(min_cost)

    print(best_k, best_b, min_cost)

    plot_by_k_and_b(best_k, best_b, price_by_random_k_and_b)

    # 打印下降曲线图
    # plt.plot(losses)
    # plt.show()

# nd_1()


# 方法2
def nd_2():
    # 进行方向的调整，k的变化有两种，变大和减小；b的变化有两种，变大和减小
    directions = [
        (+1, -1),
        (+1, +1),
        (-1, -1),
        (-1, +1),
    ]

    # 循环生成若干组y_hat，找到最小损失函数的那组
    trying_times = 1000  # 循环多少次
    best_k, best_b, price_by_random_k_and_b = None, None, None  # 初始化最优k和b
    min_cost = float('inf')  # 初始化最小的损失函数

    # 不知道拟合直线的数据时候，取随机数尝试
    best_k = random.random() * 200 - 100  # random.randint(-100, 100)
    best_b = random.random() * 200 - 100  # random.randint(-100, 100)
    current_k, current_b = None, None
    # 随机取一个方向
    next_direction = random.choice(directions)
    # 变化步长
    scala = 0.1

    losses = []  # 记录损失函数的下降情况
    for i in range(trying_times):
        # 重新赋值当前方向
        current_direction = next_direction
        k_direction, b_direction = next_direction
        # 重新生成k和b
        current_k = best_k + k_direction*scala
        current_b = best_b + b_direction*scala

        # 循环计算卧室面积对应的价格
        price_by_random_k_and_b = [price(r, current_k, current_b) for r in X_rm]
        # # 打印查看随机生成的值
        # print('the random k:{}, b:{}'.format(k, b))
        # 计算损失函数
        cost = loss(list(y), price_by_random_k_and_b)
        # print('the loss of k:{}, b:{} is {}'.format(k, b, cost))
        # 例：the loss of k:67, b:22 is 178547.15172407706   cost的值越小越合适
        # todo loss：一件事情你只要知道如何评价它好与坏，基本上就完成了一半的工作了

        if cost < min_cost:
            min_cost = cost
            print('在第{}次，k和b更新了'.format(i))
            best_k, best_b = current_k, current_b
            losses.append(min_cost)

            # 重新赋值当前方向
            current_direction = next_direction
        else:
            # # 重新赋值当前方向:随机取
            # current_direction = random.choice(directions)
            # 重新赋值当前方向：去掉当前方向随机取
            current_direction = random.choice(list(set(directions)-{current_direction}))

    print(best_k, best_b, min_cost)

    plot_by_k_and_b(current_k, current_b, price_by_random_k_and_b)

    # 打印下降曲线图
    # plt.plot(losses)
    # plt.show()
    pass

# nd_2()


# 测试导数
def test_square():
    def square(x):
        return 10*x**2+5*x+5

    _X = np.linspace(0, 100)
    _y = [square(x) for x in _X]
    plt.plot(_X, _y)
    plt.show()


# # 测试导数
# test_square()


# 方法3
def nd_3():
    # 梯度下降（使用导数），目的：能不能每一次尝试，都按照能够让它loss减小方向走？都能够找到一个方向
    # 通过loss，对k和b取偏导
    def partial_k(x, y, y_hat):
        # 取k的偏导
        gradient = 0
        for x_i, y_i, y_hat_i in zip(list(x), list(y), list(y_hat)):
            gradient += (y_i - y_hat_i) * x_i

        return -2 / len(y) * gradient

    def partial_b(y, y_hat):
        # 取b的偏导
        gradient = 0
        for y_i, y_hat_i in zip(list(y), list(y_hat)):
            gradient += (y_i - y_hat_i)

        return -2 / len(y) * gradient

    # 循环生成若干组y_hat，找到最小损失函数的那组
    trying_times = 10000  # 循环多少次
    best_k, best_b, price_by_random_k_and_b = None, None, None  # 初始化最优k和b
    min_cost = float('inf')  # 初始化最小的损失函数

    # 不知道拟合直线的数据时候，取随机数尝试 todo 这里就是比较重要的，参数初始化问题：initizalition问题/或者叫权重 weight
    k = random.random() * 100 - 200  # random.randint(-100, 100)
    b = random.random() * 100 - 200  # random.randint(-100, 100)

    # 变化步长 todo 这里就是比较重要的，更新速率问题：optimizer rate
    learning_rate = 1e-3

    losses = []  # 记录损失函数的下降情况
    for i in range(trying_times):
        # 循环计算卧室面积对应的价格 y_hat
        price_by_random_k_and_b = [price(r, k, b) for r in X_rm]
        # # 打印查看随机生成的值
        # print('the random k:{}, b:{}'.format(k, b))
        # 计算损失函数
        cost = loss(list(y), price_by_random_k_and_b)
        # print('the loss of k:{}, b:{} is {}'.format(k, b, cost))
        # 例：the loss of k:67, b:22 is 178547.15172407706   cost的值越小越合适
        # todo loss：一件事情你只要知道如何评价它好与坏，基本上就完成了一半的工作了

        if cost < min_cost:
            min_cost = cost
            # print('在第{}次，k和b更新了'.format(i))
            best_k, best_b = k, b
            losses.append(min_cost)
        else:
            pass
        # 通过偏导计算变化的方向 todo 这里就是比较重要的，优化器：optimizer 比如：adam/momentum动量
        k_gradient = partial_k(X_rm, y, price_by_random_k_and_b)
        b_gradient = partial_b(y, price_by_random_k_and_b)

        k = k + (-1 * k_gradient) * learning_rate
        b = b + (-1 * b_gradient) * learning_rate

    print(k, b, min_cost, len(losses))

    plot_by_k_and_b(best_k, best_b, price_by_random_k_and_b)

    # 打印下降曲线图
    plt.plot(losses)
    plt.show()
    pass


# 基本最优解方案
# nd_3()
# 下一步封装成框架：把重要的功能封装为一块一块的引用函数，别人使用时不需要重新写底层代码
# 学习要点：1.一定要复现代码；2.尝试调整loss函数，然后求解梯度下降，并观察梯度下降的趋势/loss函数改变意味着partial也需要改变；
# endregion


# region 非线性的拟合函数
# todo 如何将拟合函数变成非线性的呢？

# 生成非线性数据返回
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# # 初始化x数据
# test_x = np.linspace(-10, 10, 2000)
# # 生成非线性数据
# test_y = sigmoid(test_x)
# # 显示非线性图样
# plt.plot(test_x, test_y)
# plt.show()



# endregion


# region 拓扑图绘制
# 拓扑图绘制模块
import networkx as nx


# 流程图绘制方法
def visited_procedure(graph, postion, visited_order, step, sub_plot_index=None, colors=('red', 'green')):
    '''

    :param graph:
    :param postion:
    :param visited_order:
    :param step:
    :param sub_plot_index:
    :param colors:
    :return:
    '''
    changed = visited_order[:step] if step is not None else visited_order
    before, after = colors
    color_map = [after if c in changed else before for c in graph]

    nx.draw(graph, postion, node_color=color_map, with_labels=True, ax=sub_plot_index)
    plt.show()


value_graph = {
    'x': ['linear'],
    'k1': ['linear'],
    'b1': ['linear'],
    'linear': ['sigmoid'],
    'sigmoid': ['linear_2'],
    'k2': ['linear_2'],
    'b2': ['linear_2'],
    'linear_2': ['loss']
}


visitor_order = [
    'x',
    'k1',
    'b1',
    'k2',
    'b2',
    'linear',
    'sigmoid',
    'linear_2',
    'loss'
]
graph = nx.DiGraph(value_graph)
layout = nx.layout.spring_layout(graph)
visited_procedure(graph, layout, visitor_order, step=9)


dimension = int(len(visitor_order)**0.5)
fig, ax = plt.subplots(dimension, dimension+1, figsize=(15,15))

for i in range(len(visitor_order) + 1):
    ix = np.unravel_index(i, ax.shape)
    plt.sca(ax[ix])
    ax[ix].title.set_text('Feed Forward Step: {}'.format(i))
    visited_procedure(graph, layout, visitor_order, step=i, sub_plot_index=ax[ix])

# endregion
