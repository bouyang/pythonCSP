def DNA_strand(dna):
    comp = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join([comp.get(base) for base in dna])