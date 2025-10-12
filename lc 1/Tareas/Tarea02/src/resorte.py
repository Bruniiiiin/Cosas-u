import numpy as np
import matplotlib.pyplot as plt

datos4 = np.genfromtxt("Tareas\Tarea02\Compl\datos_resorte.txt")

x = datos4[:,0]
y = datos4[:,1]

plt.scatter(x, y)
plt.xlabel("Masa (g)")
plt.ylabel("Desplazamiento (cm)")
plt.title("Comportamiento de un resorte")
plt.grid()
plt.show()