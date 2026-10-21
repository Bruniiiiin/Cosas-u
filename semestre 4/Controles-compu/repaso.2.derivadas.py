import numpy as np
import matplotlib.pyplot as plt

# ej 1

def deriv_adelantada(f, a, h):
	return (f(a+h) - f(a)) / h

f = np.cos
a = 0.3
df = lambda x: -np.sin(x)

print("h | df | df_num | error")
for h in [1e-1, 1e-2, 1e-3, 1e-4]:
	print(f"{h} | {df(a)} | {deriv_adelantada(f, a, h)} | {np.abs(df(a) - deriv_adelantada(f,a,h))}")
	
# ej 2

def deriv_centrada(f, a, h):   # a tres puntos
	return (f(a+h) - f(a-h)) / (2*h)

print("h | df | df_num | error")
for h in [1e-1, 1e-2, 1e-3, 1e-4]:
    print(f"{h} | {df(a)} | {deriv_centrada(f, a, h)} | {np.abs(df(a) - deriv_centrada(f,a,h))}")
	
# claramente la centrada tiene mucha mas precision con error del orden de 10^{-10} para h=1e-4 comparado con 10^{-5} de la adelantada

# ej 3

def error_absoluto(a,b):
	return np.abs(a-b)

h_list = np.geomspace(1e-10, 1e-1, 30)
df_num = deriv_adelantada(f, a, h_list)
plt.loglog(h_list, error_absoluto(df(a), df_num))
plt.show()

# para cierto h pequeño el programa falla debido a errores de redondeo

# Derivada segunda centrada de tres puntos

def segunda_deriv_centrada(f, a, h=0.1):
    return (f(a+h) - 2*f(a) + f(a-h)) / (h**2)