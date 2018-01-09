from numpy import array

N=100

r = array([0,0])

i = 1
while i < N:
    i += 1
    r += array([-2,1])

print(abs(r[0]) + abs(r[1]))
