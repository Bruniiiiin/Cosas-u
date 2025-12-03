import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt(r"src\datoslab.txt")
v = datos[:, 0]    # V [V]
b = datos[:, 1]    # B en mT

# ---- 1) Conversion mT -> T para el FIT ----
b_T = b * 1e-3       # ahora B está en tesla [T]

res = 0.8            # ohm
i = v / res          # corriente en A

# Ajuste lineal B = m*I + n
c, cov = np.polyfit(i, b_T, 1, cov=True)
m = c[0]
n = c[1]

print(f"Ecuación: B = {m:.6e} * I + {n:.6e}  (B en T, I en A)")

# ---- 2) Gráfico (en mT) ----
x = np.linspace(min(i), max(i), 200)
B_fit_mT = (m * x + n) * 1e3   # convertir el ajuste de T -> mT

plt.plot(i, b, "o", label="Datos")
plt.plot(x, B_fit_mT, label="Ajuste Lineal")

plt.xlabel("Corriente $I$ [A]")
plt.ylabel("Campo magnético $B$ [mT]")

plt.grid(True)
plt.legend()
plt.show()

# ---- 3) mu0 experimental (usa la pendiente en Tesla/A) ----
N = 77
R = 0.20
mu0_exp = m * R / N * (4/5)**(-3/2)

print(f"mu0 experimental = {mu0_exp:.6e} H/m")
