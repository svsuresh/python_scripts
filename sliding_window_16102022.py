#! /usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(
    description='Generate fasta file with sliding windows')
parser.add_argument('-i', '--input', help='Input fasta file',
                    required=True, action='store')
parser.add_argument('-o', '--output', help='Output fasta file',
                    required=True, action='store')
parser.add_argument('-w', '--window', help='Window size',
                    required=True, action='store')
parser.add_argument('-s', '--step', help='Step size',
                    required=True, action='store')
parser.add_argument('-t', '--type', help='forwad or reverse',
                    required=True, action='store')
args = parser.parse_args()

f = args.input
o = args.output
w = int(args.window)
s = int(args.step)
t = str(args.type)

_final = []


def _output(x):
    _header = line.rstrip()+"_"+str(x+1)+"_"+str(x+w)
    _sequence = seq[x:x+w]
    _final.append(_header)
    _final.append(_sequence)


with open(f, "r") as q:
    for line in q:
        if line.startswith(">"):
            seq = next(q,  ' ').rstrip()
            seqlen = seq.__len__()
            if s*w > seqlen:
                sys.exit(
                    "Error:  sequence length is less than calculated sequence length")
            steps = int(((seqlen-w)/s)+1)
            if t == "forward":
                [_output(i) for i in range(0, steps*s, s)]
            elif t == "reverse":
                [_output(i-w) for i in range(seqlen, seqlen-steps*s,  -s)]
        print(*_final, sep="\n", file=open(o, "w"))

print("file written to "+o)
