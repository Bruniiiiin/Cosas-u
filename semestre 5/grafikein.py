import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('dateins.txt')

l = datos[:, 0]
t = datos[:, 1]
t2 = t ** 2

#Ajuste lienal

m, b = np.polyfit(l, t2, 1)
t2_ajuste = m * l + b


#Grafico

plt.plot(l, t2_ajuste, color='red', label='Ajuste sobre $t^2$')
plt.scatter(l, t2, color='blue', label='Datos')
plt.title('Gráfica de Datos')
plt.xlabel('Longitud (m)')
plt.ylabel('Tiempo (s)')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.show()
print(f'Pendiente: {m:.6f}')
print(f'Intercepto: {b:.6f}')