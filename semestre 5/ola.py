import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('ola.txt')
x = datos[:, 0]
y = datos[:, 1]

error = np.loadtxt('olaerror.txt')

m, b = np.polyfit(x, y, 1)

ajuste = m * x + b

plt.plot(x, ajuste, color='red', label='Ajuste lineal')
plt.errorbar(x, y, yerr=error, fmt='o', ecolor='red', capsize=5)
plt.title('Grafico Voltaje vs carga')
plt.xlabel('q')
plt.ylabel('Voltaje')
plt.grid()
plt.show()