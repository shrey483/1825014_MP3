import numpy as np

def f(x):
    return np.exp(x)

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))

n = int(input("Enter number of points: "))

if n <= 0:
    print("Number of points must be positive.")

else:
    x, w = np.polynomial.legendre.leggauss(n)

    t = (b - a) / 2 * x + (a + b) / 2

    integral = (b - a) / 2 * np.sum(w * f(t))

    print("Gauss-Legendre Integral =", integral)

    exact = np.exp(b) - np.exp(a)

    print("Exact Integral =", exact)
    print("Absolute Error =", abs(exact - integral))
