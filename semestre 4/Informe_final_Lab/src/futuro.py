import numpy as np
import matplotlib.pyplot as plt

#Datos experimentales
datos = np.genfromtxt("src/datoslab.txt")
v = datos[:, 0]
b_mT = datos[:, 1]

res = 0.8
i = v / (2 * res)           # corriente por bobina [A]

#Pendiente experimental (ya obtenida)
alpha = 2.464e-4            # T/A

#Prediccion a futuro
i_futuro = np.linspace(max(i), max(i) * 1.5, 20)
b_futuro_T = alpha * i_futuro
b_futuro_mT = b_futuro_T * 1e3

#Ajuste en rango experimental
i_fit = np.linspace(min(i), max(i), 200)
b_fit_mT = alpha * i_fit * 1e3

#Grafico
plt.plot(i, b_mT, "o", label="Datos experimentales")
plt.plot(i_fit, b_fit_mT, "-", label="Modelo lineal")
plt.plot(i_futuro, b_futuro_mT, "s", label="Predicción futura")

plt.xlabel("Corriente $I$ [A]")
plt.ylabel("Campo magnético $B$ [mT]")
plt.grid(True)
plt.legend()
plt.show()


