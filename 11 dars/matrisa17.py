import numpy as np
i=0
k=int(input('k = '))
matrix=np.array([1,2,3,4,5,6,7,8,9,10,11,12],dtype='int32').reshape(4,3)
for i in  range(matrix[k][0]):
    print(matrix[k])
    break
array=matrix[k]
s=0
k=1
for j in range(0,len(array)):
    s+=array[j]
    k*=array[j]

print(s,k)

 