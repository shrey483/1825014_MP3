
import numpy as np
import matplotlib.pyplot as plt

N = 20

T = np.zeros((N + 1, N + 1))

T[N, 1:N] = 100

tolerance = 1e-5
max_iterations = 100000

for iteration in range(max_iterations):

    old_T = T.copy()

    for i in range(1, N):
        for j in range(1, N):

            T[i, j] = 0.25 * (
                T[i + 1, j] +
                T[i - 1, j] +
                T[i, j + 1] +
                T[i, j - 1]
            )

    error = np.max(np.abs(T - old_T))

    if error < tolerance:
        break

print("Number of iterations:", iteration + 1)
print("Final maximum change:", error)

plt.imshow(
    T,
    origin="lower",
    extent=[0, 1, 0, 1],
    cmap="hot",
    aspect="equal"
)

plt.colorbar(label="Temperature (°C)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Steady-State Temperature Distribution")
plt.show()
