import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy() #copy current array
arr[0]=24 #replace 0th index by 24

print(arr) #new replaced array
print(x) #originial copied array


arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=42

print(arr)
print(x)

#copy() copies original array  / view() replaces original array