'''
Numpy 2D array indexing:

ary = np.array([[1, 2], [3, 4]])
ary[0,1] # --> 2 


How to index a 3D array?

ary = np.array([
    [[1], [2]], 
    [[3], [4]]
])
ary[0, 0, 0] # --> 1
ary[0, 1, 0] # --> 2
ary[1, 0, 0] # --> 3
ary[1, 1, 0] # --> 4
'''
#Retrieve the element (using indexing) that contains the value 5 from the 3D array ary

import numpy as np
ary = np.array([ [ [ 0, 1 ], [ 2, 3 ] ], [ [ 4, 5 ], [ 6, 7 ] ] ])

res = ary[1, 0, 1] # <-- Complete the indexing

print(res) # Don't touch


