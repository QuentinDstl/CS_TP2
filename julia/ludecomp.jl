function luDecomp(A::Matrix{T}) where T <: Number
    n = size(A, 1)
    L = zeros(n,n)
    U = zeros(n,n)
    for j = 1:n
        L[j, j] = 1
        U[1, j] = A[1, j]
        for i = 1:n
            U[i, j] = A[i, j]
        end
    end
    for i = 1:n
        for k = i+1:n
            μ = U[k, i]/U[i, i]
            L[k, i] = μ
            U[k, 1] = 0
            for j = 2:n
                U[k, j] = U[k, j] - μ*U[i, j]
            end
        end
    end
    return [L, U]
end