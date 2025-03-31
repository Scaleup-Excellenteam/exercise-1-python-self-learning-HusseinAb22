def group_by(func, iterable):
    """
    Groups elements of an iterable based on the result of a given function.

    Parameters:
    - func: A function to classify each item (e.g., len, str.lower).
    - iterable: A list or other iterable of values to group.

    Returns:
    - dict: A dictionary where each key is a result of `func`, and the value is a list of items matching that result.
    """
    result = {func(value): [word for word in iterable if func(word) == func(value)] for value in iterable}
    print(result)
    return result


if __name__ == '__main__':
    group_by(len, ["hi", "bye", "yo", "try"])