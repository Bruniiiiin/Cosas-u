import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt(r"src\datoslab.txt")
v = datos[:, 0]    # V [V]
b = datos[:, 1]    # B en mT

# conversion mT -> T
b = b * 1e-3       # ahora B está en tesla [T]

res = 0.8         # ohm
i = v / res        # corriente en A

c, cov = np.polyfit(i, b, 1, cov=True)   # B = m*I + n
m = c[0]; n = c[1]

print(f"Ecuación: B = {m:.6e} * I + {n:.6e}  (B en T, I en A)")

# grafico
x = np.linspace(min(i), max(i), 100)
plt.plot(x, m*x + n, label="Ajuste Lineal")
plt.plot(i, b, "o", label="Datos")
plt.xlabel("Corriente (I) [A]")
plt.ylabel("Campo magnético (B) [T]")
plt.legend(); plt.grid(); plt.show()

# calculo mu0 experimental (Helmholtz)
N = 77
R = 0.20
mu0_exp = m * R / N * (4/5)**(-3/2)
print(f"mu0 experimental = {mu0_exp:.6e} H/m")

