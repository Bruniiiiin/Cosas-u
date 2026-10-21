import numpy as np

mu_77 = 8.95e-7   # H/m (valor experimental con N = 77)
N = np.array([75, 76, 77, 78, 79])

mu = mu_77 * 77 / N

print(mu)