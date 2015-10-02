__author__ = 'Nathen'

# read and parse integers
a, b = map(lambda s: int(s), input('Enter numbers: ').split(' '))
# compute answer
c = pow(a, 2) + pow(b, 2)
# print answer
print(c)

