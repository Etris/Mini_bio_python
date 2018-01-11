import math
"""Functions for dealing with DNA sequences."""

CODONS = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}

MASS = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694,
    'E': 129.04259, 'F': 147.06841, 'G': 57.02146,
    'H': 137.05891, 'I': 113.08406, 'K': 128.09496,
    'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
    'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
    'S': 87.03203, 'T': 101.04768, 'V': 99.06841,
    'W': 186.07931, 'Y': 163.06333
}
def complement(seq):
    """Return the complement DNA sequence."""
    d = {'A': 'T', 'C': 'G', 'G': 'C', 'T':'A'}
    return "".join([d.get(nt, 'N') for nt in seq])

def reverse_complement(seq):
    """Return the reverse complement DNA sequence."""
    return complement(seq[::-1])

def translate(seq, frame = 1):
    if(frame < 0):
        seq = reverse_complement(seq)
        frame = abs(frame)
    tmpSeq = ""
    for i in range(int(frame - 1), len(seq), 3):
        if CODONS.get(str(seq[int(i): int(i+3)])):
            tmpSeq += CODONS.get(str(seq[int(i): int(i+3)]))
    return tmpSeq

def countNucleos(seq):
    temp = dict({'A': 0, 'C': 0,  'G': 0, 'T': 0})
    for el in seq.replace('\n', ''):
        temp[str(el)] += 1
    return temp

def DNAtoRNA(seq):
    temp = ""
    for el in seq:
        if el == 'T':
            temp += 'U'
        else:
            temp += el
    return temp

def RNAtoDNA(seq):
    temp = ""
    for el in seq:
        if el == 'U':
            temp += 'T'
        else:
            temp += el
    return temp

def gc_content_count(seq):
    temp = 0
    for el in seq.upper():
        if el == 'G' or el == 'C':
            temp += 1
    return temp

def gc_content(tmpDict):
    returnDict = dict()
    for key in tmpDict.keys():
        returnDict[key] = (round((gc_content_count(tmpDict[key]) / len(tmpDict[key]) * 100), 6))
    return returnDict

def hammingDistance(first, second):
    temp = 0
    for i in range (0, len(first), 1):
        if first[i] != second[i]:
            temp += 1
    return temp

def calc_mass(seq):
    temp = 0
    for el in seq:
        temp += MASS[el]
    return round(temp, 3)