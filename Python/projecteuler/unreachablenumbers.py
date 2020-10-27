n = 23*17*19
lst = list(range(1,17*n+19*n+23*n + 1))

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            try:
                lst.remove(17*i + 19*j + 23*k)
            except:
                continue

print(sum(lst))