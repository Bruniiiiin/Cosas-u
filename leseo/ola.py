import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.special import jn, jn_zeros

# 1. Parámetros físicos y de la malla
R = 1.0          # Radio del disco
alpha = 0.5      # Difusividad térmica (aumentada para acelerar la animación)
T_prom = 1.0     # Temperatura promedio
rho0 = 0.75 * R  # Posición inicial rho (3R/4)
phi0 = 0.0       # Posición inicial phi (0 rad)

r = np.linspace(0, R, 80)
theta = np.linspace(0, 2*np.pi, 80)
R_grid, Theta_grid = np.meshgrid(r, theta)

# 2. Precomputar ceros de Bessel para ahorrar tiempo en la animación
M_terms = 15
N_terms = 15
ceros_bessel = np.zeros((M_terms, N_terms))
for m in range(M_terms):
    ceros_bessel[m, :] = jn_zeros(m, N_terms)

# 3. Configurar la figura polar
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(6, 6))
fig.canvas.manager.set_window_title('Difusión de Calor')

# 4. Función de actualización para cada "frame" del GIF
def actualizar(frame):
    ax.clear()
    
    # El tiempo avanza con cada frame
    t = frame * 0.02 
    
    # Para t=0 exacto la serie diverge (Delta de Dirac), partimos de un t muy pequeño
    if t == 0:
        t = 0.001 
        
    Z = np.zeros_like(R_grid)
    
    # Cálculo de la doble sumatoria
    for m in range(M_terms):
        for n in range(N_terms):
            alpha_mn = ceros_bessel[m, n]
            
            J_m_rho0 = jn(m, alpha_mn * rho0 / R)
            J_m_rho = jn(m, alpha_mn * R_grid / R)
            denominador = (jn(m+1, alpha_mn))**2
            
            exponencial = np.exp(- (alpha * alpha_mn / R)**2 * t)
            
            if m == 0:
                angular = 1.0 
            else:
                angular = 2 * np.cos(m * (Theta_grid - phi0))
                
            termino = (angular * J_m_rho0 * J_m_rho / denominador) * exponencial
            Z += termino
            
    # Dibujar el contorno. 
    # vmin y vmax se fijan para que la escala de colores no "salte" entre frames
    contorno = ax.contourf(Theta_grid, R_grid, Z, 40, cmap='inferno', vmin=0, vmax=3.0)
    
    ax.set_title(f"Evolución térmica | Tiempo t = {t:.3f}\n", fontsize=14)
    ax.set_yticklabels([]) # Ocultar los números de los radios para que quede limpio
    ax.grid(alpha=0.3)
    

    return contorno,

# 5. Crear y guardar la animación
print("Generando animación... (esto tomará unos segundos)")
ani = animation.FuncAnimation(fig, actualizar, frames=60, interval=100, blit=False)

# Guardar como GIF usando Pillow (viene por defecto con matplotlib)
ani.save('difusion_calor.gif', writer='pillow', fps=15)
print("¡GIF guardado con éxito como 'difusion_calor.gif'!")