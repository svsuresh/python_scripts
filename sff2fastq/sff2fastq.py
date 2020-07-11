from Bio import SeqIO
import sys
from pathlib import Path

sff_file = Path(sys.argv[1])

records = SeqIO.parse(sff_file, "sff")
count = SeqIO.write(records, sff_file.with_suffix(".fastq"), "fastq-illumina")
