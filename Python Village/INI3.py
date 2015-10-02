__author__ = 'Nathen'


def parse_file(file_name):
    with open(file_name, 'r') as f:
        s, nums = f.readlines()
        a, b, c, d = map(
            lambda i: int(i),
            nums.split(' '))
        return s, a, b, c, d

# parse file contents
s, a, b, c, d = parse_file(input('File path: '))
# calculate substrs
sub1 = s[a:b + 1]
sub2 = s[c:d + 1]
# print substrs
print(sub1, sub2, sep=' ')
