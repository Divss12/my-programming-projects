def palinsum(n):
    '''generates all palindromic sums for the integer n, outputting the sum as a list of integers'''
    if n == 0:
        yield []
    elif n == 1:
        yield [1]
    else:
        for i in range(1,n//2 + 1):
            for j in palinsum(n - 2*i):
                yield [i] + j + [i]
        yield [n]

def twopals(n,b=False):
    '''generates all palindromic sums of n that contain the integer 2''' 
    if n == 0 and b:
        yield []
    elif n == 1 and b:
        yield [1]
    else:
        for i in range(1,n//2 + 1):
            for j in twopals(n - 2*i, i==2 or b):
                yield [i] + j + [i]
        if b or n==2:
            yield [n]

def t(n):  
    out = 0 
    for i in twopals(n):
        out = (out+1)
    return out

print(t(33))
'''
for i in range(60,101,10):
    print(i)
    ti = t(i)
    print(ti)
    if ti%1000000 == 0:
        print(i)
        print(len(list(twopals(i))))
        break
'''