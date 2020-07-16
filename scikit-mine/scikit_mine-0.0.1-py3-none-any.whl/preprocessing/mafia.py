"""
MAFIA: A Maximal Frequent Itemset Algorithm for Transactional Databases
"""

from collections import defaultdict

import pandas as pd
from roaringbitmap import RoaringBitmap
from sortedcontainers import SortedDict, SortedSet

from ..base import BaseMiner, DiscovererMixin

import logging

logger = logging.getLogger(__name__)


def dfs(item_to_tids, min_supp, head, head_tids, mfi):
    """
    Depth First Traversal
    Parameters
    ----------
    item_to_tids: SortedDict
        a sorted dictionary, mapping each item to its transaction ids
        in a vertical format
    """
    p = item_to_tids.bisect_right(head[-1])
    tail = item_to_tids.keys()[p:]

    # HUTFMI : check wether {head}U{tail}
    # is frequent for superset pruning
    # see Figure 3 in the original paper
    hut = head + tail
    if frozenset(hut) in mfi:
        return

    node = None

    trimmed_tail = list()
    for e in tail:
        supp = head_tids.intersection_len(item_to_tids[e])

        # PEP : move child from tail to head
        # see Figure 2 in the original paper
        if len(head_tids) == supp:
            head.append(e)

        elif supp >= min_supp:
            trimmed_tail.append((e, supp))


    # dynamic reordering : See figure 5 in the original paper
    trimmed_tail = sorted(trimmed_tail, key=lambda e: e[1])

    for cand, _ in trimmed_tail:
        node = head + [cand]
        tids = head_tids.intersection(item_to_tids[cand])
        dfs(item_to_tids, min_supp, node, tids, mfi)

        if cand == tail[0] and len(trimmed_tail) == len(tail):
            break

    if node is None:
        head = frozenset(head)
        if any((e > head for e in mfi.keys())): return
        mfi[head] = head_tids



class Mafia(BaseMiner, DiscovererMixin):
    def __init__(self, min_supp=.2):
        self.min_supp_ = min_supp
        self.item_to_tids_ = None
        self.mfi_ = None

    def _prefit(self, D):
        d = defaultdict(RoaringBitmap)
        tid = 0

        for t in D:
            for e in t:
                d[e].add(tid)
            tid += 1

        min_supp = self.min_supp_ * tid if isinstance(self.min_supp_, float) else self.min_supp_

        self.item_to_tids_ = SortedDict(
            {k: v for k, v in d.items() if len(v) >= min_supp}
        )

        logger.info(f'keeping track of {len(self.item_to_tids_)} items')

        return self

    def fit(self, D, y=None):
        self._prefit(D)

        mfi = dict()

        for item, tids in self.item_to_tids_.items():
            logger.info(f'eploring item {item}')
            dfs(self.item_to_tids_, self.min_supp_, [item], tids, mfi)

        self.mfi_ = mfi

        return self

    def discover(self):
        s = pd.Series(self.mfi_)
        s.index = s.index.map(tuple)
        return s
