from numpy import zeros,array
from trianginf import trianginf
from triangsup import triangsup

def ludecomp(A):
    #A est la matrice principale
    n=len(A[1])
    L=zeros(n,n)
    y=trianginf(L,)
    x=triangsup(U,y)

