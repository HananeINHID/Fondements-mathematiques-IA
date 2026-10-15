
import math


def f(x):
    return math.exp(-(x ** 2))


a = 0
b = 1
I_exact = math.sqrt(math.pi) / 2 * math.erf(1)


def absolute_error(approx):
    return abs(I_exact - approx)


# Trapezoidal rule
I_trap_simple = (b - a) / 2 * (f(a) + f(b))

print("Reference value:", I_exact)
print("\nSimple trapezoid")
print("Result :", I_trap_simple)
print("Error:", absolute_error(I_trap_simple))


def trapezoid_rule(n):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2

    for i in range(1, n):
        x = a + i * h
        total += f(x)

    return h * total


print("\n Composite trapezoid")
for n in [4, 6]:
    value = trapezoid_rule(n)
    print("n =", n)
    print("Result:", value)
    print("Error:", absolute_error(value))


# Simpson's rule
I_simpson_simple = (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

print("\nSimple Simpson")
print("Result:", I_simpson_simple)
print("Error:", absolute_error(I_simpson_simple))


def simpson_rule(n):
    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)

    return (h / 3) * total


print("\n Composite Simpson")
for n in [4, 6]:
    value = simpson_rule(n)
    print("n =", n)
    print("Result:", value)
    print("Error:", absolute_error(value))
