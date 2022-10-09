from numpy import zeros,array

def trianginf(T, b):
    # T est la matrice triangulaire inférieure
    # b est le vecteur second membre
    n = len(b)
    x = zeros(n)
    x[0] = b[0] / T[0][0] #b1 / T11
    for i in range(1, n):
        S = 0
        for k in range(0, i):
            S += T[i][k] * x[k]
        x[i] = (b[i] - S) / T[i][i]
    return x

# x=trianginf(array([[4,0,0],[3,-3,0],[-1,1,1]]), array([8,9,-2]))
# print(x)