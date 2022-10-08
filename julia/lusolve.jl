include("trianginf.jl")
include("triangsup.jl")

A = [4. 0. 0.; 3 -3. 0.; -1. 1. 1.]
b = [8., 9., -2.]
print(triangSup(A, b))