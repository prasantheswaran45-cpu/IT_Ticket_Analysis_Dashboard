print("hello world")
import numpy as np
print(np.__version__)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print(type(a))


b=np.array([[1,2,3],
          [4,5,6]] )
print(b)

print("shape a:",a.shape)
print("shape b:",b.shape)
print("size a:",a.size)
print("ndimensional b:",b.ndim)


print(">>>>>>>>>>practice<<<<<<<<<<<<<<<")
import numpy as np
my_array=np.array([10,20,30,40,50])
print("my_array :",my_array)
print("my_array shape :",my_array.shape)
print("my_array size :",my_array.size)
print("my_array dimension :",my_array.ndim)



# to create array automatically 

zero=np.zeros((3,3))
print("Zero :\n",zero)

ones=np.ones((2,4))
print("ones:\n",ones)



#range array
r=np.arange(0,10,2)
print("Arange :",r)

#line space
n=np.linspace(0,1,4)
print("Linespace :",n)

# Special matrix - diagonal is 1, rest 0
eye = np.eye(3)
print("Identity:\n", eye)



print(">>>>>>>>>>>practice 2<<<<<<<<<<<<<<<<<<<<<")
import numpy as np
#task 1
a=np.zeros((2,3))
print("Task 1:\n",a)

#task 2
n=np.arange(1, 10, 3)
print("Task 2 :", n)
# print("dimension",n.ndim)

#task 3
c=np.linspace(0,100,5)
print("Task 3:",c)




