This folder contains two scripts of the same function except that one function filters by gene name, takes user inputs (gbk file and output file name). `gbtofasta.py` extracts nucleotide and aminoacid (CDS) sequences where as `gbk2seq.py` extracts only CDS sequences, but filters on user input (eg used here **pol**). `gbk2seq.py` takes user input for input file name and output file name. If output file name is not given, input file name would be used with .fasta as extension. New file will be created in the same folder. Following is the usage.

```code
./gbk2seq.py input.gbk
./gbk2seq.py input.gbk output.fa
```
In fist case, output file name would be `input.fasta` and in later case, output would be `output.fa`
