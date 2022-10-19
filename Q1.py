import numpy as np
a=np.random.randint(1,20,(15))
print(a)

#Reshape the array to 3 by 5
b=a.reshape(3,5)
print(b)

#Print array shape
print(np.shape(b))

#Replace the max in each row by 0
maxNum = np.amax(b, axis=1)
print(maxNum)

d = np.where(np.isin(b,maxNum), 0, b)
print(d)
