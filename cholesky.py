from numpy import size, zeros,array,linalg,dot
from math import *

def IsSymmetrical(A):
    n=len(A[0])
    for i in range(0,n):
        for j in range(0,n):
            if A[i][j]!=A[j][i]:
                return False
    return True

def cholesky(A):
    if(IsSymmetrical(A)):
        raise Exception("A is not symmetrical")

    n=len(A[0])
    C=zeros((n,n))
    C[0][0]=sqrt(A[0][0])
    for i in range(1,n):
        C[i][0]=A[i][0]/C[0][0]
    for j in range(1,n):
        S=0
        for k in range(0,j):
            S+=(C[j][k])*(C[j][k])
        C[j][j]=sqrt(A[j][j]-S)

        for l in range(j+1,n):
            S=0
            for m in range(0,j):
                S+=C[l][m]*C[j][m]
            C[l][j]=(A[l][m]-S)
    return C

C=cholesky(array([[15,10,18,12],[10,15,7,13],[18,7,27,7],[12,13,7,22]]))
print(C)