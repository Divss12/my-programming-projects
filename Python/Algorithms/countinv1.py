def countinv(lst):
    inv = []
    def mergesort(lst):
        if len(lst)<=1:
            return lst
        else:
            lst1, lst2, i, j, out = mergesort(lst[:len(lst)//2]), mergesort(lst[len(lst)//2:]), 0, 0, []
            while True:
                if lst1[i] < lst2[j]:
                    out.append(lst1[i])
                    i += 1
                    if i == len(lst1):
                        return out + lst2[j:]
                else: 
                    inv.append(len(lst1[i:]))
                    out.append(lst2[j])
                    j += 1
                    if j == len(lst2):
                        return out + lst1[i:]
    mergesort(lst)
    return sum(inv)

a = [5,2,3,4,1,6]
print(countinv(a))    


'''
def majorindex(lst):
    ind = 0
    for i in range(len(lst)-1):
        ind += max(0,lst[i]-lst[i+1])
    return ind

def perms(lst):
    if len(lst) <=1:
        yield lst
    else:
        for p in perms(lst[1:]):
            for i in range(len(lst)):
                yield p[:i] + [lst[0]] + p[i:]

s = []
for i in perms(list(range(1,7))):
    l = ['even','odd']
    c = countinv(i)%2
    print(i,l[c])
    s.append(str(c))
print(s)

for j in range(len(s)-1):
    if s[j] == s[j+1]:
        s.insert(j+1,'\n')

print(''.join(s))


for a in range(2,9):
    print(a)
    dicI = {}
    dicM = {}
    for A in perms(list(range(1,a+1))):
        if majorindex(A) in dicM.keys():
            dicM[majorindex(A)] += 1
        else:
            dicM[majorindex(A)] = 1
        if countinv(A) in dicI.keys():
            dicI[countinv(A)] += 1
        else:
            dicI[countinv(A)] = 1

    #print('inversion no.')
    avgI = 0 
    for a,b in dicI.items():
        #print(f'{a}: {b}')
        avgI += a*b
    avgI /= sum(dicI.values())
    #print(f'avgI: {avgI}')
    #print('major index')
    avgM = 0
    for c,d in dicM.items():
        #print(f'{c}: {d}')
        avgM += c*d
    avgM /= sum(dicM.values())
    print(f'avgI: {avgI};   avgM: {avgM}')
'''