'''
Reshape

We can create powerful arrays with the reshape method.

The syntax is: np.reshape(ary, newshape)

the reshape changes the shape of the array. the new shape is a tuple or a list that must be the same multiplication result as 
the old shape

For example: old shape: (2, 5), multiplication result: 2*5=10, the new shape can be any combination of numbers as long as the 
multiplication is 10, meaning the new shape can be either one of: (1, 10) , (10, 1) , (5, 2)
'''

#Create a numpy array that contains incrementing elements from 1 to 200(including): [1, 2, 3, 4, 5, 6, ..., 200]
import numpy as np
ary = np.arange(1, 201)
ary = np.reshape(ary, (20, 10))
print(ary)
