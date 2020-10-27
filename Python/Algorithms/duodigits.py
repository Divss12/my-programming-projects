isDuodigit = lambda n: len(list(set(list(str(n))))) < 3

def d(n):
    i = n
    while True:
        if isDuodigit(i):
            print(f'{n}: {i//n}: {i}')
            break
            #return i
        else:
            i += n
            
def D(k):
    s = 0
    for i in range(k+1):
        s += d(i)
    
    return s

for i in range(120,200):
    d(i)
    