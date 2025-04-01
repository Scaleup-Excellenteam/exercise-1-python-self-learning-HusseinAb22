"""
Provides two functions to interleave multiple iterables in a round-robin fashion.

- `interleave`: Returns a list of elements from all iterables interleaved together.
- `generator_interleave`: Yields elements from all iterables interleaved one by one.
"""


def interleave(*iterables):
    """
    Returns a list of elements taken in round-robin order from the given iterables.
    Args:
        *iterables: Any number of iterable objects.
    Returns:
        list: A list containing elements interleaved from the input iterables.

    """
    iterators = [iter(it) for it in iterables]
    result = []
    while iterators:
        next_round = []
        for it in iterators:
            try:
                result.append(next(it))
                next_round.append(it)
            except StopIteration:
                continue
        iterators = next_round
    return result


def generator_interleave(*iterables):
    """
    A generator version of `interleave` that yields elements in round-robin order from multiple iterables.
    Args:
        *iterables: Any number of iterable objects.
    Yields:
        Elements from the input iterables interleaved in round-robin order.

    """
    iterators = [iter(it) for it in iterables]
    while iterators:
        next_round = []
        for it in iterators:
            try:
                yield next(it)
                next_round.append(it)
            except StopIteration:
                continue
        iterators = next_round


if __name__ == '__main__':
    lst = list(interleave('ab', [1, 2, 3], ('!', '@')))
    print(lst)
