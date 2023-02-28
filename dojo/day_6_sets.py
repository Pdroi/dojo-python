######### Sets - Día 6 ######### 

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['SAP','TCS', 'DXC'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('SAP')
print(it_companies)

# What is the difference between remove and discard
it_companies.discard('Fruteria Manolo')
#it_companies.remove('Fruteria Manolo')  -->  KeyError

# Join A and B
A.update(B)
print(A)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
A_B = A.union(B)
B_A = B.union(A)
print(A_B)
print(B_A)

# What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(len(age_st))
print(len(age))

# Explain the difference between the following data types: string, list, tuple and set

string = 'only txt'
lst = ['conjunto de todo tipo de datos', 'ordenados', 'modificable', 'admite duplicados']
tpl = ('conjunto de todo tipo de datos', 'ordenados', 'no modificable', 'admite duplicados')
st = {'conjunto de todo tipo de datos', 'desordenado', 'No modificable', 'No admite duplicados'}

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

string = 'I am a teacher and I love to inspire and teach people'

st = string.split(' ')
print(len(st))
print(len(st))

st_set = set(st)
print(len(st_set))
