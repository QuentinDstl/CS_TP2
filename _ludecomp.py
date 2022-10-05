from numpy import zeros,array

def HasZerosOnDiag(A):
    n = len(A[0])
    for i in range(n):
        if A[i][i] == 0:
            return True
    return False

def _ludecomp(A):
    if(HasZerosOnDiag(A)):
        raise Exception("A has zeros on diagonal")
    
    n = len(A[0])
    L = zeros((n,n))
    U = zeros((n,n,n)) 
    
    for j in range(n):
        L[j][j] = 1
        U[1][0][j] = A[0][j]
        for i in range(n):
            U[0][i][j] = A[i][j]
    
    for d in range(1,n):
        for i in range(n):
            for k in range(i+1,n):
                mu = U[d-1][k][i]/U[d-1][i][i]
                L[k][i] = mu
                U[d][k][0] = 0
                for j in range(1,n):
                    U[d][k][j] = U[d-1][k][j] - mu*U[d-1][i][j]
    
    print(A)
    print(L)
    print(U)

_ludecomp(array([[1,2,3],[4,5,6],[7,8,9]]))