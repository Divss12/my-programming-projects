#converts integer to roman numeral
#also converts roman numeral to integer
import sys

def rom(n):
    l = list(str(n))
    r = [['I','V','X'],['X','L','C'],['C','D','M'],['M']]
    d = {   
            '0':[],
            '1':[0],
            '2':[0,0],
            '3':[0,0,0],
            '4':[0,1],
            '5':[1],
            '6':[1,0],
            '7':[1,0,0],
            '8':[1,0,0,0],
            '9':[0,2]
        }
    o = ''
    for i in range(len(l)):
        for j in d[l[i]]:
            o += r[len(l)-1-i][j]
    return o

def dec(x):
    l = { 
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,  
        'M': 1000         
    } 
    p,q = 0,0

    for i in list(x[::-1]):
        if l[i] >= p:
            q += l[i]
        else:
            q -= l[i]
        p = l[i]
    
    return q