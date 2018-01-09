import string

alphabet = [ x for x in string.ascii_uppercase ]

lim = 90101894

def findCharacters(lst,number):
    a = int(number/26)
    if number <= 26:
        lst.append(alphabet[number-1])
        return lst
    else:
        lst.append(alphabet[number%26-1])
        findCharacters(lst,a)
    return lst

chars = findCharacters([],lim)
chars.reverse()
print("".join(chars))
