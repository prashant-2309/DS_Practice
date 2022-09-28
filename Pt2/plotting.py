import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('D1_1.csv')
plt.hist(df1['A'], bins='auto')
plt.title("Histogram A")
plt.show()

df2 = pd.read_csv('D1_2.csv')
plt.hist(df2['B'], bins=50)
plt.title("Histogram B")
plt.show()

df3 = pd.read_csv('D1_3.csv')
plt.hist(df3['C'], bins=50)
plt.title("Histogram C")
plt.show()
