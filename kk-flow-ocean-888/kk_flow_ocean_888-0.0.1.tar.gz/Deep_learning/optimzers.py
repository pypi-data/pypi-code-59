

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


def sgd(graph, learning_rate=1e-2):
    for t in graph:
        if t.is_trainable:
            t.value += -1 * t.gradients[t] * learning_rate
