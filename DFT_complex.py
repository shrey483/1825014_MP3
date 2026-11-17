
import math
import cmath

N = int(input("Enter number of data points: "))

if N <= 0:
    print("Number of data points must be positive.")

else:
    x = []

    print("Enter the signal values:")

    for i in range(N):
        value = float(input("x[" + str(i) + "] = "))
        x.append(value)

    X = []

    for k in range(N):

        total = 0

        for n in range(N):

            angle = -2 * math.pi * k * n / N

            total += x[n] * cmath.exp(1j * angle)

        X.append(total)

    print("\nDiscrete Fourier Transform:")

    for k in range(N):
        print("X[", k, "] =", X[k])
        print("Magnitude =", abs(X[k]))
        print("Phase =", cmath.phase(X[k]))
        print()
