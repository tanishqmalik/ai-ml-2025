import numpy as np

arr = np.array([1,2,3,4,5])

print(arr , type(arr))

print(np.__version__)


# 0D arrays

arr = np.array(42)

print(arr)

# 1D arrays

arr=np.array([1,2,3,4,5], ndmin =3)

print(arr)

#2d arrays



# arr = np.array([[1,2,3],[4,5,6]])
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr.ndim)

arr=np.array([1,2,3,4,5], ndmin =1)
print(arr[0]+arr[2])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])


print(arr[1, -1])


arr = np.array([329322,8433,1,4,2395])

print(arr[::-1])