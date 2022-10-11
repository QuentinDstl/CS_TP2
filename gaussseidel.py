from numpy import size, zeros,array,linalg,dot
from math import *
from trianginf import trianginf

def gaussseidel(A,N,b,E,x):
    n=len(A[0])
    D=zeros((n,n))
    for i in range(0,n):
        D[i][i]=A[i][i]
    M=trianginf(A,b)