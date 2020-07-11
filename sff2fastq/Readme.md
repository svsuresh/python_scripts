Sff2fastq folder containts two python scripts. Both the scripts need biopython libraries are preinstalled on the system.
1. sff2fastq.py script converts user given sff (filename.sff) to fastq file (filename.fastq). Scores are sanger sequencing scores as I understand. function to use is
sff2fastq.py input.sff
2. bulk_sff2fastq_converter.py script iterates over all the files with .sff extension, converts them fastq, creates a new directory with name "fastq_date" (date is system date) and stores the new files in the newly created directory. Function is bulk_sff2fastq_converter.py <path> sff.
Currently it supports sff. However user can try other formats too. Internally, file extension (thus file type) is not hard coded.
