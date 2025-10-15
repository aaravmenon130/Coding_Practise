'''
ary = np.array([1, 2, 3, 5, 8, 3, 9, 10, 2])
ary[(ary > 5) & (ary < 10)]
>>> [8, 9]

Python	Numpy
 and	    &
  or	    |
 not	    ~
'''
#Create a function called condition_master that receives a python list and returns all the elements that are smaller
#or equal to 0 or bigger than 5 and not equal to 10.
#Return the result as a python list
import numpy as np
def condition_master(lst):
    lst = np.array(lst)
    return list(lst[((lst <= 0) | (lst > 5)) & (lst != 10)])
    # Complete here
