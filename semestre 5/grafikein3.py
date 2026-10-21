import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
datos = np.loadtxt('dateins.txt')
l = datos[:, 0]
t = datos[:, 1]

# Número de oscilaciones
N = 7

# Calcular T y T^2
T = t / N
T2 = T**2

# Ajuste lineal CON covarianza
coef, cov = np.polyfit(l, T2, 1, cov=True)
m, b = coef

# Error de la pendiente
sigma_m = np.sqrt(cov[0][0])

# Recta de ajuste
T2_ajuste = m * l + b

# Calcular g y su error
g = (4 * np.pi**2) / m
sigma_g = (4 * np.pi**2 / m**2) * sigma_m

# Gráfico
plt.scatter(l, T2, label='Datos')
plt.plot(l, T2_ajuste, label='Ajuste lineal')
plt.title('Gráfica de $T^2$ vs Longitud')
plt.xlabel('Longitud (m)')
plt.ylabel('$T^2$ (s²)')
plt.legend()
plt.grid()
plt.show()

# Resultados
print(f'Pendiente: {m:.6f} ± {sigma_m:.6f}')
print(f'Intercepto: {b:.6f}')
print(f'g = {g:.4f} ± {sigma_g:.4f} m/s²')