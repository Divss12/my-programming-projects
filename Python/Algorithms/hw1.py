#1. You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
#Give an algorithm that identifies the second-largest number in the array, and that uses at most n+log(n)−2 comparisons.

n = 12
lst = list(range(1,2**n + 1))

def secondlargest(lst):
    l = len(lst)
    if l == 2:
        if lst[0] > lst[1]:
            return lst[1]
        else:
            return lst[0]
    else:
        a,b = secondlargest(lst[:l//2]),secondlargest(lst[l//2:])
        if a > b:
            return a
        else:
            return b

print(secondlargest(lst))