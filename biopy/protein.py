"""Functions for dealing with proteins."""
AROMA = {
    'Y': 1, 'W':1, 'F':1
}
def aromaticity(seq):
    tmpVal = 0;
    for i in seq:
        if i in AROMA:
            tmpVal += 1
    return round((tmpVal/len(seq))*100, 1)
