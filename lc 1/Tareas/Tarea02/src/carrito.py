import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

datos5 = np.genfromtxt("Tareas\Tarea02\Compl\datos_car.txt")

theta = datos5[:,0]
t_p = datos5[:,1]

coef_polinomios = np.polyfit(theta, t_p, 1)

polinomio = np.poly1d(coef_polinomios)

u = np.linspace(min(theta), max(theta), 100)

v = polinomio(u)

print("Constante aceleracion de gravedad =", coef_polinomios[0], "m/s²S")

plt.scatter(theta, t_p)
plt.plot(u, v, "r-", color='green', linewidth=2)
plt.legend(["Datos experimentales", "Ajuste lineal"])
plt.xlabel("Ángulo (rad)")
plt.ylabel("Tiempo promedio (s)")
plt.title("Comportamiento de un carrito en un plano inclinado")
plt.grid()
plt.show()
