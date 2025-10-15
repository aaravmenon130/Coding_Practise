'''
Numpy has the option to select elements with conditions. 

Use the following syntax: ary[ary operator number]

ary[ary > 5]
ary[ary == 5]
ary[ary <= 5]
etc
Example 1
Retrieve all numbers under 5

x = np.array([1, 5, 2, 4, 9 ,10 ,13, 7])
x[x < 5]
>>> [1, 2, 4]
Example 2
What happens with higher dimensions?

x = np.array([[1, 5], [2, 4], [9 ,10] ,[13, 7]])
x[x < 5]  # --> [1, 2, 4]
x[x >= 5] # --> [5, 9, 10, 13, 7]
x[x == 6] # --> []
Did you see that? It returned a single array with all the elements that satisfy the condition

When we apply a condition on x it returns a boolean array that represents for each index if it satisfies the condition.

Example 3
This time we will examine what happens if we simply use a condition without the brackets []

x = np.array([1, 2, 3])
x < 2
>>> [True, False, False]
It returns a list of all the indices that satisfy the condition

Example 4
Instead of placing a condition inside the brackets [], We can instead place a boolean list just like we received in the previous example to retrieve the desired elements.

x = np.array([8, 4, 10])
x[[False, True, False]]  # --> [4]
x[[True, True, False]]   # --> [8, 4]
x[[True, False, True]]   # --> [8, 10]
x[[False, False, False]] # --> []

Example 3 and 4 explain why x[x < 5] works.
'''
#Write a function called small_five that receives a list and returns the sum of all elements smaller than 5
import numpy as np
def small_five(lst):
	# Complete your code
    lst = np.array(lst)
    return sum(lst[lst < 5])
