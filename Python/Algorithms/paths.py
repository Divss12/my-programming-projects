lst = [
    [2,4,7],
    [1,7],
    [5,7],
    [1,5],
    [3,4],
    [7],
    [1,2,3,6]
]

def listmat(lst):
    return [[1 if j in i else 0 for j in range(1,len(lst)+1)] for i in lst]

def matlist(mat):
    return [[i+1 for i,v in enumerate(j) if v == 1] for j in mat]

print('hi')
print(matlist(listmat(lst)))