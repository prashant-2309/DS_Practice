import numpy as np
#1. Create a function that takes in a name as a string argument and returns a string of the form - "Hello name"

def print_name(name):
    print(f'Hello, {name}')
name = input("Enter the name: ")
print_name(name)

#2. Create a function that accepts two arguments, an integer, and a vector of integers. It returns the count of the number of occurrences of the integer in the input vector.

def count_num(lst,a):
    print('Vector is: ', lst)
    print('Count of ', a, ' : ', np.count_nonzero(lst == a))
lst = np.array([int(item) for item in input("Enter the integer values to enter in the vector array : ").split()])
a = int(input("Enter the integer to be found: "))
count_num(lst, a)

#3. Create a function that accepts 3 integer values and returns their sum. However, if an integer value is evenly divisible by 3, then it does not count towards the sum. Return zero if all numbers are evenly divisible by 3.

x = []
def add(x):
    for i in range(3):
        a = int(input("Enter the integer to get the sum: "))
        if a%3!=0:
            x.append(a)
        else:
            x.append(0)

    print('Sum is', sum(x))
add(x)

#4. Create a function that will return TRUE if an input integer is prime. Otherwise, return FALSE.

def prime(num):
    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                print(False)
                break
        else:
            print('TRUE')
    else:
        print('FALSE')
num = int(input("Enter the number to determine prime: "))
prime(num)

input()#dummy input