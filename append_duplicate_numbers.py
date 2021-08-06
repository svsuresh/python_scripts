#! /usr/bin/env python3
import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys

input=sys.argv[1]
output=sys.argv[2]

rpid=""
num=1
new_seq=[]

for record in SeqIO.parse(input, "fasta"):
    if record.id == rpid:
        new_num+=num
    else:
        new_num=num
    newrecord_id='{0}#{1}'.format(record.id,new_num)
    new_seq.append(SeqRecord(record.seq,newrecord_id, description=""))
    rpid=record.id
SeqIO.write(new_seq, output, format="fasta")


