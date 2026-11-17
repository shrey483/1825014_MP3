
import numpy as np
import matplotlib.pyplot as plt

# Transformed function
def g(t):
    if t >= 1:
        return 0.0

    return np.exp(-t/(1-t)) / (1-t)**2


# Composite Trapezoidal Rule
def trapezoidal(n):
    a = 0
    b = 1
    h = (b-a)/n

    total = (g(a) + g(b))/2

    for i in range(1, n):
        total += g(a + i*h)

    return h * total


# Composite Simpson's Rule
def simpson(n):
    a = 0
    b = 1
    h = (b-a)/n

    total = g(a) + g(b)

    for i in range(1, n):
        x = a + i*h

        if i % 2 == 0:
            total += 2*g(x)
        else:
            total += 4*g(x)

    return (h/3) * total


# Gauss-Legendre Quadrature
def gauss_legendre(n):
    x, w = np.polynomial.legendre.leggauss(n)

    # Transform nodes from [-1,1] to [0,1]
    t = (x + 1)/2

    integral = 0

    for i in range(n):
        integral += w[i] * g(t[i])

    return integral/2


# Exact analytical value
exact = 1.0

# Number of intervals / quadrature points
N = [2, 4, 8, 16, 32, 64]

trap_errors = []
simp_errors = []
gauss_errors = []

print("Comparison of Numerical Integration Methods")
print("---------------------------------------------")

print("N       Trapezoidal       Simpson       Gauss")

for n in N:

    trap = trapezoidal(n)
    simp = simpson(n)
    gauss = gauss_legendre(n)

    trap_errors.append(abs(exact - trap))
    simp_errors.append(abs(exact - simp))
    gauss_errors.append(abs(exact - gauss))

    print(n, trap, simp, gauss)


# Plot convergence
plt.figure(figsize=(8, 6))

plt.loglog(N, trap_errors, 'o-', label="Trapezoidal")
plt.loglog(N, simp_errors, 's-', label="Simpson")
plt.loglog(N, gauss_errors, '^-', label="Gauss-Legendre")

plt.xlabel("Number of intervals / points")
plt.ylabel("Absolute Error")

plt.title("Convergence of Numerical Integration Methods")

plt.legend()
plt.grid(True, which="both")

plt.show()
