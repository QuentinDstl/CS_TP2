function triangInf(A::Matrix{T}, b::Vector{T}) where T <: Number
    n = size(A, 1)
    x = zeros(n)
    x[1] = b[1] / A[1, 1]
    for i = 2:n
        Σ = 0
        for j = 1:i
            Σ += A[i, j] * x[j]
        end
        x[i] = (b[i] - Σ) / A[i, i]
    end
    return x
end