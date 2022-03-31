# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"hello {user_name}!")

hello_name('Frank')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for n in range(1,100):
        if n % 2 != 0:
            print(n, end=' ')

first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    numbers = [1,5,4,3,10,7]
    max_in_list = max(numbers)
    return max_in_list

max_num = max_num_in_list('numbers')
print('\n', max_num)

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0:
        print(f"The year {str(a_year)} is a leap year.")
    else:
        print(f"The year {str(a_year)} is not a leap year.")
    return a_year

year = is_leap_year(2022)
print(year)

# Question 5 
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    numbers = iter([2,4,5,6,7,1])
    for n in numbers:
        if n + 1 != next(numbers):
            return False
        else:
            return True

is_list_consecutive = is_consecutive('numbers')
print(is_list_consecutive)