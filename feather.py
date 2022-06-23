# %%
from msilib.schema import Class
import numpy as np
import matplotlib.pyplot as plt

# Número máximo de iterações  e módulo máximo
itmax = 1000
mod_max = 30

def iterate(z, c, p):
    x = z.real
    y = z.imag
    return (z**p/(1 + x**2 + 1j*y**2) + c)

def num_it(c):
    n = 0
    z = 0 
    while (n <= itmax and abs(z) <= mod_max):
        z = iterate(z, c, 3)
        n += 1

    return n

# Máximo de pontos em cada eixo
max_x = 1000
max_y = 1000

# domínio do plano complexo
re = [0.25, 0.5]
im = [-0.85, -0.6]
# im = re

x = np.linspace(re[0], re[1], max_x)
y = np.linspace(im[0], im[1], max_y)

# criação do plano complexeo 
X, Y = np.meshgrid(x, y)
Z = X + 1j*Y

# %%
# variável que guarda o número de iterações
N = np.zeros([max_x, max_y])


for i in range(max_x):
    for j in range(max_y):
        N[i, j] = num_it(Z[i, j])

# %%
fig, ax = plt.subplots(figsize = (9,9))
ax.imshow(N,  cmap = 'PRGn')
ax.set_xlim = re
ax.set_ylim = im
fig.tight_layout()
plt.show()
fig.savefig('feather.pdf')
# %%
# print(N)
# %%
