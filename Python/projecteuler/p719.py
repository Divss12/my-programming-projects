#https://projecteuler.net/problem=719

"""We define an S-number to be a natural number, n, that is a perfect square and its square root can be obtained by 
splitting the decimal representation of n into 2 or more numbers then adding the numbers."""

#For example, 81 is an S-number because √81 = 8+1.
#6724 is an S-number: √6724 = 6+72+4.
#8281 is an S-number: √8281 = 8+2+81 = 82+8+1.
#9801 is an S-number: √9801 = 98+0+1

#Further we define T(N) to be the sum of all S numbers n≤N. 
#You are given T(10^4) = 41333

#Find T(10^12)

#NOTE: I have solved this problem, however since solving it I have realised there is a more efficient way of coding this.

import math

def genArr(st):
    """Takes a string and generates different ways to split it up
    For example: 123 will yield:
    123
    12 3
    1 23
    1 2 3"""
    n = len(st)
    if n == 1:
        yield st
    else:
        for i in genArr(st[:n//2]):
            for j in genArr(st[n//2:]):
                yield i + j 
                yield i + ' ' + j

def isSno(n,check):
    """Checks if n is an S-no. as defined in the header comments. 
    The square root of n is passed in the parameter 'check' for optimisation"""
    for i in genArr(str(n)):
        if sum(map(int,i.split(' '))) == check:
            return True
    return False

#driver code
n = 1000000 
T = 0
j = 4
for i in range(9,n+1,9): #Iterating through to 10^6, j holds the value of i^2
    if isSno(j,i):
        T += j
        print(i,j)
    j = j + i + i + 1 #Based on the idea that (n+1)^2 = n^2 + n + (n+1)

for i in range(10,n+1,9):
    if isSno(j,i):
        T += j
        print(i,j)
    j = j + i + i + 1 

print(T)


def f(n,x):
    '''Just a function I wrote to test something im not sure'''
    if x <= n:
        return True
    pow10 = 10
    while pow10 <= x and pow10 <= n:
        if f(n - x%pow10, x//pow10):
            return True
        pow10 *= 10