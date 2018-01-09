N = 1337
numbers = [ x for x in range(1,N+1) ]

def replace_seven(x, cnt):
    if "7" in str(x) or x%7 == 0:
        cnt += 1 
        return numbers[cnt-1], cnt
    else:
        return x, cnt

def calculate_seven(numbers, cnt):
    for i in range(N):
        numbers[i], cnt = replace_seven(numbers[i], cnt)
    print(numbers[-1])
    return numbers

calculate_seven(numbers, 0)
