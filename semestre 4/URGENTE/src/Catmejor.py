import numpy as np
import matplotlib.pyplot as plt

N = 15
cats = [0] * (N + 1)
cats[0] = 1

for n in range(N):
    cats[n + 1] = (4 * n + 2) * cats[n] // (n + 2)

x = list(range(N + 1))
y = cats

plt.plot(x,y, "o-")
plt.ylabel("$C_n$")
plt.xlabel("$n$")
plt.title("Números de Catalán")
plt.yscale("log")
plt.grid()
plt.show()  