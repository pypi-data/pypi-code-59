from typing import List


def format_column_name(levels: List[str]) -> str:
    """Take a Monocl multi-index and squash it down to a single-index."""
    prefix, level2, *_ = levels
    suffix = '' if 'Unnamed' in level2 else ' ' + level2
    return (prefix + suffix).replace('\n', ' ')
