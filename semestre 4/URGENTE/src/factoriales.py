import numpy as np

#Factorial solo con python

def factorial(N):
    f = 1
    return [1 if n==0 else (f:=f*n) for n in range(N+1)]

# (2n)! factorial con python

def factorial_2n(N):
    f = 1
    return [1 if n==0 else (f:=f*(2*n-1)*(2*n)) for n in range(N+1)]

# (n+1)! factorial con python}

def factorial_n1(N):
    f = 1
    return [1 if n==0 else (f:=f*(n+1)) for n in range(N+1)]

###############################################################################

#Factorial con numpy

def factorial_numpy(N, dtype=np.int32):
    f = np.arange(N+1, dtype=dtype)
    f[0] = 1
    return f.cumprod(dtype=dtype)

# (2n)! factorial con numpy

def factorial_2n_numpy(N, dtype=np.int32):
    f = np.arange(2*N+1, dtype=dtype)
    f[0] = 1
    return f.cumprod(dtype=dtype)[::2]

# (n+1)! factorial con numpy

def factorial_n1_numpy(N, dtype=np.int32):
    f = np.arange(N+2, dtype=dtype)
    f[0] = 1
    return f.cumprod(dtype=dtype)[1:]
