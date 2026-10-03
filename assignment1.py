import numpy as np

# Interpolation points
x_i = np.array([1.0, 10.0, 8.0])
y_i = np.array([3.0, 7.0, 5.0])


def lagrange(x, x_i, y_i):
    P = 0.0
    for i in range(len(x_i)):
        L_i = 1.0
        for j in range(len(x_i)):
            if i != j:
                L_i *= (x - x_i[j]) / (x_i[i] - x_i[j])
        P += y_i[i] * L_i
    return P


# Check the interpolation
for x, y in zip(x_i, y_i):
    print(f"P({x}) = {lagrange(x, x_i, y_i)}")
    print(f"Expected = {y}")
    print()

# Interpolation at x = 5
x = 5
print(f"P({x}) = {lagrange(x, x_i, y_i)}")