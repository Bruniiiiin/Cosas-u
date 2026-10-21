import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

datos5 = np.genfromtxt("Tareas\Tarea02\Compl\datos_car.txt")

theta = datos5[:,0]
t = datos5[:,1]
err = datos5[:,2]

x = 1 / np.sqrt(np.sin(theta))
y = t              

coef_polinomios = np.polyfit(x, y, 1)

polinomio = np.poly1d(coef_polinomios)

u = np.linspace(min(x), max(x), 100)

v = polinomio(u)

L = 0.95

m = coef_polinomios[0]

g = 2*L/m**2

delta_g = 2*L*err**2/m**4

plt.errorbar(x, y, yerr=err, fmt='o', color='blue', label='Datos')
plt.plot(u, v, "r-", color="green", linewidth=2, label="Ajuste lineal")
plt.xlabel("1/$\sqrt{sin(θ)}$")
plt.ylabel("t [s]")
plt.title("Gráfico de t vs 1/$\sqrt{sin(θ)}$")
plt.legend()
plt.grid()
plt.show()

print(f"Pendiente de la recta: m = {m:.3f}")
print(f"Gravedad calculada: g = {g:.3f} m/s²")
