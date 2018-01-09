from numpy import array, zeros

infile = open("../res/7.dat")

pos = zeros(2)

def move(string):
    dist, cardinal = int(string.split()[1]), string.split()[3]
    d = 1 if cardinal == "north" or cardinal == "west" else -1
    
    new_pos = [0,dist] if cardinal == "west" or cardinal == "east" else [dist,0]
    return d*array(new_pos)

for line in infile:
    pos += move(line)

print(pos)
