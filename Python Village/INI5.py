__author__ = 'Nathen'


file_name = input('File path: ')
with open(file_name, 'r') as f:
    file_lines = f.readlines()
    # generate 1-based indexes
    indexes = map(lambda i: i+1, range(len(file_lines)))
    # zip lines with 1-based indexes
    tuples = zip(indexes, file_lines)
    # choose lines with even-numbered indexes
    lines = [line.rstrip() for index, line in tuples if index % 2 == 0]
    # recombine lines and print to file
    with open('out.txt', 'w') as fout:
        print(*lines, sep='\n', file=fout)
