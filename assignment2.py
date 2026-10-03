
import numpy as np
import matplotlib.pyplot as plt


# 1. Functions and their derivatives

def f1(x):
    return np.exp(x)

def df1(x):
    return np.exp(x)

def f2(x):
    return np.sin(x)

def df2(x):
    return np.cos(x)


# 2. Lagrange interpolation

def lagrange(x, x_i, y_i):
    n = len(x_i)
    P = 0.0

    for i in range(n):
        L = 1.0

        for j in range(n):
            if i != j:
                L *= (x - x_i[j]) / (x_i[i] - x_i[j])

        P += y_i[i] * L

    return P


# 3. Newton interpolation

def newton(x, x_i, y_i):
    n = len(x_i)
    P = y_i[0]

    for i in range(1, n):
        f = y_i.copy()

        for j in range(1, i + 1):
            for k in range(n - j):
                f[k] = (
                    (f[k + 1] - f[k])
                    / (x_i[k + j] - x_i[k])
                )

        prod = 1.0

        for j in range(i):
            prod *= (x - x_i[j])

        P += f[0] * prod

    return P


# 4. Hermite interpolation

def hermite(x, x_i, y_i, dy_i):
    n = len(x_i)
    P = 0.0

    for i in range(n):

        # Calculation of L_i(x)
        L = 1.0

        for j in range(n):
            if i != j:
                L *= (x - x_i[j]) / (x_i[i] - x_i[j])

        # Calculation of L_i'(x_i)
        dL = 0.0

        for j in range(n):
            if i != j:
                dL += 1.0 / (x_i[i] - x_i[j])


        H = (1 - 2 * (x - x_i[i]) * dL) * L**2
        K = (x - x_i[i]) * L**2

        # the Hermite polynomial
        P += y_i[i] * H + dy_i[i] * K

    return P



# 5. Comparison of the three methods

def comparer(f, df, nom, a, b):

    nombres_points = [3, 5, 8, 12]

    x_plot = np.linspace(a, b, 500)
    y_original = f(x_plot)

    print("\nFunction:", nom)
    print("-" * 75)
    print("Points | Lagrange Error | Newton Error | Hermite Error")
    print("-" * 75)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()

    for k, n in enumerate(nombres_points):

        # Interpolation points
        x_i = np.linspace(a, b, n)
        y_i = f(x_i)
        dy_i = df(x_i)

        # Calculation of the polynomials
        P_L = np.array([
            lagrange(x, x_i, y_i) for x in x_plot
        ])

        P_N = np.array([
            newton(x, x_i, y_i) for x in x_plot
        ])

        P_H = np.array([
            hermite(x, x_i, y_i, dy_i) for x in x_plot
        ])

        # Calculation of the maximum errors
        E_L = np.max(np.abs(y_original - P_L))
        E_N = np.max(np.abs(y_original - P_N))
        E_H = np.max(np.abs(y_original - P_H))

        print(
            f"{n:6d} | {E_L:15.6e} | "
            f"{E_N:13.6e} | {E_H:13.6e}"
        )

       
        ax = axes[k]

        ax.plot(x_plot, y_original, label="Original function")
        ax.plot(x_plot, P_L, "--", label="Lagrange")
        ax.plot(x_plot, P_N, ":", label="Newton")
        ax.plot(x_plot, P_H, "-.", label="Hermite")
        ax.scatter(x_i, y_i, s=20, label="Points")

        ax.set_title(f"{nom} - {n} points")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.legend(fontsize=8)

    plt.tight_layout()
    plt.show()


# 6. Execution

comparer(f1, df1, "exp(x)", 0, 1)

comparer(f2, df2, "sin(x)", 0, np.pi)