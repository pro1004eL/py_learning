
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(string)
print('1:', result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string2 = ['Coding', 'For' , 'All']
result2 = ' '.join(string2)
print('2:', result2)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
# 4. Print the variable company using print().
# 5. Print the length of the company string using len() method and print().
company = "Coding For All"
print('3,4:', company)
print('5:', len(company))

# 6. Change all the characters to uppercase letters using upper() method.
company = "Coding For All"
print('6:', company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
company = "Coding For All"
print('7:', company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = "Coding For All"
print('8.1:', company.capitalize())  # only first letter upp
print('8.2:', company.title())  # all words with first character upp
print('8.3:', company.swapcase())  # changed lower -> upper and upper -> lower

# 9. Cut(slice) out the first word of Coding For All string.
company = "Coding For All"
print('9:', company[7:])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
company = "Coding For All"
sub_string = 'Coding'
indexx = company.find(sub_string)
print('10:', f'the index of first finding: {indexx}')

# 11. Replace the word coding in the string 'Coding For All' to Python.
company = "Coding For All"
new_str = company.replace('Coding', 'Python')
print('11:', new_str)

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
company = "Python for Everyone"
new_str = company.replace('Everyone', 'All')
print('12:', new_str)

# 13. Split the string 'Coding For All' using space as the separator (split())
company = "Coding For All"
new_str = company.split()
print('13:', new_str)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
new_str = companies.split(', ')
print('14:', new_str)

# 15. What is the character at index 0 in the string Coding For All.
company = "Coding For All"
character = company[0]
print('15:', f'the first character:{character}')

# 16. What is the last index of the string Coding For All.
company = "Coding For All"
last_character = company[-1:]
print('16:', f'the last character:{last_character}')

# 17. What character is at index 10 in "Coding For All" string.
company = "Coding For All"
character = company[10]
print('17:', f'the character #10:{character}')  # пробіл (space)

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
company = "Python For Everyone"
split_str = company.split()
abreviatura = [i[0] for i in split_str]
print('18: abbreviation for the name "Python For Everyone":', ''.join(abreviatura))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
company = "Coding For All"
split_str = company.split()
abreviatura2 = [i[0] for i in split_str]
print('19: abbreviation for the name "Coding For All":', ''.join(abreviatura2))

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
company = "Coding For All"
index_c = company.index("C")
print('20:', f'index_C: {index_c}')

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
company = "Coding For All"
index_f = company.index("F")
print('21:', f'index_F: {index_f}')

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
company = "Coding For All People"
last_l = company.rfind("l")
print('22:', f'rfind_l: {last_l}')

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
company = "You cannot end a sentence with because because because is a conjunction"
word_because = company.find("because")
print('23:', f'index of the first word_because: {word_because}')

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
company = "You cannot end a sentence with because because because is a conjunction"
word_because = company.rindex("because")
print('24:', f'index of the last word_because: {word_because}')

# 25. Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
company = "You cannot end a sentence with because because because is a conjunction"
slice_out_words = 'because because because'
cut_start = company.index('because')
cut_end = cut_start + len(slice_out_words)
slice_out = company[:cut_start] + company[cut_end:]
print('25:', f'sentence without words because: {slice_out}')

# 26 and 27 tasks are dublicate of 23 and 25 tasks

# 28. Does 'Coding For All' start with a substring Coding?
coding = 'Coding For All'
check_start = coding.startswith('Coding')
print('28. starts with a substring Coding?:', check_start)

# 29. Does 'Coding For All' end with a substring coding?
coding = 'Coding For All'
check_ends = coding.endswith('coding')
print('29. ends with a substring coding?:', check_ends)

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
coding = '   Coding For All      '
check_strip = coding.strip()
print('30. remove the left and right trailing spaces', check_strip)

# 31. Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
check_right_name1 = '30DaysOfPython'
check_name1 = check_right_name1.isidentifier()
check_right_name2 = "thirty_days_of_python"
check_name2 = check_right_name2.isidentifier()
print(f'31. variable name "30DaysOfPython" correct?: {check_name1} '
      f'\nvariable name "thirty_days_of_python" correct?: {check_name2}')

# 32. The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_libra = ' / '.join(libraries)
print(f'32. python libraries: {join_libra}')

# 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
sentences = 'I am enjoying this challenge. \nI just wonder what is next.'
print('33.', sentences)

# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
sentences = '\nName \t\tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki'
print('34.', sentences)

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2

print(f'35. The area of a circle with radius {radius} is {area} meters square.')

# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

print(f'36. {8+6, 8 * 6}')










