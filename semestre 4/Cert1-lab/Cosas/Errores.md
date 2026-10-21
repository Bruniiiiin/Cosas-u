# Exactitud, precisión y sensibilidad
* La exactitud se define como el grado de condordancia entre el valor "verdadero" y el experimental.

* La precision hace referncia a la concordancia entre las medidas

* La sensibilidad es la capacidad de un instrumento  de medida para apreciar cambios en la magnitud que se mide.

# Error
Diferencia entre el valor medido y el "real"

# Error sistematico
Es el error que es constante a lo largo de todo el proceso de medida.

* Error instrumental: Error de calibrado en instrumentos.

* Error Humano: Problemas de tipo visual o paralaje.

* Error método de medida: Mala eleccion del metodo de medida.

# Error aleatorio
Aquellas que se deben a las pequeñas variaciones que aparecen entre observaciones sucesivas bajo las mismas condiciones.

# Error aparato de medida
Es la mitad de la sensibilidad del instrumento.

# Notación de errores
Cuando indiquemos el resultado de una medida tendremos que indicar siempre el grado de error de la misma: $x \pm \Delta x$

# Error absoluto y relativo
* El error absoluto se define como la diferencia entre el valor real y el aproximado: $\varepsilon_a = |X - X_i|$

* El Error relativo es el cociente entre el error absoluto y el valor medido: $\varepsilon_r = \dfrac{\varepsilon_a}{X}$

# Cifras significativas
Es un digito que aporta informacion a una medicion real, dando precision.

# Medidas estadisticas
* Media: np.mean(x)

* Mediana.

* Moda.

* La varianza es una medida de dispersión que representa la variabilidad de los datos respecto a la media:  $\\ \sigma^2 = \dfrac{1}{N} \displaystyle \sum_{i=1}^N (x_i - \bar{x})^2$ 

* La desviacion estándar es la medida cuantitativa de las dimensiones de los errores aleatorios, es decir, la dispercion estadística y se define como la raiz cuadrada de la varianza.

* El error estándar del promedio es el error asociado a cuanto varian los promedios de distintas muestras en una misma poblacion, y para medidas sacadas a partir de una serie de datos $\bar{x} \pm \delta x$  y la formula para calcular el error estandar del promedio será: $\delta x = \dfrac{\sigma}{\sqrt{N}}$

# Incertidumbres en las funciones
* Sera el error propagado en una funcion: $\delta f = |f_x \delta x|+|f_y \delta y|$ 
* Para variables independientes: $\delta f = \sqrt{|f_x \delta x|+|f_y \delta y|}$

# Método mínimos cuadrados

Primero tenemos que:

* Datos: $$(x_i, y_i) \quad ; \quad i = 1, \dots , N$$ 

* Recta: $$f(x) = a_0 + a_1x$$

Se define como: 

$$\begin{align}                                                                                         \chi^2 &= \displaystyle \sum_{i=1}^N (y_i - f(x_i))^2 \\                                                \chi(a_0, a_1)^2 &= \displaystyle \sum_{i=1}^N (y_i - a_0 - a_1 x_i)^2 \\                               \end{align}$$

Ahora a esta funcion $$\chi(a_0, a_1)^2$$ la queremos minimizar utilizando el gradiente y luego igualamos a 0 (optimizacion):

$$\dfrac{\partial \chi^2}{\partial x} = -2 \displaystyle \sum_{i=1}^N (y_i - a_0 - a_1 x_i)^2 \qquad , \qquad \dfrac{\partial \chi^2}{\partial y} = -2 \displaystyle \sum_{i=1}^N (y_i - a_0 - a_1 x_i)^2 x_i$$

Luego igualando a 0 ambas ecuaciones: 

$$\displaystyle \sum_{i=1}^N y_i - a_0\sum_{i=1}^N 1 - a_1\left(\sum_{i=1}^N x_i\right) = 0$$

$$\displaystyle \sum_{i=1}^N (y_i) - a_0\left(\displaystyle \sum_{i=1}^N 1\right) - a_1\left(\displaystyle \sum_{i=1}^N (x_i)^2\right) = 0$$

Si dividimos todo por el numero de datos y consideramos que $$\dfrac{\displaystyle \sum_{i=0}^N a_i}{N} = \overline{a}$$

$$\overline{y} - a_0 - a_1\overline{x} = 0$$

$\overline{xy} - a_0\overline{x} - a_1\overline{x^2} = 0$

Luego resolviendo el sistema para encontrar la pendiente y el coef de posicion:

$a_1 = \dfrac{\overline{xy} - \overline{x} \cdot \overline{y} }{\overline{x^2} - \overline{x}^2 }$

$a_0 = \overline{y} - a_1 \overline{x}$

Gracias a esto podemos calcular el valor de $\chi^2$ y mientras mas se acerque a 0 mejor sera nuestra aproximacion lineal a los datos.