import csv
import sys

# TODO: read arguments in a better way (argparse)
# TODO: add tests

if len(sys.argv) < 2:
    print 'Need to pass the name of the file'
    sys.exit()
else:
    filename = sys.argv[1]

lines = open(filename).readlines()
lines = [l.strip('\n') for l in lines]

genes = {}

id_ = ""
name = ""
sequence = ""

for line in lines:
    if line[0] == '>':
        id_ = line.split(' ')[0].strip('>')
        name = " ".join(line.split(',')[0].split(' ')[1])
        genes[id_] = {}
        genes[id_]['name'] = name
        genes[id_]['sequence'] = ""
    else:
        genes[id_]['sequence'] += line

for g, v in genes.items():
    C_count = 0
    G_count = 0
    CG_count = 0
    seq = v['sequence']
    for i in range(len(seq)-1):
        if seq[i] == "C":
            C_count += 1
        elif seq[i] == "G":
            G_count += 1
        if seq[i] + seq[i+1] == 'CG':
            CG_count += 1

    if seq[-1] == 'G':
        G_count += 1
    elif seq[-1] == 'C':
        C_count += 1
    genes[g]['C_count'] = C_count
    genes[g]['G_count'] = G_count
    genes[g]['CG_count'] = CG_count

with open('mRNA_analysis.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(genes.items())
