import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    rev_array = numpy.array(arr, float)[::-1]
    return rev_array
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++


"""
[[0 1 2]
 [3 4 5]
 [6 7 8]]
"""
import numpy as np
a = np.reshape(np.arange(9, (3,3))
print[:,1] #[1, 4, 7]
print[1,:] #[3, 4, 5]

b = np.reshape(np.arange(3,12), (3,3))
# [[3 4 5]
#  [6 7 8]
#  [9 10 11]]
               
c = a.reshape((1,9))
# [[0, 1, 2, 3, 4, 5, 6, 7, 8]]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++               
               
import numpy as np

def arrays(arr):
    a = np.reshape(np.array(arr, int),((3,3)))
    return a
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)           
               
#++++++++++++++++++++++++++++++++++++++++++++++++++++++               
