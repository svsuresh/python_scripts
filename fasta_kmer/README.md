Script extracts the motifs of user defined size, with user defined window, from user defined fasta file. Example is as follows:
```
python /home/suresh/scripts/python_exercises/fasta_motif_search_09042021/fasta_motifs.py test1.fa 5 1
```
test1.fa is input file (provided here), 5 is kmer size of interest, 1 is window. Output from the file is provided below. Output would print kmer from each sequence of the file, prints sequence name and sequence start and end in that sequence. For eg. seq1_1_5 means sequence is from seq1 (original sequence from input) and start position of the sequence 1 and end position is 5 from the original sequence.

output:
```
>seq1_1_5
ACCGG
>seq1_2_6
CCGGT
>seq2_1_5
AATTT
>seq2_2_6
ATTTC
```
