from factoriales import factorial 
from factoriales import factorial_2n
from factoriales import factorial_n1

import matplotlib.pyplot as plt

#Primero calculamos el numero de catalan para N=15
N = 15

f = factorial(N)[-1]        #Toma el ultimo elemento de la lista n!
f2n = factorial_2n(N)[-1]   #Toma el ultimo elemento de la lista (2n)!
f_n1 = factorial_n1(N)[-1]  #Toma el ultimo elemento de la lista (n+1)!

c_n = f2n / (f * f_n1) #Calcula el numero de catalan utilizando el ultimo elemento

print(c_n)

###############################################################################

#Ahora calculamos y graficamos los numeros de catalan desde n=0 hasta n=15
fac = factorial(N)        # lista de n!
fac2n = factorial_2n(N)   # lista de (2n)!
fac_n1 = factorial_n1(N)  # lista de (n+1)!

#Usa la longitud de cualquiera de las listas, en este caso de n!
L = len(fac)

#Definimos la lista vacia para ir guardando los num de catalan
cat=[]

for i in range(L):
    cat.append(fac2n[i] // (fac[i] * fac_n1[i]))
print(cat)

#Lo que nos grafica los numeros de catalan definiendolos solo con fun de python
plt.plot(cat, 'o-')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('C_n')
plt.title('Números de Catalán')
plt.grid()
plt.show()