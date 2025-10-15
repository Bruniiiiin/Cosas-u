import numpy as np
import matplotlib.pyplot as plt

datos5 = np.genfromtxt("Tareas\Tarea02\Compl\datos_carrito.txt")

theta = datos5[:,0] 
t = datos5[:,1]
l = 0.94 #m
d = l * np.sin(theta)

plt.scatter(d, t)
plt.xlabel("ns")
plt.ylabel("Tiempo (s)")
plt.title("Comportamiento de un carrito")
plt.grid()
plt.show()

#########################

import numpy as np
import matplotlib.pyplot as plt

datos5 = np.genfromtxt("Tareas\Tarea02\Compl\datos_carrito.txt")
theta = datos5[:,0]
t = datos5[:,1]

l = 0.94  # m

s = np.sin(theta)

#aceleración a partir de s = 1/2 a t^2 -> a = 2 s / t^2
#aquí usamos la distancia recorrida l (constante) proyectada: s = l*sin(theta)

a = 2 * (l * s) / (t**2)

#ajuste lineal simple a = g * sin(theta)
coef = np.polyfit(s, a, 1)  # [g, intercept]
g = coef[0]

# gráfica simple
plt.figure(figsize=(6,4))
plt.scatter(s, a, s=50, edgecolor='k', label='datos')
s_line = np.linspace(s.min(), s.max(), 100)
plt.plot(s_line, np.polyval(coef, s_line), color='C1', label=f'ajuste: g={g:.3f} m/s²')
plt.xlabel('sin(θ)')
plt.ylabel('Aceleración (m/s²)')
plt.title('Aceleración vs sin(θ)')
plt.grid()
plt.show()