import os
from Bio import SeqIO
import sys

input_fa=sys.argv[1]
input_function=sys.argv[2]
seqs = list(SeqIO.parse(input_fa, "fasta"))
seqs_dict = {}
input = str(input_function)

if input == "reverse":
    for i in seqs:
        seqs_dict[i.id] = i.seq[::-1]
elif input == "reverse_complement":
    for i in seqs:
        seqs_dict[i.id] = i.seq.reverse_complement()
elif input == "complement":
    for i in seqs:
        seqs_dict[i.id] = i.seq.complement()
elif input == "count":
    for i in seqs:
        seqs_dict[i.id] = len(i.seq)
elif input == "transcribe":
    for i in seqs:
        seqs_dict[i.id] = i.seq.transcribe()
elif input == "translate":
    for i in seqs:
        seqs_dict[i.id] = i.seq.translate()

# seqs_dict={i.id:i.seq.translate() for  i in seqs if input == "translate"}

for k, v in seqs_dict.items():
    print('>{}\n{}'.format(k, v))
