import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

datos4 = np.genfromtxt("Tareas\Tarea02\Compl\datos_resorte.txt")

x = datos4[:,0]
y = datos4[:,1]

coef_polinomios = np.polyfit(x, y, 1)
#Ajustar un polinomio de grado n a los datos (x, y)

polinomio = np.poly1d(coef_polinomios)
#Crear una función polinómica a partir de los coeficientes obtenidos

u = np.linspace(min(x), max(x), 100)
#Generar 100 puntos equiespaciados entre el mínimo y máximo de x

v = polinomio(u)
#Evaluar el polinomio en los puntos generados

print("Constante elástica k =", coef_polinomios[0], "N/m")

plt.scatter(x, y)
plt.plot(u, v, "r-", color='green', linewidth=2)

plt.legend(["Datos experimentales", "Ajuste lineal"])
plt.xlabel("Masa (kg)")
plt.ylabel("Desplazamiento (m)")
plt.title("Comportamiento de un resorte")
plt.grid()
plt.show()