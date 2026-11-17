
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Enter number of intervals: "))

if N < 2:
    raise ValueError("Enter at least 2 intervals.")

h = 1.0 / N

x = np.linspace(0, 1, N + 1)

A = np.zeros((N, N))
B = np.zeros(N)

for i in range(1, N):

    row = i - 1

    A[row, row] = -(2 + h**2)

    if i == 1:
        B[row] = -1
    else:
        A[row, row - 1] = 1

    A[row, row + 1] = 1

A[N-1, N-2] = 2
A[N-1, N-1] = -(2 + h**2)

y_unknown = np.linalg.solve(A, B)

y = np.concatenate(([1.0], y_unknown))

y_exact = np.cosh(1 - x) / np.cosh(1)

print("\nResults:")
print("Position     Numerical     Analytical")

for i in range(N + 1):
    print(f"{x[i]:.3f}        {y[i]:.6f}       {y_exact[i]:.6f}")

print("\nMaximum absolute error:",
      np.max(np.abs(y - y_exact)))

plt.plot(x, y, 'o-', label="Finite Difference")
plt.plot(x, y_exact, '--', label="Analytical Solution")

plt.xlabel("Position x")
plt.ylabel("Concentration y(x)")
plt.title("Reaction-Diffusion Boundary Value Problem")

plt.legend()
plt.grid()
plt.show()
