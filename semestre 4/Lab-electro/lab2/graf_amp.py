import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

ampolleta = np.genfromtxt("ampolleta.txt")
resis = np.genfromtxt("res_serie.txt")

Vol1 = ampolleta[:,0]
Corr1 = ampolleta[:,1]

Vol2 = resis[:,0]
Corr2 = resis[:,1]

print(227.5/32.6)

#Ajuste lineal
coef1 = np.polyfit(Corr1, Vol1, 1)
poly21 = np.poly1d(coef1)
print(poly21)

coef2 = np.polyfit(Corr2, Vol2, 1)
poly22 = np.poly1d(coef2)
print(poly22)

x = np.linspace(min(Corr1), max(Corr1), 100)
plt.plot(Corr1, Vol1, 'o', label="Datos ampolleta")
plt.plot(x, poly21(x), '-', label="Ajuste ampolleta")
plt.legend()

y = np.linspace(min(Corr2), max(Corr2), 100)
plt.plot(Corr2, Vol2, 'o', label="Datos Resistencia")
plt.plot(y, poly22(y), '-', label="Ajuste Resistencia")
plt.legend()

plt.xlabel("Corriente (A)")
plt.ylabel("Voltaje (V)")
plt.title("Voltaje vs Corriente")
plt.grid(True, color='0.7', linestyle='-.', linewidth=1)
plt.show()
