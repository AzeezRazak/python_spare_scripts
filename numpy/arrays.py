import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    rev_array = numpy.array(arr, float)[::-1]
    return rev_array
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
