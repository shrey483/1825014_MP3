
import numpy as np
import matplotlib.pyplot as plt

L = float(input("Enter length of bar: "))
T1 = float(input("Enter left-end temperature: "))
T2 = float(input("Enter right-end temperature: "))
N = int(input("Enter number of divisions: "))

if L <= 0 or N < 2:
    raise ValueError("L must be positive and N >= 2")

x = np.linspace(0, L, N + 1)

T = np.linspace(T1, T2, N + 1)

T[0] = T1
T[-1] = T2

tolerance = 1e-8

for iteration in range(100000):

    old_T = T.copy()

    for i in range(1, N):
        T[i] = (T[i-1] + T[i+1]) / 2

    error = np.max(np.abs(T - old_T))

    if error < tolerance:
        break

T_exact = T1 + (T2 - T1) * x / L

print("\nPosition    Numerical T    Exact T")

for i in range(N + 1):
    print(f"{x[i]:.3f}       {T[i]:.3f}       {T_exact[i]:.3f}")

print("\nIterations:", iteration + 1)
print("Maximum error:", np.max(np.abs(T - T_exact)))

plt.plot(x, T, 'o-', label="Finite Difference")
plt.plot(x, T_exact, '--', label="Analytical")

plt.xlabel("Position along bar (m)")
plt.ylabel("Temperature (°C)")
plt.title("Equilibrium Temperature Distribution")
plt.legend()
plt.grid()

plt.show()
