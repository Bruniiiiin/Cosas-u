import numpy as np
def runge_kutta(f, u, t, h=0.01):

    for n in range(t.size - 1):
        k1 = f(u[n], t[n])
        k2 = f(u[n] + 0.5*h*k1, t[n] + 0.5*h)
        k3 = f(u[n] + 0.5*h*k2, t[n] + 0.5*h)
        k4 = f(u[n] + h*k3, t[n] + h)

        u[n+1] = u[n] + (h/6)*(k1 + 2*k2 + 2*k3 + k4) 
    return u

# Con N y h a gusto del consumidor. 
# x = np.zeros(N)
# x[0] = 1
# x = runge_kutta(f, x, t ,h)

#También es posible realizar una forma un poco más generalizada del método de Runge-Kutta de 4to orden que admite tanto argumentos extra como variables complejas.

def runge_kutta_4(f, u0, t, *args, **kwargs):
    """
    Resuelve una ecuación diferencial ordinaria (EDO) utilizando el método de Runge-Kutta de cuarto orden.

    Args:
        f: La función que define la EDO, de la forma f(u, t, *args, **kwargs).
        u0: El valor inicial de la variable dependiente (u) en el tiempo t[0].
        t: Un array de NumPy que representa los puntos de tiempo en los que se desea calcular la solución.
        *args: Argumentos adicionales para pasar a la función f.
        **kwargs: Argumentos de palabra clave adicionales para pasar a la función f.

    Returns:
        Un array de NumPy que contiene la solución aproximada de la EDO en los puntos de tiempo especificados en t.
    """
    N = len(t) #Size of the time array
    u = np.zeros([N, len(u0)], dtype=u0.dtype) # Initialize u as a 2D array
    dt = t[1] - t[0] #Consistent time step among the time array
    u[0] = u0 # Set the initial condition

    for n in range(N - 1):
        
        k1 = f(u[n], t[n], *args, **kwargs)
        k2 = f(u[n] + 0.5 * dt * k1, t[n] + 0.5 * dt, *args, **kwargs)
        k3 = f(u[n] + 0.5 * dt * k2, t[n] + 0.5 * dt, *args, **kwargs)
        k4 = f(u[n] + dt * k3, t[n] + dt, *args, **kwargs)

        u[n + 1] = u[n] + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return u