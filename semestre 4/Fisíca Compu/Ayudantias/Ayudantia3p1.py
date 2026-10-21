import numpy as np 
import matplotlib.pyplot as plt 


'''
Descargue los datos "Datos01.txt", corra este código y proponga una derivada finita numérica para aplicarla a los datos. Al correr el código tenga precaución de la ubicación del archivo de datos, del código y la ubicación en la que esta la terminal. 
'''


datos = np.genfromtxt("Datos01.txt", delimiter="\t", skip_header=2)

t = datos[:, 0]
Voltaje = datos[:, 1]
#dV_dt = ?
t_prime = (t[1:] + t[:-1]) / 2

#Calculo de la derivada finita
n = len(t)
dV_dt = np.zeros(n)

#Derivada centrada
dV_dt[1:-1] = (Voltaje[2:] - Voltaje[:-2]) / (t[2:] - t[:-2])

#Derivada en los extremos
dV_dt[0]  = (Voltaje[1] - Voltaje[0]) / (t[1] - t[0])
dV_dt[-1] = (Voltaje[-1] - Voltaje[-2]) / (t[-1] - t[-2])

#Comparamos con np.gradient
dV_dt_np = np.gradient(Voltaje, t)

plt.plot(t, dV_dt, "r-", label="dV/dt Centrado + extremos")
plt.plot(t, dV_dt_np, "k--", label="dV/dt Con numpy")
plt.scatter(t,Voltaje, label= 'Normal')
#plt.scatter(t_prime, dV_dt, label=r"$\frac{\Delta V}{\Delta t}$")

# Detalles del Canvas
plt.xlabel('t [s]')
plt.ylabel('[V]')
plt.legend()
#plt.xlim(0,1)
plt.legend()
plt.show()

with open("output.txt", "w") as file:
    for i in range(n):
        
        file.write(f"{t[i]}\t{np.log10(t[i])}\n")