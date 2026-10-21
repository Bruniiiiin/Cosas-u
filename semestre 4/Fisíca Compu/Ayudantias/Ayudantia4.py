import numpy as np
import matplotlib.pyplot as plt



dt = 0.1
N = 1000
t = dt*np.arange(0,N) # intervalos de tiempo

def f(x,t): #definicion funcion vectorial
    O, w = x
    return np.array([w, -np.sin(O)])

x = np.zeros((N,2)) #matriz para guardar las soluciones
x[0] = np.pi/6 , 0 #condiciones iniciales 

for i in range(N-1): 
    x[i+1] = x[i] + f(x[i], i*dt)*dt 
    
O = x[:,0] #funcion solucion (posicion, theta)
w = x[:,1] #velocidad angular (omega)

plt.plot(t,O)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posicion (rad)')
plt.title('Pendulo Simple')
plt.grid()
plt.show()