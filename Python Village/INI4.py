__author__ = 'Nathen'


# get min and max bounds
a, b = map(lambda i: int(i), input('Nums: ').split(' '))
# create generator of all odd nums
nums = [x for x in range(a, b + 1) if x % 2 == 1]
# sum nums
ans = sum(nums)
# print answer
print(ans)