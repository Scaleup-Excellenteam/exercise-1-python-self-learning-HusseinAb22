def cup_of_join(*matrix, sep=None):
    """
    This function takes one or more lists as input and flattens them into a single list.
    If a separator is provided, it is added after each inner list.
    If no lists are given, the function returns None.
    """
    if not matrix:
        return None
    #
    cup = []

    for num_list in matrix:
        for num in num_list:
            cup.append(num)
        if sep:
            cup.append(sep)

    return cup


if __name__ == '__main__':
    print(cup_of_join([9, 5, 6], sep='@'))
