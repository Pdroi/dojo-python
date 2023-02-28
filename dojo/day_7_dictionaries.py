######### Dictionaries - Día 7 ######### 

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Renda', 
    'color':'White', 
    'breed':'Dogo', 
    'legs':4, 
    'age':4
}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Pedro',
    'last_name': 'Ruiz',
    'gender':'Male',
    'age':37,
    'marital_status':'Single',
    'skills': ['Git','SQL','Python','Maths'],
    'country':'Spain',
    'city':'Madrid',
    'address': 'Gnral. Ricardos'
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills


# Get the dictionary keys as a list
tpl = student.keys()
print(tpl)
print(type(tpl))

# Get the dictionary values as a list
tpl = student.values()
print(tpl)
print(type(tpl))

# Change the dictionary to a list of tuples using items() method
tpl = student.items()
print(tpl)
print(type(tpl))

# Delete one of the items in the dictionary
print(len(student))
student.pop('skills')
print(len(student))

# Delete one of the dictionaries
del dog