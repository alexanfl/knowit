import string

message = open("../res/5.dat").readlines()[0][:-1].split(", ")
print(len(message))

def string_to_int(numeral):
    integer = 0
    for string in numeral:
        if string == "I":
            integer += 1
        if string == "V":
            integer += 5
        if string == "X":
            integer += 10
    return integer

def roman_to_int(numeral):
    l = len(numeral) if numeral != 0 else 1
    if l < 1 or l > 4:
        print("Error")

    elif l == 1:
        integer = 0
        integer = 1 if numeral == "I" else integer
        integer = 5 if numeral == "V" else integer
        integer = 10 if numeral == "X" else integer

    elif l == 2 and numeral[0] == "I":
        integer = 2
        integer = 4 if numeral[1] == "V" else integer
        integer = 9 if numeral[1] == "X" else integer
    else:
        integer = string_to_int(numeral)
    return integer    

alphabet = string.ascii_lowercase

sentence = []
for i in range(int(len(message)/2)):
    letter = roman_to_int(message[i]) + roman_to_int(message[-1-i])
    sentence.append(alphabet[letter-1])

print("".join(sentence))
