#!/usr/bin/env python3

sequences = ["GAGGTAAACTCTG", "TCCGTAAGTTTTC", "CAGGTTGGAACTC",
             "ACAGTCAGTTCAC", "TAGGTCATTACAG", "TAGGTACTGATGC"]


def count_first_base(sequences=sequences, base="A", pos=0):
    count = [int(i[pos] == base) for i in sequences]
    return [base, count, sum(count)]


#print(*count_first_base(), sep="\t")
#print(*count_first_base(base="G", pos=2), sep="\t")

# def count_first_base(sequences=sequences, pos=0):
for seq in sequences:
    print(seq[0])
    

# Other methods to count
#count = [int(i[0] == "A") for i in sequences]
# print(count)
#
#
#count = []
# for i in sequences:
#    count.append(1 if i[0] == "A" else 0)
# print(count)
#
#count = []
# for i in sequences:
#    count.append((0, 1)[i[0] == "A"])
# print(count)
# print(sum(count))
