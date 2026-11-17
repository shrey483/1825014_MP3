import math 
import cmath

a = float(input("Enter Real Part: "))
b = float(input("Enter Imag Part: "))
z = complex(a,b)



n = int(input("Enter number of roots: "))

if n<0:
    print("negative numbers are not allowed")
elif n==0:
    print("0 roots")
else: 
    for k in range(n):
        r = abs(z)
        theta = cmath.phase(z)
        angle = (theta + 2 * math.pi * k ) / n
        mod = r**1/n 

        real = mod * math.cos(angle)
        imag = mod * math.sin(angle)

        root = complex(real,imag)
        print(f"\nRoot{k+1}")
        print(root)

        