import re

infile = open("../res/19.dat")

for line in infile:
    line = re.sub("[13579]","#",line)
    line = re.sub("[02468]"," ",line)
    print line,
