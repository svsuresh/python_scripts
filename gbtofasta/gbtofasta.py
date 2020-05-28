# import os
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


_NTSequences = []
_AASequences = []

# For writing nucleotide sequences
for rec in SeqIO.parse("test.gb", "genbank"):
    id = "{}:{}{}".format(rec.id, rec.features[2].location, rec.description)
    sequence = SeqRecord(rec.seq, id=id, description="")
    _NTSequences.append(sequence)
    for feature in rec.features:
        if feature.type == "CDS":
            aaseq = Seq(*feature.qualifiers["translation"])
            aaid = "{}:{} {}".format(rec.id, feature.location, rec.description)
            aasequence = SeqRecord(aaseq, id=aaid, description="")
            _AASequences.append(aasequence)


SeqIO.write(_NTSequences, "testNT.fa", 'fasta')
SeqIO.write(_AASequences, "testAA.fa", 'fasta')
