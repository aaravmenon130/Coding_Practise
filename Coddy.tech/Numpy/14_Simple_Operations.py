#Create a function called func_operation the receives three python lists
#and returns the sum of ary1 * ary2 / ary3
#Round the result to two decimal places after the dot.
#To round the result use the round method: round(num, 2)

import numpy as np
def func_operation(lst1, lst2, lst3):
    # Complete here	
    lst1 = np.array(lst1)
    lst2 = np.array(lst2)
    lst3 = np.array(lst3)
    lst1 = lst1 * lst2
    lst1 = lst1 / lst3
    return round(sum(lst1), 2)
