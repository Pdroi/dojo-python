######### Lists - Día 4 ######### 

#1. Declare an empty list
lista = []

#2. Declare a list with more than 5 items
lista = [1, 2, 3 ,4, 5, 6,]

#3. Find the length of your list
print(len(lista))                                   #6

#4. Get the first item, the middle item and the last item of the list
lista = [1, 2, 3 ,4, 5]
print(lista[0], lista[2], lista[4])

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Pedro',37, 1.80,'single','Gnral. Ricardos']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companie = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()
print(it_companie)

#8. Print the number of companies in the list
print(len(it_companie))

#9. Print the first, middle and last company
print(it_companie[0], it_companie[3], it_companie[6])

#10. Print the list after modifying one of the companies
it_companie[0] = 'Futeria Manolo'
print(it_companie)

#11. Add an IT company to it_companies
it_companie.extend(['Facebook'])
print(it_companie)

#12. Insert an IT company in the middle of the companies list
it_companie.insert(3, 'Xiaomi')
print(it_companie)

#13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companie[0] = 'FRUTERIA MANOLO'
print(it_companie)

#14. Join the it_companies with a string '#;  '
print(str(it_companie).replace(',', '#;'))

#15. Check if a certain company exists in the it_companies list.
print('FRUTERIA MANOLO' in it_companie)

#16. Sort the list using sort() method
it_companie.sort()
print(it_companie)

#17. Reverse the list in descending order using reverse() method
it_companie.reverse()
print(it_companie)

#18. Slice out the first 3 companies from the list
print(it_companie[3:])

#19. Slice out the last 3 companies from the list
print(it_companie[:-3])

#20. Slice out the middle IT company or companies from the list
it_midle_out = it_companie[:3] + it_companie[6:]
print(it_midle_out)

#21. Remove the first IT company from the list
it_companie.remove('Xiaomi')
print(it_companie)

#22. Remove the middle IT company or companies from the list
print(len(it_companie))
it_companie.remove('Google')
it_companie.remove('Facebook')
print(it_companie)

#23. Remove the last IT company from the list
it_last_item = it_companie.pop()
print(it_companie)

#24. Remove all IT companies from the list
it_companie.clear()
print(it_companie)

#25. Destroy the IT companies list
del it_companie

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

print(full_stack)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

print(full_stack)

#28. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#28.1. Sort the list and find the min and max age
ages.sort()
max_age = len(ages)

print('el estudiante más joven tiene: ', ages[0])
print('el estudiante más mayor tiene: ', ages[max_age -1])

#28.2. Add the min age and the max age again to the list
ages.append(19)
ages.append(26)

#28.3. Find the median age (one middle item or two middle items divided by two)
print(ages[6])

#28.4. Find the average age (sum of all items divided by their number )
a,b,c,d,f,g,h,i,j,k,l,m = ages

total = a + b + c + d + f + g + h + i + j + k + l + m
print(int(total / 12))

#28.5. Find the range of the ages (max minus min)
ages.sort()
min_ages = ages[0]
max_ages = ages[-1]

range_ages = max_ages - min_ages
print(range_ages)

#28.6. Compare the value of (min - average) and (max - average), use abs() method
print(abs(min_ages))
print(abs(max_ages))

#28.7. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

n_contries = len(countries)
mid_n_contries = int(n_contries / 2)
print(mid_n_contries)

print(countries[96])

#. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_list_countries = countries[:97]
second_list_countries = countries[-98:]

print(first_list_countries)
print('-----------------++++++++++++++++++++++-----------------')
print(second_list_countries)

#. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Rusia', 'EE. UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']

ch, ru, eu, *escandinavos = countries

print(ch)
print(ru)
print(eu)
print(escandinavos)