import numpy as np

def fit_line(xs, ys):

    x = np.array(xs, dtype=float) #convertir a array de numpy
    y = np.array(ys, dtype=float) # "" "" "" 

    mx = x.mean() #mx el promedio de x
    my = y.mean() #my el promedio de y
    mxx = (x * x).mean() #mxx el promedio de x^2
    mxy = (x * y).mean() #mxy el promedio de xy

    a1 = (mxy - mx * my) / (mxx - mx * mx) #pendiente
    a0 = my - a1 * mx #coef posicion

    y_fit = a0 + a1 * x #valores ajustados
    chi2 = np.sum((y - y_fit) ** 2) #suma de los errores al cuadrado

    return a0, a1, chi2, y_fit #retorna coef posicion, pendiente, suma de errores al cuadrado y valores ajustados

#Por si lo piden aqui esta :p