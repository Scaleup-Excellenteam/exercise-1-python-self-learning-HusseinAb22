import time


def running_2000(func, *args, **kwargs):
    """
    Measures and returns the execution time (in seconds) of any given function.

    Parameters:
    - func: The function to execute.
    - *args, **kwargs: Arguments and keyword arguments to pass to the function.

    Returns:
    - float: The time taken to execute the function.
    """
    start_time = time.time()
    func(*args, **kwargs)
    return time.time() - start_time


if __name__ == '__main__':
    print(running_2000(zip, [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]))
