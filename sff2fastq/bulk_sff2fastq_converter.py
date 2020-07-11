#! /usr/bin/env python

import os
import glob
from Bio import SeqIO
from datetime import date
import sys

Raw_path = sys.argv[1]
Input_format = sys.argv[2]

if not os.path.exists(Raw_path):
    print(Raw_path + " doesn't exist")

files = glob.glob(Raw_path + "/" + '*.sff')

if len(files) == 0:
    print("no files are uploaded")
elif len(files) == 1:
    print("1 file is read")
else:
    print(len(files, " are read"))


if not os.path.isdir(Raw_path + "/" + "fastq_" + str(date.today())):
    os.mkdir(Raw_path + "/" + "fastq_" + str(date.today()))


for i in files:
    record = SeqIO.parse(i, Input_format)
    print("converting", i, "to fastq")
    SeqIO.write(record, Raw_path + "/" + "fastq_" + str(date.today()) + "/" + os.path.splitext(os.path.basename(i))[0] + ".fastq", "fastq-illumina")
    print(Raw_path + "/" + "fastq_" + str(date.today()) + "/" + os.path.splitext(os.path.basename(i))[0] + ".fastq created")
