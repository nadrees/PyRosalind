__author__ = 'Nathen'


string = input('Paste DNA String: ')

counts = {}
for letter in string:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

print(counts['A'], counts['C'], counts['G'], counts['T'])
