'''
Another great feature in Numpy is the ability to select specific indices from an array. Place a List inside the [] brackets and specify which indices you want to select: ary[indices] 

Example 1
Retrieve the 0th, 2nd, 4th elements:

x = np.arange(5, 15) # np.array([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
x[[0, 2, 4]]
>>> [5, 7, 9]
Example 2
Retrieve the first and last element (but now from a 2D array)

x = np.array([[0, 1], [2, 3], [4, 5], [6, 7]])
x[[0, -1]]
>>> [[0, 1], [6, 7]]
What about fetching specific elements from a 2D array?

We use ary[[Row indices], [Element indices]]

Example 3
Retrieve the first and last element from the 2nd and 3rd rows

x = np.array([
    [ 0,  1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10, 11],
    [12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23],
])
x[[1, 1, 2, 2], [0, -1, 0, -1]]
>>> [6, 11, 12, 17]
What happened?

Numpy looks at the corresponding index of each list inside the bracket [] and returns the element:

x[[1, 1, 2, 2], [0, -1, 0, -1]]

x[1, 0]  # --> 6
x[1, -1] # --> 11
x[2, 0]  # --> 12
x[2, -1] # --> 17
How to get from all rows the first and last index?
'''
#Given a 2D array ary retrieve all numbers divided by five with no remainder (0, 5, 10, ...) with the methods we learned this lesson.
import numpy as np
'''
ary looks like:
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19]])
'''
ary = np.arange(0, 20).reshape(4, 5)  # don't change ary
res = ary[[0, 1, 2, 3], [0, 0, 0, 0]]  # <-- Complete indices
print(str(res).replace("\n", ""))  # don't change this line
