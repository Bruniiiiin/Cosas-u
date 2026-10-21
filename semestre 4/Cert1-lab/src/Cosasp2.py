import numpy as np
import matplotlib.pyplot as plt

coef_polinomios = np.polyfit(x, y, n)
#Ajustar un polinomio de grado n a los datos (x, y)

polinomio = np.poly1d(coef_polinomios)
#Crear una función polinómica a partir de los coeficientes obtenidos

u = np.linspace(min(x), max(x), 100)
#Generar 100 puntos equiespaciados entre el mínimo y máximo de x

v = polinomio(u)
#Evaluar el polinomio en los puntos generados

plt.scatter(x, y)
plt.plot(u, v, 'r-')
#Graficar los datos originales y el polinomio ajustado

#Extras para mas placer
plt.xlabel()
plt.ylabel()
plt.title()
plt.grid()