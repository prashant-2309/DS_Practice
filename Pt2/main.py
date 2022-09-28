import pandas as pd
import numpy as np
df = pd.read_csv('D1.csv')



a = df.drop(['B','C'],axis=1)
a.to_csv('./D1_1.csv', index=False)
df1 = a[a['A'].notnull()]
print('The data set with targeted column A: ')
print(pd.read_csv('./D1_1.csv', encoding='unicode_escape'))             #The data set with targeted column A
print('The data set without any row containing NULL values: ')
print(df1)                                                              #The data set without any row containing NULL values


b = df.drop(['A','C'],axis=1)
b.to_csv('./D1_2.csv', index=False)
df2 = b[b['B'].notnull()]
print('The data set with targeted column B: ')
print(pd.read_csv('./D1_2.csv', encoding='unicode_escape'))             #The data set with targeted column B
print('The data set without any row containing NULL values: ')
print(df2)                                                              #The data set without any row containing NULL values


c = df.drop(['A','B'],axis=1)
c.to_csv('./D1_3.csv', index=False)
df3 = c[c['C'].notnull()]
print('The data set with targeted column C: ')
print(pd.read_csv('./D1_3.csv', encoding='unicode_escape'))             #The data set with targeted column C
print('The data set without any row containing NULL values: ')
print(df3)                                                              #The data set without any row containing NULL values

input()