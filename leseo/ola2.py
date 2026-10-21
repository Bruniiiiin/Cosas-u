import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jn_zeros

# Parámetros del problema
R = 1.0          # Radio del disco
alpha = 0.1      # Difusividad térmica
T_prom = 1.0     # Temperatura promedio (T barra)
rho0 = 0.75 * R  # Posición inicial rho (3R/4)
phi0 = 0.0       # Posición inicial phi

# Configuración de la malla polar
r = np.linspace(0, R, 100)
theta = np.linspace(0, 2*np.pi, 100)
R_grid, Theta_grid = np.meshgrid(r, theta)

# Tiempos representativos a graficar
tiempos = [0.01, 0.1, 0.5, 2.0]

# Precomputar ceros de Bessel
M_terms = 15
N_terms = 15
ceros_bessel = np.zeros((M_terms, N_terms))
for m in range(M_terms):
    ceros_bessel[m, :] = jn_zeros(m, N_terms)

fig, axes = plt.subplots(1, 4, subplot_kw=dict(projection='polar'), figsize=(20, 5))

for idx, t in enumerate(tiempos):
    Z = np.zeros_like(R_grid)
    
    # Doble sumatoria de la serie de Fourier-Bessel
    for m in range(M_terms):
        for n in range(N_terms):
            alpha_mn = ceros_bessel[m, n]
            
            # Coeficientes simplificados (absorbiendo constantes)
            J_m_rho0 = jn(m, alpha_mn * rho0 / R)
            J_m_rho = jn(m, alpha_mn * R_grid / R)
            denominador = (jn(m+1, alpha_mn))**2
            
            # Factor de atenuación temporal
            exponencial = np.exp(- (alpha * alpha_mn / R)**2 * t)
            
            # Parte angular
            if m == 0:
                angular = 1.0  # El modo m=0 no tiene factor 2
            else:
                angular = 2 * np.cos(m * (Theta_grid - phi0))
                
            termino = (angular * J_m_rho0 * J_m_rho / denominador) * exponencial
            Z += termino
            
    # Graficar
    c = axes[idx].contourf(Theta_grid, R_grid, Z, 50, cmap='inferno')
    axes[idx].set_title(f"Tiempo t = {t}")
    axes[idx].set_yticklabels([]) # Ocultar etiquetas radiales
    plt.colorbar(c, ax=axes[idx], fraction=0.046, pad=0.04)

plt.tight_layout()
plt.show()