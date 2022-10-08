function triangSup(A::Matrix{T}, b::Vector{T}) where T <: Number
    n = size(A, 1)
    x = zeros(n)
    x[n] = b[n] / A[n, n]
    for i = n-1:-1:1
        Σ = 0
        for j = i+1:n
            Σ += A[i, j] * x[j]
        end
        x[i] = (b[i] - Σ) / A[i, i]
    end
    return x
end