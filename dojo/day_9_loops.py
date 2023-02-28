######### Loops - Día 9 ######### 



# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i = i + 1 

# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i)

i = 10
while i > -1:
    print(i)
    i = i - 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######

a = '#'
while len(a) < 8:
    print(a)
    a = a + '#'

# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    print('# # # # # # # #')

""" 
Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100 
"""

for i in range(11):
    print( i, 'x', i, '=', (i*i) )

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in range(len(lst)):
    print(lst[i])

# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 102, 2):
    print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101, 2):
    print(i)

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
a = 0
for i in range(101):
    a = a + i
    print(a)
    i = i + 1

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
a = 0
for i in range(0, 102, 2):
    a = a + i
    print(a)
    i = i + 1


a = 0
for i in range(1, 101, 2):
    a = a + i
    print(a)
    i = i + 1

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from zz_countrie import countries

for i in countries:
    if 'land' in countries[i]:
        print(countries[i])
    else:
        pass

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit_list)-1,-1, -1):
    print(fruit_list[i])

# Go to the data folder and use the countries_data.py file.
from zz_countries_data import countries_data

# What are the total number of languages in the data
print(len(countries_data))

#######################################################################
# Find the ten most spoken languages from the data

# Find the 10 most populated countries in the world 

#######################################################################
