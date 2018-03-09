from biopy import protein as prot
from biopy import dna as dna
from biopy import fastaFileParser as parser
import operator
#print("#gene_id    aromaticity")
#print(prot.aromaticity(dna.translate(parser.getSpecSequence('raw.txt', 'CCU60975'))))

#stats = dna.gc_content(parser.getAllSequences('test.txt'))
#print(max(stats, key=stats.get) + ' : ' + str(stats[str(max(stats, key=stats.get))]))

#print(prot.calculateInterffering("MA") % 1000000)

####

#TCCGGGATC

parser.read_multi_fasta('genbank.txt')