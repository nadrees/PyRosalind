__author__ = 'Nathen'


def dna_to_rna(dna_str):
    """
    Translates the dna string to an rna string by replacing all instances of T with U
    :param dna_str: The dna string to translate
    :return: an rna string with all instances of T replaced with U
    """
    return dna_str.replace('T', 'U')
