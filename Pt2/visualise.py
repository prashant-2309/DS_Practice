import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel('Plot.xlsx')
x = var['X']
y = var['Y']
plt.plot(x,y)
plt.title('2-D plot of the data')
plt.show()

input()