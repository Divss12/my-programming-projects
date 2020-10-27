import random
def quicksort(lst):
    n = len(lst)
    if n < 2:
        return lst
    else:
        p = random.randrange(0,n) #pivot
        q = lst[p]
        
        lst = [q] + lst[:p] + lst[p+1:]
        l = 0
        for i,j in enumerate(lst[1:]):
            if j < q:
                lst = [j] + lst[:i+1] + lst[i+2:]
                l += 1
        
        return quicksort(lst[:l]) + [q] + quicksort(lst[l+1:])


count2 = []
def quicksort1(lst):
    n = len(lst)
    if n < 2:
        return lst
    else:
        p = 0 #pivot
        q = lst[p]
        
        lst[0],lst[p] = q,lst[0]
        i,j = 1,1
        for k in lst[1:]:
            if k < q:
                lst[i],lst[j] = lst[j],lst[i]
                i += 1
            j += 1
        return quicksort1(lst[1:i]) + [q] + quicksort1(lst[i:])


with open('QuickSort.txt','r') as fp:
    lst = list(map(lambda x: int(x.strip()),fp.readlines()))

    quicksort1(lst)
    print(sum(count2))