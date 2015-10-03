from bio.conversions import dna_to_rna

__author__ = 'Nathen'


dna_str = input('Paste DNA String: ')
rna_str = dna_to_rna(dna_str)
print(rna_str)
