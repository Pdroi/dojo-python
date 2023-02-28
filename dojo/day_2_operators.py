######### Operators - Día 2 ######### 

#·Declare your age as integer variable
int_edad = 18

#·Declare your height as a float variable
floor_edad = 18.0

#·Declare a variable that store a complex number
complex_edad = 10 + 8j

#·Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input('Enter base: ')
height = input('Enter height: ')

int_base = int(base)
int_height = int(height)

area = 0.5 * int_base * int_height

print('The area of the triangle is ', area)

#·Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')

int_a = int(a)
int_b = int(b)
int_c = int(c)

perimeter = int_a + int_b + int_c
print('The perimeter of the triangle is ', perimeter)

#·Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input('Enter length new rectangle: ')
width = input('Enter width new rectangle: ')

int_length = int(length)
int_width = int(width)


area = int_length * int_width
perimeter = 2 * (int_length + int_width)
print('The area of the rectangle is ', area)
print('The perimeter of the rectangle is ', perimeter)

#·Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
from math import pi

radius = input('Enter radius: ')

int_radius = int(radius)

area = pi * int_radius * int_radius
circumference = 2 * pi * int_radius

print('The area of the circle is ', area)
print('The circumference of the circle is ', circumference)

#·Calculate the slope, x-intercept and y-intercept of y = 2x -2
length = input('Enter length new rectangle: ')
width = input('Enter width new rectangle: ')

int_length = int(length)
int_width = int(width)

area = int_length * int_width
perimeter = 2 * (int_length + int_width)
print('The area of the rectangle is ', area)
print('The perimeter of the rectangle is ', perimeter)

#·Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = 'python'
dragon = 'dragon'

print(len(python))
print(len(dragon))

print(python == dragon)

#·Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in python)

#·I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jerga' in 'Espero que este curso no esté lleno de jerga')

#·There is no 'on' in both dragon and python
print('on' in python, 'on' in dragon)

#·Find the length of the text python and convert the value to float and convert it to string
length_python = len(python)

float(length_python)
print(length_python)
print(type(length_python))

str(length_python)
print(length_python)
print(type(length_python))

#·Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = 9
num2 = 10

print(num % 2 == 0)
print(num2 % 2 == 0)

#·Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
division = 7 // 3
print(division)

#·Check if type of '10' is equal to type of 10
print('10' == 10)

#·Check if int('9.8') is equal to 10
print(int(9.8) == 10)

#·Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input('Enter hours: ')
rate = input('Enter rate per hour: ')

int_hours = int(hours)
int_rate = int(rate)
earning = int_hours * int_rate

print('Your weekly earning is ', earning)

#·Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
days = input('Enter number of years you have lived: ')
int_days= int(days)

total = int_days * 31557600
print('You have lived for ', total, ' seconds.')

#·Write a Python script that displays the following table
print('1\t1\t1\t1\t1\n')
print('2\t1\t2\t4\t8\n')
print('3\t1\t3\t9\t27\n')
print('4\t1\t4\t16\t64\n')
print('5\t1\t5\t25\t125\n')