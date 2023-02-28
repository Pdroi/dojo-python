######### Variables, funciones integradas - Día 1 ######### 

#· Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta crea un archivo llamado variables.py

#· Escriba un comentario de python que diga 'Día 2: 30 días de programación en python'
#'Día 2: 30 días de programación en python'

#· Declarar una variable de nombre y asignarle un valor
var = ''

#· Declarar una variable de nombre completo y asignarle un valor
variable = True

#· Declarar una variable de país y asignarle un valor
Spain = 1

#· Declarar una variable de edad y asignarle un valor
edad = 18

#· Declarar una variable is_married y asignarle un valor
is_married = True

#· Declarar una variable is_light_on y asignarle un valor
is_light_on = False

#· Declarar múltiples variables en una línea
uno, dos, tres, cuatro = 1, 2, 3, 4

#· Verifique el tipo de datos de todas sus variables usando la función incorporada type ()
print(type(uno))

#· Usando la función incorporada len() , encuentre la longitud de su nombre
nombre = 'Pedro'
print(len(nombre))

#· Compare la longitud de su nombre y su apellido
apellido = 'Ruiz'
print(len(apellido))

#·Declarar 5 como num_one y 4 como num_two 
#       Agregue num_one y num_two y asigne el valor a un total variable
#       Reste num_two de num_one y asigne el valor a una variable diff
#       Multiplique num_two y num_one y asigne el valor a un producto variable
#       Divide num_one por num_two y asigna el valor a una división variable
#       Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un resto variable
#       Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
#       Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
num_one = 5
num_two =4

sum_num = num_one + num_two
rest_num = num_one - num_two
mult_num = num_one * num_two
div_num = num_one / num_two
div_mod_num = num_two % num_one
pot_num = num_one ** num_two
floor_num = num_one // num_two

#·El radio de un círculo es de 30 metros.
circle = 30
radio = circle /2
print(radio)

#·Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
from math import pi
area_of_circle = pi * (radio ** 2)
print(area_of_circle)

#·Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
circum_of_circle = pi * circle
print(circum_of_circle)

#·Tome el radio como entrada del usuario y calcule el área.
user_radio = input('dame un radio: ')

user_area_of_circle = pi * (int(user_radio) ** 2)
print(user_area_of_circle)

#·Use la función de entrada incorporada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
nombre = input('Cómo te llamas? ')
apellido = input('Cuál es tu apellido? ')
pais = input('De dónde eres? ')
edad = input('Cuántos años tienes? ')