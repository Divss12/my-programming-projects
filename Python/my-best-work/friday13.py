#creates a function that check the month and year to see if there is a friday the 13th.
#returns True if friday 13 exists in month and year
import sys

def f13(m,y):
    mon = {1:5,2:1,3:1,4:4,5:6,6:2,7:4,8:0,9:3,10:5,11:1,12:3}
    d = (y + int((y-1)/4)-int((y-1)/100)+int((y-1)/400))%7
    if ((y%4 == 0 and y%100 != 0) or y%400 == 0) and m > 2:
        f = (d + mon[m] + 1)%7
    else:
        f = (d+mon[m])%7
    if f == 5:
        return True
    else:
        return False


month = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
for i in range(1900,2051):
    for m in range(1,13):
        if f13(m,i) == True:
            print(i,month[m])

