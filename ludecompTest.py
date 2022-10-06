from numpy import zeros,array
from trianginf import trianginf
from triangsup import triangsup

def ludecomp(A):
    #A est la matrice principale
    S=0
    Q=0
    V=0
    n=len(A[0])
    L=zeros((n,n))
    U=zeros((n,n))
    L[0][0]=1
    for i in range(0, n): 
        U[0][i]=A[0][i] 
    for j in range(1, n): 
        L[j][0]=A[j][0]/2
    for p in range(1, n): 
        L[p][p]=1   
        for k in range(0, p-1):
            S += L[p][k] * U[k][p]
        U[p][p]=A[p][p]-S
        for m in range(p, n):
            for o in range(0, p-1):
                Q += L[p][o] * U[o][m]
                V += L[m][o] * U[o][p]
            U[p][m]=A[p][m]-Q
            L[m][p]=(A[m][p]-V)/U[p][p]
    return [L,U]


[L,U]=ludecomp(array([[2,4,3,5],[-4,-7,-5,-8],[6,8,2,9],[4,9,-2,14]]))
print(L)
print(U)
B=L*U
print(B)

