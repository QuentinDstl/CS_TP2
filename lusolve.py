from numpy import zeros,array
from trianginf import trianginf
from triangsup import triangsup
from ludecomp import ludecomp

def lusolve(A,b):
   [L, U]=ludecomp(A)
   y=trianginf(L,b)
   x=triangsup(U,y)
   return x

# x=lusolve(array([[1,1,-1],[2,-1,1],[-1,2,2]]), array([-2, 5, 1]))
# print(x)