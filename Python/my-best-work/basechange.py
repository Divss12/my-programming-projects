#Attempt to make a function that changes any base to any other base.
#The digits of the nth base after base 10 are A,B,C...X,Y,Z,a,b,c....x,y,z
#As such only bases up till base 62 are supported
#For operations in greater bases, input list of digits as another argument
#base(number,origin base, target base)
#origin base and target base must be passed as integers in base10, number could be passed as string or integer
import sys

def base(n,b1=10,b2=10,lst=['0','1','2','3','4','5','6','7','8','9',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]):
    num = list(str(n))
    c = 0
    for i in num:
        c = (b1*c) + lst.index(i)
#C is the value in base10
    p,q,s = '',c,1
    while s <= c:
        a = (q%(b2*s))
        p += lst[int(a/s)]
        q -= a
        s *= b2
    return p[::-1]

print(base(sys.argv[1],int(sys.argv[2]),int(sys.argv[3])))
