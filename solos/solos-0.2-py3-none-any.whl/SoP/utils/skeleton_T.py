import numpy as np
import random
from math import cos, sin
import torch
from random import randint
from torchtree import Tree


def random_move_numpy(data_numpy,
                      angle_candidate=[-10., -5., 0., 5., 10.],
                      scale_candidate=[0.9, 1.0, 1.1],
                      transform_candidate=[-0.2, -0.1, 0.0, 0.1, 0.2],
                      move_time_candidate=[1]):
    # CREDITS TO https://github.com/open-mmlab/mmskeleton
    # Apache 2 license
    # input: C,T,V,M
    C, T, V, M = data_numpy.shape
    move_time = random.choice(move_time_candidate)
    node = np.arange(0, T, T * 1.0 / move_time).round().astype(int)
    node = np.append(node, T)
    num_node = len(node)

    A = np.random.choice(angle_candidate, num_node)
    S = np.random.choice(scale_candidate, num_node)
    T_x = np.random.choice(transform_candidate, num_node)
    T_y = np.random.choice(transform_candidate, num_node)

    a = np.zeros(T)
    s = np.zeros(T)
    t_x = np.zeros(T)
    t_y = np.zeros(T)

    # linspace
    for i in range(num_node - 1):
        a[node[i]:node[i + 1]] = np.linspace(
            A[i], A[i + 1], node[i + 1] - node[i]) * np.pi / 180
        s[node[i]:node[i + 1]] = np.linspace(S[i], S[i + 1],
                                             node[i + 1] - node[i])
        t_x[node[i]:node[i + 1]] = np.linspace(T_x[i], T_x[i + 1],
                                               node[i + 1] - node[i])
        t_y[node[i]:node[i + 1]] = np.linspace(T_y[i], T_y[i + 1],
                                               node[i + 1] - node[i])

    theta = np.array([[np.cos(a) * s, -np.sin(a) * s],
                      [np.sin(a) * s, np.cos(a) * s]])

    # perform transformation
    for i_frame in range(T):
        xy = data_numpy[0:2, i_frame, :, :]
        new_xy = np.dot(theta[:, :, i_frame], xy.reshape(2, -1))
        new_xy[0] += t_x[i_frame]
        new_xy[1] += t_y[i_frame]
        data_numpy[0:2, i_frame, :, :] = new_xy.reshape(2, V, M)

    return data_numpy


def random_move(data_numpy, prob):
    if random.random() < prob:
        if torch.is_tensor(data_numpy):
            return torch.from_numpy(random_move_numpy(data_numpy.numpy()))
        else:
            return random_move_numpy(data_numpy)
    else:
        return data_numpy


def random_move_numpy(data_numpy,
                      angle_candidate=[-10., -5., 0., 5., 10.],
                      scale_candidate=[0.9, 1.0, 1.1],
                      transform_candidate=[-0.2, -0.1, 0.0, 0.1, 0.2],
                      move_time_candidate=[1]):
    # CREDITS TO https://github.com/open-mmlab/mmskeleton
    # Apache 2 license
    # input: C,T,V,M
    C, T, V, M = data_numpy.shape
    move_time = random.choice(move_time_candidate)
    node = np.arange(0, T, T * 1.0 / move_time).round().astype(int)
    node = np.append(node, T)
    num_node = len(node)

    A = np.random.choice(angle_candidate, num_node)
    S = np.random.choice(scale_candidate, num_node)
    T_x = np.random.choice(transform_candidate, num_node)
    T_y = np.random.choice(transform_candidate, num_node)

    a = np.zeros(T)
    s = np.zeros(T)
    t_x = np.zeros(T)
    t_y = np.zeros(T)

    # linspace
    for i in range(num_node - 1):
        a[node[i]:node[i + 1]] = np.linspace(
            A[i], A[i + 1], node[i + 1] - node[i]) * np.pi / 180
        s[node[i]:node[i + 1]] = np.linspace(S[i], S[i + 1],
                                             node[i + 1] - node[i])
        t_x[node[i]:node[i + 1]] = np.linspace(T_x[i], T_x[i + 1],
                                               node[i + 1] - node[i])
        t_y[node[i]:node[i + 1]] = np.linspace(T_y[i], T_y[i + 1],
                                               node[i + 1] - node[i])

    theta = np.array([[np.cos(a) * s, -np.sin(a) * s],
                      [np.sin(a) * s, np.cos(a) * s]])

    # perform transformation
    for i_frame in range(T):
        xy = data_numpy[0:2, i_frame, :, :]
        new_xy = np.dot(theta[:, :, i_frame], xy.reshape(2, -1))
        new_xy[0] += t_x[i_frame]
        new_xy[1] += t_y[i_frame]
        data_numpy[0:2, i_frame, :, :] = new_xy.reshape(2, V, M).astype(np.float32)

    return data_numpy


