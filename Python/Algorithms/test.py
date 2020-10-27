identity_matrix = lambda n : [[0]*i + [1] + [0]*(n-i-1) for i in range(n)]

identity_matrix(5)