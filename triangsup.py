from turtle import end_fill
from numpy import zeros,array

def triangsup(T,b):
    #T est la matrice triangulaire supérieure
    #b est le vecteur second membre
    n=len(b)
    x=zeros(n)
    x[n-1]=b[n-1]/T[n-1][n-1]
    for i in range(n-2,-1,-1):
        S=0
        for k in range(i+1,n):
            S+=T[i][k]*x[k]
        x[i]=(b[i]-S)/T[i][i]
    return x

# x=triangsup(array([[4,0,0],[3,-3,0],[-1,1,1]]), array([8, 9, -2]))
# print(x)
    
