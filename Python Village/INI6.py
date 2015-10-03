__author__ = 'Nathen'


string = input('Input string: ')

d = {}
for word in string.split(' '):
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for key, value in d.items():
    print(key, value)
