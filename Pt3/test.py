import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from math import sqrt


df = pd.read_csv('student.csv')
df.dropna(inplace = True) #clean
print(df.isnull().any())  #missing values


# print(df.to_string())
# x = df.astype(str)
# print(x)

plt.hist(df['G1'], bins=50)  #histogram
plt.title("Histogram G1")
plt.show()

plt.hist(df['G2'], bins=50)
plt.title("Histogram G2")
plt.show()

plt.hist(df['G3'], bins=50)
plt.title("Histogram G3")
plt.show()
df['split'] = np.random.randn(df.shape[0], 1)



msk = np.random.rand(len(df)) <= 0.5
# train = df[msk]
# test = df[~msk]

# print(train)
# print(test)
Z = df['G3']
Y = df['G2']
X = df['G1']


X_train = X[msk]    #split into train and test
X_test = X[~msk]

Y_train = Y[msk]
Y_test = Y[~msk]

Z_train = Z[msk]
Z_test = Z[~msk]




predictions = [i for i in Z_test]    #predictions
print(predictions)

rmse = sqrt(mean_squared_error(Z_test, predictions))
print('Test RMSE: %.3f' % rmse)
print( 'MSE is: ', mean_squared_error(Z_test, predictions))
print('R-Squared Value is: ', r2_score(Z_test, predictions))

plt.scatter(X_test,Y_test)
plt.plot(X_test,Y_test)
plt.show()