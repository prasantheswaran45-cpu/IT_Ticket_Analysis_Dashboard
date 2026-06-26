import numpy as np

a=np.array([10,20,30])
print("Task 1 dtype :",a.dtype)

b=np.array([1.7,2.9,3.1],dtype=int)
print("Task 2 array :",b)


c=np.array([100,200,300])
d=c.astype(float)
# print(d)
print("Task 3 before :",c.dtype)
print("Task 3 after :",d.dtype)