function trianginf(A::Matrix{Number}, b::Vector{Number})
    n = size(A, 1)
    x = zeros(n)
    x[1] = b[1] / A[1, 1]
    for i = 2:n
        Σ = 0
        for j = 1:i-1
            Σ += A[i, j] * x[j]
        end
        x[i] = (b[i] - Σ) / A[i, i]
    end
    return x
end

A = [1. 2. 3.; 1. 2. 4.; 2. 2. 2.]
b = [1., 2., 3.]
print(trianginf(A, b))