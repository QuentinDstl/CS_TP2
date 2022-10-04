from numpy import zeros,array


def gauss(A,b):
    #A est la matrice principale
    #b est le vecteur second memebre
    S=0
    n=len(b)
    x=zeros(n)
    m=zeros((n,n))
    #Triangulation de la matrice
    for k in range(0,n-1):
        for i in range(k,n):
            m[i][k]=A[i][k]/A[k][k]
            for j in range(k,n):
                A[i][j]=A[i][j]-m[i][k]*A[k][j]
            b[i]=b[i]-m[i][k]*b[k]
    #Resolution du syteme triangulaire superieur
    #x[n]=A[n][n]/A[n][n]
    for p in range(n-2,1):
        for m in range(p,n):
            S+=A[p][m]*x[m]
        x[p]=(b[p]-S)/(A[p][p])
    return x

x=gauss(array([[2,4,3,5],[-4,-7,-5,-8],[6,8,2,9],[4,9,-2,14]]), array([[2,4,3,5]]))
print(x)
