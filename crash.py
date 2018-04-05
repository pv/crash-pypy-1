import numpy as np
for j in range(200):
    structure = np.array([1], dtype=[(('x', 'X'), np.object_)])
    structure[0]['x'] = np.array([2])
