def isdigitsum(n):
    l = [int(x) for x in str(n)]
    for i in range(len(l)):
        if l[i] == sum(l[:i] + l[i+1:]):
            return True
    else:
        return False
    
def gendigsums(n):
    #generates all the digit sums of n digits
    for i in range(1,10):
        for j in sumsof(i,n-1):
            yield [i] + j 
            
for i in gendigsums(n):
    perms(i)       

def funcS(n):
    s = 0    
    for i in range(10**n):
        if isdigitsum(i):
            s += i
    return s
        
print(isdigitsum(352))
print(isdigitsum(3003))
print(isdigitsum(32812))

print(funcS(3))
print(funcS(7))