import numpy as np

arr = np.arange(0,24).reshape(3,8)

# 1. Calculate the size of the 2D array.

def calc_size(a):
	return (len(a)*len(a[0]))

# 2. Reshape the array into a 1D array.
arr = arr.reshape(calc_size(arr))

# 3. Sum the elements of the 1D array.

def sum_array(a):
	s = 0
	x = 0
	while x < len(a):
		s += a[x]
		x += 1
	return s
print("The sum of the elements in the array is {x}.".format(x=sum_array(arr)))
