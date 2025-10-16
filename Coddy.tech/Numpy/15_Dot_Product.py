#Create a function called calculate that receives two python lists, and performs:
#res1 = Subtraction of the two lists
#res2 = Multiplication of the two lists
#and return the dot product of res1 and res2.

import numpy as np
def calculate(lst1, lst2):
    lst1 = np.array(lst1)
    lst2 = np.array(lst2)
    res1 = lst1 - lst2
    res2 = lst1 * lst2
    return np.dot(res1, res2)
