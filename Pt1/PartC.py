import numpy as np
import pandas as pd
import IPython
from IPython.display import display

#Create 2 vectors A and B, where A is (1,2,3) and B is (4,5,6). With these vectors, use the cbind() or rbind() function to create a 2 by 3 matrix from the vectors. (Figure out which is the right option)
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
series1 = pd.Series(A)
series2 = pd.Series(B)
display(pd.concat([series1, series2], axis = 1))

# Create a 5 by 5 matrix consisting of the numbers 1-25 and assign it to the variable mat2. The top row should be the numbers 1-5.

mat2 = np.arange(1, 26).reshape(5,5)

print(mat2[0])

#Using indexing notation, grab a sub-section of mat2 from the previous exercise that looks like this: [7,8] [12,13]

print(mat2[1][1:3])
print(mat2[2][1:3])

input()#dummy input