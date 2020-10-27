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

with open('./IntegerArray.txt','r') as fp:
    lst = list(map(lambda x: int(x[:-1]),list(fp.readlines())))
    print(countinv(lst))