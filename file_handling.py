import os
import json
import csv

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
    "name":"Anton",
    "country":"Ukraine",
    "city":"Ovruch",
    "skills":["JavaScrip", "React","Python"]
}'''
print(type(person_json))

#todo Changing JSON to Dictionary
person_dic = json.loads(person_json)
print(type(person_dic))
print(person_dic)
print(person_dic['city'])

#todo Changing Dictionary to JSON
# python dictionary
person = {
    "name":"Anton",
    "country":"Ukraine",
    "city":"Ovruch",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json_to_dic = json.dumps(person, indent=4)
print(type(person_json_to_dic))
print(person_json_to_dic)

#todo File with csv Extension

with open('/Users/Anton/python/python_learning/py_30_Days/csv_exampl.csv') as f_csv:
    csv_reader = csv.reader(f_csv, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {', '.join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a lerner. He is from {row[2]}, his age: {row[3]}')
            line_count += 1
    print(f'Number of lines: {line_count}')


