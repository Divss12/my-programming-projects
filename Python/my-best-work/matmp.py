#This program calculates the inverse of a matrix using 2 lines of code

matA = [
    [3,1,3],
    [4,2,4],
    [3,3,6]
]

detMat = lambda matA : matA[0][0]*matA[1][1] - matA[0][1]*matA[1][0] if len(matA) == 2 else sum([(-2*(o%2)+1)*matA[0][o]*detMat([[matA[q][s] if s < o else matA[q][s+1] for s in range(len(matA)-1)] for q in range(1,len(matA))]) for o in range(len(matA))])
invMat = lambda matA : [[(detMat(matA)**-1)*[[r[k] for r in [[((-1)**(m+n))*detMat([l[:m]+l[m+1:] for l in matA[:n]+matA[n+1:]]) for m in range(len(matA[n]))] for n in range(len(matA))]] for k in range(len(matA[0]))][j][i] for i in range(len(matA[0]))] for j in range(len(matA))]

print(invMat(matA))