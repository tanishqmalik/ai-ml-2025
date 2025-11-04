#array slicing

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-1:-5:-1]) 
# print(arr[1:6])
print(arr[::2]) 

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2,1:4])


arr = np.array([1.1, 2.2, 3, 4, 5, 6, 7,0.343434])

newarr = arr.astype(bool)
print(newarr)

print(newarr.dtype)

# NumPy Array Copy vs View

arr = np.array([1,2,3,4,5])

x = arr.copy()
x[0] = 42

# print(arr)
# print(x)

y = arr.view()

arr[0] = 67

print(y)
print(arr)


# NumPy Array Shape

print(arr.shape)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)