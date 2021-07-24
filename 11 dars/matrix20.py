import numpy as np
matrix=np.array([1,2,3,4,5,6,7,8,9,10,11,12],dtype='int32').reshape(4,3)
s=0
i=0
for i in  range(0,len(matrix),1):
    s+=matrix[i]
print(s)

