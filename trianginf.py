from numpy import zeros,array

def trianginf(T, b):
    # T est la matrice triangulaire inférieure
    # b est le vecteur second membre
    n = len(b)
    x = zeros(n)
    x[1] = b[1] / T[1][1] #b1 / T11
    for i in range(2, n):
        S = 0
        for k in range(1, i-1):
            S += T[i][k] * x[k]
        x[i] = (b[i] - S) / T[i][i]
    return x