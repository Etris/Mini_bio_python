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


def read_multi_fasta(file_name):
    file_handler = open(file_name)
    main_list = list()
    tmp_list = list()
    read_sequence = False
    for line in file_handler:
        first = line.strip()
        if len(line.split()) > 0:
            first = line.strip().split()[0]
        if 'DEFINITION' in first:
            #print('#0' + " Size: " + str(len(tmp_list)))
            tmp_list.append(line.strip().split()[1].strip().rstrip('.'))
        if 'ACCESSION' in first:
            #print('#1 ' + "Size: " + str(len(tmp_list)))
            tmp_list.append(line.strip()[len(first):len(line)].strip().rstrip('.'))
        if 'SOURCE' in first and 'DBSOURCE' not in first:
            #print('#2 ' + "Size: " + str(len(tmp_list)))
            tmp_list.append(line.strip()[len(first):len(line)].strip().rstrip('.'))
        if 'ORIGIN' in first:
            #print('#3: ' + "Size: " + str(len(tmp_list)))
            read_sequence = True
            tmp_list.append(' ')
            continue
        if '//' in first:
            read_sequence = False
            main_list.append(tmp_list.copy())
            tmp_list.clear()
            print("Size of main: " + str(len(main_list)))
            print(tmp_list)
        if read_sequence == True:
            tmp_list[3] += ''.join([i for i in line if not i.isdigit()]).strip()
    for element in main_list:
        element[3] = element[3].replace(" ", "").upper()
        tmp_str = ""
        for i in range(0, len(element[3]), 60):
            tmp_str += element[3][i:i+60]
            tmp_str += '\n'
        element[3] = tmp_str
        print(element[3])
    file_handler_new = open(file_name[0:-4]+".fasta", 'w')
    for element in main_list:
        combine_str = ">" + element[0] + "|" + element[1] + "|" + element[2] + "\n"
        combine_str += element[3] + "\n"
        file_handler_new.write(combine_str)