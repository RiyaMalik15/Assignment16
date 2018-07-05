print("Question1")
import numpy as np
np_arr1=np.random.random((10,1))
print(np_arr1)
mean=np.mean(np_arr1)
print("Mean: ",mean)
print('*'*10)
print('\n')

print("Question2")
import numpy as np
np_arr2=np.random.random((20,1))
print(np_arr2)
variance=np.var(np_arr2)
print("Variance: ",variance)
std_dev=np.std(np_arr2)
print("Standard Deviation: ",std_dev)
print('*'*10)
print('\n')

print("Question3")
import numpy as np
np_arr3=np.random.random((10,20))
print(np_arr3)
np_arr4=np.random.random((20,25))
print(np_arr4)
multiply=np.matmul(np_arr3,np_arr4)
print("Desired Output: ",multiply)
print('*'*10)
print('\n')

print("Question4")
import numpy as np
import math
np_arr5=np.random.random((10,1))
print(np_arr5)
def f(x):
    return(1/1+math.exp(-x))
arr1=np.array(list(map(f,np_arr5)))
print(arr1)
print('*'*10)
print('\n')
