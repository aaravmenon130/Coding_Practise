'''
np.arange(start, end, increment) creates arrays with incrementing values:
np.arange(5)
>>> array([0, 1, 2, 3, 4])
np.arange(3, 7, dtype=float)
>>> array([3., 4., 5., 6.])
np.arange(1, 2, 0.1)
>>> array([1., 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
'''

#Create a numpy array named ary that will hold exactly 100 elements between 1 and 1000 (including) equally spaced, and print the sum of the array.
import numpy as np
ary = np.linspace(1, 1000, 100)
print(sum(ary)) # Don't touch
