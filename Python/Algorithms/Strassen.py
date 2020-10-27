#Strassen's recursive matrix multiplication logarithm
import numpy as np

def Strassen1(X,Y): #nxn square matrices where n is a power of 2 (UNOPTIMISED)
    #BASECASE = 2X2 matrices
    if np.shape(X) == (2,2) and np.shape(Y) == (2,2):
        Z = np.array([
            [X[0,0]*Y[0,0] + X[0,1]*Y[1,0], X[0,0]*Y[0,1] + X[0,1]*Y[1,1]],
            [X[1,0]*Y[0,0] + X[1,1]*Y[1,0], X[1,0]*Y[0,1] + X[1,1]*Y[1,1]]
        ])
        return Z
    #ELSE we will break the matrices into quadrants
    else:
        n = np.shape(X)[0]//2
        #Splitting matrices into quadrants
        A = X[:n,:n]
        B = X[:n,n:]
        C = X[n:,:n]
        D = X[n:,n:]
        E = Y[:n,:n]
        F = Y[:n,n:]
        G = Y[n:,:n]
        H = Y[n:,n:]

        #Computing products and adding
        P = Strassen1(A,E) + Strassen1(B,G)
        Q = Strassen1(A,F) + Strassen1(B,H)
        R = Strassen1(C,E) + Strassen1(D,G)
        S = Strassen1(C,F) + Strassen1(D,H)

        #Combining matrices
        Z = np.append(np.append(P,Q,axis = 1),np.append(R,S,axis = 1),axis = 0)
        return Z

def Strassen2(X,Y): #nxn square matrices where n is a power of 2 (OPTIMISED)
    #BASECASE = 2X2 matrices
    if np.shape(X) == (2,2) and np.shape(Y) == (2,2):
        Z = np.array([
            [X[0,0]*Y[0,0] + X[0,1]*Y[1,0], X[0,0]*Y[0,1] + X[0,1]*Y[1,1]],
            [X[1,0]*Y[0,0] + X[1,1]*Y[1,0], X[1,0]*Y[0,1] + X[1,1]*Y[1,1]]
        ])
        return Z
    #ELSE we will break the matrices into quadrants
    else:
        n = np.shape(X)[0]//2
        #Splitting matrices into quadrants
        A = X[:n,:n]
        B = X[:n,n:]
        C = X[n:,:n]
        D = X[n:,n:]
        E = Y[:n,:n]
        F = Y[:n,n:]
        G = Y[n:,:n]
        H = Y[n:,n:]

        #Calculating the 7 products:
        P1 = Strassen2(A, F-H)
        P2 = Strassen2(A+B, H)
        P3 = Strassen2(C+D,E)
        P4 = Strassen2(D,G-E)
        P5 = Strassen2(A+D,E+H)
        P6 = Strassen2(B-D,G+H)
        P7 = Strassen2(A-C,E+F)

        #Adding
        P = P5 + P4 - P2 + P6
        Q = P1 + P2
        R = P3 + P4
        S = P1 + P5 - P3 - P7

        #Combining matrices
        Z = np.append(np.append(P,Q,axis = 1),np.append(R,S,axis = 1),axis = 0)
        return Z

def RegMult(A,B):
    return np.array([[sum([A[p,r]*B[r,q] for r in range(np.shape(B)[1])]) for q in range(np.shape(B)[0])] for p in range(np.shape(A)[0])])


n = 8
E = np.array([[n*i + j + 1 for j in range(n)] for i in range(n)]) #simple nxn matrix that just goes 1,2,3...n^2
F = np.array([[1 if i==j else 0 for j in range(n)] for i in range(n)]) #nxn identity matrix


print(RegMult(E,F))
print(Strassen2(E,F))

'''
n = n//2

A = E[:n,:n]
B = E[:n,n:]
C = E[n:,:n]
D = E[n:,n:]

print(E)
print('-'*15)
print(A)
print('-'*15)
print(B)
print('-'*15)
print(C)
print('-'*15)
print(D)
print('-'*15)
print('-'*15)
print(np.append(np.append(A,B,axis = 1),np.append(C,D,axis = 1),axis = 0))
'''
