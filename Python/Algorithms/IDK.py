lst = ['A','B','C','D','E','F','G','H']
mn = [[i,j] for j in lst for i in lst]
for i in lst:
    mn.remove([i,i])
pl = [[q,r] for p,q in enumerate(lst) for r in lst[p+1:]]

print(len(lst),len(mn),len(pl))