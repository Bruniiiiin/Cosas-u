import numpy as np
import matplotlib.pyplot as plt

def deriv_adelantada(f, a, h=0.1):
    return (f(a+h)-f(a)) / h

def error_absoluto(a,b):
    return np.abs(a-b)

f = np.cos
def df(x): # derivada analítica
    return -np.sin(x)
a = 0.3

print("h | f | df | df_num")
for h in [1e-4, 1e-3, 1e-2, 1e-1]:
    df_num = deriv_adelantada(f, a=a, h=h)
    print(f"(h) | {f(a):.2f} | {df(a):.2f} | {df_num:.2f}")

h_list = np.geomspace(1e-20, 1e-1, 30)
df_num = deriv_adelantada(f, a=a, h=h_list)

plt.loglog(h_list, error_absoluto(df(a), df_num), marker='*')
plt.show()

# Comparación gráfica entre derivada analítica y numérica

f = np.cos
df = lambda x: -np.sin(x) # usamos lambda para definir funciones pequeñas

h = 0.001
a = np.linspace(-4,4,100)
df_num = (f(a+h) - f(a)) / h

plt.plot(a, df(a)) # derivada analítica
plt.plot(a, df_num, "*") # derivada numérica
plt.show()

# Derivada atrasada

def deriv_retrasada(f, a, h=0.1):
    return (f(a) - f(a-h)) / h

# Derivada centrada

def deriv_centrada(f, a, h=0.1):
    return (f(a+h) - f(a-h)) / (2*h)

# Segunda derivada centrada de tres puntos

def segunda_deriv_centrada(f, a, h=0.1):
    return (f(a+h) - 2*f(a) + f(a-h)) / (h**2)

