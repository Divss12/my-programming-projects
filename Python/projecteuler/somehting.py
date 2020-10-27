#problem 720 failed attempt (palindsum)

def r(n):
    if n < 1:
        return 1
    else:
        return (2**(n//2))

def t(n):
    if n == 0:
        return 0
    elif n == 1:
        return -1
    else:
        out = (t(n-2) + r(n-4))
        for i in range(3,n//2):
            out = (out + t(n - 2*i))
        return out



for i in range(81,101):
    ti = t(i)
    print(f"{i}: {ti}")
    if ti == 0:
        print('FINISHED')
        break

    