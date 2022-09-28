import numpy as np
print('Two to the power five: ', 2**5)  #Two to the power five

dp = [23, 27, 25, 45, 67]
dp_vector = np.array(dp)    #Creating the vector of data points: 23,27,25,45,67
print('Vector is: ', dp)

dp = {23: 'Monday', 27: 'Tuesday', 25: 'Wednesday', 45: 'Thursday', 67: 'Friday'}   #Assigning names to the above data points in the vector relating to the day of the week

avg = np.mean(dp_vector)    #Average(mean) of the values in the vector
print('Average of the values is: ', avg)

print('Day when the value was the highest: ', dp[max(dp)])  #Day when the value was the highest


input() #dummy input
