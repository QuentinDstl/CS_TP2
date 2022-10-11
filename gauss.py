from numpy import size, zeros,array,linalg,dot

def HasZerosOnDiag(A):
    n = len(A[0])
    for i in range(n):
        if A[i][i] == 0:
            return True
    return False

def gauss(A,b):
    #A est la matrice principale
    #b est le vecteur second memebre
    if(HasZerosOnDiag(A)):
        raise Exception("A has zeros on diagonal")
    
    S=0
    n=len(b)
    x=zeros(n)
    m=zeros((n,n))
    #Triangulation de la matrice
    for k in range(0,n-1):
        for i in range(k+1,n):
            m[i][k]=A[i][k]/A[k][k]
            #print(m[i][k])
            for j in range(k,n):
                A[i][j]=A[i][j]-m[i][k]*A[k][j]
            b[i]=b[i]-m[i][k]*b[k]
    #Resolution du syteme triangulaire superieur
    x[n-1]=b[n-1]/(A[n-1][n-1])
    for p in range(n-2,-1,-1):
        for l in range(p+1,n):
            S+=A[p][l]*x[l]
        x[p]=(b[p]-S)/(A[p][p])
        S=0
    return x

#test matrice inverse
def matinv(A,b):
    if(HasZerosOnDiag(A)):
        raise Exception("A has zeros on diagonal")
    
    n=len(b)
    x=zeros(n)
    C=linalg.inv(A)
    for i in range(0,n):
        S=0
        for j in range(0,n):
            S+=C[i][j]*b[j]
        x[i]=S
    return x

x=gauss(array([[1,1,-1],[2,-1,1],[-1,2,2]]), array([-2, 5, 1]))
x=matinv(array([[1,1,-1],[2,-1,1],[-1,2,2]]), array([-2, 5, 1]))
print(x)
