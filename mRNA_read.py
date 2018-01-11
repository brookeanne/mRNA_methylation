# DELETE THIS:
# test
# 10 C's, 10 G's
text = "GCCGCCGCGCGGGCGCGCCGC"
characters = list(text)
#
#
import sys
# read arguments in a better way

if len(sys.argv) < 2:
    print 'Need to pass the name of the file'
    sys.exit()
else:
    filename = sys.argv[1]

text = open(filename).read()
##print text
characters = list(text)
##print characters

C_count = 0
G_count = 0
CG_count = 0

for i in range(len(characters)-1):
    if characters[i] == "C":
        C_count += 1
    elif characters[i] == "G":
        G_count += 1
    if characters[i] + characters[i+1] == 'CG':
        CG_count += 1

if characters[-1] == 'G':
    G_count += 1
elif characters[-1] == 'C':
    C_count += 1

print "c count:", C_count, "g count:", G_count, "CG count", CG_count
