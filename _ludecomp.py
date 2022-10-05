from numpy import zeros,array,dot

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
    U = zeros((n,n)) 
    
    for j in range(n):
        L[j][j] = 1
        U[0][j] = A[0][j]
        for i in range(n):
            U[i][j] = A[i][j]
    
    for i in range(n):
        for k in range(i+1,n):
            mu = U[k][i]/U[i][i]
            L[k][i] = mu
            U[k][0] = 0
            for j in range(1,n):
                U[k][j] = U[k][j] - mu*U[i][j]
    return [L,U]

[L,U] = _ludecomp(array([[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]]))

print(L)
print(U)
print(dot(L,U))