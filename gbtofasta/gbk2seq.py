#!/usr/bin/env python
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

new_sequences = []
gbinput = str(sys.argv[1])

if len(sys.argv) < 3:
    faout = gbinput.split(".")[0] + ".fasta"
else:
    faout=str(sys.argv[2])

#faout = gbinput.split(".")[0] + ".fasta"

for i in SeqIO.parse(gbinput, "gb"):
    for f in i.features:
        if (f.type == "CDS" and f.qualifiers['gene'] == ['pol']):
            new_sequences.append(SeqRecord(Seq(*(f.qualifiers['translation'])), id="_".join(
                [i.description, *(f.qualifiers['protein_id'])]), description=""))
#            print(">{0}_{1}\n{2}".format(
#                i.description, *(f.qualifiers['protein_id']), *(f.qualifiers['translation'])), #end="\n")
if len(new_sequences) == 0:
    print ("No sequences were converted")
else:
    SeqIO.write(new_sequences, faout, format="fasta")
