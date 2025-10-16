import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

ampolleta = np.genfromtxt("ampolleta.txt")

Vol = ampolleta[:,0]
Corr = ampolleta[:,1]

#Cálculo de promedios
print(np.mean(Vol))
print(np.mean(Corr))

#Ajuste lineal
coef = np.polyfit(Corr, Vol, 1)
poly = np.poly1d(coef)
print(poly)

x = np.linspace(min(Corr), max(Corr), 100)
plt.plot(Corr, Vol, 'o', label="Datos experimentales")
plt.plot(x, poly(x), '-', label="Ajuste polinómico")
plt.xlabel("Voltaje (V)")
plt.ylabel("Corriente (A)")
plt.title("Corriente vs Voltaje en Ampolleta")
plt.grid(True, color='0.7', linestyle='-.', linewidth=1)
plt.show()
