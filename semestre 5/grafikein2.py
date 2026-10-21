import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt('dateins.txt')

l = datos[:, 0]
t = datos[:, 1]

N = 7
T = t / N
T2 = T**2

# Ajuste lineal
m, b = np.polyfit(l, T2, 1)
T2_ajuste = m * l + b

# Gráfico
plt.scatter(l, T2, label='Datos')
plt.plot(l, T2_ajuste, label='Ajuste sobre $T^2$')
plt.title('Gráfica de $T^2$ vs Longitud')
plt.xlabel('Longitud (m)')
plt.ylabel('$T^2$ (s²)')
plt.legend()
plt.grid()
plt.show()

print(f'Pendiente: {m:.6f}')
print(f'Intercepto: {b:.6f}')

# Calcular g
g = (4 * np.pi**2) / m
print(f'Valor de g: {g:.4f} m/s²')

#Valores de t2

print(T2)