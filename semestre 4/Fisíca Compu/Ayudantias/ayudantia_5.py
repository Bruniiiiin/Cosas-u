import numpy as np
import matplotlib.pyplot as plt
plt.style.use("dark_background")

m1, m2, l1, l2, g = 1, 1, 2, 1, 9.81

def f_vectorial(u, t, m1=m1, m2=m2, l1=l1, l2=l2):

    theta1, theta2, W1, W2 = u

    a = (m1 + m2) * l1**2
    b = m2 * l1 * l2 * np.cos(theta1 - theta2)
    c = m2 * l2**2
    d = m2 * l1 * l2 * (W2**2) * np.sin(theta1 - theta2) + l1 * g * (m1 + m2) * np.sin(theta1)
    e = -m2 * l1 * l2 * (W1**2) * np.sin(theta1 - theta2) + l2 * m2 * g * np.sin(theta2)
    return np.array([W1, W2, (-b / a) * (((d * b) / a - e) / (c - (b**2) / a)) - d / a, ((b * d) / a - e) / (c - (b**2) / a)])

from Rungekutta import runge_kutta_4

dt = 0.001
x0 = np.array([np.pi/4, np.pi/4, 0, 0]) #Condiciones iniciales [Theta1, Theta2, Omega1, Omega2]
t = np.linspace(0, 30, 1000) #Tiempo

runge_kutta_4(f_vectorial, x0, t)

sol = runge_kutta_4(f_vectorial, x0, t, m1, m2, l1, l2)

theta1 = sol[:, 0]
theta2 = sol[:, 1]
omega1 = sol[:, 2]
omega2 = sol[:, 3]

x1 = l1 * np.sin(theta1)
y1 = -l1 * np.cos(theta1)
x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)

plt.figure(figsize=(10, 6))
plt.plot(t, theta1, label='Theta 1 (rad)')
plt.plot(t, theta2, label='Theta 2 (rad)')
plt.title('Ángulos del Péndulo Doble vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.legend()
plt.show()

v1_x = l1*omega1*np.cos(theta1)
v2_x = v1_x + l2*omega2*np.cos(theta2)

v1_y = -l1*omega1*np.sin(theta1)
v2_y = v1_y -l2*omega2*np.sin(theta2)

#Energias Cineticas:
K1 = 0.5*m1*l1**2*omega1**2
K2 = 0.5*m2*(v2_x**2 + v2_y**2)

#Energia Potencial: 
U = m1*g*y1 + m2*g*y2 

#Energia Total:
E = K1 + K2 + U

#Grafico de espacio de fase

plt.figure(figsize=(6, 6))
plt.plot(theta1, omega1, label='Péndulo 1')
plt.plot(theta2, omega2, label='Péndulo 2')
plt.title('Espacio de Fase del Péndulo Doble')
plt.xlabel('Ángulo (rad)')
plt.ylabel('Velocidad Angular (rad/s)')
plt.legend()
plt.show()

#Grafico de la trayectoria

plt.figure(figsize=(8, 8))
plt.plot(x1, y1, label='Masa 1')
plt.plot(x2, y2, label='Masa 2')
plt.title('Trayectoria del Péndulo Doble')
plt.xlabel('Posición X (m)')
plt.ylabel('Posición Y (m)')
plt.legend()
plt.axis("equal")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t, E, label='Energía Total')
plt.title('Energía Total del Péndulo Doble vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Energía (J)')
plt.legend()
plt.show()