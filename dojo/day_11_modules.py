######### Modules - Día 11 ######### 

""" 
# Writ a function which generates a six digit/character random_user_id.
#           print(random_user_id());
#           '1ee33d'

import random 
import string

def generate_user_id():
    user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return user_id

print(generate_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
#               print(user_id_gen_by_user()) # user input: 5 5
#               output:
#                   kcsy2
#                   SMFYb
#                   bWmeq
#                   ZXOYh
#                   2Rgxf 
#               print(user_id_gen_by_user()) # 16 5
#                   1GCSgPLMaBAVQZ26
#                   YD7eFwNQKNs7qXaT
#                   ycArC5yrRupyG00S
#                   UbGxOFI7UXSWAyKN
#                   dIV0SSUTgAdKwStr

import random
import string

def user_id_gen_by_user():
    char_num = int(input("Enter the number of characters for the user ID: "))
    id_num = int(input("Enter the number of IDs to generate: "))
    user_ids = []
    for i in range(id_num):
        user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=char_num))
        user_ids.append(user_id)
    for id in user_ids:
        print(id)
user_id_gen_by_user() 


# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
#           print(rgb_color_gen())
#           rgb(125,244,255) - the output should be in this form 3-3

import random 
import string

def rgb_color_gen():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    print('rgb(',red,',',green,',',blue,')') 

rgb_color_gen()
 """

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random 
import string


def list_of_hexa_colors(num_colors):
    colors = []
    for i in range(num_colors):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append(color)
    return colors

print(list_of_hexa_colors(6))



# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

""" 
Write a function generate_colors which can generate any number of hexa or rgb colors.
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
Exercises: Level 3
Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique. 
"""