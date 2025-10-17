# Usando expansion en serie de taylor demostrar

## Para $f'(x)$
$
\begin{equation}
    f'(x) = \dfrac{f(x- \frac{3}{2} h) - 27f(x+ \frac{1}{2}h)+27f(x+\frac{1}{2})-f(x+\frac{3}{2}))}{24h} + O(h^4)
\end{equation}
$

$
\begin{equation}
    f'''(x) = \dfrac{-f(x- \frac{3}{2} h) + 3f(x- \frac{1}{2}h)-3f(x+\frac{1}{2})+f(x+\frac{3}{2})}{24h} + O(h^4)
\end{equation}
$

Primero calcularemos la expansion en serie de taylor de $f(x +\frac{1}{2}) , f(x -\frac{1}{2}), f(x +\frac{3}{2}) , f(x -\frac{3}{2}) $

Entonces:

$\begin{align}
    f(x + \frac{1}{2}) &= f(x) +\frac{1}{2}f'(x)h + \frac{1}{8}f''(x)h^2 + \frac{1}{48}f'''(x)h^3 + \frac{1}{384}f^{(4)}(x)h^4 + \frac{1}{23040}f^{(5)}(\xi)h^5 \\
    &= f(x) +\frac{1}{2}f'(x)h + \frac{1}{8}f''(x)h^2 + \frac{1}{48}f'''(x)h^3 + \frac{1}{384}f^{(4)}(x)h^4 + O(h^5) \\
\end{align}
$
$
\begin{align}
    f(x - \frac{1}{2}) &= f(x) - \frac{1}{2}f'(x)h + \frac{1}{8}f''(x)h^2 - \frac{1}{48}f'''(x)h^3 + \frac{1}{384}f^{(4)}(x)h^4 - \frac{1}{23040}f^{(5)}(\xi)h^5 \\
    &= f(x) - \frac{1}{2}f'(x)h + \frac{1}{8}f''(x)h^2 - \frac{1}{48}f'''(x)h^3 - \frac{1}{384}f^{(4)}(x)h^4 + O(h^5) \\
\end{align}
$
$
\begin{align}
    f(x + \frac{3}{2}) &= f(x) +\frac{3}{2}f'(x)h + \frac{9}{8}f''(x)h^2 + \frac{27}{48}f'''(x)h^3 + \frac{81}{384}f^{(4)}(x)h^4 + \frac{243}{23040}f^{(5)}(\xi)h^5 \\
    &= f(x) +\frac{3}{2}f'(x)h + \frac{9}{8}f''(x)h^2 + \frac{27}{48}f'''(x)h^3 + \frac{81}{384}f^{(4)}(x)h^4 + O(h^5) \\
\end{align}
$
$
\begin{align}
    f(x - \frac{3}{2}) &= f(x) -\frac{3}{2}f'(x)h + \frac{9}{8}f''(x)h^2 - \frac{27}{48}f'''(x)h^3 + \frac{81}{384}f^{(4)}(x)h^4 - \frac{243}{23040}f^{(5)}(\xi)h^5 \\
    &= f(x) +\frac{3}{2}f'(x)h - \frac{9}{8}f''(x)h^2 + \frac{27}{48}f'''(x)h^3 - \frac{81}{384}f^{(4)}(x)h^4 + O(h^5) \\
\end{align}$

Luego, al restar $(4)$ a $(6)$ tenemos que:

$
\begin{equation}
    f(x - \frac{1}{2}) - f(x + \frac{1}{2}) = -f'(x)h - \frac{1}{24}f'''(x)h^3 - O(h^5) 
\end{equation}
$

Lo mismo con $(8)$ y $(10)$:

$
\begin{equation}
    f(x - \frac{3}{2}) - f(x + \frac{3}{2}) = -3 f'(x)h - \frac{27}{24}f'''(x)h^3 - O(h^5) 
\end{equation}
$

Luego restamos $27 \cdot(11)$ y $(12)$:

$
\begin{equation}
    f(x - \frac{3}{2}) - f(x + \frac{3}{2}) - 27f(x - \frac{1}{2}) + 27f(x + \frac{1}{2}) = 24f'(x)h + O(h^5)
\end{equation}
$

Luego despejando $f'(x)$:

$
\begin{equation}
    f'(x) = \dfrac{f(x - \frac{3}{2}) - f(x + \frac{3}{2}) - 27f(x - \frac{1}{2}) + 27f(x + \frac{1}{2})}{24h} + O(h^4)
\end{equation}
$

## Para $f^{(3)}(x)$ 

Utiizando $3 \cdot (11) - (12)$:

$
\begin{equation}
    3f(x - \frac{1}{2}) - 3f(x + \frac{1}{2}) - f(x - \frac{3}{2}) + f(x + \frac{3}{2}) = f^{(3)}(x)h^3 + O(h^5)
\end{equation}
$

luego despejando:

$
\begin{equation}
    f^{(3)}(x) = \dfrac{3f(x - \frac{1}{2}) - 3f(x + \frac{1}{2}) - f(x - \frac{3}{2}) + f(x + \frac{3}{2})}{h^3} + O(h^2)
\end{equation}
$

# Derivadas

Forma analitica, considerando $f(x) = x^3 -x$, considerando que $x = 1$ y $h = 0.1$

## Derivada atrasada

Tenemos que:

$
\begin{equation}
    f'(x) = \dfrac{f(x)- f(x-h)}{h}
\end{equation}
$

Al calcularla de forma "normal" tenemos que $f'(1) = 2$, pero utilizando $(17)$ tenemos que $f'(1) \approx 1.71$ y calculando su error relativo tenemos que:

$
\begin{align}
    E_{rel} &= \dfrac{|f'(x) - Df'(x)|}{f'(x)}\cdot 100\% \\
            &= \dfrac{|2 - 1.71|}{2}\cdot 100\% \\
            &= 14.5 \%
\end{align}
$

## Derivada adelantada

Tenemos que:

$
\begin{equation}
    f'(x) = \dfrac{f(x+h)- f(x)}{h}
\end{equation}
$

Al calcularla de forma "normal" tenemos que $f'(1) = 2$, pero utilizando $(21)$ tenemos que $f'(1) \approx 2.31$ y calculando su error relativo tenemos que:

$
\begin{align}
    E_{rel} &= \dfrac{|f'(x) - Df'(x)|}{f'(x)}\cdot 100\% \\
            &= \dfrac{|2 - 2.31|}{2}\cdot 100\% \\
            &= 15.5 \%
\end{align}
$

## Derivada centrada

Tenemos que:

$
\begin{equation}
    f'(x) = \dfrac{f(x+h)- f(x-h)}{h}
\end{equation}
$

Al calcularla de forma "normal" tenemos que $f'(1) = 2$, pero utilizando $(25)$ tenemos que $f'(1) \approx 2.01$ y calculando su error relativo tenemos que:

$
\begin{align}
    E_{rel} &= \dfrac{|f'(x) - Df'(x)|}{f'(x)}\cdot 100\% \\
            &= \dfrac{|2 - 2.01|}{2}\cdot 100\% \\
            &= 0.5 \%
\end{align}
$

# Metodo a 5 puntos

La plantilla de cinco puntos (five-point stencil) proporciona una aproximación numérica para la derivada de una función real, dada por la expresión:
 $$f^{(1)}(x)\approx\frac{f(x-2h)-8f(x-h)+8f(x+h)-f(x+2h)}{12h}$$