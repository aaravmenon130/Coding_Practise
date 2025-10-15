#Slice [[1,2],[3,4]] and [[9,10], [11,12]] from the ary
#Save the result in the res variable and print res
import numpy as np
ary = np.array([ [ [ 1,2 ],[ 3,4 ] ], [ [ 5,6 ],[ 7,8 ] ], [ [ 9,10 ], [ 11,12 ] ] ]) # Don't touch
res = ary[0::2] # <-- Slice
print(str(res).replace('\n', '')) # Don't touch
