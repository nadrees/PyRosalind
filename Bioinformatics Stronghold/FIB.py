import iterables

__author__ = 'Nathen'


def fib(k, start_num):
    n0 = start_num
    yield n0
    n1 = start_num
    yield n1
    while True:
        n2 = (k * n0) + n1
        yield n2
        n0, n1 = n1, n2

n, k = map(lambda num: int(num), input("Paste input: ").split(' '))
count = iterables.nth(fib(k, 1), (n - 1))
print(count)