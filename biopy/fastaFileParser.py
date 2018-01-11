"""Functions for reading fasta files"""
sequences = dict()

def getSpecSequence(file, id):
    print("File: " + str(file) + " find: " + str(id))
    readFile(file)
    #print(sequences)
    if str(id) in sequences:
        return sequences.get(str(id))
    else:
        return ""

def getAllSequences(file):
    readFile(file)
    return sequences

def readFile(file):
    lastReadedID = ""
    file = open(file)
    for line in file:
        if ">" in line:
            tmpLine = line.split()
            lastReadedID = tmpLine[0][1:]
            sequences[str(lastReadedID)] = ""
        else:
            sequences[str(lastReadedID)] += line.replace('\n', '')