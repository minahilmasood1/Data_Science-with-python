import numpy as np
array = np.array([[10,15,20,25],
         [30,35,40,45],
         [50,55,60,65],
         [70,75,80,85],
         [90,95,100,105]])
          #Array slicing and manipulation
slice_array = array[0:5:2,0:4:3].copy()
slice_array[0,0] = 55
print(slice_array)
slice_array_2 = array[::2,::2]
slice_array_2[0,1] = 99
print(slice_array_2)
print(array)
print(array.flatten())
#Operations
print(f"Maximum value is {array.max()}")
print(f"If array is considered flatten than ndex number of minimum value is {array.argmin()}")
print(array.clip(45,50))
