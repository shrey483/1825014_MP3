
import numpy as np
import matplotlib.pyplot as plt

N = 256

L = 5

x = np.linspace(-L, L, N, endpoint=False)

f = np.exp(-x**2)

dx = x[1] - x[0]

F = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(f))) * dx

freq = np.fft.fftshift(np.fft.fftfreq(N, d=dx))

F_exact = np.sqrt(np.pi) * np.exp(-(np.pi*freq)**2)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, f)

plt.title("Original Gaussian Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()

plt.subplot(1, 2, 2)

plt.plot(freq, np.abs(F), label="Numerical FFT")
plt.plot(freq, F_exact, "--", label="Analytical FT")

plt.title("Fourier Transform")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

zero_index = N // 2

print("Numerical F(0) =", abs(F[zero_index]))
print("Analytical F(0) =", np.sqrt(np.pi))
