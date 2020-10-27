def base10to2(c, lst = [False, True]):
    p,q,s = [],c,1
    while s <= c:
        a = (q%(2*s))
        p += [lst[int(a/s)]]
        q -= a
        s *= 2
    return [False]*(4-len(p)) + p[::-1]





def sevenseg(a,b,c,d,e,f,g):
    print(' _ ') if a else print('   ')   
    print('|',end='') if b else print(' ', end='')
    print('_',end ='') if d else print(' ',end='')
    print('|') if c else print(' ')
    print('|',end='') if e else print(' ', end='')
    print('_',end ='') if g else print(' ',end='')   
    print('|') if f else print(' ')

for i in range(16):
    ABCD = base10to2(i)
    A = ABCD[0]
    B = ABCD[1]
    C = ABCD[2]
    D = ABCD[3]
    
    a = ((not B) and (not D)) or ((not A) and C) or (B and C) or (A and not D) or ((not A) and B and D) or (A and not B and not C)
    b = ((not C) and (not D)) or (A and (not B)) or (A and C) or (B and (not D)) or ((not A) and B and (not C))
    c = ((not B) and (not A or not D)) or (not C and (not A^D)) or (not A and (not C^D))
    d = (A and not B) or (C and not D) or (not B and C) or (A and D) or (not A and B and not C)
    e = (not D and (not B or C)) or (A and (B or C or not D))
    f = (not A and not C) or (A^B) or (not C and D) or (not B and D)
    g = (A and not C) or (not B^C^D) or (not D and (not A^B))
    #g = (A and not C) or (not A and not B and not D) or (D and B^C) or (B and C^D)
    
    sevenseg(a,b,c,d,e,f,g)