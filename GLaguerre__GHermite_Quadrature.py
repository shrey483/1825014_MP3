
import numpy as np

print("Numerical Integration")
print("1. Gauss-Laguerre Quadrature")
print("2. Gauss-Hermite Quadrature")

choice = int(input("Enter your choice: "))

n = int(input("Enter number of quadrature points: "))

if n <= 0:
    print("Number of points must be positive.")

elif choice == 1:

    # Gauss-Laguerre method
    x, w = np.polynomial.laguerre.laggauss(n)

    # Function f(x) = x^2
    integral = np.sum(w * x**2)

    # Analytical result
    exact = 2.0

    print("\nGauss-Laguerre Method")
    print("Numerical Integral =", integral)
    print("Analytical Integral =", exact)
    print("Absolute Error =", abs(exact - integral))

elif choice == 2:

    # Gauss-Hermite method
    x, w = np.polynomial.hermite.hermgauss(n)

    # Function f(x) = x^2
    integral = np.sum(w * x**2)

    # Analytical result
    exact = np.sqrt(np.pi) / 2

    print("\nGauss-Hermite Method")
    print("Numerical Integral =", integral)
    print("Analytical Integral =", exact)
    print("Absolute Error =", abs(exact - integral))

else:
    print("Invalid choice")
