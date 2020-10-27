#algorithm to find the closest pair of points
import random
import math

lst = [(random.random()*10,random.random()*10) for i in range(5)] #List of points
print(lst)

#iterative method
def closestiter(lst):
    d = math.sqrt((lst[0][0]-lst[1][0])**2 + (lst[0][1]-lst[1][1])**2)
    cp = [lst[0],lst[1]]
    for i,j in enumerate(lst):
        for k in lst[i+1:]:
            if math.sqrt((j[0]-k[0])**2 + (j[1]-k[1])**2) < d:
                d = math.sqrt((j[0]-k[0])**2 + (j[1]-k[1])**2)
                cp = [j,k]
    return cp + [d]


#recursive method
def closestpoint(lst):
    lstx = [i[0] for i in lst]
    lsty = [j[1] for j in lst]

    def dist(ax,ay,bx,by):
        return math.sqrt((bx-ax)**2 + (by-ay)**2)

    def closestrecur(lstx,lsty):
        ln = len(lstx)
        if ln <= 3:
            '''
            d = dist(lstx[0],lsty[0],lstx[1],lsty[1])
            p1,p2 = 0,1
            for i in range(ln):
                for j in range(i+1,ln):
                    if dist(lstx[i],lsty[i],lstx[j],lsty[j]) < d:
                        d = dist(lstx[i],lsty[i],lstx[j],lsty[j])
                        p1,p2 = i,j
            return [(lstx[i],lsty[i]),(lstx[j],lsty[j]),d]
            '''
            lst = [(i,j) for i,j in zip(lstx,lsty)]
            return closestiter(lst)
        else:
            lstx.sort()

            qx = lstx[:ln//2]
            rx = lstx[ln//2:]
            qy = lsty[:ln//2]
            ry = lsty[ln//2:]

            *cpq,dq = closestrecur(qx,qy)
            *cpr,dr = closestrecur(rx,ry) 

            x = lstx[len(lstx)//2 -  1]
            ds = min(dq,dr)
            cps = None
            sy = [(lstx[i],j) for i,j in enumerate(lsty) if lstx[i] >= x-ds and lstx[i] <= x+ds]
            for i in range(len(sy)-1):
                for j in range(min(7,len(sy)-i)):
                    if dist(*sy[i],*sy[i+j]) < ds:
                        ds = dist(*sy[i],*sy[i+j])
                        cps = [sy[i],sy[i+j]]

            if ds < dq and ds < dr:
                print(1)
                return cps + [ds]
            elif dq < dr:
                print(2)
                return cpq + [dq]
            else: 
                print(3)
                return cpr + [dr]

    return closestrecur(lstx,lsty)

print('—'*25)
print('Recursive Method:')
print(closestpoint(lst))
print('—'*25)
print('Iterative Method:')
print(closestiter(lst))