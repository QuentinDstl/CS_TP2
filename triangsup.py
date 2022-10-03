from turtle import end_fill
from numpy import zeros,array

def triangsup(T,b):
    #T est la matrice triangulaire supérieure
    #b est le vecteur second membre
    n=len(b)
    x=zeros(n)
    x[n]=b[n]/T[n][n]
    for i in range(n-1,1):
        S=0
        for k in range(i+1,n):
            S+=T[i][k]*x[k]
        x[i]=(b[i]-S)/T[i][i]
    return x
    
