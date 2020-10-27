#[1,2,6,3,17,82,23,234] -> 26
#Solution [3,6]

#[1,2,6,3,17,82,23,234] -> 40
#Solution [4,6]

#[1,2,6,3,17,82,23,234] -> 23
#Solution [6]

'''My understanding is that I have to find any number of values in the list that:
    1. Sum up to the target
    2. The sum of their indices is a minimum
    3. No indice can be repeated
    4. In the case of multiple solutions, the solution with the fewer number of indices is favored'''
    
'''Since the challenge is to minimise the sum of the indices used; the approach I used puts this first'''

def findsums(n):
    if n == 0:
        yield []
    else:
        for i in range(n//2 + 1):
            for j in findsums(i):
                if n-i not in j:
                    yield [n-i] + j
        
        
for i in range(1,11):
    for j in findsums(i):
        print(j,end='')
    print()

'''
print('-'*10)
findindices([1,2,6,3,17,82,23,234], 26)
print('-'*10)
findindices([1,2,6,3,17,82,23,234], 40)
print('-'*10)
findindices([1,2,6,3,17,82,23,234], 23)
'''