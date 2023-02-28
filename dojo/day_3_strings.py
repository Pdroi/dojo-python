######### Strings - Día 3 ######### 

#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
var = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(var)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
var = 'Coding ' + 'For ' + 'All '
print(var)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4. Print the variable company using print().
print(company)                                  # Coding For All

#5. Print the length of the company string using len() method and print().
print(len(company))                             # 14

#6. Change all the characters to uppercase letters using upper() method.
print(company.upper())                          # CODING FOR ALL

#7. Change all the characters to lowercase letters using lower() method.
print(company.lower())                          # coding for all

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())                     # Coding for all
print(company.title())                          # Coding For All
print(company.swapcase())                       # cODING fOR aLL

#9. Cut(slice) out the first word of Coding For All string.
print(company[1:3])                             # od

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))                  # 0
print(company.find('Coding'))                   # 0
print('Coding' in company)                      # True

#11. Replace the word coding in the string 'Coding For All' to Python.
company = company.replace('All', 'Python')
print(company)

#12. Change Python for Everyone to Python for All using the replace method or other methods.
company = company.replace('Python', 'All')
print(company)

#13. Split the string 'Coding For All' using space as the separator (split()).
company = company.split(' ')
print(company)                                  # ['Coding', 'For', 'All']

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"
print(companies)                                # ('Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon')

#15. What is the character at index 0 in the string Coding For All.
company = "Coding For All"
print(company[0])                               # C

#16. What is the last index of the string Coding For All.
print(company[-1])                              # l

#17. What character is at index 10 in "Coding For All" string.
print(company[10])                              # ' '

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
company = 'Python For Everyone'
company = company[0] + company[7] + company[11]
print(company)                                  # PFE

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
company = 'Coding For All'
company = company[0] + company[7] + company[11]
print(company)                                  # CFA

#20. Use index to determine the position of the first occurrence of C in Coding For All.
company = 'Coding For All'
print(company.index('C'))                       # 0

#21. Use index to determine the position of the first occurrence of F in Coding For All.
company = 'Coding For All'
print(company.index('F'))                       # 7

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
coding = 'Coding For All People'
print(coding.rfind('l'))                        # 19

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))                 # 31                
print(sentence.index('because'))                # 31

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rfind('because'))                # 47                

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because = sentence[31:54]
print(because)

#26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))                 # 31

#27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because = sentence[31:54]
print(because)

#28. Does ''Coding For All' start with a substring Coding?
cfa = 'Coding For All'
coding = cfa[0:6]
print(coding)

#29. Does 'Coding For All' end with a substring coding?
new_cfa = cfa + ' ' + coding
print(new_cfa)

#30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
cfa = '   Coding For All      ' 
print(cfa[3:17]) 

#31. Which one of the following variables return True when we use the method isidentifier():
#       . 30DaysOfPython
#       . thirty_days_of_python
var1 = '30DaysOfPython'
var2 = 'thirty_days_of_python'

print(var1.isidentifier())
print(var2.isidentifier())

#32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lista = str(libraries)

print(type(lista))
print(lista.replace(',', '#'))

#33. Use the new line escape sequence to separate the following sentences.
var = 'I am enjoying this challenge.\nI just wonder what is next.'
print(var)

#34. Use a tab escape sequence to write the following lines.
var = 'Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki'
print(var)

#35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
var =f'The area of a circle with radius {radius} is {int(area)} meters square.'
print(var)
