import random
from perms import perms

def find(lst,m):
    """Finds the mth smallest element in the array"""
    n = len(lst)
    if n == 0:
        return 0
    if n == 1:
        return lst[0]
    else:
        p = random.randint(0,n-1)
        q = lst[p]
        lst[0],lst[p] = q,lst[0]
        i,j = 1,1
        for k in lst[1:]:
            if k < q:
                lst[i],lst[j] = lst[j],lst[i]
                i += 1
            j += 1
        if i == m:
            return q
        elif i < m:
            return find(lst[i:],m-i)
        else:
            return find(lst[1:i],m)


"""Checking if it works by searching for all numbers in all permutations of all lists of type [1,2,3...i-1] where i ranges from 2 to 8"""
for i in range(2,8):
    for j in perms(list(range(1,i))):
        for k in range(1,i):
            if find(j,k) != k:
                print(f'ERROR on {k}th smallest element of {j}, returned {find(j,k)}')



