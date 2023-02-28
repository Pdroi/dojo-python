######### Conditional - Día 8 ######### 

 
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

str_age = input('Enter your age: ')
int_age = int(str_age)

if int_age >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need 3 more years to learn to drive.')


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

print('Who is older (me or you)?')
my_age = 37
str_your_age = input('Enter your age: ')
your_age = int(str_your_age)

if my_age == your_age - 1:
    print('I am one year older than you')
elif my_age == your_age:
    print('you are my age')
elif my_age == your_age + 1:
    print('you are one year older than me')
elif my_age > your_age:
    a = my_age - your_age
    print('I am', a, 'years older than you')
elif my_age < your_age:
    a = your_age - my_age
    print('I am', a, 'yaers older than you')   
else:
    print('Enter a number....')

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

str_one = input('Enter a first number: ')
str_two = input('Enter a second number: ')

int_one  = int(str_one)
int_two  = int(str_two)

if int_one > int_two:
    print('The first number is greater')
elif int_one < int_two:
    print('The second number is greater')
else:
    print('the two numbers are equal')


# Write a code which gives grade to students according to theirs scores:
str_note = input('Enter your score: ')
int_note = int(str_note)

if int_note >= 80:
    print('your note is A')
elif int_note >= 70:
    print('your note is B')
elif int_note >= 60:
    print('your note is C')
elif int_note >= 50:
    print('your note is D')
else:
    print('your note is F')


# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
str_station = input('what month is it? ')
station = str_station.capitalize()

if station in ('September', 'October', 'November'):
    print('the season is Autumn')
elif station in ('December', 'January', 'February'):
    print('the season is Winter')
elif station in ('March', 'April', 'May'):
    print('the season is Spring')
elif station in ('June', 'July', 'August'):
    print('the season is Summer')
else:
    print('the month you have provided is wrong')

# The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

user_fruits = input('give me the name of a fruit: ')
format_user_fruits = user_fruits.lower()

fruits = ['banana', 'orange', 'mango', 'lemon']

if format_user_fruits in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(format_user_fruits)
    print(fruits)


# Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print('skills' in person)

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print('Python' in person['skills'])

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'JavaScript' or 'React' in person['skills']:
    print('He is a front end developer')
elif  'Node' or 'Python' or 'MongoDB' in person['skills']:
    print('He is a backend developer')
else:
    print('unknown title')

# If the person is married and if he lives in Finland, print the information in the following format:
    # Asabeneh Yetayeh lives in Finland. He is married.

if person['is_marred'] is True:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is single.")