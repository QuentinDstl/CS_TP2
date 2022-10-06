from numpy import size, zeros,array,linalg,dot
from math import *

def cholesky(A):
    n=len(A[0])
    C=zeros((n,n))
    C[0][0]=sqrt(A[0][0])
    return C