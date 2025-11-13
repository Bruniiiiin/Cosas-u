import numpy as np
import matplotlib.pyplot as plt

dat = np.genfromtxt("res_serie.txt")

V = dat[:,0]
I = dat[:,1]

plt.plot(V, I, 'o', label="Datos experimentales")
plt.xlabel("Voltaje (V)")
plt.ylabel("Corriente (A)")
plt.title("Corriente vs Voltaje en Resistencia en Serie")
plt.grid()
plt.show()