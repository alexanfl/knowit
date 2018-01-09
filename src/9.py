infile = open("../res/9.dat")

accounts = {}

for line in infile:
    line = line.split(",")
    line[2] = int(line[2])

    if line[1] in accounts:
        accounts[line[1]] += line[2]
    else:
        accounts[line[1]] = line[2]

    if line[0] in accounts:
        accounts[line[0]] -= line[2] 
    else:
        accounts[line[0]] = -line[2]

cnt = 0
for elem in accounts:
    if accounts[elem] > 10:
        print(elem)
        cnt += 1

print(cnt)
