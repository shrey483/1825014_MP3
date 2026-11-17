import numpy as np
import matplotlib.pyplot as plt

# Get function from user
print("Enter a complex function of z:")
print("Examples: z**2, 1/z, np.exp(z), z**3 + 2*z")

expression = input("Enter f(z) = ")

# Define the function
f = lambda z: eval(expression, {"z": z, "np": np})

# Generate grid
t = np.linspace(-2, 2, 400)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Original z-plane
ax = axes[0]

for x in np.linspace(-2, 2, 9):
    z = x + 1j*t
    ax.plot(z.real, z.imag, 'b')

for y in np.linspace(-2, 2, 9):
    z = t + 1j*y
    ax.plot(z.real, z.imag, 'b')

ax.set_title("Original z-plane")
ax.set_xlabel("Real part")
ax.set_ylabel("Imaginary part")
ax.grid()
ax.axis("equal")

# Transformed w-plane
ax = axes[1]

for x in np.linspace(-2, 2, 9):
    z = x + 1j*t
    w = f(z)
    ax.plot(w.real, w.imag, 'r')

for y in np.linspace(-2, 2, 9):
    z = t + 1j*y
    w = f(z)
    ax.plot(w.real, w.imag, 'r')

ax.set_title("Transformed w-plane: f(z) = " + expression)
ax.set_xlabel("Real part")
ax.set_ylabel("Imaginary part")
ax.grid()
ax.axis("equal")

plt.tight_layout()
plt.show()