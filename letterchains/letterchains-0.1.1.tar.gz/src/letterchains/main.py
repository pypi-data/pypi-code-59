import typing as t
import itertools

import click

T = t.TypeVar("T")


def subwords(word: str) -> t.Iterator[str]:
    """Generate strings excluding each character of given word."""
    for i in range(len(word)):
        yield word[:i] + word[i + 1 :]


def make_adjacency(wordlist: t.Iterable[str]) -> t.Dict:
    """Map each word to its children."""
    wordlist = set(wordlist)
    adjacency: t.Dict[str, t.Set[str]] = {word: set() for word in wordlist}
    for word in wordlist:
        for subword in subwords(word):
            if subword in wordlist:
                adjacency[word].add(subword)

    return adjacency


def identity(x: T) -> T:
    """Return the argument."""
    return x


def maxes(items: t.Iterable[T], key: t.Callable[[T], t.Any] = identity) -> t.List[T]:
    """Return a list of maximal elements."""
    items = list(items)
    if not items:
        raise ValueError(items, "is empty")
    max_value = key(items[0])
    values = []
    for item in items:
        if key(item) == max_value:
            values.append(item)
        elif key(item) > max_value:
            values.clear()
            values.append(item)
            max_value = key(item)

    return values


def longest_paths_from(
    adjacency: t.Dict[str, t.Set[str]], origin: str
) -> t.List[t.List[str]]:
    """Get the list of max-length paths from origin."""
    paths = [[origin]]
    for child in adjacency.get(origin, set()):
        for path in longest_paths_from(adjacency, child):
            paths.append([origin] + path)

    return maxes(paths, key=len)


def longest_paths_from_each_origin(
    wordlist: t.List[str], n: t.Optional[int] = None
) -> t.List[t.List[str]]:
    """Return n longest paths in wordlist."""
    adjacency = make_adjacency(wordlist)
    paths = [longest_paths_from(adjacency, origin) for origin in wordlist]
    return sum(sorted(itertools.islice(paths, n), key=lambda lst: len(lst[0])), [])[:n]


@click.command()
@click.option("-n", type=int, help="Number of chains to generate. Defaults to all.")
def cli(n):
    """Generate letter chains from line-separated wordlist."""
    wordlist = click.get_text_stream("stdin").read().splitlines()
    paths = longest_paths_from_each_origin(wordlist, n)
    print("\n".join(" ".join(path) for path in paths))
