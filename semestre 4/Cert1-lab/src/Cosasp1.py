import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt("Datos.txt") #Extraer datos como una matriz
x = datos[:,0] #Extraer la primera columna
y = datos[:,1] #Extraer la segunda columna

promedio = np.mean(y) #Calcular el promedio de y
desviacion = np.std(y) #Calcular la desviacion estandar de y

#########################################################################################

plt.errorbar(x, y , yerr=0.2, fmt='o')#Grafica los datos con barras de error

plt.hist(y, bins=10)#Grafica un histograma de los datos

plt.scatter(x, y)#Grafica los datos como puntos

plt.xscale('log')#Escala logaritmica en x
plt.yscale('log')#Escala logaritmica en y

plt.show()#Muestra las graficas

