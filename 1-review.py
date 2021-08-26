#vektor python numpy dengan range value
import numpy as np
print("vektor default python\n")
a = np.arange(1,20,1)
b = np.arange(1,20,2)

print (" \n vektor via numpy \n")

#vektor via numpy 
c = np.array ([1,2,3,4,5])
d = np.array ([1.5, 2.5, 5, 6, 7])

print(a)
print(b)
print(a.ndim)
print(a.shape)

#matriks
a = np.arange(1,21,1)
c = a.reshape((4,5))
print(c)

#list
list1 = ["apple", "banana", "cherry"]
list2 = [1,5,7,9,3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

print(list1); 

#dataframe
import pandas as pd
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
print(df)
