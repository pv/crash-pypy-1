import numpy as np

for j in range(200):
    structure = np.recarray([1], dtype=[(('x', 'X'), np.object_)])
    structure['x'][0] = np.array([2])
