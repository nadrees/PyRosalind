__author__ = 'Nathen'


def reverse_compliment(dna_str):
    """
    :param dna_str: The DNA string to reverse and compliment
    :return: The reverse compliment of the DNA string
    """
    def compliment(dna_char):
        if dna_char == 'A':
            return 'T'
        elif dna_char == 'T':
            return 'A'
        elif dna_char == 'C':
            return 'G'
        elif dna_char == 'G':
            return 'C'

    return [compliment(c) for c in dna_str[::-1]]
