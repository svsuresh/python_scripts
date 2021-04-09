import os
from Bio import SeqIO
from Bio.Seq import Seq
import sys

input_file=sys.argv[1]
window_size=int(sys.argv[2])
step_size=int(sys.argv[3])

records=list(SeqIO.parse(input_file,"fasta"))

for i in records:
    for j in range(0, len(i.seq)-window_size+1):
        print(">"+i.id+"_"+str(j+1)+"_"+str(j+window_size),i.seq[j:j+window_size], sep="\n")
