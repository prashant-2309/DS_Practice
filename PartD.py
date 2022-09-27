import pandas as pd

# Import CSV mtcars
# data = pd.read_csv('https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/64f1660f38ef523b2a1a13be77b002b98665cdfe/mtcars.csv', index_col=0)

#1. Display the first 6 rows of df
data = pd.read_csv('mtcars.csv', index_col=0)
print(pd.read_csv("mtcars.csv", nrows=6, index_col=0))

#2. What is the average mpg value for all the cars?
df2 = data["mpg"].mean()
print('Average of mpg column is: ',df2)

#3. Select the rows where all cars have 6 cylinders (cyl column)
df = data[data['cyl']==6]
print(df)

#4. Select the columns am, gear, and carb.
col_list = ['am', 'gear', 'carb']
df3 = pd.read_csv('mtcars.csv', usecols=col_list)
print(df3)

#5. Create a new column called performance, which is calculated by hp/wt.
data['performance'] = (data['hp']/data['wt'])
print(data)

#6. What is the mpg of the Hornet Sportabout?
df4 = data.mpg['Hornet Sportabout']
print('mpg of the Hornet Sportabout is: ', df4)

input() #dummy input