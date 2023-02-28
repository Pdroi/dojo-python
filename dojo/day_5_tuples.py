######### Tuples - Día 5 ######### 

# Create an empty tuple
tpl =()
print(type(tpl))

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tpl_brothers, tpl_sisters = ('Nombre 1','Nombre 2','Nombre 3'), ('Nombre 4','Nombre 5')

# Join brothers and sisters tuples and assign it to siblings
tpl_brothers = tpl_brothers + tpl_sisters
print(tpl_brothers)

# How many siblings do you have?
print(len(tpl_brothers))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = tpl_brothers + ('father','mother')
print(family_members)

# Unpack siblings and parents from family_members
tpl_brothers = (family_members[:-2])
tpl_parents = (family_members[-2:])

print(tpl_brothers)
print(tpl_parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits, vegetables, animal_products = ('naranja','manzana','pera','kiwi'), ('cebolla','pimiento','lechuga','nabo'), ('pollo','cerdo','vaca','cordero')
food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)
print(type(food_stuff_lt))

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_tp))
print(food_stuff_tp[6])

# Slice out the first three items and the last three items from food_staff_lt list
tpl_slice = food_stuff_lt[:3] + food_stuff_lt[-3:]
print(tpl_slice)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

""" 
check if an item exists in tuple:
    Check if 'Estonia' is a nordic country
    Check if 'Iceland' is a nordic country 
"""

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
