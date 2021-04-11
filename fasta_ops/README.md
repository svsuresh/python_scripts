This script does following operations:

1. Reverse the sequence (reverse)
2. Reverse complement (reverse_complement)
3. Complement the sequence (complement)
4. Counts the bases (count)
5. Translate the ORF sequence (translate)

For each function, program options are given in brackets. Example code is 

```
python fasta_ops.py input.fa complement
```
This would print the output to the screen. Count function also print the data in fasta format. Use following command to print the count in tabular format.

```
python fasta_ops.py file1.fa count | awk -v RS=">" -v OFS="\t" 'NR>1{print $1,$2}'
```
This would print sequence headers in first column and count in second column. Example fasta file is provided with the code.
