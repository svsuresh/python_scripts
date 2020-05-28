# import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
# from Bio.Seq import Seq


_Sequences = []

# For writing nucleotide sequences
for rec in SeqIO.parse("test.gb", "genbank"):
    #    print(rec.seq)
    #    print(rec.features[2])
    #    print(rec.features[2].location)
    id = "{}:{}{}".format(rec.id, rec.features[2].location, rec.description)
    sequence = SeqRecord(rec.seq, id=id, description="")
    _Sequences.append(sequence)


# For writing protein sequence with custom header
#        if feature.type == "CDS":
#            seq = Seq(*feature.qualifiers["translation"])
#            id = "{}:{} {}".format(rec.id, feature.location, rec.description)

SeqIO.write(_Sequences, "test.fa", 'fasta')
