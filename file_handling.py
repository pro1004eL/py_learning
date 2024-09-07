import os

print('')

f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
print(f)

txt = f.read()
print(type(txt))
print(txt)
f.close()

# only 1 line
f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
line1 = f.readline()
print(type(line1))
print(line1)
f.close()

# str => list
f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
line1 = f.readlines()
print(type(line1))
print(line1)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
line1 = f.read().splitlines()
print(type(line1))
print(line1)
f.close()

# There is a new way of opening files using with - closes the files by itself. Let us rewrite the the previous example with the with method:
with open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt') as f:
    lines = f.readlines()
    print(type(lines))
    print(lines)

# Opening Files for Writing and Updating
# with open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt', 'a') as f:
#     f.write('This text has  end32131213123')
#
# with open('/Users/Anton/python/python_learning/py_30_Days/write_file_example.txt', 'w') as f:
#     f.write('This text will be written in a newly created file')

#todo Deleting Files

if os.path.exists('/Users/Anton/python/python_learning/py_30_Days/write_file_example.txt'):
    os.remove('/Users/Anton/python/python_learning/py_30_Days/write_file_example.txt')
else:
    print('The file does not exist')

# we use three quotes and make it multiple line to make it more readable
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

