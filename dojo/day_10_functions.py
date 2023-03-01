######### Functions - Día 10 ######### 
""" 
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(parameter1, parameter2):
   sum = parameter1 + parameter2
   print(sum)

user_request1_str = input('give me one number: ')
user_request1 = int(user_request1_str)
user_request2_str = input('give other number: ')
user_request2 = int(user_request2_str)

print('the sum of the two numbers is:', add_two_numbers(user_request1 , user_request2) )


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
from math import pi

def area(radius):
    calculate = pi * radius**2
    return(calculate)

user_request_str = input('Radius of a circle: ')
user_request = int(user_request_str)

print('The area of the circle is', area(user_request) )


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "Error: all arguments must be numbers"
        total += arg
    return total

print(add_all_nums(20,30,74,85,90))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def c_onverted_to_f(degrees):
    f = (degrees * 9 / 5) +32
    return f

user_request = int(input('How many degrees Celsius is it? '))
print("that's", c_onverted_to_f(user_request), 'degrees in fahrenheit')

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if station in ('September', 'October', 'November'):
        month = 'the season is Autumn'
        return month 
    elif station in ('December', 'January', 'February'):
        month = 'the season is Winter'
        return month 
    elif station in ('March', 'April', 'May'):
        month ='the season is Spring'
        return month 
    elif station in ('June', 'July', 'August'):
        month ='the season is Summer'
        return month 
    else:
        month ='the month you have provided is wrong'
        return month 

str_station = input('what month is it? ')
station = str_station.capitalize()

print('we are in the month of ', check_season(station))


# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return None 
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):

    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # No real roots
    elif discriminant == 0:
        root = -b / (2*a)
        return [root]  # One real root
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return [root1, root2]  # Two real roots
    
print(solve_quadratic_eqn(1, -5, 6))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(list):
    for i in list:
        print(i)

lst = ['Python' ,2 , 'SQL' ,4, 5]
print(print_list(lst))


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
#        print(reverse_list([1, 2, 3, 4, 5]))
#        [5, 4, 3, 2, 1]
#        print(reverse_list1(["A", "B", "C"]))
#        ["C", "B", "A"]

def reverse_list(my_list):
    reversed_list = []
    for i in range(len(my_list)-1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(my_list):
    capitalized_list = []
    capitalized = ''
    for i in range(len(my_list)):
        capitalized = str.capitalize(my_list[i])
        capitalized_list.append(capitalized)
    return capitalized_list

my_list = ["apple", "banana", "cherry"]
print(capitalize_list_items(my_list))


def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
#       food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#       print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
#       numbers = [2, 3, 7, 9];
#       print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

def add_item(lst, i):
    added = lst.copy()
    added.append(i)
    return added

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))

numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
#               food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#               print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#               numbers = [2, 3, 7, 9];
#               print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(list, item):
    added = list.copy()
    added.remove(item)
    return added

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) 

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#               print(sum_of_numbers(5))  # 15
#               print(sum_all_numbers(10)) # 55
#               print(sum_all_numbers(100)) # 5050

def sum_of_numbers(number):
    return sum(range(1, number+1))
    
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(n):
    total = 0
    for i in range(1, n+1, 2):
        total += i
    return total
  
print(sum_of_odds(10))


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(n):
    total = 0
    for i in range(0, n+1, 2):
        total += i
    return total
  
print(sum_of_even(10))

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
                # print(evens_and_odds(100))
                # The number of odds are 50.
                # The number of evens are 51.


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n- 1)
    
print(factorial(10))


# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(x):
    if not x:
        print('variable is not empty')
    else: 
        print('variable is empty')

param = ''
param2 = 2
is_empty(param)
is_empty(param2)


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics

def calculate_mean(lst):
    x = statistics.mean(lst)
    return x

def calculate_median(lst):
    x = statistics.median(lst)
    return x

def calculate_mode(lst):
    x = statistics.mode(lst)
    return x

def calculate_range(lst):
    x = range(lst)
    return x

def calculate_variance(lst):
    x = statistics.variance(lst)
    return x

def calculate_std(lst):
    x = statistics.stdev(lst)
    return x

print(calculate_variance([10,20,30]))


# Write a function called is_prime, which checks if a number is prime.

def is_prime(n):
    for i in range(2, n+-1):
        if n % i == 0:
            print("is not prime", i, "is divisor")
            return False
    print("it's prime")
    return True

is_prime(17)


# Write a functions which checks if all items are unique in the list.

def check_unique(lst):
    check = []
    for i in lst:
        if i in check:
            print('item ', i, ' is repeated')
        else:
            check.append(i)
    return check

lista = ['manzana','pera','kiwi','platano']

print(check_unique(lista))
 """

# Write a function which checks if all the items of the list are of the same data type.

# Write a function which check if provided variable is a valid python variable

# Go to the data folder and access the countries-data.py file.

# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order. 
