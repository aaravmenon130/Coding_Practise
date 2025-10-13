'''
Create a function named dtype_converter that receives the number of bits for the type and a value.
The functions return a 0-dimension numpy array (Remember that a 0-dimension array is just a single value passed into the np.array) with the specified dtype and the value incremented by one
bits can be one of the following values: 8, 16, 32, 64
'''
import numpy as np

def dtype_converter(bits, value):
    try:
        if bits == 8:
            return np.array(value+1, dtype=np.int8)
        elif bits == 16:
            return np.array(value+1, dtype=np.int16)
        elif bits == 32:
            return np.array(value+1, dtype=np.int32)
        else:
            return np.array(value+1, dtype=np.int64)
        # Write your code here
    except:
        print("Overflow:", value+1)
