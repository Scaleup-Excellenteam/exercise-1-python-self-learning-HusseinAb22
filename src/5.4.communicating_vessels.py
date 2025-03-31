def interleave(*iterables):
    """
    Takes multiple iterables and returns a list of their elements interleaved in round-robin order.

    Each element is taken one-by-one from each iterable in sequence.
    Iterables that are exhausted are skipped in the next rounds.
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

    Iterables are processed one item at a time.
    Once an iterable is exhausted, it’s skipped in future rounds.
    Useful for memory-efficient iteration.
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