def random_move_pytorch(data_numpy,
                        angle_candidate=[-10., -5., 0., 5., 10.],
                        scale_candidate=[0.9, 1.0, 1.1],
                        transform_candidate=[-0.2, -0.1, 0.0, 0.1, 0.2],
                        move_time_candidate=[1]):
    # CREDITS TO https://github.com/open-mmlab/mmskeleton
    # Apache 2 license
    # input: C,T,V,M
    C, T, V, M = data_numpy.shape
    move_time = random.choice(move_time_candidate)
    node = torch.arange(start=0, end=T, step=T * 1.0 / move_time).round().int()
    node = torch.cat([node, torch.tensor([T]).int()])
    num_node = len(node)

    A = torch.from_numpy(np.random.choice(angle_candidate, num_node))
    S = torch.from_numpy(np.random.choice(scale_candidate, num_node))
    T_x = torch.from_numpy(np.random.choice(transform_candidate, num_node))
    T_y = torch.from_numpy(np.random.choice(transform_candidate, num_node))

    a = torch.zeros(T)
    s = torch.zeros(T)
    t_x = torch.zeros(T)
    t_y = torch.zeros(T)

    # linspace
    for i in range(num_node - 1):
        a[node[i]:node[i + 1]] = torch.linspace(
            A[i], A[i + 1], node[i + 1] - node[i]) * np.pi / 180
        s[node[i]:node[i + 1]] = torch.linspace(S[i], S[i + 1],
                                                node[i + 1] - node[i])
        t_x[node[i]:node[i + 1]] = torch.linspace(T_x[i], T_x[i + 1],
                                                  node[i + 1] - node[i])
        t_y[node[i]:node[i + 1]] = torch.linspace(T_y[i], T_y[i + 1],
                                                  node[i + 1] - node[i])

    theta = torch.tensor([[torch.cos(a) * s, -torch.sin(a) * s],
                          [torch.sin(a) * s, torch.cos(a) * s]])

    # perform transformation
    for i_frame in range(T):
        xy = data_numpy[0:2, i_frame, :, :]
        new_xy = torch.dot(theta[:, :, i_frame], xy.view(2, -1))
        new_xy[0] += t_x[i_frame]
        new_xy[1] += t_y[i_frame]
        data_numpy[0:2, i_frame, :, :] = new_xy.view(2, V, M)

    return data_numpy


def rotation(data_numpy, angle):
    # Input T,Poeple,[XYC],Joints
    # Rotation Matrix
    if torch.is_tensor(data_numpy):
        R = torch.tensor([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]).to(data_numpy.device)
        rot = torch.einsum('...cj,lc->...lj', data_numpy[..., :2, :], R)
        data_numpy[..., :2, :] = rot
    else:
        R = np.array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])

        rot = np.einsum('...cj,lc->...lj', data_numpy[..., :2, :], R)
        data_numpy[..., :2, :] = rot
    return data_numpy


def random_rotation(data_numpy, angle_range=(0, 10)):
    angle = random.randint(*angle_range)
    return rotation(data_numpy, angle)


def scaling(data_numpy, scale):
    # Input T,Poeple,[XYC],Joints
    data_numpy[..., :2, :] *= scale
    return data_numpy


def random_scaling(data_numpy):
    return scaling(data_numpy, randint(8, 12) / 10.)


def box_normalization(data_numpy):
    def rescale_numpy(x, max_range, min_range):
        max_val = np.max(x)
        min_val = np.min(x)
        return (max_range - min_range) / (max_val - min_val) * (x - max_val) + max_range

    def rescale_pytorch(x, max_range, min_range):
        max_val = x.max()
        min_val = x.min()

        return (max_range - min_range) / (max_val - min_val) * (x - max_val) + max_range

    def rescale(x):
        if torch.is_tensor(x):
            return rescale_pytorch(x, 20, 10)
        else:
            return rescale_numpy(x, 20, 10)

    # Input T,Poeple,[XYC],Joints
    data_numpy[..., :2, :][data_numpy[..., :2, :] != 0] = rescale(data_numpy[..., :2, :][data_numpy[..., :2, :] != 0])

    return data_numpy


def absolute_mean_padding(data_numpy):
    coords = data_numpy[:, :2, :]
    mask = data_numpy[:, 2, :].unsqueeze(1).expand_as(coords) == 0  # 25,2,J
    mean = coords.new_zeros(2, data_numpy.size(-1))
    for c in range(2):
        for j in range(data_numpy.size(-1)):
            mean[c, j] = data_numpy[:, c, j][~mask[:, c, j]].mean()
    mean[torch.isnan(mean)] = 0
    for i in range(data_numpy.size(0)):
        mask_i = mask[i]
        coords[i][mask_i] = mean[mask_i]
    data_numpy[:, :2, :] = coords
    return data_numpy


