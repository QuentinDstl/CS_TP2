include("trianginf.jl")
include("triangsup.jl")
include("ludecomp.jl")

function luSolve(A::Matrix{T}, b::Vector{T}) where T <: Number
    luA = luDecomp(A)
    L = luA[1]
    U = luA[2]
    y = triangInf(L,b)
    x = triangSup(U,y)
    return x
end

A = [1. 1. -1.; 2. -1. 1.; -1. 2. 2.]
b = [-2., 5., 1.]

x = luSolve(A,b)
print(x)