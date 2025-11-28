import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("src\datoslab.txt")
v = datos[:, 0]
b = datos[:, 1]
res = 1.25

i = v / res

c = np.polyfit(i, b, 1)
m = np.poly1d(c)

print(f"Ecuación de la recta: B = {c[0]}*I + {c[1]}")
x = np.linspace(min(i), max(i), 100)

plt.plot(x, m(x), label="Ajuste Lineal", color="orange")

plt.plot(i, b, "o" ,label="Corriente vs Campo Magnético")
plt.xlabel("Campo Magnético (B)")
plt.ylabel("Corriente (I)")
plt.title("Relación entre Corriente y Campo Magnético")
plt.legend()
plt.grid()
plt.show()

mu = c[0] * 0.20 / 154 * (4 / 5) ** (-3 / 2)

print(mu)