class Graph(object):
    def __init__(self, graph):
        self.graph = sorted([sorted(x) for x in graph])
        self.tree = Tree()
        self.build_tree(self.tree, 0)

    def iter_graph(self, c):
        triggered = False
        for edge in self.graph:
            if edge[0] == c and edge[1] != c:
                triggered = True
                yield edge
        if not triggered:
            yield (c, None)

    def build_tree(self, tree, c):
        for edge in self.iter_graph(c):
            x, y = str(edge[0]), edge[1]
            if y is None:
                tree.add_module(x, Tree())
            else:
                if x not in tree._modules and int(x) != y:

                    new_tree = Tree()
                    tree.add_module(x, new_tree)
                    self.build_tree(new_tree, y)
                else:
                    self.build_tree(new_tree, y)

    def get_ordered_graph(self):
        x = []
        self.iter_ordered_graph(self.tree, -1, x)
        del x[0]
        return x

    def iter_ordered_graph(self, tree, prev, lista):
        for el, mod in self.iter_children(tree, prev):
            lista.append(el)
            self.iter_ordered_graph(mod, el[1], lista)

    def iter_children(self, tree, prev):
        for name, mod in tree.named_children():
            yield (prev, int(name)), mod


class RelMeanPadding(object):
    def __init__(self, graph):
        self.graph = Graph(graph).get_ordered_graph()

    def __call__(self, data_numpy):
        coords = data_numpy[:, :2, :]
        mask = data_numpy[:, 2, :].unsqueeze(1).expand_as(coords) == 0  # 25,2,J
        abs_mean = coords.new_zeros(2, data_numpy.size(-1))
        for c in range(2):
            for j in range(data_numpy.size(-1)):
                abs_mean[c, j] = data_numpy[:, c, j][~mask[:, c, j]].mean()
        # abs_mean[torch.isnan(abs_mean)] = 0
        if torch.is_tensor(data_numpy):
            rel_mean = abs_mean.clone()
        else:
            rel_mean = abs_mean.copy()
        for m, n in self.graph:
            rel_mean[:, :2, m] -= abs_mean[:, :2, n]


def rel_normalization(data_numpy, j=0):
    if torch.is_tensor(j):
        disp = j
    else:
        if torch.is_tensor(data_numpy):
            disp = data_numpy[:, :2, j, None].clone()
        else:
            disp = data_numpy[:, :2, j, None].copy()
    data_numpy[:, :2, :] -= disp
    return data_numpy


def diferencies(data_numpy):
    # Input T,[XYC],Joints
    data_numpy_t = data_numpy[:24, ...]
    data_numpy_t1 = data_numpy[1:25, ...]

    if torch.is_tensor(data_numpy):
        coef = torch.stack([data_numpy_t, data_numpy_t1])[..., 2, :].min(dim=0)[0]
    else:
        coef = np.stack([data_numpy_t, data_numpy_t1])[..., 2, :].min(axis=0)
    dif = data_numpy_t1 - data_numpy_t
    dif[..., 2, :] = coef
    return dif


def impose_positive_numbers(data_numpy, min_space=15):
    # Input T,Poeple,[XYC],Joints
    X_min = data_numpy[..., 0, :].min()
    Y_min = data_numpy[..., 1, :].min()

    if X_min < 0:
        data_numpy[..., 0, :][data_numpy[..., 0, :] != 0] += abs(X_min) + min_space
    if Y_min < 0:
        data_numpy[..., 1, :][data_numpy[..., 1, :] != 0] += abs(Y_min) + min_space

    return data_numpy


def random_displacement(data_numpy, x_range, y_range):
    data_numpy[..., 0, :][data_numpy[..., 0, :] != 0] += random.randint(*x_range)
    data_numpy[..., 1, :][data_numpy[..., 1, :] != 0] += random.randint(*y_range)
    return data_numpy


def openpose25toopenpose18(data_numpy):
    if torch.is_tensor(data_numpy):
        new_data = torch.zeros(25, 3, 18)
    else:
        new_data = np.zeros((25, 3, 18))
    new_data[..., :8] = data_numpy[..., :8]
    new_data[..., 8:13] = data_numpy[..., 9:14]
    new_data[..., 14:17] = data_numpy[..., 15:18]
    return new_data


def openpose25toupperbody(data_numpy):
    if torch.is_tensor(data_numpy):
        new_data = torch.zeros(25, 3, 7)
    else:
        new_data = np.zeros((25, 3, 7))
    new_data[..., 0] = data_numpy[..., 1]
    new_data[..., 1:] = data_numpy[..., 2:8]
    return new_data


def openpose65toopenpose58(data_numpy):
    if torch.is_tensor(data_numpy):
        new_data = torch.zeros(25, 3, 58)
    else:
        new_data = np.zeros((25, 3, 58))
    new_data[..., :8] = data_numpy[..., :8]
    new_data[..., 8:13] = data_numpy[..., 9:14]
    new_data[..., 14:17] = data_numpy[..., 15:18]
    new_data[..., 18:] = data_numpy[..., :25]
    return new_data


def horizontal_flip(data_numpy, p=0.5):
    if random.random() < p:
        if torch.is_tensor(data_numpy):
            new_data = data_numpy.clone()
        else:
            new_data = data_numpy.copy()
        new_data[..., 1:4] = data_numpy[..., 4:7]
        new_data[..., 4:7] = data_numpy[..., 1:4]
        new_data[..., 7:27] = data_numpy[..., 7 + 20:7 + 20 * 2]
        new_data[..., 7 + 20:7 + 20 * 2] = data_numpy[..., 7:27]
        return new_data
    else:
        return data_numpy
