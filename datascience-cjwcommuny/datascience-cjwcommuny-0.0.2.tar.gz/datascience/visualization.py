from collections import Counter
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from typing import List, Tuple, Dict, Optional, Callable, Union, Any, Set


def draw_bar_graph(distribution, title: str, longgest_bar: int=50):
    """
    visualize bar graph in console
    example:
    >>> x = [1,2,3,1,1,2,5,6,6,0,9,0]
    >>> draw_bar_graph(x, title="test", longgest_bar=20)
    test:
    0: ▇▇▇▇▇▇▇▇▇▇▇▇▇ 2
    1: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 3
    2: ▇▇▇▇▇▇▇▇▇▇▇▇▇ 2
    3: ▇▇▇▇▇▇▇ 1
    5: ▇▇▇▇▇▇▇ 1
    6: ▇▇▇▇▇▇▇▇▇▇▇▇▇ 2
    9: ▇▇▇▇▇▇▇ 1
    """
    histogram = Counter()
    histogram.update(distribution)
    largest_count = histogram.most_common(1)[0][1]
    histogram_sorted = sorted(histogram.items())
    largest_key = histogram_sorted[-1][0]
    key_width = len(str(largest_key))
    print("{}:".format(title))
    for key, count in histogram_sorted:
        key_format_str = "%%%dd: " % key_width
        print(key_format_str % key, end="")
        bar_count = round(count * longgest_bar / largest_count)
        for _ in range(bar_count):
            print("▇", end="")
        print(" {}".format(count))


def visualize_2d_array_heap_map(array: np.narray, dump_path: Optional[str]):
    """
    if dump_path is None, then display image, else dump image to `dump_path`
    :param array: dim() == 2
    :param dump_path:
    """
    assert isinstance(array, np.ndarray)
    assert array.ndim == 2

    sns.set()
    ax = sns.heatmap(array)
    if dump_path is None:
        plt.show()
    else:
        plt.savefig(dump_path)
