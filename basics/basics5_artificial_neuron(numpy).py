"""
> a simple artificial neuron using numpy.
"""

import numpy as np

inputs = [1.3, 5.5, 3.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = np.dot(inputs, weights) + bias
print(output)