import numpy as np
arr=np.array([1.9, 2.5, 3.4]) #float
new_arr=arr.astype(int) #converts float to int
print(new_arr) #outputs digit before decimal point
print(new_arr.dtype)


import numpy as np
arr1=np.array([-1,0,3]) #int
arr2=arr1.astype(bool) #converts int to boolean
print(arr2) #when there is number=True, when zero=False
print(arr2.dtype)