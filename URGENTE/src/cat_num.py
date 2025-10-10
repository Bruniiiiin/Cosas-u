from factoriales import factorial_numpy
from factoriales import factorial_2n_numpy
from factoriales import factorial_n1_numpy 
import numpy as np
import matplotlib.pyplot as plt

#Primero calculamos el numero de catalan para N=15
N = 15

f = factorial_numpy(N, dtype=np.int32)[-1]        #Toma el ultimo elemento de la lista n!
f2n = factorial_2n_numpy(N, dtype=np.int32)[-1]   #Toma el ultimo elemento de la lista (2n)!
f_n1 = factorial_n1_numpy(N, dtype=np.int32)[-1]    #Toma el ultimo elemento de la lista (n+1)!

c_n = f2n / (f * f_n1) #Calcula el numero de catalan utilizando el ultimo elemento

print(c_n)  #podemos notar que por overflow nos da un numero negativo

###############################################################################

#Ahora calculamos y graficamos los numeros de catalan desde n=0 hasta n=15
fac = factorial_numpy(N, dtype=np.int32)        # lista de n!
fac2n = factorial_2n_numpy(N, dtype=np.int32)   # lista
fac_n1 = factorial_n1_numpy(N, dtype=np.int32)  # lista de (n+1)!

#Usa la longitud de cualquiera de las listas, en este caso de n!
L = len(fac)

#Definimos la lista vacia para ir guardando los num de catalan
cat=[]
for i in range(L):
    cat.append(fac2n[i] // (fac[i] * fac_n1[i]))

print(cat)  #podemos notar que por overflow nos da numeros negativos a partir de n=13

#Lo que nos grafica los numeros de catalan definiendolos solo con fun de numpy

plt.plot(cat, 'o-')
plt.title("Numeros de Catalan con 32 bits")
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("C_n")
plt.grid()
plt.show()