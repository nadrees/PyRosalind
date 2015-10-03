from bio.dna import reverse_compliment

__author__ = 'Nathen'


dna_str = input('Paste DNA String: ')
ans = reverse_compliment(dna_str)
print(*ans, sep='')
