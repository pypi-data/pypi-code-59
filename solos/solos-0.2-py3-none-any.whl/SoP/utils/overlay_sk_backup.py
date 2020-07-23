import cv2
import torch
import numpy as np
from torchtree import Tree

class Skeleton_Plotter(object):
    def __init__(self, graph, th=0.05):
        self.th = th
        self.graph = graph

    @property
    def img(self):
        if torch.is_tensor(self._img):
            return self._img.clone()
        else:
            return self._img.copy()

    @img.setter
    def img(self, img):
        self._img = img

    def _set_sk(self, skeleton):
        self.img, self.X_disp, self.Y_disp = define_img(skeleton)
        self.skeleton = skeleton
        self.skeleton[:, 0, :] += self.X_disp
        self.skeleton[:, 1, :] += self.Y_disp

        return skeleton

    def __len__(self):
        return len(self.skeleton)

    def __call__(self, skeleton):
        self._set_sk(skeleton)
        wd = self.plot(self.th)
        wd.main()
        return skeleton

    def as_image(self, frame, th):
        return plot(self.skeleton[frame, ..., :], self.img, self.graph, th)

    def as_video(self, th):
        return [self.as_image(idx, th) for idx in range(len(self.skeleton))]

    def plot(self, th):
        return Window(self, 'Image', th)


def overlay_sk(img, tensor, graph, th):
    colorcode = (255, 0, 255)
    RED = (0, 0, 255)
    BLUE = (255, 0, 0)
    miss_colorcode = (0, 255, 0)
    for edge in graph:
        j0, j1 = edge
        x0, y0, c0 = tensor[:, j0]
        x1, y1, c1 = tensor[:, j1]
        c = min(c0, c1).item()
        if th == 0 and c == 0:
            cv2.line(img, (x0, y0), (x1, y1), miss_colorcode, 4)
        elif c >= th:
            colorcode = (round(255 * (1 - c)), 0, round(255 * c))
            cv2.line(img, (x0, y0), (x1, y1), colorcode, 4)

    return img


def define_img(tensor):
    X_max = int(tensor.max(dim=0)[0].max().item())
    Y_max = int(tensor.max(dim=1)[0].max().item())
    X_min = int(tensor.min(dim=0)[0].min().item())
    Y_min = int(tensor.min(dim=1)[0].min().item())

    print('Image range (x,y): (%d,%d) to (%d,%d)' % (X_min, Y_min, X_max, Y_max))

    X_disp, Y_disp = 0, 0
    if X_min < 0:
        X_disp += int(abs(X_min) * 1.1)
    if Y_min < 0:
        Y_disp += int(abs(Y_min) * 1.1)
    print('Image range (x,y): (%d,%d) to (%d,%d)' % (X_min + X_disp, Y_min + Y_disp, X_max + X_disp, Y_max + Y_disp))

    img = np.zeros((int(1.2 * (X_max + X_disp)), int(1.2 * (Y_max + Y_disp)), 3), dtype=np.uint8) + 255
    return img, X_disp, Y_disp


def plot(tensor, img, graph, th=0.2):
    img = overlay_sk(img, tensor, graph, th)
    return img


class Window():
    def __init__(self, flow, name, th):
        self.flow = flow
        self.name = name
        self.N = len(self.flow)
        self.idx = 0
        self.th = th
        self._reset()
        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        # keep looping until the 'q' key is pressed

    def main(self):
        self._reset()
        while True:
            # display the image and wait for a keypress
            cv2.imshow(self.name, self.image)
            key = cv2.waitKey(1) & 0xFF
            # if the 'r' key is pressed, reset the cropping region
            flag = self.run_key(key)
            if flag.all() == self.key2mask(ord('q')).all():
                break
        cv2.destroyAllWindows()
        return self.flow

    def key2mask(self, key):
        ascii_ = ord('a')
        tmp = np.zeros(25, dtype=bool)
        tmp[key - ascii_] = True
        return tmp

    def run_key(self, key):
        if key == ord('r') and self.allow_key(key):
            self._reset()
        # if the 'c' key is pressed, break from the loop
        elif key == ord('q') and self.allow_key(key):
            return self.key2mask(key)
        elif key == ord('a') and self.allow_key(key):
            self.overflow_idx(-1)
            self.display(self.idx)
        elif key == ord('s') and self.allow_key(key):
            self.overflow_idx(+1)
            self.display(self.idx)
        elif key == ord('l') and self.allow_key(key):
            speed = 125
            pause = False
            while True:
                cv2.imshow(self.name, self.image)
                if not pause:
                    self.overflow_idx(1)
                    self.display(self.idx)
                key = cv2.waitKey(int(speed)) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('a'):
                    speed *= 1.1
                elif key == ord('s'):
                    speed *= 0.9
                elif key == ord('p'):
                    pause = not pause

        return np.ones(25, dtype=bool)

    def overflow_idx(self, i):
        idx_ = self.idx + i
        if idx_ >= self.N:
            self.idx = 0
        elif idx_ < 0:
            self.idx = self.N - 1
        else:
            self.idx += i

    def allow_key(self, key):
        k = self.key2mask(key)
        return k.all() == (k.all() and self.state.all()).all()

    def _reset_state(self):
        self.state = np.ones(25, dtype=bool)

    def _reset(self):
        self.refPt = []
        self.cropping = False
        self.idx = 0
        self.display(self.idx)
        self._reset_state()

    def display(self, idx):
        self.image = self.flow.as_image(idx, self.th)
        self.clone = self.flow.as_image(idx, self.th)

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
        return tuple(x)

    def iter_ordered_graph(self, tree, prev, lista):
        for el, mod in self.iter_children(tree, prev):
            lista.append(el)
            self.iter_ordered_graph(mod, el[1], lista)

    def iter_children(self, tree, prev):
        for name, mod in tree.named_children():
            yield (prev, int(name)), mod