import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarray = arr.reshape(2,3,2)

# print(newarray)

# for x in arr:
#     print(x)

arr = np.array([[1,2,3], [4,5,6]])

# for x in arr:
#     for y in x:
#         print(y)

arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in arr1:
#     for y in x:
#         for z in y:
#             print(z)

# for x in np.nditer(arr):
#     print(x)


arr3 = np.array([1,2,3])
arr4 = np.array([4,5,6])


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

# arr = np.concatenate((arr1, arr2), axis =1 )
arr = np.stack((arr1, arr2) ,axis =1 )

print(arr)

# print(np.concatenate((arr3,arr4)))


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

print(np.hstack((arr1,arr2)))