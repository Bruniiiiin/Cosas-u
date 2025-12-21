import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("\\Users\\Catazla\\Desktop\\Universidad\\Lab I\\src\\datoslab.txt")
v = datos[:, 0]
b = datos[:, 1]
res = 1.25

i = v / res

c = np.polyfit(i, b, 1)
m = np.poly1d(c)

print(f"Ecuación de la recta: B = {c[0]}*I + {c[1]}")
x = np.linspace(min(i), max(i), 100)

plt.plot(x, m(x), label="Ajuste Lineal", color="orange")

plt.errorbar(i, b,yerr=0.005,fmt=".",label="Corriente vs Campo Magnético")
plt.xlabel("Campo Magnético (B)")
plt.ylabel("Corriente (I)")
plt.title("Relación entre Corriente y Campo Magnético")
plt.legend()
plt.grid()
plt.show()

mu = c[0] * 0.20 / 154 * (4 / 5) ** (-3 / 2)

print(mu)

res= b-(c[1]+c[0]*i)

plt.scatter(i,res,marker=".")
plt.grid(True)
plt.xlabel("Campo Magnético")
plt.ylabel("Corriente - Valores del Modelo")
plt.title("Gráfico del Residuo")
plt.grid()
plt.show()

sigma = 0.005
w = np.ones_like(i) / sigma  
coef, matriz = np.polyfit(i, b, 1, w=w, cov="unscaled")

sigma_b1, sigma_b0 = np.sqrt(np.diagonal(matriz))
print("desv. estándar coef. de posición =", sigma_b0)
print("desv. estándar de pendiente =", sigma_b1)