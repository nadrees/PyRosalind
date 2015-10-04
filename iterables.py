from itertools import islice

__author__ = 'Nathen'


def nth(iterable, n, default=None):
    """
    Returns the nth item or a default value
    :param iterable: The iterable to retrieve the item from
    :param n: index of the item to retrieve. Must be >= 0
    :param default: the value to return if the index isn't valid
    :return: the nth item, or the default value if n isn't a valid index
    """
    return next(islice(iterable, n, None), default)
