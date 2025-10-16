#np.matmul(matrix1, matrix2)
#matrix1.dot(matrix2)
#A @ B

#Create a function called matrix_master that receives three python lists and return the 
#matrix multiplication of the first two lists and perform a dot product of the result with the last list
import numpy as np
def matrix_master(lst1, lst2, lst3):
    # complete
    lst1 = np.array(lst1)
    lst2 = np.array(lst2)
    lst3 = np.array(lst3)

    lst1 = lst1 @ lst2
    return np.dot(lst1, lst3)
