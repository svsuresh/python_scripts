#### Python scripts mostly jupyter notebooks

This folder contains python scripts (and mostly as ipython/jupyter notebooks). Following is the description:
1. hgvs_p_syntax_conversion.ipynb: This script converts HGVS pSyntax from 3 letter code to 1 letter code and vice vers. It asks for codon length (3 or 1) in your file and then the file path. Currently, script takes only one column file. Column should contain pSyntax without any header. Output will have two columns. One with old syntax and second column with converted syntax. Input can be in any case and output would be in case sentense. Input also support versions in protein IDs. 

Example input for 3 letter syntax

  + NP1457:p.ser2ala
  + p.ala3tyr
  + NP123.1:p.Tyr3pHe

Output for example output would be:

  + NP1457:p.ser2ala&nbsp;&nbsp;&nbsp;&nbsp;NP1457:p.S2A
  + p.ala3tyr&nbsp;&nbsp;&nbsp;&nbsp;p.A3Y
  + NP123.1:p.Tyr3pHe&nbsp;&nbsp;&nbsp;&nbsp;NP123.1:p.Y3F

Example input for single letter syntax:
  + p.a2G
  + NP.2123:p.C2p
  + p.D3e

Output for Example input would be:
  + p.a2G	&nbsp;&nbsp;&nbsp;&nbsp;p.Ala2Gly
  + NP.2123:p.C2p	&nbsp;&nbsp;&nbsp;&nbsp;NP.2123:p.Cys2Pro
  + p.D3e&nbsp;&nbsp;&nbsp;&nbsp;	p.Asp3Glu

2. psqldf_multiple_df_with_dots_join.ipynb. This script is an example in joining multiple data frames in pandas. Joining data frames with period(.) in names could be tricky in SQL join. This example shows how to do that. This script joins 3 data frames with . in column names. 
3. extract_motifs - Folder has python code to extract motifs (from-to) from fasta file based on full name of the sequence and regions of interest. At this point script doesn't support partial name search.
4. bioservices_kegg_python.ipynb - This script uses bioservices python library to download KEGG pathway IDs and names given gene symbols.
5. ncbi_id_converter_py.ipynb - This script uses biopython libraries to convert PMIDs to PMCIDs.
6. gbtofasta folder contains python script for extracting nucleotide and protein sequence from the gb (genebank file). From multientry genbank file, it extracts nucleotide and protein sequence. Please change the script as you need.
7. count_a_first_position.py takes 3 arguements: list of sequences, base to be searched for, position at which based to be searched for. This script looks for a base (user provided single base, argument: base=""), at given position in each sequence in the list of the sequence. It outputs base, if it is present in each sequence or not (1 present and 0 absent) and total number of sequences in which user furnished base is present at user furnished position.
8. append_duplicate_numbers.py takes an input fasta file (eg. test.fa) and an output fasta file (eg. out.fa). It appends numbers at the end of the each header depending on the number of times it is present. For eg if header is present only once, it would have #1 appended to the header. If header is present 4 times, each duplicated header will carry numbers from 1 to 4. 
9. sliding_window_16102022.py: Takes an input with one or more fasta sequences. If user provides sliding window size, and step size, script outputs a fasta file with sequences as per user input parameters, in both forward and reverse directions.
