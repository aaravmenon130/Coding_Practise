#Create a function named array_modifier that receives 3 values: a list, a value, and an index.
#Convert the list to a numpy array, and insert the new value in the specified index. You are not allowed to use list functionalities.
#This problem can easily be solved with the builtin .insert, but I want you to practice other functionalities.
import numpy as np
def array_modifier(lst, value, index):
    ar = np.array(lst[:index])
    ar = np.append(ar, value)
    ar2 = np.array(lst[index:])
    ar = np.append(ar, ar2)
    return ar
