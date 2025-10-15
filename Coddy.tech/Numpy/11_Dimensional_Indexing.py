'''
Numpy support an extremely powerful tool - Indexing dimensions.

To index dimension we use the colon :. the colon takes all of the elements at the specific index it is placed. For example assume we have an array with the shape ary.shape # --> (2, 1, 3, 1), placing the colon : at ary[:, 0, 0, 0] will take the two left most elements of the shape and for each one of these it will extract the zeroth element for the rest of dimensions.

Note: The location of the colon at the brackets [] is the dimension we are indexing, meaning

ary[:, 0, 0, 0] Index the 4D dimension
ary[0, :, 0, 0] Index the 3D dimension
ary[0, 0, :, 0] Index the 2D dimension
ary[0, 0, 0, :] Index the 1D dimension
ary[:, :, 0, 0] Index the 4D and the 3D dimensions
etc
Example 1
ary = np.array([
    [1, 2], 
    [3, 4]
])
ary[:, 0] # --> [1, 3]
ary[0, :] # --> [1, 2]
The colon takes all of the elements at the specified index and continues to the next index

In our case: 

ary[:, 0] We take all the first elements and at each element we take the 0 element
ary[0, :] We take the first element and at the element we take all elements.
Exmaple 2
3D array

ary = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
ary[:, 0, :] # --> [[1, 2], [5, 6]]
ary[:, :, 0] # --> [[1, 3], [5, 7]]
ary[:, 0, :] We take all the elements, then we take the first element and at last we take everything there
ary[:, :, 0] We take all the elements, then we take all of these elements and at last we take the first element at each.
Can you guess what is the output for ary[0, :, :]
Exmaple 3
Get the first and last index from every row

x = np.array([
    [ 0,  1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10, 11],
    [12, 13, 14, 15, 16, 17],
    [18, 19, 20, 21, 22, 23],
])
x[:, np.array([0, -1])]
>>> [0, 5, 6, 11, 12, 17, 18, 23]
Example 4
An array with the shape (2, 1, 3, 1) just like in the opening example

ary = np.array([
    [
        [
            [1],[2],[3]
        ]
    ],
    [
        [
            [4],[5],[6]
        ]
    ]
])
ary[:, 0, 0, 0] # --> [1, 4]
ary[0, :, 0, 0] # --> [1]
ary[0, 0, :, 0] # --> [1, 2, 3]
ary[0, 0, 0, :] # --> [1]
Note: it is possible to use the slicing syntax: start:stop:step we learned at the Slicing lesson as well

ary[:, 0:5, 2:3, :]
'''
#Given a 3D array ary retrieve the 2nd, 3rd and 4th numbers from each 1D array
import numpy as np
'''
ary looks like:
array([[[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]],

       [[20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]],

       [[40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
        [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]],

       [[60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
        [70, 71, 72, 73, 74, 75, 76, 77, 78, 79]],

       [[80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
        [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]])
'''
ary = np.arange(0, 100).reshape(5, 2, 10) # don't change ary
res = ary[:, :,1:4] # <-- Complete indices
print(str(res).replace("\n", "")) # don't change this line
